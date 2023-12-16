import pygame

try:
    width, height = map(int, input().split())
    screen = pygame.display.set_mode((width, height))
    pygame.init()


    def draw(screen):
        screen.fill((0, 0, 0))
        pygame.draw.polygon(screen,
                            (255, 0, 0),
                            ((1, 1), (width - 1, 1), (width - 1, height - 1), (1, height - 1)),
                            width=0)


    draw(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
except:
    print('Неправильный формат ввода')