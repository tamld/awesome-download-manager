#!/usr/bin/env python3
"""
Deterministic README Builder for Awesome Download Manager.
Compiles data/tools.json into a perfectly formatted, drift-free README.md.
Guarantees:
- 100% Professional English
- Zero broken Markdown tables
- Collapsible Technical Dossiers (Design Axioms, Citations, Strengths, Tradeoffs)
"""

import json
import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(ROOT_DIR, "data", "tools.json")
README_PATH = os.path.join(ROOT_DIR, "README.md")

def escape_pipe(text):
    return text.replace("|", "\\|").strip()

def render_dossier(tool):
    lines = []
    lines.append(f"<details>")
    lines.append(f"<summary>🔍 <b>Architecture & Axioms: {tool['name']}</b> <i>(Click to expand)</i></summary>\n")
    lines.append(f"- **Design Axiom**: {tool['axiom']}")
    
    citations = tool.get("citations", [])
    if citations:
        citation_links = ", ".join(f"[{c}]({c})" for c in citations)
        lines.append(f"- **Technical Citations & Proof**: {citation_links}")
        
    highlights = tool.get("highlights", [])
    if highlights:
        lines.append(f"- **Key Strengths**: {'; '.join(highlights)}")
        
    tradeoffs = tool.get("tradeoffs", [])
    if tradeoffs:
        lines.append(f"- **Engineering Tradeoffs**: {'; '.join(tradeoffs)}")
        
    lines.append("\n</details>\n")
    return "\n".join(lines)

