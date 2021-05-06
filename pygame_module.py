import pygame
import time

pygame.init()

display = pygame.display.set_mode((550,550))
def create_window(width, height, s):
    display = pygame.display.set_mode((550, 550), pygame.SCALED)
    pygame.display.set_caption("Dattebayo!!!")

button_quit = pygame.QUIT

button_1 = pygame.K_1
button_2 = pygame.K_2
button_3 = pygame.K_3
button_a = pygame.K_a
button_d = pygame.K_d
button_m = pygame.K_m
button_escape = pygame.K_ESCAPE




def fill(color):
    display.fill(color)

def Screen_update():
    pygame.display.update()

def delay(t):
    time.sleep(t)

def Picture_insert(s, width, height, deg_x, deg_y, scale=1, fon=(255, 254, 255), angle=0):
    serf = pygame.Surface((width, height)).convert()
    serf.fill(fon)
    serf.set_colorkey(fon)
    pic = pygame.image.load('Things/'+s).convert_alpha()
    pic = pygame.transform.scale(pic, (pic.get_width() // scale, pic.get_height() // scale))
    pic = pygame.transform.rotate(pic, angle)
    serf.blit(pic, (0, 0))
    display.blit(serf, (deg_x, deg_y))

def Text_insert(s,color,x ,y,size=20):
    if not hasattr(Text_insert, 'txt'):
        Text_insert.txt = pygame.font.Font(str('Things/Arial.ttf'),size)
    text = Text_insert.txt.render(s, False, color)
    display.blit(text, (x, y))

def check_event():
    listok=[]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            listok.append('QUIT')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            listok.append('K_1')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            listok.append('K_2')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            listok.append('K_3')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            listok.append('K_a')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            listok.append('K_d')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            listok.append('K_m')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            listok.append('K_ESCAPE')

        if event.type == pygame.MOUSEBUTTONDOWN:
            listok.append('MOUSEBUTTONDOWN')
    return listok

def check_coords():
    return pygame.mouse.get_pos()