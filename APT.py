import pygame
from random import randint


if __name__ == "__main__":
    pygame.init()
    window = "1000 1000".split()
    try:
        size, count_cells = list(map(int, window))
        size = (size, size)
        screen = pygame.display.set_mode(size)
        difficult = int(
            input("Выбери уровень сложности:\n1 - легкий\n2 - средний\n3 - сложный\n")
        )
        if difficult == 1:
            screen.fill((255, 255, 255))
        elif difficult == 2:
            screen.fill((0, 0, 0))
        elif difficult == 3:
            screen.fill((89, 48, 41))
        else:
            print("Нормальное число вводи бля, ты че тупой?")
            pygame.quit()
        pygame.display.flip()
        image = pygame.image.load("элина1.png").convert_alpha()
        x_image, y_image = randint(0, 900), randint(0, 900)
        screen.blit(image, (x_image, y_image))
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except ValueError:
        print("Нормально, вводи нормально будет, заебал")
        pygame.quit()
