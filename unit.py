import sys
import random
import time
from collections import OrderedDict
from abc import ABC, abstractmethod
import unittest


class CUnits:
    HP = 0
    Def = 0
    DMG = 0
    Speed = 0
    pose_x = 0
    pose_y = 0
    tip = 'CU'
    attack_tip = ''

    @abstractmethod
    def walk(self, x, y):
        pass

    @abstractmethod
    def get_HP(self):
        pass

    @abstractmethod
    def set_HP(self, x):
        pass

    @abstractmethod
    def get_DMG(self):
        pass

    @abstractmethod
    def set_DMG(self, x):
        pass

    @abstractmethod
    def get_Speed(self):
        pass

    @abstractmethod
    def set_Speed(self, x):
        pass

    @abstractmethod
    def get_Def(self):
        pass

    @abstractmethod
    def set_Def(self, x):
        pass

    @abstractmethod
    def get_pose_x(self):
        pass

    @abstractmethod
    def set_pose_x(self, x):
        pass

    @abstractmethod
    def get_pose_y(self):
        pass

    @abstractmethod
    def set_pose_y(self, x):
        pass

    def get_tip(self):
        return self.tip

    def get_attack_tip(self):
        return self.attack_tip


class Beasts(CUnits):
    HP = 0
    Def = 0
    Speed = 0
    DMG = 0
    pose_x = 0
    pose_y = 0
    tip = 'B'
    attack_tip = ''

    def __init__(self):
        super().__init__()

    def walk(self, x, y):
        pass

    def get_HP(self):
        return self.HP

    def set_HP(self, x):
        self.HP = x

    def get_Speed(self):
        return self.Speed

    def set_Speed(self, x):
        self.Speed = x

    def get_Def(self):
        return self.Def

    def set_Def(self, x):
        self.Def = x

    def get_pose_x(self):
        return self.pose_x

    def set_pose_x(self, x):
        self.pose_x = x

    def get_pose_y(self):
        return self.pose_y

    def set_pose_y(self, x):
        self.pose_y = x

    def get_tip(self):
        return self.tip

    def get_DMG(self):
        return self.DMG

    def set_DMG(self, x):
        self.DMG = x

    def get_attack_tip(self):
        return self.attack_tip


class Shukaku(Beasts):

    def __init__(self, x=25, y=25, col='white'):
        super().__init__()
        self.HP = 500
        self.Def = 75
        self.DMG = 50
        self.Speed = 10
        self.pose_x = x
        self.pose_y = y
        self.distance = 10
        self.tip = 'SH'
        self.attack_tip = 'shot'
        self.color = col

    def get_color(self):
        return self.color

    def set_color(self, x):
        self.color = x

    def attack(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.DMG)

    def walk(self, x, y):
        self.set_pose_x(x)
        self.set_pose_y(y)


class Kurama(Beasts):

    def __init__(self, x=25, y=25, col='white'):
        super().__init__()
        self.HP = 900
        self.Def = 50
        self.DMG = 200
        self.Speed = 20
        self.pose_x = x
        self.pose_y = y
        self.tip = 'Kurama'
        self.attack_tip = 'attack'
        self.color = col

    def get_color(self):
        return self.color

    def set_color(self, x):
        self.color = x

    def walk(self, x, y):
        self.set_pose_x(x)
        self.set_pose_y(y)

    def attack(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.DMG)


class Humans(CUnits):
    HP = 1
    Def = 0
    Speed = 0
    DMG = 0
    pose_x = 0
    pose_y = 0
    count = 0
    pay = 0
    tip = 'Hum'
    attack_tip = ''
    color = ''

    def __init__(self):
        super().__init__()

    def get_color(self):
        return self.color

    def set_color(self, x):
        self.color = x

    def get_count(self):
        return self.count

    def set_count(self, x):
        self.count = x

    def get_pay(self):
        return self.pay

    def set_pay(self, x):
        self.pay = x

    def get_HP(self):
        return self.HP * self.count

    def set_HP(self, x):
        self.count = x // self.HP

    def get_Speed(self):
        return self.Speed

    def set_Speed(self, x):
        self.Speed = x

    def get_Def(self):
        return self.Def * self.count

    def set_Def(self, x):
        self.Def = x

    def get_pose_x(self):
        return self.pose_x

    def set_pose_x(self, x):
        self.pose_x = x

    def get_pose_y(self):
        return self.pose_y

    def set_pose_y(self, x):
        self.pose_y = x

    def get_tip(self):
        return self.tip

    def get_DMG(self):
        return self.DMG * self.count

    def set_DMG(self, x):
        self.DMG = x

    def get_attack_tip(self):
        return self.attack_tip

    def walk(self, x, y):
        self.set_pose_x(x)
        self.set_pose_y(y)


