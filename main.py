import sys
import random
import time
from collections import OrderedDict
from abc import ABC, abstractmethod
import object
import unit
import unittest
import action
import pygame

Buffd = object.Def_buff()
Buffa = object.Attack_buff()
Buffm = object.Multi_cast()
act = action.Action()

pygame.init()
# create display & run update
#print(pygame.font.get_fonts())
width = 550
height = 550
display = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.update()
pygame.display.set_caption("Dattebayo!!!")

def Picture_insert(s, width, height, deg_x, deg_y, scale=1, fon=(255, 254, 255), angle=0):
    serf = pygame.Surface((width, height)).convert()
    serf.fill(fon)
    serf.set_colorkey(fon)
    pic = pygame.image.load('Things/'+s).convert_alpha()
    pic = pygame.transform.scale(pic, (pic.get_width() // scale, pic.get_height() // scale))
    pic = pygame.transform.rotate(pic, angle)
    serf.blit(pic, (0, 0))
    display.blit(serf, (deg_x, deg_y))

Picture_insert('map.png', 515, 515, 0, 0, 1, (255, 255, 255))
pygame.display.update()

end = True
act.turn = random.randint(0,1)
print(pygame.font.get_fonts())

time.sleep(2)
while end:
    if act.turn == 0:
        display.fill((255,0,0))
    else:
        display.fill((0,0,255))
    if action.location.map[(0,0)].HP <= 0:
        txt = pygame.font.Font(str('Things/Arial.ttf'), 100)
        text = txt.render('BLUE WINS!!!', False, (0,0,255))
        display.blit(text, (50, 50))
        pygame.display.update()
        time.sleep(5)
        break
    if action.location.map[(10,0)].HP <= 0:
        txt = pygame.font.Font(str('Things/Arial.ttf'), 100)
        text = txt.render('RED WINS!!!', False, (255,0,0))
        display.blit(text, (50, 50))
        pygame.display.update()
        time.sleep(5)
        break

    deg_x = 0
    deg_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            act.create_sword()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            act.create_archer()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            act.create_thief()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            act.turn^=1
            if act.turn == 0:
                Buffa.buff(action.RArmy)
            else:
                Buffa.buff(action.BArmy)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            act.turn^=1
            if act.turn == 0:
                Buffd.buff(action.RArmy)
            else:
                Buffd.buff(action.BArmy)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            act.turn^=1
            if act.turn == 0:
                Buffm.buff(action.RArmy)
            else:
                Buffm.buff(action.BArmy)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            deg_x = pygame.mouse.get_pos()[0]//46
            deg_y = pygame.mouse.get_pos()[1]//46
            if action.RArmy.tact.get((deg_x, deg_y))!= None and act.turn==0:
                end1 = True
                while end1:
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            deg_xx = pygame.mouse.get_pos()[0] // 46
                            deg_yy = pygame.mouse.get_pos()[1] // 46
                            if (0 <= deg_xx <= 10) and (0 <= deg_yy <= 10):
                                act.doing(action.RArmy.tact[(deg_x, deg_y)], deg_xx, deg_yy)
                                end1 = False


            if action.BArmy.tact.get((deg_x, deg_y))!= None and act.turn==1:
                end1 = True
                while end1:
                    for e in pygame.event.get():
                        if e.type == pygame.MOUSEBUTTONDOWN:
                            deg_xx = pygame.mouse.get_pos()[0] // 46
                            deg_yy = pygame.mouse.get_pos()[1] // 46
                            if (0 <= deg_xx <= 10) and (0 <= deg_yy <= 10):
                                act.doing(action.BArmy.tact[(deg_x, deg_y)], deg_xx, deg_yy)
                                end1 = False
        Picture_insert('map.png', 515, 515, 0, 0, 1, (255, 255, 255))
        for key in action.RArmy.tact:
            Picture_insert('red_'+action.RArmy.tact[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))
        for key in action.BArmy.tact:
            Picture_insert('blue_'+action.BArmy.tact[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))
        for key in  action.location.map:
            if action.location.map[key].tip != 'BCastle' and action.location.map[key].tip != 'RCastle':
                Picture_insert(action.location.map[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))

        txt = pygame.font.Font(str('Things/Arial.ttf'),20)
        text = txt.render(str(action.location.map[(0,0)].HP), False, (255,0,0))
        display.blit(text, (0, 0))
        text = txt.render(str(action.RArmy.money), False, (255,0,0))
        display.blit(text, (0, 20))
        text = txt.render(str(action.location.map[(10,0)].HP), False, (0,0,255))
        display.blit(text, (515-56, 0))
        text = txt.render(str(action.BArmy.money), False, (0,0,255))
        display.blit(text, (515-56, 20))
        pygame.display.update()
