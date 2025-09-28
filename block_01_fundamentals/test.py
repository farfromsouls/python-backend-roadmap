from random import uniform, randint

from calculator import calculate


def main()->None:
    tests_n = int(input("tests amount: "))
    for i in range(tests_n):
        x = uniform(-(10**10), 10**10)
        y = uniform(-(10**10), 10**10)
        operation = "+-*/"[randint(0,3)]
        assert calculate(x, y, operation) == eval(f"{x}{operation}{y}")

if __name__ == "__main__":
    main()
    print("Everything passed")