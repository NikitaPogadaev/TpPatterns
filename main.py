import sys
import random
import time
from collections import OrderedDict
from abc import ABC, abstractmethod
import object
import unit
import unittest
import action
import pygame_module

Buffd = object.Def_buff()
Buffa = object.Attack_buff()
Buffm = object.Multi_cast()
act = action.Action()

# create display & run update
#print(pygame.font.get_fonts())
width = 550
height = 550
pygame_module.create_window(550,550,'Dattebayo!!!')
pygame_module.Screen_update()

pygame_module.Picture_insert('map.png', 515, 515, 0, 0, 1, (255, 255, 255))
pygame_module.Screen_update()

pygame_module.delay(2)

end = True
act.turn = random.randint(0,1)

if act.turn == 0:
    pygame_module.fill((255, 0, 0))
else:
    pygame_module.fill((0, 0, 255))
pygame_module.Picture_insert('map.png', 515, 515, 0, 0, 1, (255, 255, 255))
for key in action.RArmy.tact:
    pygame_module.Picture_insert('red_' + action.RArmy.tact[key].tip + '.png', 41, 41, key[0] * 46, key[1] * 46, 1,
                                 (255, 255, 255))
for key in action.BArmy.tact:
    pygame_module.Picture_insert('blue_' + action.BArmy.tact[key].tip + '.png', 41, 41, key[0] * 46, key[1] * 46, 1,
                                 (255, 255, 255))
for key in action.location.map:
    if action.location.map[key].tip != 'BCastle' and action.location.map[key].tip != 'RCastle':
        pygame_module.Picture_insert(action.location.map[key].tip + '.png', 41, 41, key[0] * 46, key[1] * 46, 1,
                                     (255, 255, 255))

pygame_module.Text_insert(str(action.location.map[(0, 0)].HP), (255, 0, 0), 0, 0)
pygame_module.Text_insert(str(action.RArmy.money), (255, 0, 0), 0, 20)
pygame_module.Text_insert(str(action.location.map[(10, 0)].HP), (0, 0, 255), 515 - 56, 0)
pygame_module.Text_insert(str(action.BArmy.money), (0, 0, 255), 515 - 56, 20)

pygame_module.Screen_update()



while end:
    if action.location.map[(0,0)].HP <= 0:
        pygame_module.fill((255,0,0))
        pygame_module.Text_insert('BLUE WINS!!!', (0,0,255),50,50,100)
        pygame_module.Screen_update()
        pygame_module.delay(5)
        break
    if action.location.map[(10,0)].HP <= 0:
        pygame_module.fill((0,0,255))
        pygame_module.Text_insert('RED WINS!!!', (255,0,0),50,50,100)
        pygame_module.Screen_update()
        pygame_module.delay(5)
        break

    deg_x = 0
    deg_y = 0
    for event in pygame_module.check_event():
        if event == 'QUIT':
            end = False
        if event == 'K_1':
            act.create_sword()
        if event == 'K_2':
            act.create_archer()
        if event == 'K_3':
            act.create_thief()
        if event == 'K_a':
            act.turn^=1
            if act.turn == 0:
                Buffa.buff(action.RArmy)
            else:
                Buffa.buff(action.BArmy)
        if event == 'K_d':
            act.turn^=1
            if act.turn == 0:
                Buffd.buff(action.RArmy)
            else:
                Buffd.buff(action.BArmy)
        if event == 'K_m':
            act.turn^=1
            if act.turn == 0:
                Buffm.buff(action.RArmy)
            else:
                Buffm.buff(action.BArmy)
        if event == 'K_ESCAPE':
            end = False

        if event == 'MOUSEBUTTONDOWN':
            deg_x = pygame_module.check_coords()[0]//46
            deg_y = pygame_module.check_coords()[1]//46
            if action.RArmy.tact.get((deg_x, deg_y))!= None and act.turn==0:
                end1 = True
                while end1:
                    for e in pygame_module.check_event():
                        if e == 'MOUSEBUTTONDOWN':
                            deg_xx = pygame_module.check_coords()[0] // 46
                            deg_yy = pygame_module.check_coords()[1] // 46
                            if (0 <= deg_xx <= 10) and (0 <= deg_yy <= 10):
                                act.doing(action.RArmy.tact[(deg_x, deg_y)], deg_xx, deg_yy)
                                end1 = False


            if action.BArmy.tact.get((deg_x, deg_y))!= None and act.turn==1:
                end1 = True
                while end1:
                    for e in pygame_module.check_event():
                        if e == 'MOUSEBUTTONDOWN':
                            deg_xx = pygame_module.check_coords()()[0] // 46
                            deg_yy = pygame_module.check_coords()[1] // 46
                            if (0 <= deg_xx <= 10) and (0 <= deg_yy <= 10):
                                act.doing(action.BArmy.tact[(deg_x, deg_y)], deg_xx, deg_yy)
                                end1 = False

        if act.turn == 0:
            pygame_module.fill((255, 0, 0))
        else:
            pygame_module.fill((0, 0, 255))
        pygame_module.Picture_insert('map.png', 515, 515, 0, 0, 1, (255, 255, 255))
        for key in action.RArmy.tact:
            pygame_module.Picture_insert('red_'+action.RArmy.tact[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))
        for key in action.BArmy.tact:
            pygame_module.Picture_insert('blue_'+action.BArmy.tact[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))
        for key in  action.location.map:
            if action.location.map[key].tip != 'BCastle' and action.location.map[key].tip != 'RCastle':
                pygame_module.Picture_insert(action.location.map[key].tip +'.png', 41, 41, key[0]*46, key[1]*46, 1, (255, 255, 255))

        pygame_module.Text_insert(str(action.location.map[(0,0)].HP), (255,0,0), 0, 0)
        pygame_module.Text_insert(str(action.RArmy.money), (255,0,0), 0, 20)
        pygame_module.Text_insert(str(action.location.map[(10,0)].HP), (0,0,255), 515-56, 0)
        pygame_module.Text_insert(str(action.BArmy.money), (0,0,255), 515-56, 20)

        pygame_module.Screen_update()
