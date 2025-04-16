import pygame
import random
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="Makaron99"
)
cur = conn.cursor()

# Запрос имени игрока
username = input("Enter your name: ")

# Проверяем, есть ли такой игрок в базе
cur.execute("SELECT id, score, level FROM user_score WHERE name = %s;", (username,))
player = cur.fetchone()

if player is None:
    cur.execute("INSERT INTO user_score (name, score, level) VALUES (%s, 0, 1) RETURNING id;", (username,))
    user_id = cur.fetchone()[0]
    score = 0
    level = 1
    conn.commit()
else:
    user_id, score, level = player

pygame.init()

# Остальной код без изменений
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SPEED = 8 + (level - 1)
SCORE_TO_LEVEL_UP = 4

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (GRID_SIZE, 0)

food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

running = True
game_over = False
menu = True
paused = False
clock = pygame.time.Clock()

def generate_food():
    while True:
        new_food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if new_food not in snake:
            return new_food

def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    render_text = font.render(text, True, color)
    text_rect = render_text.get_rect(center=(x, y))
    screen.blit(render_text, text_rect)

def show_menu():
    screen.fill(BLACK)
    draw_text("SNAKE GAME", WIDTH // 10, GREEN, WIDTH // 2, HEIGHT // 4)
    start_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 20, 150, 50)
    pygame.draw.rect(screen, WHITE, start_button)
    draw_text("Start", WIDTH // 15, BLACK, WIDTH // 2, HEIGHT // 2 + 5)
    pygame.display.flip()
    return start_button

while menu:
    start_button = show_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                menu = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_q:
                    running = False
            else:
                if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                    snake_dir = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                    snake_dir = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                    snake_dir = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                    snake_dir = (GRID_SIZE, 0)
                elif event.key == pygame.K_p:
                    paused = not paused

    if paused:
        draw_text("PAUSED", WIDTH // 10, WHITE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        continue

    if game_over:
        draw_text("YOU LOSE", WIDTH // 10, RED, WIDTH // 2, HEIGHT // 3)
        pygame.display.flip()
        continue

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    new_head = (new_head[0] % WIDTH, new_head[1] % HEIGHT)

    if new_head in snake:
        game_over = True
        continue

    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = generate_food()
        if score % SCORE_TO_LEVEL_UP == 0:
            level += 1
            SPEED += 1
    else:
        snake.pop()

    pygame.draw.rect(screen, DARK_GREEN, (snake[0][0], snake[0][1], GRID_SIZE, GRID_SIZE))
    for segment in snake[1:]:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    draw_text(f"Score: {score}", WIDTH // 25, WHITE, 70, 15)
    draw_text(f"Level: {level}", WIDTH // 25, WHITE, 70, 35)

    pygame.display.flip()
    clock.tick(SPEED)

# Сохраняем данные при завершении
cur.execute("UPDATE user_score SET score = %s, level = %s WHERE id = %s;", (score, level, user_id))
conn.commit()
cur.close()
conn.close()
pygame.quit()
