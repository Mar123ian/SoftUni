from project.pokemon import Pokemon



class Trainer:
    def __init__(self, name, pokemons=[]):
        self.pokemons = pokemons
        self.name = name

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon):
        for el in self.pokemons:
            if el.name==pokemon:
                pokemon=el
                break
        if pokemon in self.pokemons:
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        info=[f"Pokemon Trainer {self.name}",
              f"Pokemon count {len(self.pokemons)}"]

        for p in set(self.pokemons):
            info.append(f"- {p.pokemon_details()}")

        return "\n".join(info)

