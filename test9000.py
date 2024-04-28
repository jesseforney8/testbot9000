# This example requires the 'message_content' intent.
import random
import discord
from datetime import datetime
import pokebase as pd


def pokedex_lookup(name):

    try:
    
        pokemon_ = pd.pokemon(name)

        pokemon_type = ""
        p_type_list = []

        
        for t in pokemon_.types:
            
            p_type_list.append(str(t.type))
            pokemon_type = ", ".join(p_type_list)
            pokemon_type += "."

        
        pokemon_height = pokemon_.height
        name = str(name).capitalize()

        return f"Name: {name}\nElement Type: {pokemon_type}\nHeight: {pokemon_height}"
    
    except:
        return "Could not find Pokemon. :("
    
    #for x in pokemon_.moves:
     #   print(x.move)

    

    


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!poop'):
        poop_facts = ["Wanna eat my ass? hehe", "Poop is mostly water.",
                       "Trillions of bacteria live in your poop :)"," Fiber is your friend.", "The perfect poop looks like a sausage."
                       ]

        msg = random.choice(poop_facts)
        await message.channel.send(msg)

    if message.content.startswith("!time"):
        now = datetime.now()
        if now.hour < 12:
            hour = now.hour
            day_night = "AM"
        else:
            hour = now.hour - 12
            day_night = "PM"

        current_time = f"{hour}:{now.minute}{day_night}"
        await message.channel.send(current_time)



    if message.content.startswith('!pokemon'):
        pokemon_name = message.content.split(" ")[-1]
        
        await message.channel.send(pokedex_lookup(pokemon_name))




client.run('')

