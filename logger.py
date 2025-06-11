# log_system/logger.py

import sys
import os
import platform
import subprocess
from multiprocessing import Queue
from multiprocessing.managers import BaseManager
from colorama import Fore, init

init(autoreset=True)

# Configuration du logger
log_queue = Queue()

class LogQueueManager(BaseManager): pass
LogQueueManager.register('get_queue', callable=lambda: log_queue)
manager = LogQueueManager(address=('', 50000), authkey=b'abc')
manager.start()

# Fonctions de log
def log_en_cours(msg):
    log_queue.put(f"{Fore.YELLOW}[⏳ EN COURS ] {msg}")

def log_termine(msg):
    log_queue.put(f"{Fore.GREEN}[✅ TERMINÉ ] {msg}")

def log_erreur(msg):
    log_queue.put(f"{Fore.RED}[❌ ERREUR  ] {msg}")

def open_log_terminal():
    os_type = platform.system()
    if os_type == "Windows":
        subprocess.Popen(["start", "cmd", "/k", "python", "log_system/log_receiver.py"], shell=True)
    elif os_type == "Linux":
        subprocess.Popen(["gnome-terminal", "--", "python3", "log_system/log_receiver.py"])
    elif os_type == "Darwin":
        apple_script = 'tell application "Terminal" to do script "python3 log_system/log_receiver.py"'
        subprocess.Popen(["osascript", "-e", apple_script])
    else:
        print("OS non reconnu")
        log_erreur("OS non reconnu")