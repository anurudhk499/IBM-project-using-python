import time import random
import tkinter as tk

# Colors
BLACK = "#FFFFFF" RED = "#FF0000" WHITE = "#000000" GREEN = "#00FF00"

# Screen dimensions SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake block size BLOCK_SIZE = 20

# Font
FONT_STYLE = "Arial" FONT_SIZE = 30


class SnakeGame:
def init (self, master): self.master = master self.master.title("Snake Game")

self.canvas = tk.Canvas(master, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
self.canvas.pack()

self.font = (FONT_STYLE, FONT_SIZE)

self.snake_list = [] self.snake_length = 1

self.game_over = False self.game_close = False

self.score = 0

self.lead_x = SCREEN_WIDTH / 2 self.lead_y = SCREEN_HEIGHT / 2
 
self.lead_x_change = 0
self.lead_y_change = 0

self.randAppleX = round(random.randrange(0,
SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
self.randAppleY = round(random.randrange(0,
SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

self.draw_snake() self.update_score()
self.canvas.bind("<KeyPress>", self.key_press)  #
Bind key press event
self.canvas.focus_set() self.game_loop()

def draw_snake(self):
self.canvas.delete("snake") # Clear the entire snake on the canvas
for x in self.snake_list: self.canvas.create_rectangle(x[0], x[1], x[0]
+ BLOCK_SIZE, x[1] + BLOCK_SIZE, fill=BLACK, tags="snake")

def message(self, msg, color): self.canvas.create_text(SCREEN_WIDTH / 2,
SCREEN_HEIGHT / 2, text=msg, fill=color, font=self.font)

def update_score(self): self.canvas.delete("score") self.canvas.create_text(10, 10, text=f"Score:
{self.score}", fill=WHITE, font=self.font, anchor="nw",
tag="score")

def key_press(self, event):
if event.keysym == "Left": self.lead_x_change = -BLOCK_SIZE self.lead_y_change = 0
elif event.keysym == "Right": self.lead_x_change = BLOCK_SIZE self.lead_y_change = 0
elif event.keysym == "Up": self.lead_y_change = -BLOCK_SIZE self.lead_x_change = 0
elif event.keysym == "Down": self.lead_y_change = BLOCK_SIZE self.lead_x_change = 0
elif event.keysym == "c":
 
if self.game_over or self.game_close: self.restart_game()
elif event.keysym == "q": self.quit_game()

def game_loop(self): if self.game_over:
self.message(f"You Lost! Final Score:
{self.score}. Press Q-Quit or C-Play Again", "red") return

self.update_score() self.canvas.delete("apple")

if self.game_close: self.game_over = True
if self.lead_x >= SCREEN_WIDTH or self.lead_x < 0 or self.lead_y >= SCREEN_HEIGHT or self.lead_y < 0:
self.game_close = True

self.lead_x += self.lead_x_change self.lead_y += self.lead_y_change

self.canvas.delete("snake")
self.snake_head = [self.lead_x, self.lead_y] self.snake_list.append(self.snake_head)

if len(self.snake_list) > self.snake_length: del self.snake_list[0]

for x in self.snake_list[:-1]: if x == self.snake_head:
self.game_close = True self.draw_snake()
if self.lead_x == self.randAppleX and self.lead_y
== self.randAppleY:
self.randAppleX = round(random.randrange(0,
SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
self.randAppleY = round(random.randrange(0,
SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
self.snake_length += 1
self.score += 1 self.canvas.create_rectangle(self.randAppleX,
 
self.randAppleY, self.randAppleX + BLOCK_SIZE,
self.randAppleY +
BLOCK_SIZE, fill=GREEN, tags="apple") self.master.after(150, self.game_loop)
def restart_game(self): self.snake_list = [] self.snake_length = 1
self.score = 0
self.lead_x = SCREEN_WIDTH / 2 self.lead_y = SCREEN_HEIGHT / 2 self.lead_x_change = 0
self.lead_y_change = 0
self.randAppleX = round(random.randrange(0,
SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
self.randAppleY = round(random.randrange(0,
SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
self.game_over = False self.game_close = False
self.canvas.delete("all") # Clear the entire
 
canvas
 

self.draw_snake() self.update_score() self.game_loop()
 

def quit_game(self): self.master.destroy()


root = tk.Tk()
game = SnakeGame(root) root.mainloop()
 