class Swordman(Humans):

    def __init__(self, x=0, y=0, col='white', n=0):
        super().__init__()
        self.HP = 16
        self.Def = 10
        self.Speed = 6
        self.DMG = 14
        self.pose_x = x
        self.pose_y = y
        self.count = n
        self.pay = 10
        self.tip = 'Swordman'
        self.attack_tip = 'attack'
        self.color = col


    def attack(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.get_DMG())


class Archer(Humans):

    def __init__(self, x=0, y=0, col='white', n=0):
        super().__init__()
        self.HP = 10
        self.Def = 5
        self.Speed = 8
        self.DMG = 18
        self.pose_x = x
        self.pose_y = y
        self.count = n
        self.pay = 12
        self.distance = 10
        self.tip = 'Archer'
        self.attack_tip = 'shot'
        self.color = col


    def attack(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.get_DMG())


class Shaman(Humans):

    def __init__(self, x=0, y=0, col='white', n=0):
        super().__init__()
        self.HP = 20
        self.Def = 8
        self.Speed = 6
        self.DMG = 20
        self.pose_x = x
        self.pose_y = y
        self.count = n
        self.pay = 30
        self.tip = 'Sm'
        self.attack_tip = 'heal'
        self.color = col


    def heal(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.get_DMG())


class Thief(Humans):

    def __init__(self, x=0, y=0, col='white', n=0):
        super().__init__()
        self.HP = 20
        self.Def = 8
        self.Speed = 6
        self.DMG = 20
        self.pose_x = x
        self.pose_y = y
        self.count = n
        self.pay = 30
        self.tip = 'Thief'
        self.attack_tip = 'steal'
        self.color = col
        self.garbage = 0


    def get_DMG(self):
        return (self.DMG + self.garbage * 2) * self.count

    def set_DMG(self, x):
        self.DMG = x

    def get_garbage(self):
        return self.garbage

    def set_garbage(self, x):
        self.garbage = x

    def attack(self, kek):
        temp = kek.get_HP()
        if (kek.get_Def() - self.get_DMG()) < 0 and (temp > 0):
            kek.set_HP(temp + kek.get_Def() - self.get_DMG())
        self.set_garbage(self.get_garbage() + self.get_DMG()//4)


class CFactoryBeasts:

    @abstractmethod
    def Beast_create_Red(self):
        pass

    @abstractmethod
    def Beast_create_Blue(self):
        pass

    @abstractmethod
    def Beast_create_White(self):
        pass


class CKuramaFactory(CFactoryBeasts):

    def __init__(self):
        super().__init__()

    def Beast_create_Red(self, x1=25, y1=25):
        return Kurama(col='red', x=x1, y=y1)

    def Beast_create_Blue(self, x1=25, y1=25):
        return Kurama(col='blue', x=x1, y=y1)

    def Beast_create_White(self, x1=25, y1=25):
        return Kurama(x=x1, y=y1)


class CShukakuFactory(CFactoryBeasts):

    def __init__(self):
        super().__init__()

    def Beast_create_Red(self, x1=25, y1=25):
        return Shukaku(col='red', x=x1, y=y1)

    def Beast_create_Blue(self, x1=25, y1=25):
        return Shukaku(col='blue', x=x1, y=y1)

    def Beast_create_White(self, x1=25, y1=25):
        return Shukaku(x=x1, y=y1)


class CFactoryHumans:

    @abstractmethod
    def Human_create_Red(self):
        pass

    @abstractmethod
    def Human_create_Blue(self):
        pass

    @abstractmethod
    def Human_create_White(self):
        pass


class CSwordmanFactory(CFactoryHumans):

    def __init__(self):
        super().__init__()

    def Human_create_Red(self, x=1, x1=0, y1=0):
        return Swordman(col='red', n=x, x=x1, y=y1)

    def Human_create_Blue(self, x=1, x1=0, y1=0):
        return Swordman(col='blue', n=x, x=x1, y=y1)

    def Human_create_White(self, x=1, x1=0, y1=0):
        return Swordman(col='white', n=x, x=x1, y=y1)


class CArcherFactory(CFactoryHumans):

    def __init__(self):
        super().__init__()

    def Human_create_Red(self, x=1, x1=0, y1=0):
        return Archer(col='red', n=x, x=x1, y=y1)

    def Human_create_Blue(self, x=1, x1=0, y1=0):
        return Archer(col='blue', n=x, x=x1, y=y1)

    def Human_create_White(self, x=1, x1=0, y1=0):
        return Archer(col='white', n=x, x=x1, y=y1)


class CShamanFactory(CFactoryHumans):

    def __init__(self):
        super().__init__()

    def Human_create_Red(self, x=1, x1=0, y1=0):
        return Shaman(col='red', n=x, x=x1, y=y1)

    def Human_create_Blue(self, x=1, x1=0, y1=0):
        return Shaman(col='blue', n=x, x=x1, y=y1)

    def Human_create_White(self, x=1, x1=0, y1=0):
        return Shaman(col='white', n=x, x=x1, y=y1)


class CThiefFactory(CFactoryHumans):

    def __init__(self):
        super().__init__()

    def Human_create_Red(self, x=1, x1=0, y1=0):
        return Thief(col='red', n=x, x=x1, y=y1)

    def Human_create_Blue(self, x=1, x1=0, y1=0):
        return Thief(col='blue', n=x, x=x1, y=y1)

    def Human_create_White(self, x=1, x1=0, y1=0):
        return Thief(col='white', n=x, x=x1, y=y1)


class CArmy:

    def __init__(self):
        self.KurF = CKuramaFactory()
        self.ShuF = CShukakuFactory()
        self.SwordF = CSwordmanFactory()
        self.ArF = CArcherFactory()
        self.ShaF = CShamanFactory()
        self.ThF = CThiefFactory()

    @abstractmethod
    def get_moral(self):
        pass

    @abstractmethod
    def get_total_DMG(self):
        pass

    @abstractmethod
    def get_total_PRT(self):
        pass

    @abstractmethod
    def get_max_size(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_is_Beast(self):
        pass

    @abstractmethod
    def get_money(self):
        pass

    @abstractmethod
    def get_side(self):
        pass

    @abstractmethod
    def set_moral(self, x):
        pass

    @abstractmethod
    def set_max_size(self, x):
        pass

    @abstractmethod
    def set_size(self, x):
        pass

    @abstractmethod
    def set_is_Beast(self, x):
        pass

    @abstractmethod
    def set_money(self, x):
        pass

    @abstractmethod
    def add_Kurama(self):
        pass

    @abstractmethod
    def add_Shukaku(self):
        pass

    @abstractmethod
    def add_Swordman(self):
        pass

    @abstractmethod
    def add_Archer(self):
        pass

    @abstractmethod
    def add_Shaman(self):
        pass

    @abstractmethod
    def add_Thief(self):
        pass

    @abstractmethod
    def del_Unit(self):
        pass

    @abstractmethod
    def get_Unit(self):
        pass


class CArmy_Red(CArmy):

    def __init__(self):
        super().__init__()
        self.moral = 0
        self.total_DMG = 0
        self.total_PRT = 0
        self.max_size = 30
        self.size = 0
        self.is_Beast = 0
        self.money = 50000
        self.tact = OrderedDict()

    def get_moral(self):
        return self.moral

    def get_total_DMG(self):
        return self.total_DMG

    def get_total_PRT(self):
        return self.total_PRT

    def get_max_size(self):
        return self.max_size

    def get_size(self):
        return self.size

    def get_is_Beast(self):
        return self.is_Beast

    def get_money(self):
        return self.money

    def get_side(self):
        return 'Blue'

    def set_moral(self, x):
        self.moral = x

    def set_max_size(self, x):
        self.max_size = x

    def set_size(self, x):
        self.size = x

    def set_is_Beast(self, x):
        self.is_Beast = x

    def set_money(self, x):
        self.money = x

    def add_Kurama(self, x1=25, y1=25):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size:
            self.size += 1
            temp = self.KurF.Beast_create_Red(x1, y1)
            self.tact[h] = temp
            self.moral += 1
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.is_Beast = 1

    def add_Shukaku(self, x1=25, y1=25):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size:
            self.size += 1
            temp = self.ShuF.Beast_create_Red(x1, y1)
            self.tact[h] = temp
            self.moral += 1
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.is_Beast = 1

    def add_Swordman(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.SwordF.Human_create_Red(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Archer(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ArF.Human_create_Red(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Shaman(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ShaF.Human_create_Red(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Thief(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ThF.Human_create_Red(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def get_Unit(self, x1=0, y1=0):
        h = (x1, y1)
        if self.tact.get(h):
            return self.tact[h]

    def del_Unit(self, x1=0, y1=0):
        h = (x1, y1)
        if self.tact.get(h):
            self.total_DMG -= self.tact.get(h).get_DMG()
            self.total_PRT -= self.tact.get(h).get_Def()
            self.tact.pop(h)


class CArmy_Blue(CArmy):

    def __init__(self):
        super().__init__()
        self.moral = 0
        self.total_DMG = 0
        self.total_PRT = 0
        self.max_size = 30
        self.size = 0
        self.is_Beast = 0
        self.money = 50000
        self.tact = OrderedDict()

    def get_moral(self):
        return self.moral

    def get_total_DMG(self):
        return self.total_DMG

    def get_total_PRT(self):
        return self.total_PRT

    def get_max_size(self):
        return self.max_size

    def get_size(self):
        return self.size

    def get_is_Beast(self):
        return self.is_Beast

    def get_money(self):
        return self.money

    def get_side(self):
        return 'Blue'

    def set_moral(self, x):
        self.moral = x

    def set_max_size(self, x):
        self.max_size = x

    def set_size(self, x):
        self.size = x

    def set_is_Beast(self, x):
        self.is_Beast = x

    def set_money(self, x):
        self.money = x

    def add_Kurama(self, x1=25, y1=25):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size:
            self.size += 1
            temp = self.KurF.Beast_create_Blue(x1, y1)
            self.tact[h] = temp
            self.moral += 1
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.is_Beast = 1

    def add_Shukaku(self, x1=25, y1=25):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size:
            self.size += 1
            temp = self.ShuF.Beast_create_Blue(x1, y1)
            self.tact[h] = temp
            self.moral += 1
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.is_Beast = 1

    def add_Swordman(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.SwordF.Human_create_Blue(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Archer(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ArF.Human_create_Blue(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Shaman(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ShaF.Human_create_Blue(x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def add_Thief(self, x1=25, y1=25, n=1):
        h = (x1, y1)
        if not self.tact.get(h) and len(self.tact) <= self.max_size and self.money>0:
            self.size += 1
            temp = self.ThF.Human_create_Blue(n, x1, y1)
            self.tact[h] = temp
            self.total_DMG += temp.get_DMG()
            self.total_PRT += temp.get_Def()
            self.money -= n * temp.get_pay()

    def get_Unit(self, x1=0, y1=0):
        h = (x1, y1)
        if self.tact.get(h):
            return self.tact[h]

    def del_Unit(self, x1=0, y1=0):
        h = (x1, y1)
        if self.tact.get(h):
            self.total_DMG -= self.tact.get(h).get_DMG()
            self.total_PRT -= self.tact.get(h).get_Def()
            self.tact.pop(h)


class CArmyFactory:

    def make_Red_army(self):
        return CArmy_Red()

    def make_Blue_army(self):
        return CArmy_Blue()


class UnitTest(unittest.TestCase):
    ArmyF = CArmyFactory()
    KurF = CKuramaFactory()
    ShuF = CShukakuFactory()
    SwordF = CSwordmanFactory()
    ArF = CArcherFactory()
    ShaF = CShamanFactory()
    ThF = CThiefFactory()

    def test_Kurama(self):
        temp1 = self.KurF.Beast_create_White()
        self.assertIsNotNone(temp1)
        self.assertEqual(temp1.get_pose_x(), 25)
        self.assertEqual(temp1.pose_x, 25)
        self.assertEqual(temp1.get_HP(), 300)
        self.assertEqual(temp1.HP, 300)
        self.assertEqual(temp1.get_tip(), 'KU')
        self.assertEqual(temp1.tip, 'KU')
        self.assertEqual(temp1.get_attack_tip(), 'attack')
        self.assertEqual(temp1.attack_tip, 'attack')
        temp1.set_HP(150)
        self.assertEqual(temp1.get_HP(), 150)
        self.assertEqual(temp1.HP, 150)
        self.assertEqual(temp1.get_color(), 'white')
        self.assertEqual(temp1.color, 'white')
        temp2 = self.KurF.Beast_create_Red(34, 44)
        self.assertEqual(temp2.get_pose_x(), 34)
        self.assertEqual(temp2.pose_x, 34)
        self.assertEqual(temp2.get_color(), 'red')
        self.assertEqual(temp2.color, 'red')
        temp2.walk(100, 101)
        self.assertEqual(temp2.get_pose_y(), 101)
        self.assertEqual(temp2.pose_y, 101)
        temp2.attack(temp1)
        self.assertEqual(temp1.get_HP(), 120)

    def test_Shukaku(self):
        temp1 = self.ShuF.Beast_create_White()
        self.assertIsNotNone(temp1)
        self.assertEqual(temp1.get_pose_x(), 25)
        self.assertEqual(temp1.pose_x, 25)
        self.assertEqual(temp1.get_HP(), 500)
        self.assertEqual(temp1.HP, 500)
        self.assertEqual(temp1.get_tip(), 'SH')
        self.assertEqual(temp1.tip, 'SH')
        self.assertEqual(temp1.get_attack_tip(), 'shot')
        self.assertEqual(temp1.attack_tip, 'shot')
        temp1.set_HP(150)
        self.assertEqual(temp1.get_HP(), 150)
        self.assertEqual(temp1.HP, 150)
        self.assertEqual(temp1.get_color(), 'white')
        self.assertEqual(temp1.color, 'white')
        temp2 = self.ShuF.Beast_create_Red(34, 44)
        self.assertEqual(temp2.get_pose_x(), 34)
        self.assertEqual(temp2.pose_x, 34)
        self.assertEqual(temp2.get_color(), 'red')
        self.assertEqual(temp2.color, 'red')
        temp2.walk(100, 101)
        self.assertEqual(temp2.get_pose_y(), 101)
        self.assertEqual(temp2.pose_y, 101)
        temp2.shot(temp1)
        self.assertEqual(temp1.get_HP(), 150)

    def test_Swordman(self):
        temp1 = self.SwordF.Human_create_White()
        self.assertIsNotNone(temp1)
        self.assertEqual(temp1.get_count(), 1)
        self.assertEqual(temp1.count, 1)
        self.assertEqual(temp1.get_pose_x(), 0)
        self.assertEqual(temp1.pose_x, 0)
        self.assertEqual(temp1.get_HP(), 16)
        self.assertEqual(temp1.HP, 16)
        self.assertEqual(temp1.get_tip(), 'Sw')
        self.assertEqual(temp1.tip, 'Sw')
        self.assertEqual(temp1.get_attack_tip(), 'attack')
        self.assertEqual(temp1.attack_tip, 'attack')
        temp1.set_HP(161)
        self.assertEqual(temp1.get_count(), 10)
        self.assertEqual(temp1.count, 10)
        self.assertEqual(temp1.get_HP(), 160)
        self.assertEqual(temp1.HP, 16)
        self.assertEqual(temp1.get_color(), 'white')
        self.assertEqual(temp1.color, 'white')
        temp2 = self.ShuF.Beast_create_Red()
        temp1.attack(temp2)
        self.assertEqual(temp2.get_HP(), 435)

    def test_Thief(self):
        temp1 = self.ThF.Human_create_White(x1=10, x=15, y1=20)
        self.assertIsNotNone(temp1)
        self.assertEqual(temp1.get_count(), 15)
        self.assertEqual(temp1.count, 15)
        self.assertEqual(temp1.get_pose_x(), 10)
        self.assertEqual(temp1.pose_y, 20)
        temp1.set_garbage(5)
        temp2 = self.ShuF.Beast_create_Red()
        temp1.attack(temp2)
        self.assertEqual(temp2.get_HP(), 125)

    def test_Army(self):
        RArmy = self.ArmyF.make_Red_army()
        self.assertIsNotNone(RArmy)
        RArmy.add_Kurama()
        RArmy.add_Kurama(100, 100)
        self.assertIsNotNone(RArmy.tact.get((25, 25)))
        Kurama = self.KurF.Beast_create_Red()
        h1 = (25, 25)
        h2 = (100, 100)
        self.assertEqual(RArmy.tact[h1].HP == RArmy.tact[h2].HP, 1)
        RArmy.add_Shukaku(100, 100)
        self.assertEqual(RArmy.tact[h1].HP == RArmy.tact[h2].HP, 1)
        self.assertEqual(RArmy.get_size(), 2)
        self.assertEqual(RArmy.size, 2)
        for i in range(100):
            RArmy.add_Kurama(100, i)
        h3 = (100, 50)
        self.assertEqual(RArmy.get_size(), 31)
        self.assertIsNone(RArmy.get_Unit(h3[0], h3[1]))
        RArmy.del_Unit(h2[0], h2[1])
        self.assertIsNone(RArmy.tact.get(h2))
        RArmy.add_Shukaku(100, 100)
        RArmy.add_Shukaku(1000, 1000)
        self.assertIsNone(RArmy.tact.get((1000, 1000)))


if __name__ == '__main__':
    unittest.main()