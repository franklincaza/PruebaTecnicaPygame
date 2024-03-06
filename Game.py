import pygame
import sys
import random

pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquivando Enemigos")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Jugador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 5

# Enemigos
enemy_size = 30
enemy_speed = 5
enemies = []


def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, player_size, player_size])


def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, [x, y, enemy_size, enemy_size])


def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

        # Actualizar posición de enemigos
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > HEIGHT:
                enemy[1] = 0
                enemy[0] = random.randint(0, WIDTH - enemy_size)

            # Verificar colisión
            if (
                player_x < enemy[0] + enemy_size
                and player_x + player_size > enemy[0]
                and player_y < enemy[1] + enemy_size
                and player_y + player_size > enemy[1]
            ):
                game_over()

        # Generar nuevos enemigos
        if random.randint(0, 100) < 5:
            enemies.append([random.randint(0, WIDTH - enemy_size), 0])

        # Limpiar pantalla
        screen.fill((0, 0, 0))

        # Dibujar jugador
        draw_player(player_x, player_y)

        # Dibujar enemigos
        for enemy in enemies:
            draw_enemy(enemy[0], enemy[1])

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
