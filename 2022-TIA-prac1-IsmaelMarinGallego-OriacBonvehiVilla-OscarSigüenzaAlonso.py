restaurant = {
    "kitchen": {"A1": [1, False], "A3": [1.5, False]},
    "A1": {"A3": [0.5, False], "A2": [1.75, False], "kitchen": [1, False]},
    "A2": {"A1": [1.75, False], "A4": [0.5, False]},
    "A3": {"kitchen": [1.5, False], "A1": [0.5, False], "A4": [1.75, False], "E3": [2.5, False], "E4": [2, False]},
    "A4": {"A2": [0.5, False], "A3": [1.75, False], "D3": [3.5, False], "D4": [3, False], "B3": [2, False], "B4": [2.5, False]},

    "B1": {"B2": [0.5, False], "B3": [1.75, False]},
    "B2": {"B1": [0.5, False], "B4": [1.75, False]},
    "B3": {"B1": [1.75, False], "B4": [0.5, False], "A4": [2, False], "D4": [2.5, False]},
    "B4": {"B3": [0.5, False], "B2": [1.75, False], "C4": [1.5, False], "A4": [2.5, False]},

    "C1": {"C2": [1, False], "C4": [1.75, False]},
    "C2": {"C1": [1, False], "C6": [0, False], "C3": [1, False]},
    "C3": {"C2": [1, False], "C8": [1.75, False]},
    "C4": {"B4": [1.5, False], "C7": [0.5, False], "C1": [1.75, False]},
    "C5": {"C6": [0.5, False], "C8": [0.5, False]},
    "C6": {"C2": [0, False], "C5": [0.5, False], "C7": [0.5, False]},
    "C7": {"C6": [0.5, False], "C4": [0.5, False]},
    "C8": {"C5": [0.5, False], "D3": [1.5, False], "C3": [1.75, False]},

    "D1": {"D2": [0.5, False], "D3": [1.75, False]},
    "D2": {"D1": [0.5, False], "D4": [1.75, False]},
    "D3": {"D1": [1.75, False], "D4": [0.5, False], "A4": [3.5, False], "C8": [1.5, False]},
    "D4": {"D3": [0.5, False], "D2": [1.75, False], "B3": [2.5, False], "A4": [3, False]},

    "E1": {"E2": [0.5, False], "E3": [1.75, False]},
    "E2": {"E1": [0.5, False], "E4": [1.75, False]},
    "E3": {"E4": [0.5, False], "E1": [1.75, False], "A3": [2.5, False]},
    "E4": {"E3": [0.5, False], "E2": [1.75, False], "A3": [2, False]},
}
path = []
cost = [0]
best_path = []
best_cost = [1000]
tables = []


def search():
    path.append("kitchen")
    open("kitchen", "A1")


def open(table, anterior):
    t = restaurant.get(table)
    if t.get(anterior)[1]:
        return
    if not is_solution():
        for key in t.keys():
            if not t.get(key)[1]:
                path.append(key)
                cost[0] += t.get(key)[0]
                t.get(key)[1] = True
                open(key, table)
                cost[0] -= t.get(key)[0]
                t.get(key)[1] = False
                path.pop()


def is_solution():
    solution = 0
    for t in tables:
        if path.__contains__(t):
            solution += 1

    solution = (solution == 4)
    if solution and cost[0] < best_cost[0]:
        best_cost[0] = cost[0]
        best_path.clear()
        for t in path:
            best_path.append(t)
    return solution


def input_tables():
    tables.append("C1")
    tables.append("B2")
    tables.append("D1")
    tables.append("E4")
    # for i in range(4):
    #    tables.append(input("Introduce table"+str(i+1)+": "))


input_tables()
search()
print(path)
print(best_path)
