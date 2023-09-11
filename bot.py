import discord
from discord.ext import commands

intents = discord.Intents.all()



bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents, help_command=commands.DefaultHelpCommand(dm_help=True))

@bot.event
async def on_ready():
    print("started")

@bot.command(help="Складывает два числа")
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f'Результат сложения: {result}')

# Команда вычитания
@bot.command()
async def subtract(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f'Результат вычитания: {result}')

# Запуск бота с токеном
bot.run('MTE1MDkwNjcwMDY3Nzc3OTUwOA.Gc_GjW.KX2Kb4wIb14qNt08shjglFwa-HfzhUHN8pAfhs')



