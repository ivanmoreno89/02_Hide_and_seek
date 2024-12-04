import random

class SeekerAI:
    def __init__(self, house_map):
        self.house_map = house_map
        self.noisy_locations = [
            "El armario de la habitación auxiliar delantera del segundo piso",
            "El armario de la habitación auxiliar trasera del segundo piso",
            "El armario de la habitación principal del segundo piso",
            "El baño del segundo piso",
            "La ducha del baño del segundo piso",
            "El armario del baño del primer piso",
            "El armario del patio en el primer piso",
            "El armario del estudio del primer piso",
            "Debajo del escritorio del estudio del primer piso",
            "Debajo de la mesa del comedor del primer piso",
        ]
        self.exclusive_bathroom_pairs = {
            "El armario del baño del primer piso": "El baño del primer piso",
            "La ducha del baño del segundo piso": "El baño del segundo piso",
        }

    def search_for_player(self, player, max_attempts=3, allow_move=False):
        print("\nEl buscador comienza a buscar...")
        all_locations = self.house_map.get_locations()
        remaining_locations = all_locations.copy()
        last_location = None

        for attempt in range(1, max_attempts + 1):
            # Seleccionar una ubicación para buscar
            if remaining_locations:
                location = random.choice(remaining_locations)
                remaining_locations.remove(location)
            else:
                print("\nSe acabaron las localizaciones disponibles.")
                break

            print(f"Intento {attempt}: Buscando en {location}")

            # Verificar si el jugador está en la ubicación actual
            if location == player.get_location():
                print("\n¡Te he encontrado! El buscador ha ganado.")
                return

            # Detectar automáticamente si la IA entra a la ducha o el armario y el usuario está en el baño general
            if location in self.exclusive_bathroom_pairs:
                general_bathroom = self.exclusive_bathroom_pairs[location]
                if general_bathroom == player.get_location():
                    print(f"\n¡Te he encontrado en {player.get_location()} al revisar {location}! El buscador ha ganado.")
                    return

            # Bloquear búsqueda en el baño general si ya revisó la ducha o el armario
            if last_location and last_location in self.exclusive_bathroom_pairs.values():
                paired_location = self.get_key_by_value(self.exclusive_bathroom_pairs, last_location)
                if paired_location and paired_location in remaining_locations:
                    remaining_locations.remove(paired_location)

            last_location = location

            # Permitir al jugador cambiar de escondite
            if allow_move and attempt < max_attempts:
                change = input("\n¿Quieres cambiar de escondite? (s/n): ").strip().lower()
                if change == "s":
                    new_location = self.prompt_new_location(player)
                    print(f"Te has movido a: {new_location}")

                    # Siempre mostrar si el movimiento generó ruido o no
                    if new_location in self.noisy_locations:
                        made_noise = self.does_make_noise()
                        if made_noise:
                            print("¡Has generado ruido al moverte!")
                            player_floor = self.get_floor(new_location)
                            current_floor = self.get_floor(location)

                            if current_floor != player_floor:
                                # Ruido en otro piso
                                print(f"\n¡Escuché un ruido en el {'segundo' if player_floor == 'second' else 'primer'} piso!")
                                # Priorizar las localizaciones en el piso donde se escuchó el ruido
                                remaining_locations = [
                                    loc for loc in all_locations if self.get_floor(loc) == player_floor
                                ]
                            else:
                                # Ruido en el mismo piso
                                print("\n¡Escuché un ruido cerca! ¡Voy por ti!")
                        else:
                            print("Te has movido silenciosamente. La IA no escuchó nada.")
                    else:
                        print("Te has movido a una localización silenciosa. No hiciste ruido.")

        print("\nNo encontré al jugador. ¡El jugador ha ganado!")

    def does_make_noise(self):
        """Determina si el jugador genera ruido al moverse (aleatorio)."""
        return random.choice([True, False])

    def get_floor(self, location):
        """Determina el piso basado en la ubicación."""
        second_floor_keywords = ["segundo piso"]
        return "second" if any(kw in location for kw in second_floor_keywords) else "first"

    def get_key_by_value(self, dictionary, value):
        """Obtiene la clave asociada a un valor en un diccionario."""
        for key, val in dictionary.items():
            if val == value:
                return key
        return None

    def prompt_new_location(self, player):
        """Permite al jugador seleccionar un nuevo escondite."""
        locations = self.house_map.get_locations()
        while True:
            print("\nElige un nuevo escondite:")
            for idx, loc in enumerate(locations, start=1):
                print(f"{idx}. {loc}")
            try:
                choice = int(input("Elige un número: "))
                if 1 <= choice <= len(locations):
                    player.set_location(locations[choice - 1])
                    return locations[choice - 1]
                else:
                    print(f"Elige un número entre 1 y {len(locations)}.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")
