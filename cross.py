import pygame

try:
    width, height = map(int, input().split())

    screen = pygame.display.set_mode((width, height))
    pygame.init()


    def draw(screen):
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)
        pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), width=5)


    draw(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
except:
    print('Неправильный формат ввода')