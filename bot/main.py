import os
from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")
    
###COMMANDS ETC###

##TEXT

##SNACK ORDER
@bot.command(name='gimmesnacks')
async def meme(ctx):
    order = 'u ontvangt '
    n = random.randint(2, 7)
    snacks = ['bamischijf','frikandel','frikandel speciaal','kipcorn','kaassoufle','kip nuggets','gehaktbal','loempia','patatje mayo','patatje speciaal','patatje oorlog','uienring','vlammetje','mexicano','bitterballen']
    snacks = random.sample(snacks, n)
    for item in snacks:
        if item == snacks[-1]:
            order += 'en '
            order += str(random.randint(1, 4))
            order += ' '
            order += item
        else:
            order += str(random.randint(1, 4))
            order += ' '
            order += item
            order += ', '
    response = order
    await ctx.send(response)

##WIKIS
@bot.command(name='bamischijf')
async def meme(ctx):
    response = 'Een bamischijf is een rondvormige snack die bestaat uit bami met doorhaalvloeistof en een paneerlaag eromheen. De schijf is vooral in Nederland en België bekend. Bij veel snackbars is de bamischijf ook in vierkante vorm verkrijgbaar onder de naam bamiblok. In enkele gevallen is hij ook anders van smaak, in meer of mindere mate pittig. '
    await ctx.send(response)

@bot.command(name='bitterbal')
async def meme(ctx):
    response = "Een bitterbal is een gefrituurd klein (vlees)ragoutballetje van zo'n 3 à 5 cm doorsnee. Het is in feite een kleine, ronde versie van de vleeskroket, maar met een andere verhouding tussen korst en ragout. Het gewicht is ca. 20 gram. De naam vloeit voort uit het feit dat bitterballen vroeger werden gegeten bij een bittertje, een sterk alcoholisch kruidendrankje. De snack is erg populair in België en Nederland. Ook in Suriname en Indonesië worden ze gegeten. Elders zijn ze nauwelijks bekend. De bitterbal is, vaak geserveerd met mosterd, populair als onderdeel van het 'bittergarnituur' op recepties en in het café. Een bittergarnituur bestaat, behalve uit bitterballen, uit andere kleine warme snacks. Het bittertje is doorgaans vervangen door andere dranken. In april 2020 is de bitterbal toegevoegd aan de Inventaris Immaterieel Cultureel Erfgoed Nederland."
    await ctx.send(response)

@bot.command(name='kroket')
async def meme(ctx):
    response = 'De kroket is een gefrituurd gerecht, waarbij een vulling in paneermeel is gerold. In Nederland wordt met een kroket meestal een vleeskroket bedoeld, doorgaans van rund- of kalfsvlees. Hoewel vleeskroketten vroeger een slagers- en banketbakkersproduct waren, worden vleeskroketten vooral als typische snack bij de meeste snackbars verkocht. Voor de Nederlandse automatiek zijn zij belangrijk, omdat zij handzaam zijn, makkelijk voorbereid kunnen worden (in tegenstelling tot patates frites) en snel te verkrijgen zijn, en hun smaak na een half uur warm bewaren nog behouden. Ze worden los, of op een broodje ("broodje kroket"), of samen met friet gegeten. Veel mensen eten een kroket met mosterd of een andere saus. Kleinere kroketjes, meestal gemaakt van aardappelen of groenten, worden ook in andere landen gegeten als bijgerecht bij een uitgebreide maaltijd. '
    await ctx.send(response)

@bot.command(name='frikandel')
async def meme(ctx):
    response = 'Een frikandel is een langwerpige, donkergekleurde staaf van verschillende soorten vlees die warm gefrituurd wordt gegeten. De commerciële frikandel werd in 1954 gelanceerd in de Nederlandse stad Dordrecht. Slagersknecht Gerrit de Vries maakte gehaktballen die hij aan de horeca verkocht. Door een wijziging in de Warenwet moest hij zijn product, dat in de smaak viel bij zijn klanten, veranderen. Zijn oplossing was de vorm maar niet het recept te wijzigen: van de bal maakte hij een worst. De naam voor zijn product werd hem door een vrouwelijke snackbarhouder van Duitse afkomst ingefluisterd: daar bestond de Frikadelle, een platte gehaktbal. De Vries nam die naam over: frikadel (zonder N).'
    await ctx.send(response)

