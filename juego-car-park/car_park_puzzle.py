import msvcrt
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_color():
    os.system("color 04")
 
 
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
 
def is_valid_move(board, car_positions, car, new_positions):
    for new_pos in new_positions:
        if not (0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0])):
            return False
        if board[new_pos[0]][new_pos[1]] != '.' and board[new_pos[0]][new_pos[1]] != 'M' and board[new_pos[0]][new_pos[1]] != car:
            return False
    return True
 
def move_car(board, car_positions, car, new_positions):
    # Borrar la posición actual del auto
    for pos in car_positions[car]:
        board[pos[0]][pos[1]] = '.'
    # Mover el auto a la nueva posición
    for pos in new_positions:
        board[pos[0]][pos[1]] = car
    car_positions[car] = new_positions
 
def get_new_positions(car_positions, car_to_move, move, horizontal):
    car_pos = car_positions[car_to_move]
    if horizontal:
        if move == 'a':  # Izquierda
            return [[pos[0], pos[1] - 1] for pos in car_pos]
        elif move == 'd':  # Derechaa
            return [[pos[0], pos[1] + 1] for pos in car_pos]
    else:
        if move == 'w':  # Arribaa
            return [[pos[0] - 1, pos[1]] for pos in car_pos]
        elif move == 's':  # Abajo
            return [[pos[0] + 1, pos[1]] for pos in car_pos]
    return car_pos  # No cambia la posición si el movimiento no es válido
 
def find_car_positions(board):
    car_positions = {}
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell.isalpha() and cell != 'M':  # Encontrar todas las letras que representan autos
                if cell not in car_positions:
                    car_positions[cell] = []
                car_positions[cell].append([i, j])
    return car_positions

def start(levels):
    print(""""
  ___   __   ____    ____   __   ____  __ _    ____  _  _  ____  ____  __    ____ 
 / __) / _\ (  _ \  (  _ \ / _\ (  _ \(  / )  (  _ \/ )( \(__  )(__  )(  )  (  __)
( (__ /    \ )   /   ) __//    \ )   / )  (    ) __/) \/ ( / _/  / _/ / (_/\ ) _) 
 \___)\_/\_/(__\_)  (__)  \_/\_/(__\_)(__\_)  (__)  \____/(____)(____)\____/(____)
          
          Seleccione el número del nivel que desea jugar:

          1- Nivel 1
          2- Nivel 2
          """)
    try:
        level = int(input("Digite el número del nivel: "))

        if level not in levels.keys():
            input("Nivel no válido, presione Enter para continuar: ")
            clear()
            start(levels)
        
        return level
    except:
        input("Nivel no válido, presione Enter para continuar: ")
        clear()
        start(levels)

 
def main():
    # Ejemplo de juego simple
    board1 = [['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.'],
             ['A', 'A', '.', 'C', 'B', '.', 'M'],
             ['.', '.', '.', 'C', 'B', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.']]
    
    board2 = [['.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 'F', 'F', '.', '.', '.'],
             ['.', '.', 'E', 'D', 'D', '.', '.'],
             ['A', 'A', 'E', 'C', 'B', '.', 'M'],
             ['.', '.', '.', 'C', 'B', '.', '.'],
             ['.', '.', 'G', '.', '.', '.', '.'],
             ['.', '.', 'G', '.', '.', '.', '.']]
 
    levels_boards = { 1: board1, 2: board2 }
    horizontal_cars = {"A": True, "B": False, "C": False, "D": True, "E": False, "F": True, "G": False}
    target_pos = [3, 6]

    level = start(levels_boards)
    board = levels_boards[level]
 
    while True:
        clear()
        print_board(board)
 
        # Encontrar posiciones de todos los autos
        car_positions = find_car_positions(board)
 
        # Mostrar al usuario las opciones de autos para mover
        print("Autos disponibles para mover: ", ', '.join(car_positions.keys()))
        car_to_move = input("Seleccione el auto que desea mover: ").strip().upper()
 
        if car_to_move not in car_positions:
            print("Auto no válido. Intente de nuevo.")
            continue
 
        print("Ingrese su movimiento para el auto {} (w: arriba, s: abajo, a: izquierda, d: derecha): ".format(car_to_move))
        move = msvcrt.getch().decode('utf-8').lower()
        new_positions = get_new_positions(car_positions, car_to_move, move, horizontal_cars[car_to_move])
 
        if is_valid_move(board, car_positions, car_to_move, new_positions):
            move_car(board, car_positions, car_to_move, new_positions)
        else:
            print("¡Alerta! Movimiento no válido o te has chocado con un obstáculo.")
            input("Presione Enter para continuar: ")
 
        if board[target_pos[0]][target_pos[1]] == 'A':
            clear()
            print("¡Felicidades! Has ganado el juego.")
            break
 
        print()
 
    print_board(board)
 
if __name__ == "__main__":
    set_color()
    main()