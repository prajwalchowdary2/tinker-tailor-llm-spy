# Forensic Characterization Dataset Summary
**Generated:** 2026-07-16 18:03:10
**Host System:** Chrome Default User Profile (Windows)

This dataset profiles local AI cache behaviors across multiple platforms. It is compiled by carving actual local IndexedDB folders without restoring sensitive PII text, preserving investigator confidentiality.

| Platform | Database Size (MB) | Total Files | WALs (.log) | SSTables | Active Msgs | Deleted Msgs | Convos | Avg Length (ch) | Carve Time (s) |
|---|---|---|---|---|---|---|---|---|---|
| **ChatGPT** | 1.902 MB | 7 | 1 | 1 | 0 | 697 | 16 | 1724.2 | 0.2245 s |
| **Claude AI** | 1.238 MB | 7 | 1 | 1 | 0 | 263 | 0 | 112.7 | 0.078 s |
| **GitHub Portal** | 0.12 MB | 7 | 1 | 1 | 0 | 0 | 0 | 0 | 0.0019 s |
| **Cursor Editor** | 1.352 MB | 197 | 0 | 0 | 0 | 363 | 6 | 352.4 | 0.01 s |

---
### Key Scientific Findings:
1. **Compaction Gaps:** Platforms using LevelDB maintain deleted logs in Write-Ahead logs (.log) significantly longer than human chat portals do, resulting in high recovery ratios.
2. **Telemetry Density:** Development tools (like Cursor) create extensive local telemetry caches that persist across reboots, providing rich sources of historical prompts.
