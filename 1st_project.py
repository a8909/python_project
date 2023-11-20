import sys
import pygame
BLACK = (0,0,0)
WHITE= (255,255,255)

def main():
    pygame.init()
    screen_size = (1200, 800)
    font = pygame.font.sysFont('Arial', 25, True, False)
    text = font.render('welcome to pygame', True, WHITE)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(WHITE)
        pygame.display.flip()
        clock.tick(30)
main()