import pygame
import os
import requests

coordinates = (37.620070, 55.753630)

zoom = 16

size = (600, 450)

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    dc = {
        "ll": str(coordinates[0]) + "," + str(coordinates[1]),
        "z": str(zoom),
        "l": "map"
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=dc)
    print(response.request.url)
    print(response.status_code)
    with open('map_tmp.png', 'wb') as f:
        f.write(response.content)
    screen.blit(pygame.image.load('map_tmp.png'), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass


if __name__ == '__main__':
    main()
    pygame.quit()
    os.remove('map_tmp.png')