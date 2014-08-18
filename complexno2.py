import os, pygame, math
red = (255,0,0)
black = (0,0,0)

def map_to_plane(x, y):
    return x * 2.0 / 400.0 - 1.0, y * 2.0 / 400.0 - 1

def square(a, b):
    return a * a - b * b, 2 * a * b

def magnitude2(a, b):
    return a * a + b * b

def inside(real, imaginary):
    for times in range(0, 10):
        real, imaginary = square(real, imaginary)
        if magnitude2(real, imaginary) > 2.0:
            return False
    return True

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
            real, imaginary = map_to_plane(x,y)
            in_set = inside(real, imaginary)
            if in_set:
                ar[x][y] = black
            else:
                ar[x][y] = red
    del ar
    show(surface)
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise SystemExit



if __name__ == '__main__':
    main()
