# Pygame Development
import pygame
import random
import time
import imageio

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CIRCLE_RADIUS = 20
CIRCLE_COUNT = 200
SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(CIRCLE_COUNT)]

# Create the window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Collision Game")

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1]) * SPEED
        self.dy = random.choice([-1, 1]) * SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Collision with window boundaries
        if self.x <= CIRCLE_RADIUS or self.x >= WIDTH - CIRCLE_RADIUS:
            self.dx = -self.dx
        if self.y <= CIRCLE_RADIUS or self.y >= HEIGHT - CIRCLE_RADIUS:
            self.dy = -self.dy

    def draw(self, color):
        pygame.draw.circle(win, color, (self.x, self.y), CIRCLE_RADIUS)

def draw_triangle(center_x, center_y):
    half_base = 20
    height = 35
    point1 = (center_x, center_y + half_base)
    point2 = (center_x - height, center_y - half_base)
    point3 = (center_x + height, center_y - half_base)
    pygame.draw.polygon(win, RED, [point1, point2, point3])

def is_inside_triangle(x, y, center_x, center_y):
    half_base = 20
    height = 35
    return center_x - height <= x <= center_x + height and center_y - half_base <= y <= center_y + half_base

def draw_square(center_x, center_y, size=35):
    pygame.draw.rect(win, RED, (center_x - size/2, center_y - size/2, size, size))

def is_inside_square(x, y, center_x, center_y, size=35):
    return center_x - size/2 <= x <= center_x + size/2 and center_y - size/2 <= y <= center_y + size/2

# Adding frames to create a gif

def run_game(save_gif=False):
    if save_gif:
        frames = []

    circles = [Circle(random.randint(CIRCLE_RADIUS, WIDTH - CIRCLE_RADIUS),
                      random.randint(CIRCLE_RADIUS, HEIGHT - CIRCLE_RADIUS)) for _ in range(CIRCLE_COUNT)]
    correct_clicks = 0
    incorrect_clicks = 0

    correct_latencies = []
    incorrect_latencies = []
    shape_displayed = None
    shape_time = 0
    shape_center = (0, 0)

    start_time = time.time()
    run = True
    while run:
        if time.time() - start_time > 120:  # 2 minutes duration
            break

        # Randomly decide to display shape
        if shape_displayed is None and random.random() < 0.01:
            shape_displayed = random.choice(["triangle", "square"])
            shape_time = time.time()
            shape_center = (random.randint(40, WIDTH - 40), random.randint(40, HEIGHT - 40))
        # Hide shape after 3 seconds
        if shape_displayed and time.time() - shape_time > 2:
            shape_displayed = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if shape_displayed == "triangle" and is_inside_triangle(x, y, *shape_center):
                    correct_clicks += 1
                    correct_latencies.append(time.time() - shape_time)
                    shape_displayed = None
                elif shape_displayed == "square" and is_inside_square(x, y, *shape_center):
                    incorrect_clicks += 1
                    incorrect_latencies.append(time.time() - shape_time)
                    shape_displayed = None
                else:
                    incorrect_clicks += 1
                    incorrect_latencies.append(time.time() - shape_time)

        win.fill(WHITE)

        # Move and draw circles
        for i, circle in enumerate(circles):
            circle.move()
            circle.draw(colors[i])

        if shape_displayed == "triangle":
            draw_triangle(*shape_center)
        elif shape_displayed == "square":
            draw_square(*shape_center)

        pygame.display.flip()
        if save_gif:
            pygame_image = pygame.surfarray.array3d(pygame.display.get_surface())
            frames.append(pygame_image)
        pygame.time.Clock().tick(60)

    pygame.quit()
    if save_gif:
        # Rotate the frames by 90 degrees
        rotated_frames = []
        for frame in frames:
            rotated_surf = pygame.transform.rotate(pygame.surfarray.make_surface(frame), 90)
            rotated_frames.append(pygame.surfarray.array3d(rotated_surf))
        imageio.mimsave('game_output.gif', rotated_frames, fps=60)
    return {
            "correct_clicks": correct_clicks,
            "incorrect_clicks": incorrect_clicks,
            "correct_latencies": correct_latencies,
            "incorrect_latencies": incorrect_latencies
            }

if __name__ == "__main__":
    results = run_game()

    # Save results to a file (or any other storage mechanism)
    with open("game_results.txt", "w") as f:
        f.write(str(results))