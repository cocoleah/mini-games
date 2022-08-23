#########Import libraries#########
# !pip install pygame
# !pip install windows-curses
import curses
import random
import time

#########Create Screen#########
# user = input("Press enter to begin.")
s = curses.initscr()
sh, sw = s.getmaxyx()  # set screen to be height and width of window
sh = int(sh)
sw = int(sw)
w = curses.newwin(sh, sw, 0, 0)  # Create a window with sh and sw
w.keypad(1)  # Enable keypad mode, True = 1
curses.curs_set(0)  # hide blinking cursor, 0 = False

#########Initiation#########
score = 0

# Initial position of snake
snk_x = int(sw / 4)
snk_y = int(sh / 2)
snake_head = [snk_y, snk_x]

# Create snake body with 3 pixels horizontally
snake = [[snk_y, snk_x],
         [snk_y, snk_x - 1],
         [snk_y, snk_x - 2]]

# Create food
new_dollar = [int(sh / 2), int(sw / 2)]
w.addch(new_dollar[0], new_dollar[1], curses.ACS_STERLING)

# Initial direction of snake
prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT


#########Game play#########
def get_dollar(score):
    new_dollar = [random.randint(1, sh - 1), random.randint(1, sw - 1)]  # Create new $ location
    score += 1
    return new_dollar, score


# End game scenarios:
# (1) if Y position touches heightborder (2) if X Position touches widthborder
# (3) if snakehead touches any other part of snakebody
def game_over(snake_head):
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        return 1
    else:
        snake_head = snake[0]  # Update snake position
        if snake_head in snake[1:]:
            return 1
        else:
            return 0


while True:
    w.border(0)
    w.timeout(100)  # Refresh screen every 100 milliseconds

    next_key = w.getch()  # Takes user keypad input
    key = key if next_key == -1 else next_key

    # Moving the snake's position: 0-Left, 1-Right, 3-Up, 2-Down
    if key == curses.KEY_LEFT and prev_button_direction != 1:
        button_direction = 0
        snake_head[1] -= 1
    elif key == curses.KEY_RIGHT and prev_button_direction != 0:
        button_direction = 1
        snake_head[1] += 1
    elif key == curses.KEY_UP and prev_button_direction != 2:
        button_direction = 3
        snake_head[0] -= 1
    elif key == curses.KEY_DOWN and prev_button_direction != 3:
        button_direction = 2
        snake_head[0] += 1
    else:
        pass

    prev_button_direction = button_direction

    # Increase snake length to accumulate points
    if snake_head == new_dollar:
        new_dollar, score = get_dollar(score)
        snake.insert(0, list(snake_head))
        w.addch(new_dollar[0], new_dollar[1], curses.ACS_STERLING)

    else:
        snake.insert(0, list(snake_head))
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')  # Replace tail with empty space

    # Display snake
    try:
        w.addch(int(snake[0][0]), int(snake[0][1]), "#")
    except (curses.error):
        pass

    # On collision kill snake
    if game_over(snake_head) == 1:
        break

s.addstr(10, 30, 'Your Score is:  ' + str(score))
s.addstr(11, 30, 'Thank you for playing! :) ')
s.refresh()
time.sleep(5)
curses.endwin()
print("Game has ended.")