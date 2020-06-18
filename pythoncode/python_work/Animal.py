import yaml
class Animal:
    name: str = "default"
    color: str = "default"
    age: int = 1
    gender: str = "male"

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def Call(self):
        print(f"{self.name}会叫")

    def Run(self):
        print(f"{self.name}会跑")

class Cat(Animal):
    def __init__(self,name, color, age, gender, hair="短毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def Catch_mice(self,name):
        print(f"{self.name}会抓老鼠")
        return (f"{self.name}抓到了老鼠")

    def Call(self):
        print(f"{self.name}喜欢喵喵叫")

class Dog(Animal):
    def __init__(self, name, color, age, gender, hair="长毛"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def Housekeeping(self,name):
        print(f"{self.name}会看家")

    def Call(self):
        print(f"{self.name}汪汪叫")

if __name__ == '__main__':
    with open("Cat.yml", 'r', encoding="UTF-8") as f:
        cat = yaml.safe_load(f)
        # print(cat)
        cat1 = cat['Cat1']
        nametype = cat1['name']
        colortyle = cat1['color']
        agetype = cat1['age']
        gendertype = cat1['gender']
        hairtype = cat1['hair']

        Cattype = Cat(nametype,colortyle,agetype,gendertype,hairtype)
        catable = Cattype.Catch_mice(nametype)


        print(f"{nametype}是{colortyle}色的，今年{agetype}岁了，它是只{gendertype}猫，他的毛是{hairtype},{catable}")

    with open("Dog.yml", 'r', encoding="UTF-8") as f:
        dog = yaml.safe_load(f)
        dog1 = dog['Dog1']
        nametype = dog1['name']
        colortyle = dog1['color']
        agetype = dog1['age']
        gendertype = dog1['gender']
        hairtype = dog1['hair']

        Dogtype = Dog(nametype, colortyle, agetype, gendertype, hairtype)
        dogable = Dogtype.Housekeeping(nametype)

        print(f"{nametype}是{colortyle}色的，今年{agetype}岁了，它是只{gendertype}狗，他的毛是{hairtype}")


    # cat = Cat("小白","白色",2,"male","短毛")
    # cat.Catch_mice()
    # print(f"{cat.name,cat.color,cat.age,cat.gender,cat.hair}")
    #
    # dog = Dog("旺财", "黄色", 2, "male", "长毛")
    # dog.Housekeeping()
    # print(f"{dog.name, dog.color, dog.age, dog.gender, dog.hair}")

