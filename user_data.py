def get_age(birth_year):
    current_year = 2024
    return current_year - birth_year
def get_user_data():
    full_name = input("Digite seu nome completo: ")
    while True:
        try:
            birth_year = int(input("Digite o ano de nascimento: "))
            if 1914 <= birth_year <= 2024:
                break
            else:
                print("Ano inválido. Digite um ano entre 1914 e 2024.")
        except ValueError:
            print("Ano inválido. Digite um ano valido.")
    age = get_age(birth_year)
    print(f"Ola, {full_name}! Voce tem {age} anos.")

get_user_data()