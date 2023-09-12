import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("started")
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(e)

@bot.tree.command(name="update")
@app_commands.describe(user = "Игрок", avg_energy = "Средняя энергия за неделю", activity_gw = "Активность на ВГ от 0 до 10", activity_tb = "Активность на ТБ от 0 до 10")
async def update(interaction: discord.Interaction, user: str, avg_energy: int , activity_gw: int, activity_tb: int):
    await interaction.response.send_message(f"Данные загружены для {user}\nСрендняя энергия: {avg_energy}\nАктивность на ВГ: {activity_gw}\nАктивность на ТБ: {activity_tb}")


# @bot.command(help="Складывает два числа")
# async def add(ctx, num1: int, num2: int):
#     result = num1 + num2
#     await ctx.send(f'Результат сложения: {result}')

# # Команда вычитания
# @bot.command()
# async def subtract(ctx, num1: int, num2: int):
#     result = num1 - num2
#     await ctx.send(f'Результат вычитания: {result}')

# Запуск бота с токеном

bot.run(os.getenv('DISCORD_BOT_TOKEN'))



