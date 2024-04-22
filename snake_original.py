import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 25)

# Set up the clock
clock = pygame.time.Clock()

# Define the snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.speed = 10
        self.direction = "right"
        self.body = [(x, y), (x-self.size, y), (x-(2*self.size), y)]

    def move(self):
        # food_x, food_y = food.x(), food.y()
        # head_x, head_y = self.body[0]
        # if food_x > head_x:
        #     self.direction = "right"
        # elif food_x < head_x:
        #     self.direction = "left"
        # elif food_y > head_y:
        #     self.direction = "down"
        # elif food_y < head_y:
        #     self.direction = "up"
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def draw(self):
        for pos in self.body:
            pygame.draw.rect(screen, green, [pos[0], pos[1], self.size, self.size])

    def collide_with_wall(self):
        if self.x < 0 or self.x > width-self.size or self.y < 0 or self.y > height-self.size:
            return True
        else:
            return False

    def collide_with_food(self, food):
        if self.x == food.x and self.y == food.y:
            return True
        else:
            return False
    
    def collide_with_self(self):
        for pos in self.body[1:]:
            if self.x == pos[0] and self.y == pos[1]:
                return True
        return False

    def grow(self):
        self.body.append((self.x, self.y))

    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"

# Define the food class
class Food:
    def __init__(self):
        self.size = 10
        self.x = random.randint(0, (width - self.size) // self.size) * self.size
        self.y = random.randint(0, (height - self.size) // self.size) * self.size

    def draw(self):
        pygame.draw.rect(screen, red, [self.x, self.y, self.size, self.size])

# Create the snake and food objects
snake = Snake(width/2, height/2)
food = Food()

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction("right")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")

    # Move the snake
    snake.move()

    # Check for collision with the walls
    if snake.collide_with_wall() or snake.collide_with_self():
        game_over = True

    # Check for collision with the food
    if snake.collide_with_food(food):
        snake.grow()
        food = Food()

    # Draw the screen
    screen.fill(white)
    snake.draw()
    food.draw()

    # Update the score
    score = len(snake.body)-3
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(17)

# Display the GAME OVER text and final score
game_over_text = font.render("GAME OVER", True, black)
score_text = font.render("Final Score: " + str(score), True, black)
screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()))
screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2))
pygame.display.update()

# Wait for 10 seconds
pygame.time.wait(10000)
