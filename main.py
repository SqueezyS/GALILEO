import discord
import os

from random import randint as r
from random import choice as c
h=('```GALILEO FIGARO```***SOME QUICK NEWS***\nI lost the original bot so i regenerated its token\nprefix gf!\n```ABOUT```\nGalileo is my side project amoung other things, if you have any suggestions, shoot me a DM @ One S Q E E Z Y Boi#0074\n```COMMANDS```\n**invite**: Invite this bot to your server\n**am-i**: Sees if the bot is working like it should\n**music**: What is Galileo listening to these days?\n**cl**: The change log\n**corona**: VISIT THIS SITE AND REMEMBER TO WASH YOUR HANDS FOR 20 SECONDS, STAY HOME, AND NOT GET MISINFORMED (Im lookin at you, Trump!)\n```Fun```\n**d6**: Rolls a D6 dice\n**rng** Generates a random number\n**D12** Rolls a D12 dice\n```Semi-Moderation tools```\n**mr**: Cant decide what to do with a rule breaker? use Mod Roulette!\n```GALILEO BOT "We are back baby!" 1.0```')
sh=("```Secret Help```\n **foundya** OH GOD YOU FOUND ME!!!!!")
cl=("```GALILEO NEWS```\n+We are now in full version\n+Secret update(￣y▽,￣)╭ \n-Kill command\n+D12 dice")
client = discord.Client()

DBa=("https://discord.com/api/oauth2/authorize?client_id=712749334135046165&permissions=0&redirect_uri=https%3A%2F%2Fshutplea.se%2F&response_type=code&scope=bot%20messages.read")

 
@client.event
async def on_ready():
    print('Bot is open {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
  
        print("Hello test conducted")
    if message.content.startswith('gf!corona'):
        await message.channel.send('Visit this site for Coronavirus information https://www.cdc.gov/')
    if message.content.startswith('gf!help'):
        await message.channel.send(h)
        print("Help Conducted")
    if message.content.startswith('gf!SEhelp'):
        await message.channel.send(sh)



    if message.content.startswith('gf!cl'):
        await message.channel.send(cl)
    if message.content.startswith('gf!invite'):
        await message.channel.send(DBa)
        print("Invited someone to join the bot!")
    if message.content.startswith('gf!d6'):
        b=r(1,6)
        await message.channel.send(b)
        print("d6:",b)
    if message.content.startswith('gf!cmd'):
        d=r(1,3267)
        await message.channel.send("YOU HAVE WON THE EVENT! Quick! Message One S Q U E E Z Y Boi#0074: 44573")
        print("Winning Number:",d)
    if message.content.startswith('gf!rng'):
        e=r(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
        await message.channel.send(e)
        print("RNG:",e)
    if message.content.startswith('gf!mr'):
      AAA=("Ban", "Mute", "Long mute", "Kick", "Warn")
      abc=c(AAA)
      print(abc)
      await message.channel.send(abc)
        

# Now, we can use that .env file to get the token we want to use.
token = os.environ.get("TOKEN")
client.run(token)