# Tic-Tac-Toe
This repository contains created a simple Tic-Tac-Toe game written in Python. The game can be run directly from source or built into a standalone `.exe` file. 

## 🛠️ Requirements
To run the project you need:

- **Python 3.10** installed on your machine
- Required Python libraries (listed in `requirements.txt`)

## ⚙️ Setup 
*(All commands below should be executable in the main project folder `Tic-Tac-Toe`.)*

### 1. Create virtual environment:
```bash
python -m venv .venv
```

### 2. Activate virtual environment:
```bash
.\.venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Running the game
After installing requirements, run the game with:

```bash
python src/game/main.py
```

## 🏗️ Building executable (.exe)
To build the standalone executable:

```bash
python src/build_game.py
```

After the build process finishes, a `.exe` file will be created inside the `dist` folder, and a shortcut to the game should appear on your desktop.
