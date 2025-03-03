import subprocess
import sys
import os
from datetime import datetime

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Fehler bei '{command}': {result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def git_commit_and_push():
    try:
        # Verzeichnis wechseln
        os.chdir("/games/modpack-medival")
        
        # Aktuelles Datum und Uhrzeit ermitteln
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M MESZ")
        commit_message = f"World Save {timestamp}"
        
        # Änderungen zum Staging hinzufügen
        run_command("git add .")
        
        # Änderungen committen
        run_command(f"git commit -m \"{commit_message}\"")
        
        # Änderungen pushen
        run_command("git push")
        
        print("Änderungen erfolgreich gepusht!")
    except SystemExit:
        print("Fehler beim Commit oder Push.")

if __name__ == "__main__":
    git_commit_and_push()