@bot.command(name='kaassouffle')
async def meme(ctx):
    response = 'Een kaassoufflé is een Nederlandse snack die bestaat uit een in paneermeel gewentelde envelop van bladerdeeg en een kaasvulling. De vulling bestaat uit een mengsel van smeltkaas, boter, zetmeel, water en bakstabilisator. De gebruikte kaas in de smeltkaas is afkomstig van niet voor verkoop geschikte kazen, zoals afsnijdsels, gescheurde kazen en kazen waarin gasvorming heeft plaatsgevonden. De kaas kan bijvoorbeeld Beemster kaas, Cheddar, Mozzarella, Goudse kaas of een mengsel hiervan zijn, afhankelijk van wat de leverancier in het product wil. Echter, door de toevoeging van smeltzouten gaat de specifieke smaak van de gebruikte kaas verloren. De vulling van de soufflé bestaat dus uit smeltkaas en kaasvervanger (als ‘opvulling’). Bij gebruik van bijvoorbeeld 39% smeltkaas bestaat 61% van de vulling uit analoogkaas. De uiteindelijke hoeveelheid echte kaas komt in de kaassoufflé neer op 6-9%. '
    await ctx.send(response)

@bot.command(name='kipcorn')
async def meme(ctx):
    response = "Een kipcorn is een staafvormige snack die gefrituurd wordt en warm wordt genuttigd. De kipcorn bestaat uit een krokante korst van maïspaneermeel met een zachte, ietwat smeuïge, vulling van kip en/of kalkoen. De naam in het Belgisch-Frans is 'poulycroc'. De kipcorn is in de meeste frituren en cafetaria's verkrijgbaar. Er bestaat ook een extra lange versie, de Kipcorn XL. Net als de gehaktstaaf kan de kipcorn gegeten worden met mayonaise, curry, ketchup of pindasaus."
    await ctx.send(response)

@bot.command(name='kipnugget')
async def meme(ctx):
    response = "De kipnugget (Engels: chicken nugget) is een fastfood-snack. Een kipnugget is samengesteld uit een pasta van fijn gemarineerd kippenvlees en kippenhuid die wordt gehuld in beslag of broodkruimels voordat hij wordt bereid. Fastfoodrestaurants frituren kipnuggets meestal in olie. Kipnuggets bakken in de oven is thuis de gebruikelijke wijze van bereiden. De kipnugget werd uitgevonden in de jaren 1950 door Robert C. Baker, hoogleraar levensmiddelentechnologie aan de Cornell-universiteit in de staat New York. Bakers innovatie maakte het mogelijk om kipnuggets te creëren in elke vorm. Het woord kipnugget is een combinatie van de woorden 'kip' en het Engelse woord nugget, dat 'klomp' betekent (als in goudklomp). De combinatie van woorden is gaandeweg vernederlandst."
    await ctx.send(response)


##GIFS

@bot.command(name='chips')
async def meme(ctx):
    response = 'https://media.giphy.com/media/EFUiKHUiZNQUo/giphy.gif'
    await ctx.send(response)

@bot.command(name='frikandellove')
async def meme(ctx):
    response = 'https://makesweet.com/s/1b7be2f4/'
    await ctx.send(response)

@bot.command(name='bamischijflove')
async def meme(ctx):
    response = 'https://makesweet.com/s/701e50de/'
    await ctx.send(response)

@bot.command(name='komdan')
async def meme(ctx):
    response = 'https://tenor.com/view/kom-op-dan-come-on-come-here-gif-15969461'
    await ctx.send(response)

@bot.command(name='5euro')
async def meme(ctx):
    response = 'https://tenor.com/view/5euro-muil-willems-kantine-kantine-kankerboef-gif-23789359'
    await ctx.send(response)

@bot.command(name='elmo')
async def meme(ctx):
    response = 'https://tenor.com/view/burn-elmo-pyro-burn-it-down-ashes-gif-5632946'
    await ctx.send(response)

@bot.command(name='betty')
async def meme(ctx):
    response = 'https://tenor.com/view/betty-white-dab-mood-gif-5044603'
    await ctx.send(response)

@bot.command(name='supernut')
async def meme(ctx):
    response = 'https://tenor.com/view/luigi-mario-nut-super-nut-gif-13073710'
    await ctx.send(response)