def build_readme():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        tools = json.load(f)

    # Categorize tools
    trending_tools = [t for t in tools if t.get("category") == "trending" or t.get("trending_badge")]
    legends_tools = [t for t in tools if t.get("category") == "legends" or t.get("stars", 0) >= 10000]
    # Deduplicate while preserving order
    seen_ids = set()
    unique_legends = []
    for t in legends_tools:
        if t["id"] not in seen_ids:
            seen_ids.add(t["id"])
            unique_legends.append(t)

    desktop_tools = [t for t in tools if t.get("category") == "desktop"]
    linux_tools = [t for t in tools if t.get("category") == "linux"]
    cli_tools = [t for t in tools if t.get("category") == "cli"]
    ext_tools = [t for t in tools if t.get("category") == "extensions"]
    selfhosted_tools = [t for t in tools if t.get("category") == "selfhosted"]

    out = []
    out.append("# 🌐 Awesome Download Manager\n")
    out.append("[![CI & Link Integrity](https://github.com/tamld/awesome-download-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/tamld/awesome-download-manager/actions/workflows/ci.yml)")
    out.append("[![Awesome Radar & Trending Curator](https://github.com/tamld/awesome-download-manager/actions/workflows/curator.yml/badge.svg)](https://github.com/tamld/awesome-download-manager/actions/workflows/curator.yml)")
    out.append("[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)\n")
    out.append("> A carefully curated, community-validated, and security-gated collection of high-performance download managers, stream grabbers, and terminal utilities.\n")
    out.append("---\n")
    out.append("## 📚 Table of Contents\n")
    out.append("- [🔥 Trending Spotlight](#-trending-spotlight)")
    out.append("- [🏆 All-Time Legends (≥ 10k Stars)](#-all-time-legends)")
    out.append("- [💻 Modern Desktop Powerhouses (GUI)](#-modern-desktop-powerhouses)")
    out.append("- [🐧 Native Linux Ecosystem](#-native-linux-ecosystem)")
    out.append("- [⚡ Command-Line & Terminal Power (CLI / TUI)](#-command-line--terminal-power)")
    out.append("- [🧩 Browser Extensions](#-browser-extensions)")
    out.append("- [🌐 Self-Hosted & Server Daemons](#-self-hosted--server-daemons)")
    out.append("- [🛡️ Curation & Verification Standards](#️-curation--verification-standards)\n")
    out.append("---\n")

    # 1. Trending Spotlight
    out.append("## 🔥 Trending Spotlight\n")
    out.append("*Recognizing community-proven, actively maintained download managers with exceptional momentum across GitHub.*\n")
    out.append("| Spotlight Period | Software | Stars | Technology | Key Highlights |")
    out.append("| :--- | :--- | :--- | :--- | :--- |")
    for t in trending_tools:
        badge = t.get("trending_badge", "🌟 Active")
        stars_str = f"⭐ {t['stars']:,}" if t.get("stars") else "N/A"
        out.append(f"| {badge} | [**{t['name']}**]({t['url']}) | {stars_str} | {escape_pipe(t.get('technology', 'N/A'))} | {escape_pipe(t['description'])} |")
    out.append("")
    for t in trending_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # 2. All-Time Legends
    out.append("## 🏆 All-Time Legends (≥ 10k Stars)\n")
    out.append("| Software & Link | Description | Technology Stack | License | Supported Platforms |")
    out.append("| :--- | :--- | :--- | :--- | :--- |")
    for t in unique_legends:
        stars_badge = f"⭐ {t['stars']:,}" if t.get("stars") else ""
        platforms = ", ".join(t.get("platforms", []))
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {escape_pipe(t.get('technology', 'N/A'))} | {lic} | {escape_pipe(platforms)} |")
    out.append("")
    for t in unique_legends:
        out.append(render_dossier(t))
    out.append("---\n")

    # 3. Modern Desktop Powerhouses
    out.append("## 💻 Modern Desktop Powerhouses (GUI)\n")
    out.append("| Software & Link | Description | License | Supported OS |")
    out.append("| :--- | :--- | :--- | :--- |")
    for t in desktop_tools:
        platforms = ", ".join(t.get("platforms", []))
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {lic} | {escape_pipe(platforms)} |")
    out.append("")
    for t in desktop_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # 4. Native Linux Ecosystem
    out.append("## 🐧 Native Linux Ecosystem\n")
    out.append("| Software & Link | Description | Backend Engine | License |")
    out.append("| :--- | :--- | :--- | :--- |")
    for t in linux_tools:
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {escape_pipe(t.get('technology', 'N/A'))} | {lic} |")
    out.append("")
    for t in linux_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # 5. CLI & Terminal
    out.append("## ⚡ Command-Line & Terminal Power (CLI / TUI)\n")
    out.append("| Tool & Link | Description | Primary Strength | License |")
    out.append("| :--- | :--- | :--- | :--- |")
    for t in cli_tools:
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {escape_pipe(t.get('technology', 'N/A'))} | {lic} |")
    out.append("")
    for t in cli_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # 6. Extensions
    out.append("## 🧩 Browser Extensions\n")
    out.append("| Extension & Link | Description | Target Browsers | License |")
    out.append("| :--- | :--- | :--- | :--- |")
    for t in ext_tools:
        browsers = ", ".join(t.get("platforms", []))
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {escape_pipe(browsers)} | {lic} |")
    out.append("")
    for t in ext_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # 7. Self-Hosted
    out.append("## 🌐 Self-Hosted & Server Daemons\n")
    out.append("| Software & Link | Description | Technology | License |")
    out.append("| :--- | :--- | :--- | :--- |")
    for t in selfhosted_tools:
        lic = f"🆓 Free ({t['license']})" if t.get("is_open_source") else f"💵 {t['license']}"
        out.append(f"| [**{t['name']}**]({t['url']}) | {escape_pipe(t['description'])} | {escape_pipe(t.get('technology', 'N/A'))} | {lic} |")
    out.append("")
    for t in selfhosted_tools:
        out.append(render_dossier(t))
    out.append("---\n")

    # Standards & Contributing
    out.append("## 🛡️ Curation & Verification Standards\n")
    out.append("To guarantee a high signal-to-noise ratio, zero malware, and strict user privacy, all entries must pass our **Automated 4-Quadrant Verification**:\n")
    out.append("1. 🛡️ **Safe & Auditable**: Open-source tools MUST provide transparent, inspectable source code with an OSI-approved license. Binary-only distributions with missing or dummy source code (open-washing) are strictly rejected. No cracks, keygens, or pirated tools are accepted.")
    out.append("2. 💓 **Alive & Maintained**: The repository or website must be active, resolving HTTP 200, with commits or maintenance within the last 180 days.")
    out.append("3. ⭐ **High Social Proof**: Standard additions require community validation (≥ 1,000 stars on GitHub).")
    out.append("4. 🔥 **Trending Spotlight**: Fast-growing tools with breakout momentum are automatically spotlighted in the Trending category.\n")
    out.append("---\n")
    out.append("### Contributing\n")
    out.append("Have a download manager that meets our standards? Please read our [Contributor Guide](.github/pull_request_template.md) and submit a pull request!\n")

    content = "\n".join(out)
    return content

if __name__ == "__main__":
    check_mode = "--check" in sys.argv
    rendered = build_readme()

    if check_mode:
        if not os.path.exists(README_PATH):
            print("README.md does not exist.")
            sys.exit(1)
        with open(README_PATH, "r", encoding="utf-8") as f:
            existing = f.read()
        if existing.strip() != rendered.strip():
            print("Drift detected: README.md is out of sync with data/tools.json.")
            sys.exit(1)
        print("README.md is up to date.")
        sys.exit(0)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(rendered)
    print("Successfully built README.md from data/tools.json.")
