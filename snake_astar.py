import pygame
import random
from datetime import datetime

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

    def move(self, graph, food, snake_body):
        print("x: " + str(self.x) + " y: " + str(self.y))
        path = astar(graph, self.body[0], (food.x, food.y), snake_body, width, height)
        #print("PATH: "+ str(path))
        if path:
            next_cell = path[0]
            #print("PATH NEXT: " + str(next_cell))
            head_x, head_y = self.body[0]

            # # Check if food is directly above or below the snake's head
            # if food.x == head_x:
            #     print("FOOD IS DIRECTLY ABOVE OR BELOW SNAKE'S HEAD")
            #     if food.y < head_y and self.direction != "down":
            #         self.direction = "up"
            #     elif food.y < head_y and self.direction == "down":
            #         if head_x < width // 2:
            #             self.direction = "left"
            #         else:
            #             self.direction = "right"
            #     elif food.y > head_y and self.direction != "up":
            #         self.direction = "down"
            #     elif food.y > head_y and self.direction == "up":
            #         if head_x < width // 2:
            #             self.direction = "left"
            #         else:
            #             self.direction = "right"
            # # Check if food is directly to the left or right of the snake's head
            # elif food.y == head_y:
            #     print("FOOD IS DIRECTLY LEFT OR RIGHT SNAKE'S HEAD")
            #     if food.x < head_x and self.direction != "right":
            #         self.direction = "left"
            #     elif food.x < head_x and self.direction == "left":
            #         if head_y < height // 2:
            #             self.direction = "up"
            #         else:
            #             self.direction = "down"
            #     elif food.x > head_x and self.direction != "left":
            #         self.direction = "right"
            #     elif food.x < head_x and self.direction == "right":
            #         if head_y < height // 2:
            #             self.direction = "up"
            #         else:
            #             self.direction = "down"
            
            # else:
            if next_cell[0] > head_x and self.direction != "left":  # Check if the next move is towards right and not coming from left
                self.direction = "right"
            elif next_cell[0] < head_x and self.direction != "right":  # Check if the next move is towards left and not coming from right
                self.direction = "left"
            elif next_cell[1] > head_y and self.direction != "up":  # Check if the next move is towards down and not coming from up
                self.direction = "down"
            elif next_cell[1] < head_y and self.direction != "down":  # Check if the next move is towards up and not coming from down
                self.direction = "up"
                
            # if self.direction == "right":
            #     self.x += self.speed
            # elif self.direction == "left":
            #     self.x -= self.speed
            # elif self.direction == "up":
            #     self.y -= self.speed
            # elif self.direction == "down":
            #     self.y += self.speed
            # self.body.insert(0, (self.x, self.y))
            # self.body.pop()
        else:
            print("NO PATH FOUND")
            head_x, head_y = self.body[0]
            if self.direction == "left":
                
                if head_x == 0:
                    if self.y < (height // 2):
                        path = astar(graph, self.body[0], (head_x, height-10), snake_body, width, height)
                    else:
                        path = astar(graph, self.body[0], (head_x, 0), snake_body, width, height)
                else:
                    path = astar(graph, self.body[0], (0, head_y), snake_body, width, height)
            elif self.direction == "right":
                
                if head_x == width-10:
                    if self.y < (height // 2):
                        path = astar(graph, self.body[0], (head_x, height-10), snake_body, width, height)
                    else:
                        path = astar(graph, self.body[0], (head_x, 0), snake_body, width, height)
                else:
                    path = astar(graph, self.body[0], (width-10, head_y), snake_body, width, height)
            elif self.direction == "up":
                
                if head_y == 0:
                    if self.x < (width //2):
                        path = astar(graph, self.body[0], (width-10, head_y), snake_body, width, height)
                    else:
                        path = astar(graph, self.body[0], (0, head_y), snake_body, width, height)
                else:
                    path = astar(graph, self.body[0], (head_x, 0), snake_body, width, height)
            else:
                if head_y == height-10:
                    if self.x < (width //2):
                        path = astar(graph, self.body[0], (width-10, head_y), snake_body, width, height)
                    else:
                        path = astar(graph, self.body[0], (0, head_y), snake_body, width, height)
                else:
                    path = astar(graph, self.body[0], (head_x, height-10), snake_body, width, height)
            
            # if (self.x <= 0 and self.direction == "left") or (self.x >= width - 10 and self.direction == "right"):
            #     print("X BOUNDARY")
            #     if self.y < (height // 2) :
            #         self.direction = "down"
            #     else:
            #         self.direction = "up"
            # elif (self.y >= height-10 and self.direction == "down") or (self.y <= 0 and self.direction == "up"):
            #     print("Y BOUNDARY")
            #     if self.x < (width // 2) :
            #         self.direction = "right"
            #     else:
            #         self.direction = "left"

            if path:
                next_cell = path[0]
                #print("PATH NEXT: " + str(next_cell))
                head_x, head_y = self.body[0]

                # # Check if food is directly above or below the snake's head
                # if food.x == head_x:
                #     print("FOOD IS DIRECTLY ABOVE OR BELOW SNAKE'S HEAD")
                #     if food.y < head_y and self.direction != "down":
                #         self.direction = "up"
                #     elif food.y < head_y and self.direction == "down":
                #         if head_x < width // 2:
                #             self.direction = "left"
                #         else:
                #             self.direction = "right"
                #     elif food.y > head_y and self.direction != "up":
                #         self.direction = "down"
                #     elif food.y > head_y and self.direction == "up":
                #         if head_x < width // 2:
                #             self.direction = "left"
                #         else:
                #             self.direction = "right"
                # # Check if food is directly to the left or right of the snake's head
                # elif food.y == head_y:
                #     print("FOOD IS DIRECTLY LEFT OR RIGHT SNAKE'S HEAD")
                #     if food.x < head_x and self.direction != "right":
                #         self.direction = "left"
                #     elif food.x < head_x and self.direction == "left":
                #         if head_y < height // 2:
                #             self.direction = "up"
                #         else:
                #             self.direction = "down"
                #     elif food.x > head_x and self.direction != "left":
                #         self.direction = "right"
                #     elif food.x < head_x and self.direction == "right":
                #         if head_y < height // 2:
                #             self.direction = "up"
                #         else:
                #             self.direction = "down"
                
                # else:
                if next_cell[0] > head_x and self.direction != "left":  # Check if the next move is towards right and not coming from left
                    self.direction = "right"
                elif next_cell[0] < head_x and self.direction != "right":  # Check if the next move is towards left and not coming from right
                    self.direction = "left"
                elif next_cell[1] > head_y and self.direction != "up":  # Check if the next move is towards down and not coming from up
                    self.direction = "down"
                elif next_cell[1] < head_y and self.direction != "down":  # Check if the next move is towards up and not coming from down
                    self.direction = "up"
                    
            else:
                print("DEAD END")
                if (self.x <= 0 and self.direction == "left") or (self.x >= width - 10 and self.direction == "right"):
                    print("X BOUNDARY")
                    if self.y < (height // 2) :
                        self.direction = "down"
                    else:
                        self.direction = "up"
                elif (self.y >= height-10 and self.direction == "down") or (self.y <= 0 and self.direction == "up"):
                    print("Y BOUNDARY")
                    if self.x < (width // 2) :
                        self.direction = "right"
                    else:
                        self.direction = "left"

            next_pos = self.next_position()
            if next_pos in self.body[1:]:
                print("COLLISION AVOIDED")
                # Try alternative directions to avoid collision
                if self.direction == "right":
                    self.direction = "down" if self.y < (height // 2) else "up"
                elif self.direction == "left":
                    self.direction = "down" if self.y < (height // 2) else "up"
                elif self.direction == "up":
                    self.direction = "right" if self.x < (width // 2) else "left"
                elif self.direction == "down":
                    self.direction = "right" if self.x < (width // 2) else "left"

        if self.direction == "right":
            print("HEADING RIGHT")
            self.x += self.speed
        elif self.direction == "left":
            print("HEADING LEFT")
            self.x -= self.speed
        elif self.direction == "up":
            print("HEADING UP")
            self.y -= self.speed
        elif self.direction == "down":
            print("HEADING DOWN")
            self.y += self.speed
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def next_position(self):
        if self.direction == "right":
            return (self.x + self.speed, self.y)
        elif self.direction == "left":
            return (self.x - self.speed, self.y)
        elif self.direction == "up":
            return (self.x, self.y - self.speed)
        elif self.direction == "down":
            return (self.x, self.y + self.speed)
    
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
    def __init__(self, snake_body):
        self.size = 10
        self.spawn(snake_body)

    def spawn(self, snake_body):
        valid_position = False
        while not valid_position:
            self.x = random.randint(0, (width - self.size) // self.size) * self.size
            self.y = random.randint(0, (height - self.size) // self.size) * self.size
            # Check if the food is not on the snake's body
            if (self.x, self.y) not in snake_body:
                valid_position = True
        #print("New Food Position: (" + str(self.x) + ", " + str(self.y) + ")")

    def draw(self):
        pygame.draw.rect(screen, red, [self.x, self.y, self.size, self.size])

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(graph, start, end, snake_body, width, height):
    open_set = {start}
    came_from = {}

    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        open_set.remove(current)
        for neighbor in graph[current]:
            #print("Neighbour: " + str(float(neighbor[0])) + ", "+ str(float(neighbor[1])))
            if (float(neighbor[0]),float(neighbor[1])) not in snake_body and not (neighbor[0] < 0 or neighbor[0] >= width or neighbor[1] < 0 or neighbor[1] >= height):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    open_set.add(neighbor)

    return None

def log_scores(score, filename='scores_log.txt'):
    with open(filename, 'a') as file:
        timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        file.write(f"{timestamp} - {score}\n")

def read_scores(filename='scores_log.txt'):
    try:
        with open(filename, 'r') as file:
            scores = file.readlines()
            scores = [int(score.strip()) for score in scores]
            return scores
    except FileNotFoundError:
        print("Score log file not found.")
        return []

# Create the snake and food objects
snake = Snake(width/2, height/2)
snake_body = set(snake.body)
#print(snake_body)
food = Food(snake_body)

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
    graph = {}
    for x in range(width//10):
        for y in range(height//10):
            graph[(x*10, y*10)] = [(x*10+10, y*10), (x*10-10, y*10), (x*10, y*10+10), (x*10, y*10-10)]
    snake.move(graph, food, snake_body)

    # Update the snake's body set
    snake_body = set(snake.body)
    #print(snake_body)

    # Check for collision with the walls
    if snake.collide_with_wall() or snake.collide_with_self():
        game_over = True

    # Check for collision with the food
    if snake.collide_with_food(food):
        snake.grow()
        food = Food(snake_body)

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
    clock.tick(30)

# Display the GAME OVER text and final score
game_over_text = font.render("GAME OVER", True, black)
score_text = font.render("Final Score: " + str(score), True, black)
screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()))
screen.blit(score_text, (width/2 - score_text.get_width()/2, height/2))
pygame.display.update()

# Wait for 10 seconds
pygame.time.wait(10000)

log_scores(score)

