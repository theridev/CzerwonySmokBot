'''                                                                       
                                                                           
                    ▓▓▓██▓▓▓▓▓▓             ▓█▓▓▓▓▓▓▓▓▓                    
                     █▓▓▓▓▓▓▓█▓▓           ▓▓█▓▓▓▓▓▓▓█                     
                        █▓██▓█▓▓█         █▓▓█▓██▓█                        
                          ▓▓▓▓▓▓▓█  █ █  █▓▓▓▓▓▓▓                          
                          ▓▓▓▓▓▓███████████▓▓▓▓▓▓                          
                         ██▒███████████████████▒██                         
                        █▓█▒▒█████████████████▒▒█▓█                        
                    █████▓▒▒▒█▓░███████████░██▒▒▒▓█████                    
                   ██████████░░▒░░███████░░▒░░███████████                  
   ██              ██████░░░░░░░░░███████░░░░░░░░░▓██████             ██   
 ████▓█        ███████░░░░░█▓▓▓█░░░█████▒░░█▓▓▓█░░░░░████████       █▓████ 
  █████▓██████████░░░░█▓░░░░░░░░░░░░███░░░░░░░░░░░░▓█░░░░▒████████▓▓█████  
   █▓██████░░░░░░░░░░░░░▓███████▒░░▒█░█▓░░▒███████▓░▓░░░░░░░░░░░██████▓█   
    ██████████░░██░░███░▓▓█▓▓██▓█░░░░░░░░░█▓██▓▓█▓▓░███░░██░░██████████    
     █    ██████████████▓▓▓▓██░░██░▓░░░▓░██░░██▓▓▓▓██████████████    █     
             ███████████░░░░░░░░░▓░░▒▒▓░░▒░░░░░░░░░███████████             
                 ███████░░░░░░░░░░░█▒▒▒█░░░░░░░░░░░███████                 
                    █████░░░░░▓░░░░██░██▒░░░▓░░░░░█████                    
                  ████████░░░░░░▒▒░░░░░░░▒▒░░░░░░████████                  
                     ██████░░░░░░░▓░░░░░▓░░░░░░░██████                     
                    ████████░░░░░░░░░░░░░░░░░░░████████                    
                    ███ █████░░░▒░░░▒░▒░░░▒░░▒█████ ███                    
                     █   ██████░░░░░░░░░░░░░███████  █                     
                          ██  ██  █░░░░░█  ██  ██                          
<< Czerwony Smok >>
main.py

Hejka, to ja Theri!
Opowiem wam historię.

Pewnego dnia wpadłem na pomysł zrobienia bota dla serwera Red Eye Dragon.
Takiego fajnego żeby można było się nim bawić, czaisz?

Zrealizowałem to 21 listopada 2024 roku, używając moich umiejętności nabytych rok wcześniej
podczas robienia botów "SliztBot" i "Cringeball"

Szczególne podziękowania są dla następujących osób:
Seth - pomysł na komende dyskryminacja i pomoc w testowaniu bota :3
Avalon - Inspiracja przy komendzie dyskryminacja
Meteor i Fotien - bez serwera bot by nie powstał
Oliwier - nie wydał tajemnicy podczas powstawania bota

Kod bota jest w całości dostępny online! Komentarze w kodzie pozwolą przeglądającemu go zrozumieć.
https://github.com/theridev/CzerwonySmokBot
'''

# Zaimportuj moduły: API Discorda i random używany do wybierania losowych rzeczy. Także requests dla pobrania wybranego zdjęcia.
import discord, random, requests
from discord.ext import commands
from discord.ui import Modal
from io import BytesIO
import stats.stats

# Pillow dla stópek :3
from PIL import Image

# Uprawnienia dla bota
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Ustaw aktywność oraz zdefiniuj bota
activity = discord.Activity(type=discord.ActivityType.watching, name="Serwer Red Eye Dragon")
bot = commands.Bot(command_prefix="%", activity=activity, status=discord.Status.online, intents=intents, help_command=None)

