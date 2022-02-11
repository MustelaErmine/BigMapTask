import pygame
import os
import requests

coordinates = (37.620070, 55.753630)

zoom = 16

size = (600, 450)

def main():
    global zoom
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    rerender(screen)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == 1073741899:
                    zoom += 1
                    zoom = min(zoom, 17)
                    rerender(screen)
                elif event.key == 1073741902:
                    zoom -= 1
                    zoom = max(zoom, 0)
                    rerender(screen)


def rerender(screen):
    pygame.draw.rect(screen, '#000000', (0, 0, size[0], size[1]))
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    dc = {
        "ll": str(coordinates[0]) + "," + str(coordinates[1]),
        "z": str(zoom),
        "l": "map"
    }
    response = requests.get(map_api_server, params=dc)
    with open('map_tmp.png', 'wb') as f:
        f.write(response.content)
    screen.blit(pygame.image.load('map_tmp.png'), (0, 0))
    pygame.display.flip()


if __name__ == '__main__':
    main()
    pygame.quit()
    os.remove('map_tmp.png')