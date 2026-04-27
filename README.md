# 🎲 Number Guessing Game — Codeveda Python Internship

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Internship](https://img.shields.io/badge/Internship-Codeveda-green?style=flat-square)
![Level](https://img.shields.io/badge/Level-1-brightgreen?style=flat-square)
![Task](https://img.shields.io/badge/Task-2-orange?style=flat-square)
![Type](https://img.shields.io/badge/Type-Console%20Game-teal?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

> A console-based number guessing game built with Python. A random integer is generated between 1 and 100 and the player has 7 attempts to identify it — with directional feedback (higher/lower) after every incorrect guess.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Gameplay](#gameplay)
- [Sample Output](#sample-output)
- [Technical Architecture](#technical-architecture)
- [Configuration](#configuration)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Author](#author)

---

## Overview

This project was developed as **Task 2** of the **Codeveda Python Internship – Level 1**. It implements an interactive, console-based number guessing game in which the program generates a secret random integer and challenges the player to determine it within a constrained number of attempts.

After each incorrect guess, the game provides directional feedback — informing the player whether the secret number is **higher** or **lower** than their guess — enabling a binary-search style of reasoning to narrow down the answer efficiently.

---

## ✨ Features

- ✅ Cryptographically seeded random integer generation via the `random` module
- ✅ Configurable number range (`LOWER_BOUND` to `UPPER_BOUND`)
- ✅ Configurable maximum attempts (`MAX_ATTEMPTS`)
- ✅ Directional feedback — **"Too high"** / **"Too low"** after each wrong guess
- ✅ Attempt counter displayed on every turn
- ✅ Win/loss detection with a descriptive end-game message
- ✅ Full input validation — rejects non-integer and out-of-range entries
- ✅ Type-annotated functions with docstrings throughout

---

## 📁 Project Structure

```
Codeveda_task2_number_guessing_game/
│
└── task2_number_guessing_game.py    # Main game module (127 lines, 101 loc · 3.67 KB)
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/f-anselm88/Codeveda_task2_number_guessing_game.git
```

2. Navigate into the project directory:

```bash
cd Codeveda_task2_number_guessing_game
```

3. Run the game:

```bash
python task2_number_guessing_game.py
```

No external dependencies required — built entirely on the Python standard library (`random`).

---

## 🕹️ Gameplay

At the start of each session, the program silently generates a random integer between **1 and 100**. The player has a maximum of **7 attempts** to guess the correct number.

After each incorrect guess, the game responds with directional feedback to help the player converge on the answer. The optimal strategy — binary search — can guarantee success in at most 7 attempts for any number in the 1–100 range.

---

## 📊 Sample Output

**Winning run:**

```
============================================================
       Welcome to the Number Guessing Game!
  Guess the number between 1 and 100. You have 7 attempts.
============================================================

Attempt 1 of 7 — Enter your guess: 50
  ↑  Too low! Try higher.

Attempt 2 of 7 — Enter your guess: 75
  ↓  Too high! Try lower.

Attempt 3 of 7 — Enter your guess: 63
  ↑  Too low! Try higher.

Attempt 4 of 7 — Enter your guess: 69
  🎉 Correct! You guessed the number in 4 attempts. Well done!
```

**Game over:**

```
Attempt 7 of 7 — Enter your guess: 42
  ✗  Out of attempts! The number was 57. Better luck next time.
```

---

## 🏗️ Technical Architecture

### Module Dependency

```
task2_number_guessing_game.py
    │
    └── random    # Random integer generation (random.randint)
```

### Game Loop Flow

```
play_game()
    │
    ├── generate_secret_number()    ── random.randint(LOWER_BOUND, UPPER_BOUND)
    │
    └── Loop (attempt 1 → MAX_ATTEMPTS)
            │
            ├── get_player_guess()  ── Validates integer input and range
            ├── evaluate_guess()    ── Compares guess to secret; returns feedback
            │       │
            │       ├── "Too low"   ── guess < secret
            │       ├── "Too high"  ── guess > secret
            │       └── "Correct"   ── guess == secret → WIN
            │
            └── Exhausted attempts  ── reveal secret → LOSS
```

---

## ⚙️ Configuration

All game parameters are defined as typed constants at the top of `task2_number_guessing_game.py`. Adjust these values to change the difficulty without modifying any game logic:

| Constant | Type | Default | Description |
|---|---|---|---|
| `LOWER_BOUND` | `int` | `1` | Minimum value of the random number range |
| `UPPER_BOUND` | `int` | `100` | Maximum value of the random number range |
| `MAX_ATTEMPTS` | `int` | `7` | Maximum guesses allowed per game session |

**Example — Harder difficulty:**

```python
LOWER_BOUND: int = 1
UPPER_BOUND: int = 500
MAX_ATTEMPTS: int = 5
```

---

## 🧠 Concepts Demonstrated

This project showcases the following Python programming fundamentals:

- **Randomisation** — `random.randint()` for non-deterministic secret number generation
- **Loops** — `for` loop driving the fixed-attempt game cycle
- **Conditionals** — branching logic for higher/lower/correct feedback and win/loss evaluation
- **Input validation** — `try/except ValueError` to handle non-integer input gracefully
- **Type annotations** — all constants and functions use explicit `int` type hints
- **Constants** — `LOWER_BOUND`, `UPPER_BOUND`, and `MAX_ATTEMPTS` centralise configuration
- **Modular functions** — each game responsibility is isolated in a dedicated function
- **Basic I/O** — `input()` and `print()` for a clean, interactive console experience

---

## 👤 Author

**Anselm Munango**
- GitHub: [@f-anselm88](https://github.com/f-anselm88)
- Programme: Codeveda Python Internship – Level 1

---

*Built as part of a structured internship programme to demonstrate applied Python skills in randomisation, control flow, input validation, and interactive console application design.*