# Guziki dla wiadomości w komendzie dyskryminacja.
class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180): # Guziki przestaną działać po 3 minutach od wysłania wiadomości
        super().__init__(timeout=timeout)

    # Guziki i wiadomości wysyłane po ich naciśnięciu
    @discord.ui.button(label="Dyskryminacja z powodu braku Fursuita.", style=discord.ButtonStyle.blurple, emoji="🚫")
    async def blurple_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Jak możesz nie mieć fursuita! Jeżeli jeszcze nie wiedziałeś - sprawia to że jesteś gorszy! "
            "Powinieneś no nie wiem, żyć z poczuciem że jesteś gorszy od osób które mają fursuita."
        )

    @discord.ui.button(label="Dyskryminacja z powodu posiadania Fursuita.", style=discord.ButtonStyle.green, emoji="🦊")
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Aha, masz fursuita? Jakiego? Pewnie ubierasz się w plastikową torebkę z biedronki i mówisz że masz fursuit. "
            "Dobra - a dbasz o ten fursuit? No właśnie. Pewnie cały jest wygnieciony a sama postać która pewnie miała "
            "przedstawiać twoją, tfu, fursonę - Jest łysa bo nie umiesz nawet dbać o twój cholerny fursuit!!"
        )

    @discord.ui.button(label="Dyskryminacja z powodu bycia na serwerze.", style=discord.ButtonStyle.gray, emoji="🐉")
    async def green_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Co? Jesteś na serwerze Red Eye Dragon? I co? Mam cię dyskryminować? No, zapomnij. Jeżeli nie będziesz sprawiał żadnych dram, lub nie jesteś antifurem pod przykrywką, życzę ci miłej zabawy na serwie :3")

    @discord.ui.button(label="Dyskryminacja z powodu bycia dyskryminowanym.", style=discord.ButtonStyle.red, emoji="🛡️")
    async def red_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Jesteś dyskryminowany? I co? Twój problem. Może dobrze, że się czujesz gorszy. A może rozumiesz, że wszystko co ten bot pisze jest żartem. Nie obwiniajcie Theriego, to Seth chciał mieć taką funkcję w bocie.")

# Dla testowania: Kiedy bot się zaloguje, wyświetl wiadomość w konsoli
@bot.event
async def on_ready():
    print(f'Bot zalogowany: {bot.user}!')

# W przypadku wiadomości sprawdź czy wywołuje ona bota. Nie pozwól botu żeby mógł sam wywoływać u siebie komendy.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Gdy bot zostanie spingowany, wyświetl wiadomość pomocy. Funkcja chwilowo niedziałająca.
    # if bot.user.mentioned_in(message):
    #     await help(bot)
    await bot.process_commands(message)

# POMOCYYYY
@bot.command()
async def help(ctx):
    embed=discord.Embed(color=0x99c1f1)
    embed.add_field(name="<< Już na pomoc! >>", value=" ", inline=False)
    embed.add_field(name=" ", value=" ", inline=False)
    embed.add_field(name=r"%mem", value="Wyślij serwerowy mem!", inline=True)
    embed.add_field(name=r"%cytat", value="Wyślij serwerowy cytat!", inline=True)
    embed.add_field(name=r"%help", value="Wyślij tą wiadomość.", inline=True)
    embed.add_field(name=r"%dyskryminacja", value="Doświadcz dyskryminacji!", inline=True)
    embed.add_field(name=r"%zgaduj", value="Zgadnij co to za członek serwera!", inline=True)
    embed.add_field(name=r"%stopy", value="Dodaj stópki do swojego profilowego! (Sponsorowane przez kult stópek)", inline=True)
    embed.add_field(name=r"%lysejadro", value="Dodaj łysego do swojego profilowego! (Sponsorowane przez kult Łysego Jądra)", inline=True)
    embed.add_field(name=r"%rank", value="Sprawdź ile razy zgadłeś.", inline=True)
    embed.add_field(name=r"%top", value="Sprawdź kto zgadł najwięcej razy!", inline=True)
    embed.add_field(name=r"%lysy", value="Wyślij łysego! (Sponsorowane przez kult Łysego Jądra)", inline=True)
    embed.add_field(name="Wkrótce więcej!", value=" ", inline=True)
    await ctx.send(embed=embed)

