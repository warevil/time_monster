from time_monster.timer import Timer

if __name__ == "__main__":
    name = "Loop range"
    code = """
for _ in range(10000):
    pass
    """
    timer = Timer(code=code, name=name)
    timer.log()

    name = "Loop repeat"
    setup = "from itertools import repeat"
    code = """
for _ in repeat(None, 10000):
    pass
    """
    timer.log(code=code, setup=setup, name=name)

    name = "Loop 2 lists using zip"
    setup = """
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    code = """
for a, b in zip(a_list, b_list):
    x = (a, b)
    """
    timer.log(code=code, name=name, setup=setup)

    name = "Loop 2 lists using range"
    code = """
for i in range(len(a_list)):
    x = (a_list[i], b_list[i])
    """
    timer.log(code=code, name=name)

    name = "Loop 2 lists using range (hardcoded list length)"
    code = """
for i in range(10):
    x = (a_list[i], b_list[i])
    """
    timer.log(code=code, name=name)
