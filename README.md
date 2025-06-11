# 🔍 OSINT Logging System

Ce système de logs permet d'afficher en **temps réel** les messages importants d'un script Python (progression, succès, erreurs) dans une **fenêtre de terminal séparée**.

---

## 📁 Fichiers inclus

- `logger.py` : Fichier principal pour gérer les logs (importable dans d'autres scripts).
- `log_receiver.py` : Terminal de lecture des logs (lancé séparément).

---

## ⚙️ Fonctionnement

1. `logger.py` utilise une **file partagée (Queue)** pour envoyer des messages.
2. `log_receiver.py` lit cette file dans un autre terminal.
3. Chaque message est coloré selon son type (en cours, terminé, erreur).

---

## 🚀 Utilisation

### 1. Lancer le terminal de logs

Dans ton script principal (ex. `main.py`) :

```python
from logger import log_en_cours, log_termine, log_erreur, open_log_terminal

open_log_terminal()  # Démarre la fenêtre de logs

log_en_cours("Démarrage du programme")
log_termine("Action réussie")
log_erreur("Une erreur est survenue")
```

### 2. Structure recommandée

```
mon_projet/
├── main.py
├── logger.py
├── log_receiver.py
└── ...
```

---

## 💡 Remarques

- Assure-toi d'avoir `colorama` installé :
  ```bash
  pip install colorama
  ```

- Le terminal de log utilise :
  - `gnome-terminal` sous Linux
  - `Terminal` sous macOS
  - `cmd` sous Windows

- Si ton terminal par défaut est différent (ex : `konsole`, `xterm`), tu peux modifier `open_log_terminal()` dans `logger.py`.

---

## ✅ Exemples de messages

```
[⏳ EN COURS ] Analyse du compte @john_doe
[✅ TERMINÉ ] Extraction terminée pour @john_doe
[❌ ERREUR  ] Compte introuvable
```

---

## 🧠 Auteurs

Créé pour un projet d'automatisation OSINT — adaptable à tout autre projet Python.
