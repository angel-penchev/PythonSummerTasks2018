import pygame


def main():
    pygame.init()  # Initializing the pygame module

    # Defining game window logo & title
    logo = pygame.image.load("assets/logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("2D Car Racing Game")

    # Defining the game window width & height
    screen = pygame.display.set_mode((1280, 720))

    isGameRunning = True  # Sets the game to start

    while isGameRunning:
        for event in pygame.event.get():
            # Defining game "QUIT" function
            if event.type == pygame.QUIT:
                isGameRunning = False


if __name__ == "__main__":
    main()
