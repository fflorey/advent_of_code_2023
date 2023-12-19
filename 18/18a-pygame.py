import pygame
import sys













# Pygame initialisieren
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Farben definieren
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FARBE = [RED, GREEN, BLUE]

# Punkte definieren
punkte = [(100, 100), (300, 200), (500, 300)]

# Zeichenschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # Bildschirm weiß färben

    # Punkte zeichnen
    for i, punkt in enumerate(punkte):
        pygame.draw.circle(screen, FARBE[i], punkt, 5)

    pygame.display.flip()