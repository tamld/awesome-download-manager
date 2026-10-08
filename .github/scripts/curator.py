#!/usr/bin/env python3
"""
Monthly Awesome Curator for Awesome Download Manager.
Discovers top-starred (>= 1,000 stars), active, verified open-source download managers on GitHub.
Zero external dependencies (uses standard library).
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request

MIN_STARS = 1000
BLACKLIST_KEYWORDS = [
    "activation", "crack", "patch", "keygen", "reset-trial",
    "trial-reset", "license-key", "kms", "bypass"
]
ALLOWED_LICENSES = {
    "gpl-3.0", "gpl-2.0", "agpl-3.0", "lgpl-3.0",
    "apache-2.0", "mit", "mpl-2.0", "bsd-3-clause", "bsd-2-clause"
}

def get_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Awesome-Curator-Bot"
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def fetch_json(url):
    req = urllib.request.Request(url, headers=get_headers())
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def get_existing_urls_and_names(readme_path="README.md"):
    if not os.path.exists(readme_path):
        return set()
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read().lower()
    return content

def is_blacklisted(text):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in BLACKLIST_KEYWORDS)

def search_candidates():
    existing_content = get_existing_urls_and_names()
    queries = [
        f"topic:download-manager stars:>={MIN_STARS}",
        f"topic:aria2 stars:>={MIN_STARS}"
    ]

    candidates = []
    seen_repos = set()

    for q in queries:
        encoded_q = urllib.parse.quote(q)
        url = f"https://api.github.com/search/repositories?q={encoded_q}&sort=stars&order=desc&per_page=15"
        data = fetch_json(url)
        if not data or "items" not in data:
            continue

        for item in data["items"]:
            repo_full_name = item["full_name"]
            repo_name = item["name"]
            repo_url = item["html_url"].lower()

            if repo_full_name in seen_repos:
                continue
            seen_repos.add(repo_full_name)

            # Skip if already listed in README
            if repo_url in existing_content or repo_name.lower() in existing_content:
                continue

            # Anti-piracy / anti-crack filter
            desc = item.get("description") or ""
            if is_blacklisted(repo_name) or is_blacklisted(desc):
                continue

            # License verification
            license_info = item.get("license") or {}
            license_key = (license_info.get("key") or "").lower()
            if license_key not in ALLOWED_LICENSES:
                continue

            # Invariant: Must not be archived or disabled
            if item.get("archived") or item.get("disabled"):
                continue

            candidates.append({
                "name": item["name"],
                "full_name": item["full_name"],
                "url": item["html_url"],
                "description": desc.strip(),
                "stars": item["stargazers_count"],
                "license": license_info.get("spdx_id") or license_key.upper(),
                "language": item.get("language") or "N/A"
            })

    return candidates

def generate_report(candidates, output_file="curator_summary.md"):
    if not candidates:
        print("No new top-star candidates found. Exiting quietly.")
        return False

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("### 🤖 Monthly Awesome Radar — Verified Candidate Findings\n\n")
        f.write(f"Found **{len(candidates)}** high-signal, community-proven download manager(s) with $\\ge 1,000$ stars:\n\n")
        f.write("| Software | Stars | License | Language | Description |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for c in candidates:
            f.write(f"| [**{c['name']}**]({c['url']}) | ⭐ {c['stars']:,} | `{c['license']}` | {c['language']} | {c['description']} |\n")
        f.write("\n---\n*Automated review passed: Public source code verified, OSI license confirmed, piracy keywords absent.*\n")

    print(f"Generated {output_file} with {len(candidates)} candidate(s).")
    return True

if __name__ == "__main__":
    candidates = search_candidates()
    has_candidates = generate_report(candidates)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"found={'true' if has_candidates else 'false'}\n")
            f.write(f"count={len(candidates)}\n")
