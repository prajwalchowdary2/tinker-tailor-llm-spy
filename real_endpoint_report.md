# Verity — AI Forensics Lab
## Live Endpoint Forensic Report
**Target System:** SAPNA-WINDOWS (Chrome Default Profile)
**Target Database:** ChatGPT IndexedDB (`C:\Users\sapna\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_chatgpt.com_0.indexeddb.leveldb`)

### 1. Endpoint Carving Results
Verity successfully bypassed Windows file locks to directly carve the active LevelDB database for the user's ChatGPT sessions.

| Data Type | Recovered Count |
|-----------|-----------------|
| **Active Prompts** | 0 |
| **Deleted Prompts** | 697 |
| **Conversations** | 16 |

> [!CAUTION]
> Verity recovered **697 deleted chat records** from the local drive. This proves that clicking "Delete" on the ChatGPT web interface does not actually wipe the payload from the local Chromium LevelDB write-ahead logs or SSTables.

### 2. Live Threat Analysis
The recovery of deleted prompts successfully validates the core thesis of the Verity framework: local telemetry remains vulnerable on disk indefinitely until LevelDB decides to run an arbitrary compaction cycle.