# 🌐 Awesome Download Manager

[![CI & Link Integrity](https://github.com/tamld/awesome-download-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/tamld/awesome-download-manager/actions/workflows/ci.yml)
[![Awesome Radar & Trending Curator](https://github.com/tamld/awesome-download-manager/actions/workflows/curator.yml/badge.svg)](https://github.com/tamld/awesome-download-manager/actions/workflows/curator.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A carefully curated, community-validated, and security-gated collection of high-performance download managers, stream grabbers, and terminal utilities.

---

## 📚 Table of Contents

- [🔥 Trending Spotlight](#-trending-spotlight)
- [🏆 All-Time Legends (≥ 10k Stars)](#-all-time-legends)
- [💻 Modern Desktop Powerhouses (GUI)](#-modern-desktop-powerhouses)
- [🐧 Native Linux Ecosystem](#-native-linux-ecosystem)
- [⚡ Command-Line & Terminal Power (CLI / TUI)](#-command-line--terminal-power)
- [🧩 Browser Extensions](#-browser-extensions)
- [🌐 Self-Hosted & Server Daemons](#-self-hosted--server-daemons)
- [🛡️ Curation & Verification Standards](#️-curation--verification-standards)

---

## 🔥 Trending Spotlight

*Recognizing community-proven, actively maintained download managers with exceptional momentum across GitHub.*

| Spotlight Period | Software | Stars | Technology | Key Highlights |
| :--- | :--- | :--- | :--- | :--- |
| 🚀 Trending This Month | [**AB Download Manager**](https://abdownloadmanager.com/) | ⭐ 18,300 | Kotlin / Compose Desktop | Modern, lightning-fast open-source IDM replacement with browser integration. |
| ⚡ Trending This Week | [**Gopeed**](https://gopeed.com/) | ⭐ 26,700 | Golang + Flutter | Ultra-high performance multi-protocol engine across all desktop and mobile platforms. |
| 🌟 Daily Mover | [**Open Download Manager**](https://github.com/getodm/open-download-manager) | ⭐ 20 | Java 25 + GTK4 / Libadwaita | Native Linux manager with unified queue for HTTP, Torrents, yt-dlp, and mirrors. |
| 🌟 Daily Mover | [**Rayburst**](https://github.com/AnInsomniacy/rayburst) | ⭐ 10,800 | Rust / Modern Web | High-throughput, modular download engine engineered for modern gigabit bandwidth. |

<details>
<summary>🔍 <b>Architecture & Axioms: AB Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Proprietary tools like IDM dominate Windows download acceleration through aggressive dynamic socket chunking but remain closed-source and platform-restricted. AB Download Manager re-engineers this multithreaded chunking architecture atop Kotlin and Jetpack Compose Desktop, delivering an open, transparent, and multiplatform IDM alternative.
- **Technical Citations & Proof**: [https://github.com/amir1376/ab-download-manager#features](https://github.com/amir1376/ab-download-manager#features), [https://github.com/amir1376/ab-download-manager/releases](https://github.com/amir1376/ab-download-manager/releases)
- **Key Strengths**: Modern Jetpack Compose desktop interface; Native multi-part connection splitting and queue scheduling; Official Chrome and Firefox companion extensions
- **Engineering Tradeoffs**: Native BitTorrent protocol is not yet embedded; focused strictly on HTTP/HTTPS/FTP stream acceleration.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Gopeed</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Aria2 established the gold standard for headless protocol multiplexing, but decoupling the CLI daemon from separate WebUI clients created significant operational friction. Gopeed unifies high-concurrency Go concurrency primitives with a reactive Flutter client into a single zero-dependency binary running identically across mobile and desktop.
- **Technical Citations & Proof**: [https://github.com/GopeedLab/gopeed#architecture](https://github.com/GopeedLab/gopeed#architecture), [https://github.com/GopeedLab/gopeed/releases](https://github.com/GopeedLab/gopeed/releases)
- **Key Strengths**: Embedded BitTorrent, Magnet, and HTTP/FTP engine; Cross-platform mobile and desktop consistency; JavaScript extension ecosystem for custom extractors
- **Engineering Tradeoffs**: Does not bundle advanced stream scraping (HLS/DASH) natively without user-installed extensions.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Open Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Linux desktop environments lack a cohesive, native download client that unifies diverse protocol engines. Open Download Manager solves this by orchestrating trusted system binaries (aria2, yt-dlp, and httrack) behind a native GTK4/Libadwaita interface with persistent crash-safe queue recovery.
- **Technical Citations & Proof**: [https://github.com/getodm/open-download-manager#features](https://github.com/getodm/open-download-manager#features), [https://github.com/getodm/open-download-manager/releases](https://github.com/getodm/open-download-manager/releases)
- **Key Strengths**: Native GNOME/GTK4 look and feel; Unified queue across HTTP, Torrent, and video extractors; Tor and proxychains routing support
- **Engineering Tradeoffs**: Requires host dependencies (aria2, yt-dlp) or running via standalone AppImage.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Rayburst</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Legacy download managers frequently bottleneck on high-bandwidth fiber connections due to memory allocation overhead and single-threaded queue arbitration. Rayburst leverages Rust zero-cost abstractions and asynchronous I/O to maximize bandwidth saturation with minimal CPU overhead.
- **Technical Citations & Proof**: [https://github.com/AnInsomniacy/rayburst#readme](https://github.com/AnInsomniacy/rayburst#readme)
- **Key Strengths**: Ultra-low memory footprint; High-concurrency async socket chunking; Modern clean architectural stack
- **Engineering Tradeoffs**: Relatively recent ecosystem; plugin support continues active development.

</details>

---

## 🏆 All-Time Legends (≥ 10k Stars)

| Software & Link | Description | Technology Stack | License | Supported Platforms |
| :--- | :--- | :--- | :--- | :--- |
| [**AB Download Manager**](https://abdownloadmanager.com/) | Modern, lightning-fast open-source IDM replacement with browser integration. | Kotlin / Compose Desktop | 🆓 Free (Apache-2.0) | Windows, Linux |
| [**Gopeed**](https://gopeed.com/) | Ultra-high performance multi-protocol engine across all desktop and mobile platforms. | Golang + Flutter | 🆓 Free (GPL-3.0) | Windows, macOS, Linux, Android, iOS |
| [**Rayburst**](https://github.com/AnInsomniacy/rayburst) | High-throughput, modular download engine engineered for modern gigabit bandwidth. | Rust / Modern Web | 🆓 Free (MIT) | Windows, macOS, Linux |
| [**Motrix**](https://motrix.app/) | Full-featured, elegant desktop manager supporting HTTP, FTP, BitTorrent, and Magnet. | Electron + aria2 | 🆓 Free (MIT) | Windows, macOS, Linux |
| [**aria2**](https://github.com/aria2/aria2) | The definitive multi-protocol, multi-source command-line download accelerator. | C++ | 🆓 Free (GPL-2.0) | Linux, macOS, Windows, Android, FreeBSD |

<details>
<summary>🔍 <b>Architecture & Axioms: AB Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Proprietary tools like IDM dominate Windows download acceleration through aggressive dynamic socket chunking but remain closed-source and platform-restricted. AB Download Manager re-engineers this multithreaded chunking architecture atop Kotlin and Jetpack Compose Desktop, delivering an open, transparent, and multiplatform IDM alternative.
- **Technical Citations & Proof**: [https://github.com/amir1376/ab-download-manager#features](https://github.com/amir1376/ab-download-manager#features), [https://github.com/amir1376/ab-download-manager/releases](https://github.com/amir1376/ab-download-manager/releases)
- **Key Strengths**: Modern Jetpack Compose desktop interface; Native multi-part connection splitting and queue scheduling; Official Chrome and Firefox companion extensions
- **Engineering Tradeoffs**: Native BitTorrent protocol is not yet embedded; focused strictly on HTTP/HTTPS/FTP stream acceleration.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Gopeed</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Aria2 established the gold standard for headless protocol multiplexing, but decoupling the CLI daemon from separate WebUI clients created significant operational friction. Gopeed unifies high-concurrency Go concurrency primitives with a reactive Flutter client into a single zero-dependency binary running identically across mobile and desktop.
- **Technical Citations & Proof**: [https://github.com/GopeedLab/gopeed#architecture](https://github.com/GopeedLab/gopeed#architecture), [https://github.com/GopeedLab/gopeed/releases](https://github.com/GopeedLab/gopeed/releases)
- **Key Strengths**: Embedded BitTorrent, Magnet, and HTTP/FTP engine; Cross-platform mobile and desktop consistency; JavaScript extension ecosystem for custom extractors
- **Engineering Tradeoffs**: Does not bundle advanced stream scraping (HLS/DASH) natively without user-installed extensions.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Rayburst</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Legacy download managers frequently bottleneck on high-bandwidth fiber connections due to memory allocation overhead and single-threaded queue arbitration. Rayburst leverages Rust zero-cost abstractions and asynchronous I/O to maximize bandwidth saturation with minimal CPU overhead.
- **Technical Citations & Proof**: [https://github.com/AnInsomniacy/rayburst#readme](https://github.com/AnInsomniacy/rayburst#readme)
- **Key Strengths**: Ultra-low memory footprint; High-concurrency async socket chunking; Modern clean architectural stack
- **Engineering Tradeoffs**: Relatively recent ecosystem; plugin support continues active development.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Motrix</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Complex torrent and multi-source download tooling historically suffered from cluttered, utilitarian interfaces. Motrix packaged the raw performance of aria2c within a polished, minimalist desktop interface that made advanced protocol downloading accessible to non-technical users.
- **Technical Citations & Proof**: [https://motrix.app/](https://motrix.app/), [https://github.com/agalwood/Motrix](https://github.com/agalwood/Motrix)
- **Key Strengths**: Sleek, distraction-free user interface; Automatic tracker updating; Supports up to 64 concurrent download threads
- **Engineering Tradeoffs**: Electron runtime memory footprint is higher than pure native alternatives.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: aria2</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Maximizing bandwidth utilization over unreliable networks requires simultaneous multi-source segment downloading across HTTP, FTP, and BitTorrent simultaneously. aria2 established the protocol-multiplexed chunking model that powers nearly all modern open-source download GUIs.
- **Technical Citations & Proof**: [https://aria2.github.io/manual/en/html/README.html](https://aria2.github.io/manual/en/html/README.html), [https://github.com/aria2/aria2](https://github.com/aria2/aria2)
- **Key Strengths**: Negligible CPU and RAM overhead; Full JSON-RPC and XML-RPC remote control; Metalink and BitTorrent chunk verification
- **Engineering Tradeoffs**: Pure command-line tool; requires a separate WebUI or frontend client for desktop users.

</details>

---

## 💻 Modern Desktop Powerhouses (GUI)

| Software & Link | Description | License | Supported OS |
| :--- | :--- | :--- | :--- |
| [**Internet Download Manager (IDM)**](https://www.internetdownloadmanager.com/) | Benchmark commercial download accelerator with robust browser catching. | 💵 Proprietary | Windows |
| [**Free Download Manager (FDM)**](https://www.freedownloadmanager.org/) | Established all-in-one download manager supporting torrents and media. | 💵 Proprietary (Free) | Windows, macOS, Linux, Android |

<details>
<summary>🔍 <b>Architecture & Axioms: Internet Download Manager (IDM)</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Web browsers frequently drop long-running file transfers and throttle single-stream downloads. IDM implemented dynamic file segmentation with persistent socket reuse, establishing the de facto speed benchmark for Windows desktop download management.
- **Technical Citations & Proof**: [https://www.internetdownloadmanager.com/](https://www.internetdownloadmanager.com/)
- **Key Strengths**: Unmatched browser integration and dynamic video catching; Lightweight native Windows executable; Resilient resume capability
- **Engineering Tradeoffs**: Closed source, commercial license required after 30-day trial, Windows-only.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Free Download Manager (FDM)</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Desktop users often juggle separate software for web downloads and BitTorrent transfers. FDM combines both into a single freeware client with scheduled traffic throttling and browser catching across all major desktop OSes.
- **Technical Citations & Proof**: [https://www.freedownloadmanager.org/features.htm](https://www.freedownloadmanager.org/features.htm)
- **Key Strengths**: Combined HTTP and BitTorrent queue; Traffic shaper to prevent bandwidth hogging; Native clients for Windows, macOS, Linux, and Android
- **Engineering Tradeoffs**: Closed source freeware.

</details>

---

## 🐧 Native Linux Ecosystem

| Software & Link | Description | Backend Engine | License |
| :--- | :--- | :--- | :--- |
| [**Open Download Manager**](https://github.com/getodm/open-download-manager) | Native Linux manager with unified queue for HTTP, Torrents, yt-dlp, and mirrors. | Java 25 + GTK4 / Libadwaita | 🆓 Free (GPL-3.0) |
| [**Persepolis Download Manager**](https://persepolisdm.github.io/) | Lightweight Python/Qt GUI frontend for the aria2 download engine. | Python + PyQt + aria2 | 🆓 Free (GPL-3.0) |
| [**uGet**](https://github.com/ugetdm/uget) | Classic lightweight multi-connection download manager with clipboard monitoring. | C + GTK3 | 🆓 Free (LGPL-2.1) |

<details>
<summary>🔍 <b>Architecture & Axioms: Open Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Linux desktop environments lack a cohesive, native download client that unifies diverse protocol engines. Open Download Manager solves this by orchestrating trusted system binaries (aria2, yt-dlp, and httrack) behind a native GTK4/Libadwaita interface with persistent crash-safe queue recovery.
- **Technical Citations & Proof**: [https://github.com/getodm/open-download-manager#features](https://github.com/getodm/open-download-manager#features), [https://github.com/getodm/open-download-manager/releases](https://github.com/getodm/open-download-manager/releases)
- **Key Strengths**: Native GNOME/GTK4 look and feel; Unified queue across HTTP, Torrent, and video extractors; Tor and proxychains routing support
- **Engineering Tradeoffs**: Requires host dependencies (aria2, yt-dlp) or running via standalone AppImage.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Persepolis Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: While aria2 provides unparalleled speed, non-developer users struggle with CLI flags and configuration files. Persepolis provides a native PyQt interface that manages aria2 daemon lifecycles transparently in the background.
- **Technical Citations & Proof**: [https://persepolisdm.github.io/](https://persepolisdm.github.io/), [https://github.com/persepolisdm/persepolis](https://github.com/persepolisdm/persepolis)
- **Key Strengths**: Multi-segment downloading via aria2c; Video downloading integration; Scheduled queue downloads
- **Engineering Tradeoffs**: Relies on background daemon management which can occasionally desynchronize on non-standard OS setups.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: uGet</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Resource-constrained Linux installations need a download manager that uses minimal memory. uGet was written in pure C with GTK to provide multi-connection acceleration with virtually zero memory overhead.
- **Technical Citations & Proof**: [https://github.com/ugetdm/uget](https://github.com/ugetdm/uget)
- **Key Strengths**: Ultra-low memory footprint (< 30MB); Dual backend engine support (curl or aria2); Clipboard watcher and batch imports
- **Engineering Tradeoffs**: Infrequent maintenance cycles; older GTK3 interface.

</details>

---

## ⚡ Command-Line & Terminal Power (CLI / TUI)

| Tool & Link | Description | Primary Strength | License |
| :--- | :--- | :--- | :--- |
| [**aria2**](https://github.com/aria2/aria2) | The definitive multi-protocol, multi-source command-line download accelerator. | C++ | 🆓 Free (GPL-2.0) |
| [**Surge**](https://github.com/SurgeDM/Surge) | Blazing fast Terminal User Interface (TUI) download manager built for power users. | Go | 🆓 Free (MIT) |

<details>
<summary>🔍 <b>Architecture & Axioms: aria2</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Maximizing bandwidth utilization over unreliable networks requires simultaneous multi-source segment downloading across HTTP, FTP, and BitTorrent simultaneously. aria2 established the protocol-multiplexed chunking model that powers nearly all modern open-source download GUIs.
- **Technical Citations & Proof**: [https://aria2.github.io/manual/en/html/README.html](https://aria2.github.io/manual/en/html/README.html), [https://github.com/aria2/aria2](https://github.com/aria2/aria2)
- **Key Strengths**: Negligible CPU and RAM overhead; Full JSON-RPC and XML-RPC remote control; Metalink and BitTorrent chunk verification
- **Engineering Tradeoffs**: Pure command-line tool; requires a separate WebUI or frontend client for desktop users.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Surge</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Command-line downloaders like curl or aria2 lack dynamic, interactive terminal queue visualization without opening separate monitoring ports. Surge delivers an interactive keyboard-driven TUI that provides real-time chunk progress, speed graphs, and queue management inside SSH sessions.
- **Technical Citations & Proof**: [https://github.com/SurgeDM/Surge#readme](https://github.com/SurgeDM/Surge#readme)
- **Key Strengths**: Interactive terminal UI with keyboard shortcuts; Concurrent chunk acceleration in Go; Zero graphical dependencies
- **Engineering Tradeoffs**: Targeted specifically at terminal and server operators; no desktop browser extension.

</details>

---

## 🧩 Browser Extensions

| Extension & Link | Description | Target Browsers | License |
| :--- | :--- | :--- | :--- |
| [**DownThemAll!**](https://www.downthemall.net/) | Advanced in-browser batch download utility with regex filtering. | Firefox, Chrome, Edge, Opera | 🆓 Free (GPL-2.0) |
| [**Chrono Download Manager**](https://chromewebstore.google.com/detail/chrono-download-manager/mciiogijehkdemklbdcbfkefimifhecn) | Complete download manager integrated directly inside the browser tab. | Chrome, Edge, Brave | 💵 Proprietary (Free) |

<details>
<summary>🔍 <b>Architecture & Axioms: DownThemAll!</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Downloading dozens of links or images from a webpage manually is tedious and prone to rate limits. DownThemAll! introduces advanced batch pattern matching and multi-stream acceleration directly inside browser tabs without external executables.
- **Technical Citations & Proof**: [https://www.downthemall.net/](https://www.downthemall.net/), [https://github.com/downthemall/downthemall](https://github.com/downthemall/downthemall)
- **Key Strengths**: 1-click download of all page media; Regular expression filename mask filters; Zero external binary dependencies
- **Engineering Tradeoffs**: Subject to browser WebExtension API limitations on socket management.

</details>

<details>
<summary>🔍 <b>Architecture & Axioms: Chrono Download Manager</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Traditional browser download shelves are minimal and lack queue management. Chrono replaces the default Chromium downloads shelf with a full tab-based management console, video sniffer, and batch downloader.
- **Technical Citations & Proof**: [https://chromewebstore.google.com/detail/chrono-download-manager/mciiogijehkdemklbdcbfkefimifhecn](https://chromewebstore.google.com/detail/chrono-download-manager/mciiogijehkdemklbdcbfkefimifhecn)
- **Key Strengths**: Replaces default browser download shelf; Built-in media sniffer for video and audio; Customizable rule filters
- **Engineering Tradeoffs**: Closed source.

</details>

---

## 🌐 Self-Hosted & Server Daemons

| Software & Link | Description | Technology | License |
| :--- | :--- | :--- | :--- |
| [**pyLoad**](https://github.com/pyload/pyload) | Pure Python lightweight download manager designed for NAS, Homelabs, and servers. | Python | 🆓 Free (GPL-3.0) |

<details>
<summary>🔍 <b>Architecture & Axioms: pyLoad</b> <i>(Click to expand)</i></summary>

- **Design Axiom**: Servers, NAS appliances, and Docker homelabs require an always-on headless download service that can be managed via Web UI, mobile app, or CLI without running a desktop environment. pyLoad provides a modular server architecture with built-in CAPTCHA handling and hoster plugins.
- **Technical Citations & Proof**: [https://github.com/pyload/pyload#readme](https://github.com/pyload/pyload#readme)
- **Key Strengths**: Headless core with responsive Web UI; Extensive plugin system for file hosters; REST API for remote automation
- **Engineering Tradeoffs**: Requires container or Python environment setup.

</details>

---

## 🛡️ Curation & Verification Standards

To guarantee a high signal-to-noise ratio, zero malware, and strict user privacy, all entries must pass our **Automated 4-Quadrant Verification**:

1. 🛡️ **Safe & Auditable**: Open-source tools MUST provide transparent, inspectable source code with an OSI-approved license. Binary-only distributions with missing or dummy source code (open-washing) are strictly rejected. No cracks, keygens, or pirated tools are accepted.
2. 💓 **Alive & Maintained**: The repository or website must be active, resolving HTTP 200, with commits or maintenance within the last 180 days.
3. ⭐ **High Social Proof**: Standard additions require community validation (≥ 1,000 stars on GitHub).
4. 🔥 **Trending Spotlight**: Fast-growing tools with breakout momentum are automatically spotlighted in the Trending category.

---

### Contributing

Have a download manager that meets our standards? Please read our [Contributor Guide](.github/pull_request_template.md) and submit a pull request!
