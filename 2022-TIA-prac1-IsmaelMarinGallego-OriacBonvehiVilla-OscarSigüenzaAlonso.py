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
    "C2": {"C1": 1, "C6": 0, "C3": 1},
    "C3": {"C2": 1, "C8": 1.75},
    "C4": {"B4": 1.5, "C7": 0.5, "C1": 1.75},
    "C5": {"C6": 0.5, "C8": 0.5},
    "C6": {"C2": 0, "C5": 0.5, "C7": 0.5},
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
path = []
cost = [0]
best_path = []
best_cost = [0]
tables = []


def search():
    open("kitchen")


def open(open_table):
    if not path.__contains__(open_table):
        if not is_solution():
            path.append(open_table)
            t = restaurant.get(open_table)
            for key in t.keys():
                cost[0] += t.get(key)
                open(key)
            #path.remove(open_table)




def is_solution():
    solution = 0
    for t in tables:
        if path.__contains__(t):
            solution += 1

    if cost[0] < best_cost[0]:
        best_cost[0] = cost
        best_path[0] = path
    return solution == 4


def input_tables():
    tables.append("A1")
    tables.append("A2")
    tables.append("A3")
    tables.append("C4")
    #for i in range(4):
    #    tables.append(input("Introduce table"+str(i+1)+": "))


input_tables()
search()
print(path)
print(path)
