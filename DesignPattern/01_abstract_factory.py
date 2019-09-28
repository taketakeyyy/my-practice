# -*- coding:utf-8 -*-

def main():
    factoryA = create_factory(PizzaFactoryA())
    pizza1 = factoryA.make_pizza("high")
    pizza1.check_pizza()

    print("===")

    factoryB = create_factory(PizzaFactoryB())
    pizza2 = factoryB.make_pizza("normal")
    pizza2.check_pizza()


""" Abstract Factory - 生成に関するパターン
ピザをつくることを考える

・ピザは生地、ソース、トッピングから構成される
・工場Aでは生地は小麦、ソースはトマト、トッピングにコーンを使用する
・工場Bでは生地は米粉、ソースはバジル、トッピングにチーズを使用する
・すべての素材に確認のためのメソッド（check）をもたせる

■Abstract Factoryの概要
ピザAとピザBを作るとき、

```python
pizza_factoryA = PizzaFactoryA()
pizzaA = pizza_factoryA.make()

pizza_factoryB = PizzaFactoryB()
pizzaB = pizza_factoryB.make()
```

というような作り方をするのではなく、

```python
pizzaA = make_pizza(PizzaFactoryA())
pizzaB = make_pizza(PizzaFactoryB())
```

みたいに、関数の引数にクラスインスタンスを与えて処理を共通化するアイデア


"""

amount_dict = {"hight": 1.2, "normal": 1.0, "low": 0.8}

def make_pizza(self, factory, amount_str):
    """ ピザを作る
    具体クラスがこのクラスを継承するのではなく、このクラスの引数に具体クラスを代入して動作させる」というアイデア
    """
    amount = amount_dict[amount_str]
    self.pizza_materials = []
    self.pizza_materials.append(self.factory.add_dough(amount))  # 生地
    self.pizza_materials.append(self.factory.add_source(amount)) # ソース
    self.pizza_materials.append(self.factory.add_topping(amount)) # トッピング


class AbstractPizzaFactory:
    """ ピザ工場の抽象クラス """
    def __init__(self, amount_str="normal"):
        self.factory = pizza_factory

    def check_pizza(self):
        for pizza_material in self.pizza_materials:
            pizza_material.check()

    def add_dough(self, amount=1):
        pass

    def add_source(self, amount=1):
        pass

    def add_topping(self, amount=1):
        pass

# ConcreteFactory
class PizzaFactoryA(AbstractPizzaFactory):
    """ ピザ工場A """
    # 具体的に実装
    def add_dough(self, amount=1):
        return WheatDough(amount)

    def add_source(self, amount=1):
        return TomatoSource(amount)

    def add_topping(self, amount=1):
        return CoanTopping(amount)


class PizzaFactoryB(AbstractPizzaFactory):
    """ ピザ工場B """
    # 具体的に実装
    def add_dough(self, amount=1):
        return RiceFlourDough(amount)

    def add_source(self, amount=1):
        return BasilSource(amount)

    def add_topping(self, amount=1):
        return CheeseTopping(amount)


class Dough():
    """ 生地 """
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

class WheatDough(Dough):
    """ 小麦生地 """
    def check(self):
        print("Wheat(amount): {}".format(self.amount))

class RiceFlourDough(Dough):
    """ 米粉生地 """
    def check(self):
        print("RiceFlour(amount): {}".format(self.amount))


class Source:
    """ ソース """
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

class TomatoSource(Source):
    """ トマトソース """
    def check(self):
        print("TomatoSource(amount): {}".format(self.amount))

class BasilSource(Source):
    """ バジルソース """
    def check(self):
        print("BasilSource(amount): {}".format(self.amount))


class Topping():
    """ トッピング """
    def __init__(self, amount):
        self.amount = amount

    def check(self):
        pass

class CoanTopping(Topping):
    """ コーントッピング """
    def check(self):
        print("CoanTopping(amount): {}".format(self.amount))

class CheeseTopping(Topping):
    """ チーズトッピング """
    def check(self):
        print("CheeseTopping(amount): {}".format(self.amount))


if __name__ == "__main__":
    main()