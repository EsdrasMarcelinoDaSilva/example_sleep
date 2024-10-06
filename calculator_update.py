def calculator(num1, num2, operator):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 0

    operations = {
        1: lambda num1, num2: num1 + num2,
        2: lambda num1, num2: num1 - num2,
        3: lambda num1, num2: num1 * num2,
        4: lambda num1, num2: num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    }

    operation = operations.get(operator, lambda num1, num2: 0)
    result = operation(num1, num2)

    if isinstance(result, str) and "Erro" in result:
        return 0

    return int(result) if result.is_integer() else result

def main():
    while True:
        print("Calculadora")
        print("Operacoes:")
        print("1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Sair")

        try:
            choice = int(input("Insira o numero da operacao: "))
        except ValueError:
            print("Entrada invalida. Por favor, insira um numero inteiro.")
            continue

        if choice == 5:
            print("Saindo...")
            break
        elif choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Insira o primeiro numero: "))
                num2 = float(input("Insira o segundo numero: "))
            except ValueError:
                print("Entrada invalida. Por favor, insira um numero valido.")
                continue

            result = calculator(num1, num2, choice)
            print(f"Resultado: {result}")
        else:
            print("Entrada invalida. Por favor, insira um número entre 1 e 5.")

if __name__ == "__main__":
    main()