@bot.command(name='frank')
async def meme(ctx):
    franks = ['https://cdn.discordapp.com/attachments/946485263402672219/946516337814040586/0cd.gif','https://tenor.com/view/frank-always-sunny-danny-de-vito-crawl-gif-5096399','https://tenor.com/view/egg-frank-can-i-offer-you-a-nice-egg-in-this-trying-time-gif-13802522','https://tenor.com/view/frank-reynolds-gargle-gargling-drunk-gif-15839014','https://cdn.discordapp.com/attachments/946485263402672219/946517143221055558/tumblr_o7e9o3XDGZ1u9u02so7_250.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517143594352710/tumblr_mzs3abeqEG1qi9ekco1_500.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517144026374144/franklooksbad2nxjzn.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517144517083186/43466345fe9d705a5ff72e3924175d35.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517144798117898/b05e0036d93cb2e1a229bb4ec54abd6a.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517145087516742/giphy.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517145485987930/17c0b5dfe2c900da2f17f300d8b88779.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517145741852772/frank-reynolds-iasip.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517146048008222/loot-frank.gif','https://cdn.discordapp.com/attachments/946485263402672219/946517146488422420/avvLca9.gif','https://tenor.com/view/trash-danny-de-vito-gif-12881174']
    response = random.choice(franks)
    await ctx.send(response)

@bot.command(name='geitje')
async def meme(ctx):
    geitjes = ['https://tenor.com/view/goat-gloat-funny-animals-gif-13702224','https://tenor.com/view/sexy-goat-goat-cabra-gif-23897181','https://tenor.com/view/goat-chewing-staring-watching-you-threat-gif-11516094','https://tenor.com/view/claire-gif-24279299', 'https://tenor.com/view/goat-goat-lick-tongue-out-gif-5193394','https://tenor.com/view/goats-goat-gif-13798042','https://tenor.com/view/animals-who-me-peek-a-boo-kid-baby-goat-gif-17238276','https://tenor.com/view/billy-the-goat-sunglasses-gif-15457405','https://tenor.com/view/baby-goat-sad-fall-cute-ness-gif-21145223','https://tenor.com/view/goat-goats-happy-excited-celebrate-gif-5713325']
    response = random.choice(geitjes)
    await ctx.send(response)

@bot.command(name='kitten')
async def meme(ctx):
    kittens = ['https://tenor.com/view/kitten-falls-kitten-stumbling-kitty-stumbling-kitty-stumbles-kitten-falls-over-gif-22987164','https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800','https://tenor.com/view/big-hug-mom-kitten-aww-gif-13759294','https://tenor.com/view/cat-kitten-cat-love-kitty-cute-gif-16463100','https://tenor.com/view/cat-cute-kitten-kitty-pussy-cat-gif-17669581','https://tenor.com/view/kittens-cute-cat-pet-cheeks-gif-16382546','https://tenor.com/view/cute-cat-kitten-bite-bite-my-lip-hang-nail-gif-18028430','https://i.gifer.com/5lIQ.gif','https://sheilacrosby.s3.amazonaws.com/uploads/2016/04/kittenStretching.gif','https://broadvine.com/wp-content/uploads/KITTEN-GIF-%E2%80%A2-How-hard-is-to-take-a-picture-of-10-kittens-together-It-is-impurrsible-mission.gif','https://media.giphy.com/media/cLM83RvATUc1E0SbjA/giphy.gif','https://media.giphy.com/media/tKyqZtLzZxCLbKitIq/giphy-downsized-large.gif','https://media.giphy.com/media/OmK8lulOMQ9XO/giphy.gif','https://media.giphy.com/media/3GRwYzxwdceaI/giphy-downsized-large.gif','https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif','https://media.giphy.com/media/4TlZk9B3iSUhdmXUjr/giphy-downsized-large.gif','https://media.giphy.com/media/C23cMUqoZdqMg/giphy.gif','https://media.giphy.com/media/X2A2d62PrrMCk/giphy.gif','https://tenor.com/view/kitten-jump-kitten-fail-kitten-jump-gif-20189864','https://tenor.com/view/kitten-cute-cute-kitten-kitty-gif-21923599']
    response = random.choice(kittens)
    await ctx.send(response)

