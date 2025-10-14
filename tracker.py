#!/usr/bin/env python3

# -------- COMMANDES --------

# python tracker.py total   # affiche le temps total cumulé
# python tracker.py clear   # supprime tout l’historique
# python tracker.py start <task>
# python tracker.py stop

import sys
import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.time_tracker_log.txt")

def start_task(description):
    now = datetime.now()
    with open(LOG_FILE, "a") as f:
        f.write(f"START|{now.isoformat()}|{description}\n")
    print(f"Tache démarree : {description} a {now.strftime('%H:%M:%S')}")

def stop_task():
    now = datetime.now()
    lines = []
    start_time = None
    description = None

    if not os.path.exists(LOG_FILE):
        print("Aucune tache en cours.")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("START") and "END" not in lines[i]:
            parts = lines[i].strip().split("|")
            start_time = datetime.fromisoformat(parts[1])
            description = parts[2]
            lines[i] = lines[i].strip() + f"|END|{now.isoformat()}|DUREE|{(now-start_time).total_seconds()/60:.2f} min\n"
            break

    if start_time is None:
        print("Aucune tache a stopper.")
        return

    with open(LOG_FILE, "w") as f:
        f.writelines(lines)

    print(f"Tache terminee : {description} a {now.strftime('%H:%M:%S')} - Duree {(now-start_time)}")

def total_time():
    if not os.path.exists(LOG_FILE):
        print("Aucun historique.")
        return

    total_seconds = 0
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "DUREE" in line:
                parts = line.strip().split("|")
                # la durée est en minutes
                total_seconds += float(parts[-1].split()[0]) * 60

    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"Temps total passe sur toutes les taches : {int(hours)}h {int(minutes)}m {int(seconds)}s")

def clear_history():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        print("Historique supprime.")
    else:
        print("Aucun historique a supprimer.")

def main():
    if len(sys.argv) < 2:
        print("Usage : tracker.py start <description> | stop | total | clear")
        return

    cmd = sys.argv[1].lower()
    if cmd == "start" and len(sys.argv) >= 3:
        description = " ".join(sys.argv[2:])
        start_task(description)
    elif cmd == "stop":
        stop_task()
    elif cmd == "total":
        total_time()
    elif cmd == "clear":
        clear_history()
    else:
        print("Commande invalide. Usage : tracker.py start <description> | stop | total | clear")

if __name__ == "__main__":
    main()
