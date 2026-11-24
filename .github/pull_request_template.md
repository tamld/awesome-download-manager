### 📋 Contributor Submission Checklist

Thank you for contributing to **Awesome Download Manager**! To maintain high standards of transparency, quality, and user safety, please complete the checklist below.

#### 1. Software Details
- **Software Name:** 
- **Official Repository / URL:** 
- **Primary Platform(s):** (Windows / macOS / Linux / Android / iOS / Browser Extension / CLI)
- **License Type:** (e.g., GPL-3.0, Apache-2.0, MIT, Proprietary)

#### 2. Open-Source & Trust Verification
- [ ] **Public Source Code**: The repository contains full, auditable application source code (not just binary installers, releases, or documentation).
- [ ] **Legitimate License**: The software conforms to its declared license without open-washing or deceptive claims.
- [ ] **Privacy & Security**: The software does not include unwanted adware, cryptominers, unauthorized tracking, or excessive extension permissions (e.g., unprompted access to all cookies or bookmarks).
- [ ] **Meets Curation Thresholds**: ≥ 1,000 GitHub stars (for open-source additions) and active maintenance within the last 180 days.

#### 3. SSoT Build Verification
> Note: `README.md` is generated deterministically from `data/tools.json`. Do not hand-edit `README.md` without updating `data/tools.json`.

- [ ] Added entry to `data/tools.json` (including `axiom` >= 20 chars and >= 1 `citations` URL)
- [ ] Regenerated `README.md` via `python scripts/build_readme.py`
- [ ] Verified locally with `python -m unittest discover tests` and `python scripts/build_readme.py --check`

---
*Submissions that violate open-source transparency or distribute unaudited closed binaries will be rejected.*
