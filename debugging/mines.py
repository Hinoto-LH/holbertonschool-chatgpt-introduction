#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        num_mines = min(mines, width * height -1)
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height) or self.revealed[y][x]:
            return True # Déjà révélé ou hors limite, ce n'est pas une défaite
        
        if (y * self.width + x) in self.mines:
            return False # Boum !
            
        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.reveal(x + dx, y + dy) # Propagation récursive
        return True

    def check_win(self):
        # On compte combien de cases sont encore cachées
        hidden_count = 0
        for row in self.revealed:
            hidden_count += row.count(False)
        # Si le nombre de cases cachées est égal au nombre de mines, c'est gagné !
        return hidden_count == len(self.mines)
    
    def play(self):
        while True:
            self.print_board()
            if self.check_win():
                print("Congratulations! You've won the game.")
                break
            try:
                x = int(input(f"Enter x (0-{self.width-1}): "))
                y = int(input(f"Enter y (0-{self.height-1}): "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()