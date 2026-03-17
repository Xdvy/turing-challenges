![Poetry](https://img.shields.io/badge/poetry-managed-blueviolet)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-orange)
![Licence](https://img.shields.io/badge/license-MIT-green)

# 🧠 Turing Challenges Solver (Python)

## 🇬🇧 Overview

This project is a Python package designed to solve algorithmic challenges.
It provides structured, reusable implementations of algorithms and problem-solving strategies.
⚠️ Note: The project (problem statements, inputs, outputs) is entirely in French, as it targets a French-speaking audience.

## 🚀 Features

- Modular and reusable Python implementations
- Focus on clean code and problem structuring
- Designed for learning and solving algorithmic challenges
- Includes multiple solved problems from Turing challenges

---

## 🇫🇷 Description

Un package Python pour résoudre les défis Turing, avec un notebook de démonstration interactif.  
Chaque défi est encapsulé dans un module, et peut être exécuté via une interface en ligne de commande (CLI).
📌 Remarque : Ce projet est destiné à un usage pédagogique sur des problèmes francophones. Les données et les énoncés ne sont pas traduits.

Ce projet est conçu pour être :

- 📦 facilement installable avec **Poetry**,
- ⚙️ extensible (nouveaux challenges),
- 🧪 testable,
- 📝 utilisable via CLI et notebooks.

Ce dépôt contient :

- `src/turing_challenges/` – le package Python principal,
- `notebooks/` – notebook de démonstration & exploration des solutions,
- `tests/` – tests unitaires pour garantir la fiabilité des solutions,
- `pyproject.toml` & `poetry.lock` – configuration Poetry. :contentReference[oaicite:1]{index=1}

---

## 🛠️ Installation

Cloner le dépôt :

```bash
git clone https://github.com/Xdvy/turing-challenges.git
cd turing-challenges
```

Installer les dépendances avec Poetry :

```bash
poetry install
```

Activer l’environnement :
```bash
poetry shell
```

---

## 🖥️ Utilisation – Interface CLI

Lancer l’aide de l’outil :

```bash
poetry run turing-challenges --help
```

Devrait afficher les commandes disponibles telles que :

```bash
poetry run turing-challenges solve <challenge_id>
```

Avec `<challenge_id>` le numéro du challenge à résoudre.

---

## 📓 Notebooks de démonstration

Pour tester ou visualiser des solutions via Jupyter :

```bash
poetry run jupyter notebook
```

Puis ouvrir le notebook `notebooks/demo_challenges.ipynb`.

---

## 📂 Structure du projet

```code
turing-challenges/
├── notebooks/                 # Notebooks de démonstration
├── src/
│   └── turing_challenges/     # Package Python
├── tests/                     # Tests unitaires
├── pyproject.toml             # Configuration Poetry
├── poetry.lock                # Verrouillage des dépendances
└── README.md
```

---

## 🧪 Lancer les tests unitaires

Pour valider toutes les solutions et vérifier qu’elles fonctionnent comme prévu :

```bash
poetry run pytest
```

---

## 🧾 Licence

Ce projet est sous licence MIT.

---

## Exemple d’utilisation

```bash
$ poetry run turing-challenges solve 1
Résultat : 636456
Temps d'exécution : 0.0s
```