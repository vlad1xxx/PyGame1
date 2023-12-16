import pygame

try:
    n = int(input())
    screen = pygame.display.set_mode((300, 300))
    pygame.init()


    def draw(screen):
        screen.fill((0, 0, 0))
        size = 150 // n
        for i in range(0, n):
            pygame.draw.ellipse(screen, (255, 255, 255), (150 - size * i - size, 0, (size * i + size) * 2, 300), 1)
            pygame.draw.ellipse(screen, (255, 255, 255), (0, 150 - size * i - size, 300, (size * i + size) * 2), 1)

    draw(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()

except:
    print('Неправильный формат ввода')