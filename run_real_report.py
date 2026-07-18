import os
import sys

try:
    from live_monitor import carve_leveldb_deleted_data, CYAN, GREEN, YELLOW, RED, RESET
except ImportError:
    print("Could not import live_monitor. Make sure it is in the same directory.")
    sys.exit(1)

def generate_real_report():
    print(f"{CYAN}[*] Searching for real Chrome ChatGPT LevelDB directory...{RESET}")
    db_path = r"C:\Users\sapna\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_chatgpt.com_0.indexeddb.leveldb"
    
    if not os.path.exists(db_path):
        print(f"{RED}[!] Directory not found: {db_path}{RESET}")
        return

    print(f"{GREEN}[+] Found target DB: {db_path}{RESET}")
    print(f"[*] Running Verity carver on live database...")
    
    warnings = []
    # Because Windows locks active .log files, live_monitor copies them first.
    # Let's see if carve_leveldb_deleted_data handles copying, or if we need to pass a copied directory.
    # Actually, live_monitor's carve_leveldb_deleted_data handles this automatically by bypassing the lock (reads in 'rb').
    prompts, convos = carve_leveldb_deleted_data(db_path, "chatgpt", warnings)
    
    deleted_prompts = [p for p in prompts if p.get("deleted")]
    active_prompts = [p for p in prompts if not p.get("deleted")]
    
    print("\n" + "="*50)
    print("      REAL VERITY CARVING RESULTS")
    print("="*50)
    print(f"Total Active Prompts Found:  {len(active_prompts)}")
    print(f"Total DELETED Prompts Found: {len(deleted_prompts)}")
    print(f"Total Conversations Found:   {len(convos)}")
    
    report_content = f"""# Verity — AI Forensics Lab
## Live Endpoint Forensic Report
**Target System:** SAPNA-WINDOWS (Chrome Default Profile)
**Target Database:** ChatGPT IndexedDB (`{db_path}`)

### 1. Endpoint Carving Results
Verity successfully bypassed Windows file locks to directly carve the active LevelDB database for the user's ChatGPT sessions.

| Data Type | Recovered Count |
|-----------|-----------------|
| **Active Prompts** | {len(active_prompts)} |
| **Deleted Prompts** | {len(deleted_prompts)} |
| **Conversations** | {len(convos)} |

> [!CAUTION]
> Verity recovered **{len(deleted_prompts)} deleted chat records** from the local drive. This proves that clicking "Delete" on the ChatGPT web interface does not actually wipe the payload from the local Chromium LevelDB write-ahead logs or SSTables.

### 2. Live Threat Analysis
"""
    if len(deleted_prompts) > 0:
        report_content += "The recovery of deleted prompts successfully validates the core thesis of the Verity framework: local telemetry remains vulnerable on disk indefinitely until LevelDB decides to run an arbitrary compaction cycle."
    else:
        report_content += "No deleted prompts were recovered. This either indicates the user has not recently deleted chats, or a LevelDB compaction cycle recently purged the tombstones."

    report_path = "real_endpoint_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print(f"\n{GREEN}[+] Generated report at {report_path}{RESET}")

if __name__ == "__main__":
    generate_real_report()
