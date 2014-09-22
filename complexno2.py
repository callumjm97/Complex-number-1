import os, pygame, math
red = (255,0,0)
black = (0,0,0)

cx, cy = (0.0,0.0)
scale = 4.0
screenx = 400
screeny = 400

def map_to_plane(x, y):
    def calc(p,c):
        return p * scale / max(screenx, screeny)-(scale/2.0) +c
    return calc(x, cx), calc(y,cy)


def square(a, b):
    return a * a - b * b, 2 * a * b

def magnitude2(a, b):
    return a * a + b * b

def inside(real, imaginary):
    origR, origI = real, imaginary
    for times in range(0, 50):
        real, imaginary = square(real, imaginary)
        real += origR
        imaginary += origI
        if magnitude2(real, imaginary) > 4.0:
            return times


def show(image):
    screen = pygame.display.get_surface()
    pygame.display.set_caption('Complex numbers')
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()

def main():
    pygame.init()
    black = (0,0,0)
    pygame.display.set_caption('Complex numbers')
    pygame.display.set_mode((screenx, screeny))
    surface = pygame.Surface((screenx, screeny))
    surface.fill((255,255,255))
    ar = pygame.PixelArray(surface)
    for x in range(0, screenx):
        for y in range(0, screeny):
            real, imaginary = map_to_plane(x,y)
            in_set = inside(real, imaginary)
            if in_set is None:
                ar[x][y] = black
            else:
                ar[x][y] = ((in_set * 7)%255,(in_set * 13)%255,(in_set * 17)%255)
    del ar
    show(surface)
    pygame.display.flip()
    while 1:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            raise SystemExit



if __name__ == '__main__':
    main()
