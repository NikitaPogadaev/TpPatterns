import sys
import random
import time
from collections import OrderedDict
from abc import ABC, abstractmethod
import unit
import unittest


class CObj:
    active = True

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_tip(self):
        pass




class Place_Obj(CObj):

    def __init__(self, x=25, y=25, ind=True):
        super().__init__()
        self.pose_x = x
        self.pose_y = y
        self.active = ind
        self.tip = 'Place'

    def turn_on(self):
        self.active = True

    def turn_off(self):
        self.active = False

    def set_pos_x(self, x):
        self.pose_x = x

    def set_pos_y(self, x):
        self.pose_y = x

    def get_pos_x(self):
        return self.pose_x

    def get_pos_y(self):
        return self.pose_y

    def get_active(self):
        return self.active


    def get_tip(self):
        return self.tip


class Swamp(Place_Obj):

    def __init__(self, x=1, y=1, ind=True):
        super().__init__()
        self.x_pose = x
        self.y_pose = y
        self.active = ind
        self.slow = 2
        self.tip = 'Swamp'


class Red_castle(Place_Obj):

    def __init__(self, x=25, y=25, ind=True):
        super().__init__()
        self.x_pose = x
        self.y_pose = y
        self.active = ind
        self.color = 'Red'
        self.HP = 500
        self.tip = 'RCastle'

    def set_HP(self, x):
        self.HP = x

    def get_HP(self):
        return self.HP

    def get_color(self):
        return self.color


class Blue_castle(Place_Obj):

    def __init__(self, x=25, y=25, ind=True):
        super().__init__()
        self.x_pose = x
        self.y_pose = y
        self.active = ind
        self.color = 'Blue'
        self.HP = 500
        self.tip = 'BCastle'

    def set_HP(self, x):
        self.HP = x

    def get_HP(self):
        return self.HP

    def get_color(self):
        return self.color


class Egg(Place_Obj):

    def __init__(self, x=25, y=25, ind=True):
        super().__init__()
        self.x_pose = x
        self.y_pose = y
        self.active = ind
        self.HP = 200
        self.tip = 'Egg'

    def set_HP(self, x):
        self.HP = x

    def get_HP(self):
        return self.HP


class Gold(Place_Obj):

    def __init__(self, x=25, y=25, ind=True, col=100):
        super().__init__()
        self.x_pose = x
        self.y_pose = y
        self.active = ind
        self.amount = col
        self.tip = 'Gold'

    def set_amount(self, x):
        self.amount = x

    def get_amount(self):
        return self.amount


class Spell(CObj):

    def __init__(self, ind=True):
        super().__init__()
        self.active = ind
        self.tip = 'Spell'

    def turn_on(self):
        self.active = True

    def turn_off(self):
        self.active = False

    def get_active(self):
        return self.active


class Shield(Spell):

    def __init__(self, ind=True):
        super().__init__()
        self.active = ind
        self.tip = 'Shield'


class Def_buff(Spell):

    def __init__(self, ind=True):
        super().__init__()
        self.active = ind
        self.tip = 'Def_buff'
        self.cost = 200

    def buff(self, ar):
        for i in ar.tact:
            ar.tact[i].set_Def(ar.tact[i].get_Def() * 2)
        ar.money -= self.cost
        self.cost = self.cost * 2
        ar.total_Def *= 2

    def get_cost(self):
        return self.cost


class Attack_buff(Spell):

    def __init__(self, ind=True):
        super().__init__()
        self.active = ind
        self.tip = 'Def_attack'
        self.cost = 200

    def buff(self, ar):
        for i in ar.tact:
            ar.tact[i].set_DMG(ar.tact[i].get_DMG() * 2)
        ar.total_DMG *= 2
        ar.money -= self.cost
        self.cost = self.cost * 2

    def get_cost(self):
        return self.cost

class Multi_cast:
    a = Def_buff()
    b = Attack_buff()
    cost = 300

    def buff(self, ar):
        self.a.buff(ar)
        self.b.buff(ar)
        ar.money -= self.cost

    def get_cost(self):
        return self.cost + self.a.cost + self.a.cost


class MAP:

    def __init__(self):
        self.map = OrderedDict()
        self.Shld = Shield()
        self.red_DMG_buff = Attack_buff()
        self.blue_Def_buff = Def_buff()
        self.map[(0, 0)] = Red_castle()
        self.map[(0, 50)] = Blue_castle()
        for i in range(22, 29):
            for j in range(22, 29):
                self.map[(i, j)] = Swamp()
        self.map[(25, 25)] = Egg()
        for i in range(40):
            self.map[(random.randint(0, 20), random.randint(10, 40))] = Gold(col=random.randint(50, 100))
        for i in range(40):
            self.map[(random.randint(30, 50), random.randint(10, 40))] = Gold(col=random.randint(50, 100))


class UnitTest(unittest.TestCase):
    attack = Attack_buff()
    df = Def_buff
    ArmyF = unit.CArmyFactory()
    RArmy = ArmyF.make_Red_army()

    def test_Buff(self):
        self.RArmy.add_Kurama(0, 0)
        self.RArmy.add_Archer(1, 1)
        self.attack.buff(self.RArmy)
        self.assertEqual(self.RArmy.total_DMG, 196)
        self.assertEqual(self.RArmy.get_Unit(1, 1).get_DMG(), 36)
        self.assertEqual(self.RArmy.get_Unit(0, 0).get_DMG(), 160)







if __name__ == '__main__':
    unittest.main()
