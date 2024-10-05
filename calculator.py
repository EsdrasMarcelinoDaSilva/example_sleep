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

result = calculator(10, "abc", 1)
print(f"Resultado: {result}") 

result = calculator(10, 5, 1)
print(f"Resultado: {result}")  # Deve imprimir: Resultado: 15

result = calculator(10, 5, 2)
print(f"Resultado: {result}")  # Deve imprimir: Resultado: 5

result = calculator(10, 5, 3)
print(f"Resultado: {result}")  # Deve imprimir: Resultado: 50

result = calculator(10, 5, 4)
print(f"Resultado: {result}")  # Deve imprimir: Resultado: 2.0

result = calculator(10, 5, 5)
print(f"Resultado: {result}")  # Deve imprimir: Resultado: 0



