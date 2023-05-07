class Animals:
    def __init__(self, age_in_months, breed, required_food_in_kgs, breath_type, sound_type, increament_in_age,
                 increament_in_required_food):
        if age_in_months != 1:
            raise ValueError(f'ValueError: Invalid value for field age_in_months:{age_in_months}')

        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        self.breath_type = breath_type
        self.sound_type = sound_type
        self.increament_in_age = increament_in_age
        self.increament_in_required_food = increament_in_required_food

    def breathe(self):
        print(self.breath_type)

    def make_sound(self):
        print(self.sound_type)

    def grow(self):
        self.age_in_months += self.increament_in_age
        self.required_food_in_kgs += self.increament_in_required_food


class Deer(Animals):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs, breath_type="Breath in air",
                         sound_type="Buck buck", increament_in_age=1, increament_in_required_food=2)


class Lion(Animals):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs, breath_type="Breath in air",
                         sound_type="Roar Roar", increament_in_age=1, increament_in_required_food=4)

    def hunt(self, zoo):
        removing_animal = None
        Animal_present = False
        for animal in zoo.list_of_animals:
            if isinstance(animal, Deer):
                Animal_present = True
                removing_animal = animal

        if Animal_present == True:
            zoo.list_of_animals.remove(animal)
        else:
            print("No deers to hunt")


class Shark(Animals):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs, breath_type="Breath oxygen from water",
                         sound_type="Shark sound", increament_in_age=1, increament_in_required_food=8)

    def hunt(self, zoo):
        removing_animal = None
        Animal_present = False
        for animal in zoo.list_of_animals:
            if isinstance(animal, GoldFish):
                Animal_present = True
                removing_animal = animal

        if Animal_present == True:
            zoo.list_of_animals.remove(animal)
        else:
            print("No GoldFish to hunt")


class GoldFish(Animals):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs, breath_type="Breath oxygen from water",
                         sound_type="Hum Hum", increament_in_age=1, increament_in_required_food=0.2)


class Zoo:
    count_of_animals_in_all_zoos = 0

    def __init__(self):
        self.reserved_food_in_kgs = 0
        self.list_of_animals = list()

    def count_animals(self):
        return len(self.list_of_animals)

    def add_food_to_reserve(self, added_food):
        self.reserved_food_in_kgs += added_food

    def add_animal(self, added_animal):
        Zoo.count_of_animals_in_all_zoos += 1
        self.list_of_animals.append(added_animal)

    def feed(self, added_animal):
        if self.reserved_food_in_kgs >= added_animal.required_food_in_kgs:
            self.reserved_food_in_kgs -= added_animal.required_food_in_kgs
            added_animal.grow()

    @classmethod
    def count_animals_in_all_zoos(cls):
        print(cls.count_of_animals_in_all_zoos)

    @classmethod
    def count_animals_in_given_zoos(cls, zoo_list):
        count = 0
        for zoo in zoo_list:
            count += zoo.count_animals()
        return count


class Snake(Animals):
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        super().__init__(age_in_months, breed, required_food_in_kgs, breath_type="Breath in air",
                         sound_type="Hiss Hiss", increament_in_age=1, increament_in_required_food=0.5)

    def hunt(self, zoo):
        removing_animal = None
        Animal_present = False
        for animal in zoo.list_of_animals:
            if isinstance(animal, GoldFish):
                Animal_present = True
                removing_animal = animal

        if Animal_present == True:
            zoo.list_of_animals.remove(animal)
        else:
            print("No deers to hunt")


deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
deer.breathe()
deer.make_sound()
print(deer.required_food_in_kgs)
deer.grow()
print(deer.required_food_in_kgs)
deer.breathe()
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
print(deer)

lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
print(lion.age_in_months)
print(lion.breed)
print(lion.required_food_in_kgs)
lion.grow()
print(lion.required_food_in_kgs)
print(lion.age_in_months)

lion.breathe()
lion.make_sound()

shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
print(shark.age_in_months)
print(shark.breed)
print(shark.required_food_in_kgs)
shark.grow()
print(shark.required_food_in_kgs)
print(shark.age_in_months)
print(shark.make_sound())
print(shark.breathe())

gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
print(gold_fish.age_in_months)
print(gold_fish.breed)
print(gold_fish.required_food_in_kgs)
gold_fish.grow()
print(gold_fish.required_food_in_kgs)
print(gold_fish.age_in_months)

gold_fish.breathe()
gold_fish.make_sound()

zoo = Zoo()
zoo.add_food_to_reserve(10000)
print(zoo.reserved_food_in_kgs)
print(zoo.count_animals())

gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
print(zoo.count_animals())
print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
print(zoo.reserved_food_in_kgs)
print(gold_fish.age_in_months)

nehru_zoological_park = Zoo()
zoo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
print(zoo.count_animals_in_all_zoos())
Zoo.count_animals_in_given_zoos([zoo])

deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
print(nehru_zoological_park.count_animals())
print(lion.hunt(nehru_zoological_park))

snake = Snake(age_in_months=1, breed="Indian Cobra", required_food_in_kgs=5)
print(snake.age_in_months)
print(snake.breed)
print(snake.required_food_in_kgs)
snake.grow()
print(snake.required_food_in_kgs)
print(snake.age_in_months)

snake.breathe()
snake.make_sound()