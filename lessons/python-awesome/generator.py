import random
import sys


def start():
    car_names = ["Audi", "Mers", "BMW", "Nissan", "Toyota"]
    car_colors = ["Black", "White", "Red", "Yellow"]
    car_count = 10000000

    def start_bad():
        cars = []
        for i in range(1, car_count + 1):
            cars.append({
                "id": i,
                "name": random.choice(car_names),
                "color": random.choice(car_colors)
            })
        return cars

    def start_good():
        for i in range(1, car_count + 1):
            yield {"id": i, "name": random.choice(car_names), "color": random.choice(car_colors)}

    # todo full list
    # cars1 = start_bad()  #
    # print(type(cars1), cars1)  # list[dict] [...'Nissan', 'color': 'Black'}, {'id': 9999998, 'name': 'BMW', 'color': 'Black'}, {'id': 9999999, 'name': 'Audi', 'color': 'Black'}, {'id': 10000000, 'name': 'BMW', 'color': 'Black'}]
    # print(sys.getsizeof(cars1))  # 89 095 160

    # todo generator
    cars1 = start_good()  #
    print(type(cars1), cars1)  # <class 'generator'> <generator object start.<locals>.start_good at 0x000001335FE99740>
    print(sys.getsizeof(cars1))  # 248

    # todo WORK
    with open("log.txt", "a") as file:
        for i in cars1:
            file.write(i["name"] + "\n")


if __name__ == "__main__":
    # list1 = [1, 2, 3]
    # tuple1 = (1, 2, 3)
    # dict1 = {1: "Bogdan", 2: "Bogdan", 3: "Bogdan"}
    #
    # print(sys.getsizeof(list1))
    # print(sys.getsizeof(tuple1))
    # print(sys.getsizeof(dict1))

    start()


    # def get_data():
    #     yield 10
    #     yield 12
    #     yield 13
    #
    # gen1 = get_data()
    # print(gen1.__next__())
    # print(gen1.__next__())
    # print(gen1.__next__())
