import sys
import random
import time
from collections import OrderedDict
from abc import ABC, abstractmethod
import object
import unit
import unittest

ArmyF = unit.CArmyFactory()
KurF = unit.CKuramaFactory()
ShuF = unit.CShukakuFactory()
SwordF = unit.CSwordmanFactory()
ArF = unit.CArcherFactory()
ShaF = unit.CShamanFactory()
ThF = unit.CThiefFactory()
RArmy = ArmyF.make_Red_army()
BArmy = ArmyF.make_Blue_army()
location = object.MAP()

class Action:
    turn = 0

    def death(self, pers):
        a = pers.get_pose_x()
        b = pers.get_pose_y()
        if pers.color == 'red':
            if(RArmy.tact[(a, b)].get_HP() <= 0):
                RArmy.del_Unit(a, b)
                return True
            else:
                return False
        elif pers.color == 'blue':
            if (BArmy.tact[(a, b)].get_HP() <= 0):
                BArmy.del_Unit(a, b)
                return True
            else:
                return False



    def act_shot(self, pers1, pers2):
        a1 = pers1.get_pose_x()
        b1 = pers1.get_pose_y()
        a2 = pers2.get_pose_x()
        b2 = pers2.get_pose_y()
        if pers1.color == 'red':
            RArmy.tact[(a1, b1)].attack(BArmy.tact[(a2, b2)])
        else:
            BArmy.tact[(a1, b1)].attack(RArmy.tact[(a2, b2)])
        self.turn ^= 1
        self.death(pers2)


    def act_battle(self, pers1, pers2):
        a1 = pers1.get_pose_x()
        b1 = pers1.get_pose_y()
        a2 = pers2.get_pose_x()
        b2 = pers2.get_pose_y()
        temp = 1
        self.turn ^= 1
        while not self.death(pers1) and not self.death(pers2):
            temp ^= 1
            if temp == 0:
                if pers1.color == 'red':
                    RArmy.tact[(a1, b1)].attack(BArmy.tact[(a2, b2)])
                else:
                    BArmy.tact[(a1, b1)].attack(RArmy.tact[(a2, b2)])
            else:
                if pers1.color == 'red':
                    BArmy.tact[(a2, b2)].attack(RArmy.tact[(a1, b1)])
                else:
                    RArmy.tact[(a2, b2)].attack(BArmy.tact[(a1, b1)])
        if temp == 0:
            if pers1.color == 'red':
                RArmy.tact[(a1,b1)].set_pose_x(a2)
                RArmy.tact[(a1,b1)].set_pose_y(b2)
                RArmy.tact[(a2, b2)] = RArmy.tact[(a1, b1)]
                RArmy.del_Unit(a1, b1)
            else:
                BArmy.tact[(a1,b1)].set_pose_x(a2)
                BArmy.tact[(a1,b1)].set_pose_y(b2)
                BArmy.tact[(a2, b2)] = BArmy.tact[(a1, b1)]
                BArmy.del_Unit(a1, b1)

        elif temp == 1:
            if pers2.color == 'blue':
                BArmy.tact[(a2,b2)].set_pose_x(a1)
                BArmy.tact[(a2,b2)].set_pose_y(b1)
                BArmy.tact[(a1, b1)] = BArmy.tact[(a2, b2)]
                BArmy.del_Unit(a2, b2)
            else:
                RArmy.tact[(a2,b2)].set_pose_x(a1)
                RArmy.tact[(a2,b2)].set_pose_y(b1)
                RArmy.tact[(a1, b1)] = RArmy.tact[(a2, b2)]
                RArmy.del_Unit(a2, b2)



    def merge(self, pers1, pers2):
        if pers1.tip == pers2.tip:
            a1 = pers1.get_pose_x()
            b1 = pers1.get_pose_y()
            a2 = pers2.get_pose_x()
            b2 = pers2.get_pose_y()
            self.turn ^= 1
            if pers1.color == 'red':
                RArmy.tact[(a2, b2)].count += RArmy.tact[(a1, b1)].count
                RArmy.del_Unit(a1, b1)
            else:
                BArmy.tact[(a2, b2)].count += BArmy.tact[(a1, b1)].count
                BArmy.del_Unit(a1, b1)


    def go_red_castle(self, c):
        self.turn^=1
        a1 = c.get_pose_x()
        b1 = c.get_pose_y()
        if c.color == 'red':
            if c.tip == 'Thief':
                BArmy.money += c.get_garbage()
            location.map[(0, 0)].HP += c.get_HP()
            RArmy.del_Unit(a1, b1)
        else:
            location.map[(0, 0)].HP -= c.get_HP()
            BArmy.del_Unit(a1, b1)

    def go_blue_castle(self, c):
        self.turn^=1
        a1 = c.get_pose_x()
        b1 = c.get_pose_y()
        if c.color == 'blue':
            if c.tip == 'Thief':
                BArmy.money += c.get_garbage()
            location.map[(10, 0)].HP += c.get_HP()
            BArmy.del_Unit(a1, b1)
        else:
            location.map[(10, 0)].HP -= c.get_HP()
            RArmy.del_Unit(a1, b1)

    def egg_merge(self, pers):
        self.turn^=1
        a1 = pers.get_pose_x()
        b1 = pers.get_pose_y()
        if pers.color == 'red':
            location.map[(5, 5)].HP -= pers.get_DMG()
            RArmy.del_Unit(a1, b1)
            if location.map[(5, 5)].HP <= 0:
                RArmy.add_Kurama(5, 5)
                location.map.pop((5,5))
        else:
            location.map[(5, 5)].HP -= pers.get_DMG()
            BArmy.del_Unit(a1, b1)
            if location.map[(5, 5)].HP <= 0:
                BArmy.add_Kurama(5, 5)
                location.map.pop((5,5))

    def create_sword(self):
        if self.turn == 0:
            if RArmy.tact.get((0,1)) == None and BArmy.tact.get((0,1)) == None:
                RArmy.add_Swordman(0,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,1)) == None and BArmy.tact.get((1,1)) == None:
                RArmy.add_Swordman(1,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,0)) == None and BArmy.tact.get((1,0)) == None:
                RArmy.add_Swordman(1,0,10)
                RArmy.money-=100
                self.turn ^= 1
        elif self.turn == 1:
            if BArmy.tact.get((10,1)) == None and RArmy.tact.get((10,1)) == None:
                BArmy.add_Swordman(10,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,1)) == None and RArmy.tact.get((9, 1)) == None:
                BArmy.add_Swordman(9,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,0)) == None and RArmy.tact.get((9,0)) == None:
                BArmy.add_Swordman(9,0,10)
                BArmy.money -= 100
                self.turn ^= 1

    def create_archer(self):
        if self.turn == 0:
            if RArmy.tact.get((0,1)) == None and BArmy.tact.get((0,1)) == None:
                RArmy.add_Archer(0,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,1)) == None and BArmy.tact.get((1,1)) == None:
                RArmy.add_Archer(1,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,0)) == None and BArmy.tact.get((1,0)) == None:
                RArmy.add_Archer(1,0,10)
                RArmy.money-=100
                self.turn ^= 1
        elif self.turn == 1:
            if BArmy.tact.get((10,1)) == None and RArmy.tact.get((10,1)) == None:
                BArmy.add_Archer(10,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,1)) == None and RArmy.tact.get((9,1)) == None:
                BArmy.add_Archer(9,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,0)) == None and RArmy.tact.get((9,0)) == None:
                BArmy.add_Archer(9,0,10)
                BArmy.money -= 100
                self.turn ^= 1

    def create_thief(self):
        if self.turn == 0:
            if RArmy.tact.get((0,1)) == None and BArmy.tact.get((0,1)) == None:
                RArmy.add_Thief(0,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,1)) == None and BArmy.tact.get((1,1)) == None:
                RArmy.add_Thief(1,1,10)
                RArmy.money-=100
                self.turn ^= 1
            elif RArmy.tact.get((1,0)) == None and BArmy.tact.get((1,0)) == None:
                RArmy.add_Thief(1,0,10)
                RArmy.money-=100
                self.turn ^= 1
        elif self.turn == 1:
            if BArmy.tact.get((10,1)) == None and RArmy.tact.get((10,1)) == None:
                BArmy.add_Thief(10,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,1)) == None and RArmy.tact.get((9,1)) == None:
                BArmy.add_Thief(9,1,10)
                BArmy.money -= 100
                self.turn ^= 1
            elif BArmy.tact.get((9,0)) == None and RArmy.tact.get((9,0)) == None:
                BArmy.add_Thief(9,0,10)
                BArmy.money -= 100
                self.turn ^= 1

    def doing(self, pers, a, b):
        a1 = pers.get_pose_x()
        b1 = pers.get_pose_y()
        if (self.turn == 0 and pers.color == 'blue') or (self.turn == 1 and pers.color == 'red'):
            return False
        else:
            if (a == 0) and  (b == 0):
                self.go_red_castle(pers)
            elif a == 10 and b == 0:
                self.go_blue_castle(pers)
            elif RArmy.tact.get((a, b)) != None:
                if pers.color == 'red' and (abs(a-a1) + abs(b-b1)) <= pers.Speed:
                    self.merge(pers, RArmy.tact[(a, b)])
                elif pers.attack_tip == 'shot' and (abs(a-a1) + abs(b-b1)) <= pers.distance:
                    self.act_shot(pers, RArmy.tact[(a, b)])
                else:
                    self.act_battle(pers, RArmy.tact[(a, b)])
            elif BArmy.tact.get((a, b)) != None:
                if pers.color == 'blue' and (abs(a-a1) + abs(b-b1)) <= pers.Speed:
                    self.merge(pers, BArmy.tact[(a, b)])
                elif pers.attack_tip == 'shot' and (abs(a-a1) + abs(b-b1)) <= pers.distance:
                    self.act_shot(pers, BArmy.tact[(a, b)])
                else:
                    self.act_battle(pers, BArmy.tact[(a, b)])
            elif a == 5 and b == 5:
                if abs(a1-5)+abs(b1-5) <= pers.Speed:
                    self.egg_merge(pers)
            elif abs(a-a1)+abs(b-b1) <= pers.Speed:
                self.turn^=1
                if pers.color == 'red':
                    pers.set_pose_x(a)
                    pers.set_pose_y(b)
                    RArmy.tact[(a, b)] = pers
                    RArmy.del_Unit(a1, b1)
                    if location.map.get((a, b)) != None:
                        RArmy.money += location.map[(a, b)].get_amount()
                        location.map.pop((a, b))
                else:
                    pers.set_pose_x(a)
                    pers.set_pose_y(b)
                    BArmy.tact[(a, b)] = pers
                    BArmy.del_Unit(a1, b1)
                    if location.map.get((a, b)) != None:
                        BArmy.money += location.map[(a, b)].get_amount()
                        location.map.pop((a, b))

