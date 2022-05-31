def scope():
    restaurant = {
        "kitchen": {"A1": 1, "A3": 1.5},
        "A1": {"A3": 0.5, "A2": 1.75, "kitchen": 1},
        "A2": {"A1": 1.75, "A4": 0.5},
        "A3": {"kitchen": 1.5, "A1": 0.5, "A4": 1.75, "E3": 2.5, "E4": 2},
        "A4": {"A2": 0.5, "A3": 1.75, "D3": 3.5, "D4": 3, "B3": 2, "B4": 2.5},

        "B1": {"B2": 0.5, "B3": 1.75},
        "B2": {"B1": 0.5, "B4": 1.75},
        "B3": {"B1": 1.75, "B4": 0.5, "A4": 2, "D4": 2.5},
        "B4": {"B3": 0.5, "B2": 1.75, "C4": 1.5, "A4": 2.5},

        "C1": {"C2": 1, "C4": 1.75},
        "C2": {"C1": 1, "C6": 1, "C3": 1},
        "C3": {"C2": 1, "C8": 1.75},
        "C4": {"B4": 1.5, "C7": 0.5, "C1": 1.75},
        "C5": {"C6": 0.5, "C8": 0.5},
        "C6": {"C2": 1, "C5": 0.5, "C7": 0.5},
        "C7": {"C6": 0.5, "C4": 0.5},
        "C8": {"C5": 0.5, "D3": 1.5, "C3": 1.75},

        "D1": {"D2": 0.5, "D3": 1.75},
        "D2": {"D1": 0.5, "D4": 1.75},
        "D3": {"D1": 1.75, "D4": 0.5, "A4": 3.5, "C8": 1.5},
        "D4": {"D3": 0.5, "D2": 1.75, "B3": 2.5, "A4": 3},

        "E1": {"E2": 0.5, "E3": 1.75},
        "E2": {"E1": 0.5, "E4": 1.75},
        "E3": {"E4": 0.5, "E1": 1.75, "A3": 2.5},
        "E4": {"E3": 0.5, "E2": 1.75, "A3": 2},
    }
    cost = 0
    best_cost = 1000

    path = []
    best_path = []

    origin = "kitchen"
    destiny = ""

    def the_closest_table():
        nonlocal cost, best_cost, best_path, path
        t_list = input_tables()
        pre_search(origin, t_list[0])
        print(best_path)
        print(best_cost)
        cost = 0
        best_cost = 1000
        path = []
        best_path = []

    def pre_search(t_origin, t_destiny):
        nonlocal origin, destiny, path
        #path.append(t_origin)
        origin = t_origin
        destiny = t_destiny
        search(origin)

    def search(table):
        nonlocal cost, best_cost, best_path, path
        if not is_best_route(table):
            t = restaurant.get(table)
            for key in t.keys():
                if key not in path:
                    path.append(key)
                    cost += t.get(key)
                    if cost < best_cost:
                        search(key)
                    path.pop()
                    cost -= t.get(key)

    def is_best_route(table):
        nonlocal cost, best_cost, best_path, path
        if table == destiny and cost < best_cost:
            best_cost = cost
            best_path = path.copy()
            return True
        return False

    def input_tables():
        size = int(input("Introduce the number of tables: "))
        tables = []
        for i in range(size):
            tables.append(input("Introduce table" + str(i + 1) + ": "))
        return tables

    the_closest_table()


scope()
