import pokebase as pd



def pokedex_lookup(name):
    
    pokemon_ = pd.pokemon(name)

    pokemon_type = ""
    p_type_list = []

    
    for t in pokemon_.types:
        
        p_type_list.append(str(t.type))
        pokemon_type = ", ".join(p_type_list)
        pokemon_type += "."

        
    pokemon_height = pokemon_.height


    print(name,pokemon_type, pokemon_height)
    
    

    

    
pokedex_lookup("bibarel")





