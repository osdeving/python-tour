import os

restaurants = [

    {'name': 'Italian House', 'category': 'Italiana', 'active': True},
    {'name': 'Sushi Place', 'category': 'Japonesa', 'active': False},
    {'name': 'Brazilian Grill', 'category': 'Brasileira', 'active': True},
]

def show_title():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    


def show_subtitle(text):
    os.system('clear')
    line = '*' * len(text)
    print(line)
    print(text)
    print(line)
    print()

def show_options():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Altivar/Desativar Restaurante')
    print('4. Sair\n')

def back_to_main_menu():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def invalid_option():
    print("Opção inválida!\n")
    back_to_main_menu()

def create_new_restaurant():
    ''' Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaraurantes
    '''
    show_subtitle('Cadastro de novos restaurantes')
    name = input('Digite o nome do restaurante que deseja cadastrar: ')
    category = input(f'Digite o nome da categoria do restaurante {name}: ')
    restaurant = {'name': name, 'category': category, 'active': False}
    restaurants.append(restaurant)
    print(f'O restaurante {name} foi cadastrado com sucesso!')

    back_to_main_menu()


def exit_app():
    show_subtitle('Encerrar aplicativo')

def list_restaurants():
    show_subtitle('Listando restaurantes')
    
    print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
    for restaurant in restaurants:
        name = restaurant['name']
        category = restaurant['category']
        active = 'ativado' if restaurant['active'] else 'desativado'
        print(f'{name.ljust(25)} | {category.ljust(25)} | {active}')
    
    back_to_main_menu()


def set_status():
    show_subtitle('Alterando estado do restaurante')
    name = input('Digite o nome do restaurante que deseja alterar o estado: ')
    found = False

    for restaurant in restaurants:
        if name == restaurant['name']:
            found = True
            restaurant['active'] = not restaurant['active']
            status_message = 'ativado' if restaurant['active'] else 'desativado'
            print(f'O restaurante {name} foi {status_message} com sucesso')

    if not found:
        print('O restaurante não foi encontrado')

    back_to_main_menu()

def choose_option():
    try:
        option = int(input('Escolha uma opção: '))

        if option == 1:
            create_new_restaurant()
        elif option == 2:
            list_restaurants()
        elif option == 3:
            set_status()
        elif option == 4:
            exit_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    show_title()
    show_options()
    choose_option()


if __name__ == '__main__':
    main()