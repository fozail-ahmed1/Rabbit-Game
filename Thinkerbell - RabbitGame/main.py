import os
import random
from collections import deque

class RabbitGame():
    def __init__(self, map_length=100):
        self.map_length = map_length
        self.game_map = [["_" for _ in range(self.map_length)] for _ in range(self.map_length)]
        self.carrots = []
        self.rabbit_holes = []
        self.rabbit_position = None
        self.rabbit_with_carrot = False
        self.quit_game = False

    def generate_map(self):
        # Place rabbit at a random position
        self.rabbit_position = (random.randint(0, self.map_length-1), random.randint(0, self.map_length-1))
        self.game_map[self.rabbit_position[0]][self.rabbit_position[1]] = "r"

        # Place carrots
        num_carrots = int(input("Enter the number of carrots: "))
        self.carrots = []
        for _ in range(num_carrots):
            while True:
                x, y = random.randint(0, self.map_length-1), random.randint(0, self.map_length-1)
                if self.game_map[x][y] == "_":
                    self.carrots.append((x, y))
                    self.game_map[x][y] = "c"
                    break

        # Place rabbit holes
        num_holes = int(input("Enter the number of rabbit holes: "))
        self.rabbit_holes = []
        for _ in range(num_holes):
            while True:
                x, y = random.randint(0, self.map_length-1), random.randint(0, self.map_length-1)
                if self.game_map[x][y] == "_":
                    self.rabbit_holes.append((x, y))
                    self.game_map[x][y] = "O"
                    break

    def print_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.game_map:
            print(" ".join(row))

    def move_rabbit(self, dx, dy):
        x, y = self.rabbit_position
        new_x, new_y = x + dx, y + dy

        if self.rabbit_with_carrot:
            new_char = "R"
        else:
            new_char = "r"

        if 0 <= new_x < self.map_length and 0 <= new_y < self.map_length:
            if self.game_map[new_x][new_y] == "_":
                self.game_map[x][y] = "_"
                self.rabbit_position = (new_x, new_y)
                self.game_map[new_x][new_y] = new_char

    def pick_carrot(self):
        if not self.rabbit_with_carrot:
            x, y = self.rabbit_position
            for carrot_x, carrot_y in self.carrots:
                if (x == carrot_x and abs(y - carrot_y) == 1) or (y == carrot_y and abs(x - carrot_x) == 1):
                    self.rabbit_with_carrot = True
                    self.carrots.remove((carrot_x, carrot_y))
                    self.game_map[carrot_x][carrot_y] = "_"
                    break
                
    def jump(self):
        if not self.rabbit_with_carrot:
            x, y = self.rabbit_position
            for hole_x, hole_y in self.rabbit_holes:
                if (x == hole_x and abs(y - hole_y) == 1) or (y == hole_y and abs(x - hole_x) == 1):
                    new_x, new_y = hole_x - x, hole_y - y
                    if 0 <= hole_x + new_x < self.map_length and 0 <= hole_y + new_y < self.map_length \
                            and self.game_map[hole_x + new_x][hole_y + new_y] == "_":
                        self.game_map[x][y] = "_"
                        self.rabbit_position = (hole_x + new_x, hole_y + new_y)
                        self.game_map[hole_x + new_x][hole_y + new_y] = "r"
                    break

    def deposit_carrot(self):
        if self.rabbit_with_carrot:
            x, y = self.rabbit_position
            for hole_x, hole_y in self.rabbit_holes:
                if (x == hole_x and abs(y - hole_y) == 1) or (y == hole_y and abs(x - hole_x) == 1):
                    self.game_map[x][y] = "_"
                    self.rabbit_with_carrot = False
                    self.game_map[x][y] = "r"
                    print("Congratulations! A Carrot has been dropped in a rabbit hole!")
                    return True

    def play(self):
        while not self.quit_game:
            self.print_map()
            action = input("Enter your action (a/w/d/s/j/p or q to quit): ").lower()

            if action == 'q':
                self.quit_game = True
                break
            elif action == 'a':
                self.move_rabbit(0, -1)
            elif action == 'd':
                self.move_rabbit(0, 1)
            elif action == 'w':
                self.move_rabbit(-1, 0)
            elif action == 's':
                self.move_rabbit(1, 0)
            elif action == 'j':
                self.jump()
            elif action == 'p':
                self.pick_carrot()
                if self.deposit_carrot():
                    self.quit_game = True
            elif action == 'solved':
                self.solve_game()
                break  

    # Solution generator       
    def find_shortest_path(self):
        start = self.rabbit_position
        target_hole = None
        for hole_x, hole_y in self.rabbit_holes:
            if hole_x == start[0] or hole_y == start[1]:
                target_hole = (hole_x, hole_y)
                break

        if not target_hole:
            print("No reachable rabbit hole.")
            return

        # Use BFS to find the shortest path
        queue = deque([(start, [])])
        visited = set()

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == target_hole:
                return path

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.map_length and 0 <= new_y < self.map_length and self.game_map[new_x][new_y] == "_":
                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        queue.append(((new_x, new_y), path + [(new_x, new_y)]))

    def solve_game(self):
        solution = self.find_shortest_path()
        if solution:
            for x, y in solution:
                self.game_map[self.rabbit_position[0]][self.rabbit_position[1]] = "_"
                self.rabbit_position = (x, y)
                self.game_map[x][y] = "r"
                self.print_map()
            self.deposit_carrot()
            print("Game solved!")

def main():
        map_length = int(input("Enter the grid size: "))
        game = RabbitGame(map_length)
        game.generate_map()
        game.play()

if __name__ == "__main__":
    main()
