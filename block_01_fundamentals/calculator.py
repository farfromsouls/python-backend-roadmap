def calculate(x: float, y: float, operation: str) -> float:
    match operation:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x / y
        case _:
            return ValueError("Ошибка ввода операции")

def main() -> None:
    while True:
        try:
            x = int(input("x="))
            y = int(input("y="))
        except ValueError:
            print("Ошибка ввода переменных")
            continue


        operation = input("op=")
        ans = calculate(x, y, operation)
        print(ans)

if __name__ == "__main__":
    main()