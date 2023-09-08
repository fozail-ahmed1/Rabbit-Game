# Rabbit-Game
A simple command line game of rabbit's simple life.

# Story
A simple command-line game where you help a friendly rabbit named Mr. Bunny gather carrots from the yard and store them in his rabbit hole.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/fozail-ahmed1/Rabbit-Game.git
cd Rabbit-Game
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv ./venv
source ./venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Gameplay
- Launch the game by running python main.py in your terminal.

## Controls
 - Use the following keys to control Mr. Bunny:
   - a: Move left
   - d: Move right
   - w: Move up
   - s: Move down
   - j: Jump over a rabbit hole (only if you are adjacent to it)
   - p: Pick up a carrot (only if you are adjacent to it)

- Once Mr. Bunny picks up a carrot, his character changes from r to R.
- To deposit a carrot into a rabbit hole, position Mr. Bunny adjacent to the hole and press p.
- Press q to quit the game at any time

## Gameplay Rules
- Mr. Bunny can only hold one carrot at a time.
- The game ends when Mr. Bunny successfully deposits a carrot into any of the rabbit holes.

## Contributors
1. <a href="https://www.linkedin.com/in/fozail-ahmed1/">Fozail Ahmed </a>