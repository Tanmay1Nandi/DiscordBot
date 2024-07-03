import random
import discord
from discord.ext import commands
from groq import Groq
from keep_alive import keep_alive
import os


keep_alive()

client = Groq(
    api_key="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")

TOKEN = os.environ.get('token')

intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.messages = True
intents.message_content = True

flirty_responses = [
    "are you a magician? Because whenever I look at you, everyone else disappears.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Excuse me, but I think you dropped something: MY JAW!",
    "Do you have a map? I keep getting lost in your eyes.",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "are you a magician? Because whenever I look at you, everyone else disappears.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Excuse me, but I think you dropped something: MY JAW!",
    "Do you have a map? I keep getting lost in your eyes.",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "Are you a time traveler? Cause I can see you in my future.",
    "Do you have a name, or can I call you mine?",
    "Excuse me, but I think you dropped something: MY JAW!",
    "Do you have a map? I keep getting lost in your eyes.",
    "If kisses were snowflakes, I’d send you a blizzard.",
    "If you were a vegetable, you’d be a ‘cute-cumber.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Is your name Google? Because you have everything I’ve been searching for.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "Are you a campfire? Because you’re hot and I want s’more.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a name, or can I call you mine?",
    "Is your dad a boxer? Because you're a knockout!",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is it hot in here or is it just you?",
    "Do you believe in love at first sight, or should I walk by again?",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "You must be a broom, because you just swept me off my feet!",
    "If kisses were snowflakes, I'd send you a blizzard.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a time traveler? Because I see you in my future!",
    "Is there an airport nearby or is it my heart taking off?",
    "Do you have a map? Because I just keep getting lost in your eyes.",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "Are you a parking ticket? Because you've got 'FINE' written all over you.",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "If you were a fruit, you'd be a fine-apple.",
    "Are you a time traveler? Because I can't imagine my future without you.",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "Do you have a sunburn, or are you always this hot?",
    "If beauty were a crime, you'd be serving a life sentence.",
    "Do you have a name, or can I call you mine?",
    "Is there a spark between us or is it just your smile lighting up the room?",
    "Are you a bank loan? Because you've got my interest.",
    "Are you made of copper and tellurium? Because you're Cu-Te.",
    "Can you lend me a kiss? I promise I'll give it back.",
    "Is your name Wi-Fi? Because I'm feeling a connection.",
    "Do you have a mirror in your pocket? Because I can see myself in your pants.",
    "Are you an angel? Because heaven is missing one.",
    "If you were a transformer, you'd be Optimus Fine.",
    "Do you have a map? Because I got lost in your eyes.",
    "Are you a camera? Every time I look at you, I smile.",
    "Do you like Star Wars? Because Yoda one for me!",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Are you a light bulb? Because you brighten up my day.",
    "Do you have any raisins? No? How about a date?",
    "Are you a snowstorm? Because you make my heart race.",
    "Can I tie your shoes? I don’t want you falling for anyone else.",
    "Are you an alien? Because you just abducted my heart.",
    "Is your dad a boxer? Because you're a knockout!",
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a pencil? Because I want to erase your past and write our future.",
    "Are you a dictionary? Because you add meaning to my life.",
    "Can you lend me a kiss? I promise I'll give it back.",
    "Are you a light switch? Because you turn me on.",
    "Do you believe in fate? Because I think we've met for a reason.",
    "Is your name Chapstick? Because you’re da balm!",
    "Are you a parking ticket? Because you have 'fine' written all over you.",
    "Is there a sparkle in your eye, or are you just happy to see me?",
    "Are you an ocean? Because I'm lost at sea.",
    "Do you have a map? Because I keep getting lost in your eyes.",
    "Are you a time traveler? Because I see you in my future.",
    "Do you have a sunburn, or are you always this hot?",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "Are you a snowstorm? Because you make my heart race.",
    "Do you have a name, or can I call you mine?",
    "Is your name Wi-Fi? Because I'm feeling a connection.",
    "Do you like Star Wars? Because Yoda one for me!",
    "Are you a camera? Every time I look at you, I smile.",
    "Are you a light bulb? Because you brighten up my day.",
    "Do you have any raisins? No? How about a date?",
    "Is your dad a boxer? Because you're a knockout!",
    "Can I tie your shoes? I don’t want you falling for anyone else.",
    "Are you an alien? Because you just abducted my heart.",
    "Do you have a quarter? Because I want to call my mom and tell her I met 'the one'.",
    "Are you a dictionary? Because you add meaning to my life.",
    "Is your name Chapstick? Because you’re da balm!",
    "Are you a light switch? Because you turn me on.",
    "Do you believe in fate? Because I think we've met for a reason.",
    "Is there a sparkle in your eye, or are you just happy to see me?",
    "Are you an ocean? Because I'm lost at sea.",
    "Are you a time traveler? Because I see you in my future.",
    "Can you lend me a kiss? I promise I'll give it back.",
    "Are you a snowstorm? Because you make my heart race.",
    "Do you have a pencil? Because I want to erase your past and write our future.",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "Do you have a sunburn, or are you always this hot?",
    "Is your name Wi-Fi? Because I'm feeling a connection.",
    "Do you like Star Wars? Because Yoda one for me!",
    "Are you a camera? Every time I look at you, I smile.",
    # "Are you an angel? Because heaven is missing one.",
    # "Do you have a mirror in your pocket? Because I can see myself in your pants.",
    "Are you a bank loan? Because you've got my interest.",
    "Is there a spark between us or is it just your smile lighting up the room?",
    "Do you have a name, or can I call you mine?",
    "If beauty were a crime, you'd be serving a life sentence.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Do you have a map? Because I just keep getting lost in your eyes.",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Are you a magician? Because whenever I look at you, everyone else disappears."
]

