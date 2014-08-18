import os, pygame

def show(image):
    screen = pygame.display.get_surface()
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()
def main():
    pygame.init()
    black = (0,0,0)
    pygame.display.set_mode((400, 400))
    surface = pygame.Surface((400, 400))
    surface.fill((255,255,255))
    ar = pygame.PixelArray(surface)
    for x in range(0, 400):
        for y in range(0, 400):
            u, v = (x+0.5) / 200.0 - 1.0, (y+0.5) / 200.0 - 1.0
            if u * u + v * v < 1:
                ar[x][y] = ((x % 255, y % 255, 0))
    pygame.draw.lines(surface, black, False, [(0,200), (400,200)], 4)
    pygame.draw.lines(surface, black, False, [(200,0), (200,400)], 4)

    del ar
    show(surface)
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise SystemExit



if __name__ == '__main__':
    main()
