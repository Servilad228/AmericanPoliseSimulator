import pygame
from random import randint, choice


if __name__ == '__main__':
    pygame.init()
    window = '1000 1000'.split()
    try:
        size, count_cells = list(map(int, window))
        size = (size, size)
        screen = pygame.display.set_mode(size)
        difficult = int(input('Выбери уровень сложности:\n1 - легкий\n2 - средний\n3 - сложный\n'))
        if difficult == 1:
            screen.fill((255, 255, 255))
        elif difficult == 2:
            screen.fill((0, 0, 0))
        elif difficult == 3:
            screen.fill((89, 48, 41))
        else:
            print('Нормальное число вводи бля, ты че тупой?')
            pygame.quit()
        pygame.display.flip()

        image = pygame.image.load('элина1.png').convert_alpha()
        x_image, y_image = randint(0, 900), randint(0, 900)
        screen.blit(image, (x_image, y_image))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = event.pos
                    image_rect = pygame.Rect(x_image, y_image, image.get_width(), image.get_height())
                    if image_rect.collidepoint(mouse_x, mouse_y):
                        print(choice(['попал', 'точно в цель', 'да ты снайпер']))
                        # Clear the screen
                        if difficult == 1:
                            screen.fill((255, 255, 255))
                        elif difficult == 2:
                            screen.fill((0, 0, 0))
                        elif difficult == 3:
                            screen.fill((89, 48, 41))
                        # Move the image to a new position
                        x_image, y_image = randint(0, 900), randint(0, 900)
                        screen.blit(image, (x_image, y_image))
                        pygame.display.flip()
                    else:
                        print('Ебать ты лох ахахахах')

        pygame.quit()
    except ValueError:
        print('Нормально, вводи нормально будет, заебал')
        pygame.quit()
