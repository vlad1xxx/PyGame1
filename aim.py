import pygame

try:
    w, n_circle = map(int, input().split())
    width = height = w * n_circle + w * n_circle
    screen = pygame.display.set_mode((w * n_circle + w * n_circle, w * n_circle + w * n_circle))
    pygame.init()


    def draw(screen):
        screen.fill((0, 0, 0))

        for i in range(n_circle):
            if i % 3 == 0:
                pygame.draw.circle(screen, (255, 0, 0), (width / 2, height / 2), w * i + w, w)
            elif i % 3 == 1:
                pygame.draw.circle(screen, (0, 255, 0), (width / 2, height / 2), w * i + w, w)
            else:
                pygame.draw.circle(screen, (0, 0, 255), (width / 2, height / 2), w * i + w, w)


    draw(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()

except:
    print('Неправильный формат ввода')