accepted_words_for_flirt_back = [
    'love', 'flirt', 'pyaar', 'baby', '🙈', '❤️', '', 'mohobbat', "pyaar",
    "ishq", "mohabbat", "prem", "mamta", "chaahat", "sharm", "dilchaspi",
    "dosti", "yaari", "bewafaai", "dhokha", "shikayat", "tadap", "viyog",
    "milan", "gamla", "naz", "ada", "ishara", "mastana", "mastani", "fareb",
    "farebi", "love", "affection", "care", "adoration", "passion", "romance",
    "infatuation", "devotion", "attachment", "fondness", "sweetheart",
    "darling", "honey", "beau", "belle", "charm", "allure", "enchantment",
    "flirt", "tease", "play", "banter", "charm", "seduce", "entice", "woo",
    "court", "wink", "compliment", "flattery", "innuendo", "suggestive"
]

gaalis = [
    'bhen ke l*de', 'jaa na bh*sdike', 'kutte', 'maa ki mamta', 'b@dwe',
    'chal chal baap ko mat sikha', 'Ja ja porn dekh ke muth maar',
    'Bc mera dimag mat kharab kar', 'Nikal yahan lode',
    'Chutiya ka Chutiya hi rahega tu'
]

accepted_words_for_Gaali_in_return = [
    'Bhen ke lde', 'bhosdike', 'Kutte', 'gaali', 'gali', 'kutti', 'randi',
    'gaand', 'bc', 'mc', 'kutte', 'maa ki mamta', 'ddwe',
    'chal chal baap ko mat sikha', "bkl", 'lavda', 'lavde', 'lawda', 'lawde',
    'lode', 'lolu', 'lode', 'loda', 'lodu', 'hilao', 'hilale', 'saale'
]

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message, ):

    c1 = message.content.lower() == "hello"
    c2 = message.content.lower() == "hi"
    c3 = message.content.lower() == "hey"
    c4 = ("flirt" in message.content.lower())
    c5 = ("tanu" in message.content.lower())
    if message.author == bot.user:
        return

    elif (("shaadi" in message.content.lower()) and c6 ):
        await message.reply(content="Anyday with him! ❤️")
        await bot.process_commands(message)

    elif (("shaadi" in message.content.lower()) and c7 ):
        await message.reply(content=" Shaadi mai kab bula rahe?")
        await bot.process_commands(message)
    
    elif ("shaadi" in message.content.lower()):
        await message.reply(content="Uss Behen ke lode se nhi karungi saadi. ❤️")
        await bot.process_commands(message)
    
    elif (c1 or c2 or c3 or c4 or c5):
        response = random.choice(flirty_responses)
        await message.reply(content="Hello," + response)
        await bot.process_commands(message)

    elif (any(i in message.content.lower()
              for i in accepted_words_for_Gaali_in_return)):
        response = random.choice(gaalis)
        await message.reply(content=response)
        await bot.process_commands(message)

    else:
        chat_completion = client.chat.completions.create(
            messages=[{
                "role":
                "user",
                "content":
                f'''You are a flirty bot.
                .Reply to this message " {message.content.lower()} " in 15-20 words. Either use a pickupline or be naughty. use a emojis.'''
            }],
            model="llama3-8b-8192",
        )

        await bot.process_commands(message)

        if len(message.mentions) > 0:
            mentions = []
            for i in message.mentions:
                mentions.append(i.mention)
            print(mentions)
            print("bot mention:", bot.user.mention)
            if bot.user.mention in mentions:
                print("bot in mentions  ")
                if len(mentions) > 1:
                    for i in mentions:
                        if bot.user.mention == i:
                            continue
                        elif message.author.mention == i:
                            resp = chat_completion.choices[0].message.content
                            await message.reply(content=resp)
                        else:
                            await message.reply(
                                content=f"Hey {i} , " +
                                chat_completion.choices[0].message.content)
                else:
                    resp = chat_completion.choices[0].message.content
                    await message.reply(content=resp)


bot.run(TOKEN)
