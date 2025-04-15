import discord
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$pollo'):
        #
        await message.channel.send("""Calorías:
        Una porción de 100 gramos de pollo (pulpa) contiene 170 kilocalorías. 
        Proteínas:
        El pollo es una excelente fuente de proteínas de alta calidad, con 18.2 gramos por 100 gramos. 
        Grasas:
        Contiene 10.2 gramos de grasa por 100 gramos, con una proporción de grasa saturada y monoinsaturada, según FEN. 
        Micronutrientes:
        El pollo también aporta minerales como hierro, además de vitamina A, zinc, tiamina, fósforo y ácido fólico. 
        Pechuga de pollo:
        Una pechuga de pollo de tamaño estándar puede pesar entre 150 y 200 gramos, y contiene entre 248 y 330 calorías. """)
        #
    elif message.content.startswith('$huevo'):
        await message.channel.send("""Calorías: 70-80 kcal.
        Proteínas: 6-7 gramos.
        Grasas: 4-5 gramos.
        Carbohidratos: Aproximadamente 0.5 gramos.
        Colesterol: 186 mg.
        Vitaminas: A, B12, D, E, folato.
        Minerales: Calcio, fósforo, hierro, selenio, yodo.""")
    elif message.content.startswith('$huevo'):
        await message.channel.send("""Calorías: 70-80 kcal.
        Proteínas: 6-7 gramos.
        Grasas: 4-5 gramos.
        Carbohidratos: Aproximadamente 0.5 gramos.
        Colesterol: 186 mg.
        Vitaminas: A, B12, D, E, folato.
        Minerales: Calcio, fósforo, hierro, selenio, yodo.""")
    elif message.content.startswith('$leche'):
        await message.channel.send("""Calorías: Una taza (240 ml) de leche entera contiene alrededor de 146 calorías. 
Proteínas: Una taza de leche entera contiene alrededor de 8 gramos de proteínas. 
Grasas: Una taza de leche entera contiene alrededor de 8 gramos de grasas. 
Carbohidratos: Una taza de leche entera contiene alrededor de 12 gramos de carbohidratos, principalmente en forma de lactosa. 
Calcio: La leche es una excelente fuente de calcio, que es importante para la salud ósea. 
Vitamina B12: Un solo vaso de leche (200 ml) puede proporcionar el 36% de la ingesta diaria recomendada de vitamina B12. 
Otros: La leche también contiene fósforo, yodo y potasio. """)
    else:
        await message.channel.send(message.content)
client.run("token aqui")