# Mem: losowe zdjęcie z kanału memy-serwerowe
@bot.command()
async def mem(ctx):
    await losowezdj(ctx, 1308069405351088221, "Mem")

# Cytat: losowe zdjęcie z kanału cytaty-serwerowe
@bot.command()
async def cytat(ctx):
    await losowezdj(ctx, 1295872408636358726, "Cytat")

# Lysy: Losowe zdjęcie jondra
@bot.command()
async def lysy(ctx):
    await losowezdj(ctx, 1302417266960236606, "Łysy")

# Zostań zdyskryminowany. Zdjęcie losowe. Na pomysł komendy wpadł Seth. Nie obwiniajcie mnie!
@bot.command()
async def dyskryminacja(ctx):
    embed=discord.Embed(title=" ", description="Wybierz rodzaj dyskryminacji!", color=0xff7800)
    embed.set_image(url="https://radio.bobola.church/wp-content/uploads/2023/07/maxresdefault1.jpg")
    await ctx.channel.send(embed=embed,view=Buttons())

# Wybierz losowe zdjęcie z danego kanału
async def losowezdj(ctx, channel, co):
    channel = bot.get_channel(channel)  # Wybierz kanał podany w argumencie 'channel'

    if not channel: # Jeżeli kanał nie istnieje (mało prawdopodobne) wyświetl błąd i zakończ wykonywanie funkcji
        embed=discord.Embed(color=0xe01b24)
        embed.add_field(name="Błąd!", value="Wybrany kanał nie istnieje!", inline=True)
        embed.set_footer(text="Oznacz użytkownika @theridev, żeby spojrzał na ten błąd.") # Zajmę się tym za rok lub dwa.
        await ctx.send(embed=embed)
        return
        return

    # Pobierz wiadomości z kanału.
    try:
        messages = []
        async for msg in channel.history(limit=None):  # Brak limitu na wiadomości może być ogromnym problemem. YOLO.
            messages.append(msg)
    except discord.Forbidden: # Błąd 403 - Forbidden / Zabroniony. Forbidden to najgorszy album Black Sabbath, tyle wiem.
        embed=discord.Embed(color=0xe01b24)
        embed.add_field(name="Błąd!", value="Bot nie ma uprawnień żeby odczytywać wiadomości na tym kanale!", inline=True)
        embed.set_footer(text="Oznacz użytkownika @theridev, żeby spojrzał na ten błąd.") # Zajmę się tym za rok lub dwa.
        await ctx.send(embed=embed)
        return

    # Przefiltruj wiadomości żeby znaleźć zdjęcia.
    image_messages = [
        msg for msg in messages if msg.attachments and msg.attachments[0].content_type.startswith("image")
    ]
    
    # Nie wykryto zdjęć!
    if not image_messages:
        embed=discord.Embed(color=0xe01b24)
        embed.add_field(name="Błąd!", value="Nie można było wykryć zdjęć na danym kanale.", inline=True)
        embed.set_footer(text="Oznacz użytkownika @theridev, żeby spojrzał na ten błąd.")
        await ctx.send(embed=embed)
        return

    # Wybierz losowe zdjęcie i wyślij je wraz z ładniutką wiadomością :3
    random_message = random.choice(image_messages)
    random_image = random_message.attachments[0]
    # Utwórz embed z osadzonym obrazkiem
    embed = discord.Embed(color=0x8ff0a4)
    embed.add_field(name="%s serwerowy!" % co, value=f"Wysłany przez {random_message.author.display_name}.", inline=True)
    embed.set_image(url=random_image.url)  # Osadź obrazek w embed
    await ctx.send(embed=embed)

