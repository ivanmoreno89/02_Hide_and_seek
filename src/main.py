from map import Map
from player import Player
from ai import SeekerAI

def start_game():
    print("¡Bienvenido a Hide & Seek!")

    # Elegir el número de intentos
    while True:
        try:
            max_attempts = int(input("\nElige el número de intentos que tendrá el buscador: "))
            if max_attempts > 0:
                break
            else:
                print("El número de intentos debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido.")

    # Inicializar mapa y jugador
    house_map = Map()
    player = Player()
    seeker_ai = SeekerAI(house_map)

    # Mostrar localizaciones numeradas y elegir escondite inicial
    locations = house_map.get_locations()
    for idx, loc in enumerate(locations, start=1):
        print(f"{idx}. {loc}")

    while True:
        try:
            choice = int(input("\nElige un número para esconderte: "))
            if 1 <= choice <= len(locations):
                player.set_location(locations[choice - 1])
                break
            else:
                print(f"Elige un número entre 1 y {len(locations)}.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

    # Comenzar la búsqueda
    print("\n¡El buscador comienza a buscar!")
    seeker_ai.search_for_player(player, max_attempts=max_attempts, allow_move=True)

if __name__ == "__main__":
    start_game()
