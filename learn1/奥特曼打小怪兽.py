from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Figther(metaclass=ABCMeta):
    """战斗者"""
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """攻击"""
        pass


class UItraman(Figther):
    """奥特曼"""
    __slots__ = '_name', '_hp', '_mp'

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """攻击3/4，最低50"""
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 / 4
            if injury <= 50:
                injury = 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                temp.hp -= randint(10, 15)
            return True

        else:
            randrange(others).hp -= randint(25, 35)
            return False

    def resume(self):
        """回复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return self._name + '奥特曼' + str(self._hp) + '生命值' + str(self._mp) + '魔法值'


class Monster(Figther):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        super().__init__(name, hp)

    def attack(self, other):
        other.hp -= randint(5, 15)

    def __str__(self):
        return self._name + '小怪兽' + str(self._hp) + '生命值'


def is_any_alive(monsters):
    """判断怪兽是否活着"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False
def select_alive_one(monsters):
    """选中一个活着怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster
def display_info(ultraman,monsters):
    """显示奥特曼和怪兽"""
    print(ultraman)
    for monster in monsters:
        print(monster,end=' ')

u = UItraman('杨刚',250,120)
m1 = Monster('m1',250)
m2 = Monster('m2',250)
m3 = Monster('m3',250)
ms = [m1,m2,m3]
f = 1
while u.alive and is_any_alive(ms):
    print('\n=======第%02d回合=====' % f)
    m = select_alive_one(ms)
    skill = randint(1, 10)
    if skill <= 5:
        print('%s使用普通攻击打了%s' %(u.name, m.name))
        u.attack(m)
    elif skill <= 9:
        print('%s使用魔法攻击打了%s' %(u.name, m.name))
        u.magic_attack(ms)
    else:
        print('%s使用绝招攻击打了%s' %(u.name, m.name))
        u.huge_attack(m)
    if m.alive > 0:
        print('%s使用普通攻击打了%s' %(m.name, u.name))
        m.attack(u)
    display_info(u,ms)
    f += 1
    print('\n%s回复%02d魔法值' % (u.name,u.resume()))
print('\n======战斗介结束=====\n')
if u.alive >0:
    print('%s胜利'% u.name)
else:
    print('%s胜利'% m.name)