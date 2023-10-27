import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def seskirliliğinedir(ctx):
    await ctx.send(f'Merhaba {bot.user}! Gürültü kirliliği veya diğer adıyla ses kirliliği, insan veya hayvan yaşamını olumsuz etkileyen, dengesini bozan her türlü insan, hayvan ya da makine kaynaklı ses oluşumudur. Gürültü kirliliğinin en yaygın biçimlerinden biri, özellikle motorlu araçların neden olduğu kirliliktir.')

bot.run("MTE2NzUxMDg1ODExNzY4MTI3NA.G2chEO.uukJ1521BOQxc4Awt2km44ocWEHtTxYNS-PsaA")



