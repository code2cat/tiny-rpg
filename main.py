# Author: 沈麻呆
from __future__ import annotations

class Hero:
    def __init__(self, name: str, hp: int = 100, attack: int = 10, defence: int = 5):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence

    @staticmethod
    def generate() -> Hero:
        return Hero("", 100, attack=10, defence=5)



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
        enemy = Hero('老板', defence=0)
        while True:
            if self.fight(me, enemy):
                break
            if self.fight(enemy, me):
                break

    def run(self):
        self.demo()


if __name__ == '__main__':
    Game().run()