@bot.command(name='frog')
async def meme(ctx):
    frogs = ['https://tenor.com/view/dance-frog-gif-14112820','https://tenor.com/view/frog-hat-gif-24889203','https://tenor.com/view/frog-jumping-gif-23922460','https://tenor.com/view/frog-frogs-bite-biting-cute-gif-23044464','https://tenor.com/view/frog-loop-frog-loop-viynl-frog-viynl-gif-18152140','https://tenor.com/view/frog-gif-20949327','https://tenor.com/view/frog-frogs-adorable-animals-cute-gif-23044494','https://tenor.com/view/h%C3%A2m-frog-toad-frog-l%E1%BA%AFc-wiggle-gif-14557565','https://tenor.com/view/not-original-gif-18504304','https://tenor.com/view/chunky-boi-frog-gif-18242423','https://tenor.com/view/frog-gail-fail-let-me-have-it-gif-12024489','https://tenor.com/view/frog-gif-21912345','https://media.giphy.com/media/d2cHdIj3nxK24/giphy.gif','https://tenor.com/es/ver/bro-frogs-tree-frog-gif-5275848','https://tenor.com/view/frog-gif-18807732','https://tenor.com/view/dyingaliengif-toad-frog-gif-23315375','https://thumbs.gfycat.com/AdeptElderlyAmberpenshell-size_restricted.gif','https://media4.giphy.com/media/2FayUivUIHEqyCmTC/giphy.gif?cid=790b76114e3bfbfe741f0cb86788200e05e1824f08cb42cb&rid=giphy.gif&ct=g','https://thumbs.gfycat.com/CookedCautiousBlackfish-size_restricted.gif','https://c.tenor.com/KfnNlxplAgAAAAAd/frogs-colorful.gif','https://tenor.com/view/futurama-toad-frog-mesmerized-gif-3938170','https://tenor.com/view/attack-frog-attack-frog-gif-23768297']
    response = random.choice(frogs)
    await ctx.send(response)

@bot.command(name='goeiesmorgens')
async def meme(ctx):
    response = 'https://tenor.com/view/goeiesmorgens-juffrouw-jannie-debiteuren-crediteuren-jiskefet-gif-18251742'
    await ctx.send(response)

@bot.command(name='picobellobv')
async def meme(ctx):
    response = 'https://tenor.com/view/picobello-bv-gif-18748778'
    await ctx.send(response)

@bot.command(name='cheese')
async def meme(ctx):
    response = 'https://tenor.com/view/cheese-james-may-gif-19266123'
    await ctx.send(response)

@bot.command(name='what')
async def meme(ctx):
    response = 'https://tenor.com/view/no-money-muney-nomuney-fietsopa-gif-14077097'
    await ctx.send(response)

@bot.command(name='bah')
async def meme(ctx):
    response = 'https://tenor.com/view/bah-ram-standing-chewing-animal-gif-17111234'
    await ctx.send(response)

@bot.command(name='hampter')
async def meme(ctx):
    response = 'https://tenor.com/view/hampter-gif-20240312'
    await ctx.send(response)

@bot.command(name='wtf')
async def meme(ctx):
    response = 'https://tenor.com/view/hamster-shocked-afraid-gif-13368273'
    await ctx.send(response)

@bot.command(name='egg')
async def meme(ctx):
    response = 'https://tenor.com/view/egg-frank-can-i-offer-you-a-nice-egg-in-this-trying-time-gif-13802522'
    await ctx.send(response)

@bot.command(name='bitterballove')
async def meme(ctx):
    response = 'https://tenor.com/view/bitterbal-bitterbal-cult-geliefde-nederlands-bitterbal-mijn-geliefde-gif-22519813'
    await ctx.send(response)

@bot.command(name='demon')
async def meme(ctx):
    response = 'https://tenor.com/view/hey-there-demons-its-me-ya-boi-gif-9661590'
    await ctx.send(response)

@bot.command(name='bye')
async def meme(ctx):
    response = 'https://tenor.com/view/papyrus-undertale-outwindow-lol-out-gif-5937399'
    await ctx.send(response)


##LISTEN

@bot.listen('on_message')
async def listener(message):
    if "kwarkass" in message.content:
        myid = '<@431831516541353995>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "Kwarkass" in message.content:
        myid = '<@431831516541353995>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "KWARKASS" in message.content:
        myid = '<@431831516541353995>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "kwarktaart" in message.content:
        myid = '<@313257560821989407>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "Kwarktaart" in message.content:
        myid = '<@313257560821989407>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "KWARKTAART" in message.content:
        myid = '<@313257560821989407>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "Cheesecake" in message.content:
        myid = '<@406516312676892673>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "CHEESECAKE" in message.content:
        myid = '<@406516312676892673>'
        await message.channel.send(myid)

@bot.listen('on_message')
async def listener(message):
    if "cheesecake" in message.content:
        myid = '<@406516312676892673>'
        await message.channel.send(myid)


if __name__ == "__main__":
    bot.run(TOKEN)