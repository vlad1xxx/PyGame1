import pygame

try:
    size_screen, num_square = map(int, input().split())
    screen = pygame.display.set_mode((size_screen, size_screen))
    pygame.init()


    def draw(screen):
        screen.fill((255, 255, 255))
        size_square = size_screen // num_square
        is_black = num_square % 2 != 0
        for i in range(num_square):
            for j in range(num_square):
                if is_black:
                    pygame.draw.rect(screen, (0, 0, 0), (i * size_square, j * size_square, size_square, size_square))
                    is_black = False
                else:
                    is_black = True


    draw(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()

except:
    print('Неправильный формат ввода')