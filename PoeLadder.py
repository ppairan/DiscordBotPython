import requests
import json
import discord
from discord.ext import commands
import asyncio
from itertools import cycle
from SECRETS import sec



##Setting
client = discord.Client()
TOKEN = "***********************************"
game = discord.Game("")
description =''' Das ist Der Bot der entenleague'''
intents = discord.Intents.default()
rank = "🏆"
name = "📛"
dead = "☠️ "


bot = discord.Client()
bot = commands.Bot(command_prefix='!', description=description, intents=intents)
online = ":green_circle:"
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('------')
    SECRETS.Token
    await bot.change_presence(activity=game,afk=False)

@bot.command()
async def ladder(ctx):
    res = requests.get('http://api.pathofexile.com/ladders/Entenleague+II+The+Quackening+(PL12039)')
    r_dict = res.json()
    bad_chars = '"'
    key = 'twitch'
    value = 'true'





    await ctx.message.delete()
    await ctx.channel.send("__:duck::duck:Top 5 EntenPeople!!__:duck::duck:",delete_after=300)
    for i in range(5):
            if value in json.dumps(r_dict['entries'][i]['dead']):
                if value in json.dumps(r_dict['entries'][i]['online']):
                    await ctx.channel.send("```"+rank + " : " +json.dumps(r_dict['entries'][i]['rank']) +
                                       "\n" +"📛 : " + json.dumps(r_dict['entries'][i]['character']['name']).replace(bad_chars, '') +
                                       "\n" + "Klasse"+ " : " + json.dumps((r_dict['entries'][i]['character']['class']).replace(bad_chars, '')) +
                                       "\n" +  "Level: "+ json.dumps(r_dict['entries'][i]['character']['level']) +
                                       "\n" + "Online : "+"✔️" +
                                       "\n" + dead + ":"+" Gestorben"+
                                       "\n" + "```", delete_after=300)
                else:
                    await ctx.channel.send("```" + rank + " : " + json.dumps(r_dict['entries'][i]['rank']) +
                                           "\n" + "📛 : " + json.dumps(r_dict['entries'][i]['character']['name']).replace(bad_chars, '') +
                                           "\n" + "Klasse" + " : " + json.dumps((r_dict['entries'][i]['character']['class']).replace(bad_chars, '')) +
                                           "\n" + "Level: " + json.dumps(r_dict['entries'][i]['character']['level']) +
                                           "\n" + "Online : "+"❌" +
                                           "\n" + dead + ":"+" Gestorben" +
                                           "\n" + "```", delete_after=300)
            else:
                if value in json.dumps(r_dict['entries'][i]['online']):
                    await ctx.channel.send("```" + rank + " : " + json.dumps(r_dict['entries'][i]['rank']) +
                                           "\n" + "📛 : " + json.dumps(r_dict['entries'][i]['character']['name']).replace(bad_chars, '') +
                                           "\n" + "Klasse" + " : " + json.dumps((r_dict['entries'][i]['character']['class']).replace(bad_chars, '')) +
                                           "\n" + "Level: " + json.dumps(r_dict['entries'][i]['character']['level']) +
                                           "\n" + "Online : " +"✔️" +
                                           "\n" +dead + ": Still Alive"+"```" ,delete_after= 300)
                else:
                    await ctx.channel.send("```" + rank + " : " + json.dumps(r_dict['entries'][i]['rank']) +
                                           "\n" + "📛 : " + json.dumps(r_dict['entries'][i]['character']['name']).replace(bad_chars, '') +
                                           "\n" + "Klasse : " + json.dumps(r_dict['entries'][i]['character']['class'].replace(bad_chars, '')) +
                                           "\n" + "Level : " + json.dumps(r_dict['entries'][i]['character']['level']) +
                                           "\n" + "Online : " + "❌" +
                                           "\n" + dead + ": Still Alive" +
                                           "\n" + "```", delete_after=300)



@bot.command()
async def ladexp(ctx):
    res =  requests.get('http://api.pathofexile.com/ladders/Entenleague+II+The+Quackening+(PL12039)')
    r_dict = res.json()
    bad_chars = '"'
    await ctx.channel.send("__:duck::duck:Top 10 EntenPeople Expladder!!__:duck::duck:")
    for i in range(10):
        await ctx.channel.send("```"+ rank + " : " + json.dumps(r_dict['entries'][i]['rank']) +
                               "\n"+"📛 : " + json.dumps(r_dict['entries'][i]['character']['name']).replace(bad_chars, '')+
                               "\n"+"📈 : "+json.dumps(r_dict['entries'][i]['character']['experience'])+"```",delete_after=300)

@bot.command(pass_context = True)
async def clear(ctx,number):
   nbr = int(number)
   delete = await ctx.channel.purge(limit=nbr )
   await ctx.channel.send("Es wurden : "+format(len(delete))+" Nachrichten gelöscht", delete_after=30)
   print("Clear Kommand benutzt")






bot.run(TOKEN)


