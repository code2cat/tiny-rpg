# Author: 沈麻呆
from __future__ import annotations

import random
import time
from typing import Tuple


class Hero:
    def __init__(self, name: str, hp: int = 100, attack: Tuple[int, int] = (5, 10), defence: int = 5):
        self.name = name
        self.hp = hp
        self._attack = attack
        self.defence = defence
        self._rand_seed = random.Random(time.time_ns())  # 随机数

    @property
    def attack(self) -> int:
        return self._rand_seed.randint(self._attack[0], self._attack[1])

    @staticmethod
    def generate() -> Hero:
        rand = random.Random(time.time_ns())
        hp = rand.randint(100, 150)
        attack_min = rand.randint(1, 5)
        attack_max = rand.randint(3, 10)
        attack_min, attack_max = min(attack_min, attack_max), max(attack_min, attack_max)
        defence = rand.randint(5, 10)
        return Hero("老板", hp=hp, attack=(attack_min, attack_max), defence=defence)

    def __str__(self):
        return f'name={self.name}, hp={self.hp}, attack={self._attack}, defence={self.defence}'


class Game:
    def fight(self, attacker: Hero, defender: Hero) -> bool:
        """
        :return: true表示决出胜负，否则游戏继续
        """
        damage = max(0, attacker.attack - defender.defence)
        defender.hp -= damage
        print(f'[{attacker.name}] 对 [{defender.name}] 攻击，造成 [{damage}] 点伤害')
        if defender.hp <= 0:
            print(f'[{defender.name}] 倒地不起，[{attacker.name}] 胜利了')
        return defender.hp <= 0

    def demo(self):
        me = Hero('我')
        enemy = Hero.generate()
        #  打个招呼吧
        print(me)
        print(enemy)
        while True:
            if self.fight(me, enemy):
                break
            if self.fight(enemy, me):
                break

    def run(self):
        self.demo()


if __name__ == '__main__':
    Game().run()