# Guziki dla komendy zgaduj.
class zgadujGuziki(discord.ui.View):
    def __init__(self, guess_user, guess_user_display, *, timeout=180): # Po trzech minutach od wysłania wiadomości guziki staną się nieaktywne.
        super().__init__(timeout=timeout)
        self.guess_user = guess_user
        self.guess_user_display = guess_user_display

    @discord.ui.button(label="Zgaduj", style=discord.ButtonStyle.red)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(Questionnaire(self.guess_user, self.guess_user_display))

# Kwestionarz! Pozwala on na zgadywanie użytkownika.
class Questionnaire(Modal, title='Zgadywanka'):
    name = discord.ui.TextInput(label='Co to za użytkownik?')

    def __init__(self, guess_user, guess_user_display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.guess_user = guess_user
        self.guess_user_display = guess_user_display

    async def on_submit(self, interaction: discord.Interaction):
        guessOG = self.name
        guessLowercase = str(guessOG).lower()

        # zadziała np i THERI i theri i Theri i THeRi...
        guessUserDisplayLowercase = str(self.guess_user_display).lower()

        # Sprawdź czy użytkownik trafił albo na poprawną nazwę wyświetleniową albo na poprawną nazwę użytkownika.
        # Np: i "theri" i "theridev" zadziała.
        if guessLowercase == self.guess_user.lower() or guessLowercase == guessUserDisplayLowercase or guessLowercase == "kastracja" and self.guess_user.lower() == "postal_dude_jr."or guessLowercase == "dyskryminacja" and self.guess_user.lower() == "dmnk_dsc":
            embed = discord.Embed(color=0x8ff0a4)
            embed.add_field(name="Zgadłeś! Użytkownik to %s" % self.guess_user, value=" ", inline=True)
            stats.stats.add(interaction.user.name, 1)
            await interaction.response.send_message(embed=embed)
        else:
            # ups
            embed = discord.Embed(color=0xe01b24)
            embed.add_field(name=f"Źle! Ten użytkownik to nie {guessLowercase}", value=" ", inline=True)
            await interaction.response.send_message(embed=embed)

# Zgaduj!
@bot.command()
async def zgaduj(ctx):
    global guessUser
    global guessUserDisplay
    users = ctx.guild.members  # Lista wszystkich uczestników serwera
    user = random.choice(users) # Wybierz losowego użytkownika. Boty - niestety - też sie liczą. Do naprawienia...?
    guessUser = user.name # Nazwa użytkownika
    guessUserDisplay = user.display_name # Nazwa wyświetlana
    pfp = user.avatar.url  # URL awataru, do zgadywanki.

    # Wiadomość!
    embed = discord.Embed(title=" ", description="Kto to?", color=0x8ff0a4)
    embed.set_author(name="Co to za użytkownik?")
    embed.set_image(url=pfp)
    await ctx.send(embed=embed, view=zgadujGuziki(guess_user=guessUser, guess_user_display=guessUserDisplay))  # Send message to the channel

@bot.command()
async def stopy(ctx):
    invoker = ctx.author
    invokerPFPUrl = invoker.avatar.url

    # Pobierz awatar użytkownika za pomocą requests
    response = requests.get(invokerPFPUrl, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        invokerPFP = Image.open(BytesIO(response.content)).convert("RGBA")  # musi być RGBA!!!
        stopy = Image.open("stopki.png").convert("RGBA")  # musi być RGBA!!!

        # Żeby poprawnie funkcja działała oba zdjęcia powinny być w tym samym rozmiarze.
        invokerResized = invokerPFP.resize((500, 500))
        stopyResized = stopy.resize((500, 500))

        # Puste zdjęcie
        final_image = Image.new("RGBA", (500, 500))
        final_image.paste(invokerResized, (0, 0))  # Pierwsze zdjęcie
        final_image.paste(stopyResized, (0, 0), stopyResized)  # Nakładka!

        # Przekonwertuj do RGB dla większej kompatybilności, nigdy nie wiadomo
        final_image_rgb = final_image.convert("RGB")

        # Save and send the json_object[user] + value image
        with BytesIO() as image_binary:
            final_image_rgb.save(image_binary, "PNG")
            image_binary.seek(0)
            final = discord.File(fp=image_binary, filename="image.png")
            embed = discord.Embed(color=0x8ff0a4)
            embed.add_field(name="Stópki!", value=" ", inline=True)
            embed.set_image(url="attachment://image.png")
            await ctx.send(file=final, embed=embed)
    else:
        embed = discord.Embed(color=0xe01b24)
        embed.add_field(name="Błąd!", value="Nie udało się pobrać awataru użytkownika!", inline=True)
        embed.set_footer(text="Oznacz użytkownika @theridev, żeby spojrzał na ten błąd.")
        await ctx.send(embed=embed)

@bot.command()
async def lysejadro(ctx):
    invoker = ctx.author
    invokerPFPUrl = invoker.avatar.url

    # Pobierz awatar użytkownika za pomocą requests
    response = requests.get(invokerPFPUrl, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        invokerPFP = Image.open(BytesIO(response.content)).convert("RGBA")  # musi być RGBA!!!
        lysy = Image.open("lysy.png").convert("RGBA")  # musi być RGBA!!!

        # Żeby poprawnie funkcja działała oba zdjęcia powinny być w tym samym rozmiarze.
        invokerResized = invokerPFP.resize((500, 500))
        lysyResized = lysy.resize((500, 500))

        # Puste zdjęcie
        final_image = Image.new("RGBA", (500, 500))
        final_image.paste(invokerResized, (0, 0))  # Pierwsze zdjęcie
        final_image.paste(lysyResized, (0, 0), lysyResized)  # Nakładka!

        # Przekonwertuj do RGB dla większej kompatybilności, nigdy nie wiadomo
        final_image_rgb = final_image.convert("RGB")

        # Save and send the image
        with BytesIO() as image_binary:
            final_image_rgb.save(image_binary, "PNG")
            image_binary.seek(0)
            final = discord.File(fp=image_binary, filename="lysy.png")
            embed = discord.Embed(color=0x8ff0a4)
            embed.add_field(name="ŁYSYYYYY!", value=" ", inline=True)
            embed.set_image(url="attachment://lysy.png")
            await ctx.send(file=final, embed=embed)
    else:
        embed = discord.Embed(color=0xe01b24)
        embed.add_field(name="Błąd!", value="Nie udało się pobrać awataru użytkownika!", inline=True)
        embed.set_footer(text="Oznacz użytkownika @theridev, żeby spojrzał na ten błąd.")
        await ctx.send(embed=embed)

@bot.command()
async def rank(ctx):
    invoker = ctx.author
    invokerName = ctx.author.name

    randomColor = random.randrange(0, 2**24)
    randomHex = hex(randomColor)
    randomHexINT = int(randomHex,16)

    value = stats.stats.getUserValue(invokerName)

    if value == 1:
        raz = "raz"
    else:
        raz = "razy"

    embed = discord.Embed(color=randomHexINT)
    embed.add_field(name="Użytkownik %s zgadł %s %s!" % (invokerName, str(value), raz), value=" ", inline=True)
    embed.set_image(url=ctx.author.avatar.url)  # Awatar Jupii
    await ctx.send(embed=embed)

@bot.command()
async def top(ctx):
    topValues = stats.stats.getAllValues()
    top = {k: v for k, v in sorted(topValues.items(), key=lambda item: item[1], reverse=True)}

    randomColor = random.randrange(0, 2**24)
    randomHex = hex(randomColor)
    randomHexINT = int(randomHex,16)

    embed = discord.Embed(color=randomHexINT)
    for x, (user, value) in enumerate(top.items(), start=1):
        if value == 1:
            raz = "raz"
        else:
            raz = "razy"
        embed.add_field(name=f"{x}. {user}", value=f"Zgadnął {value} {raz}.")
    
    await ctx.send(embed=embed)


# Token poniżej. Ze względów bezpieczeństwa jest on przechowywany w oddzielnym pliku, nie zapisywanym przez Git.
with open(".token", "r") as token_file:
    bot.run(token_file.read().strip())