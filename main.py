import discord
from discord.ext import commands
import os
import math
import random
from asyncio import sleep
import time
from discord import Game
import requests
from os import system
from discord.utils import get
import asyncio
from discord import utils
import json
import pyttsx3
from discord_components import DiscordComponents, Select, SelectOption, ComponentsBot, Button, ButtonStyle
import datetime

bot = commands.Bot(command_prefix ="B!")
client = commands.Bot(command_prefix ="B!")
bot.remove_command('help')


@bot.event
async def on_guild_join(guild: discord.Guild):
  print( "New server detected" )
  guilds = await bot.fetch_guilds(limit = None).flatten()
  await bot.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'за {len(guilds)} серверами.', type= discord.ActivityType.watching))
  if guild.system_channel is not None:
        await guild.system_channel.send("Спасибо, что добавили меня на сервер!")
  elif guild.system_channel is None: 
        user = client.get_user(guild.owner.id)
        await user.send("Спасибо, что добавили меня на сервер")
 
  
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(
        title = "Информация",
        description = f"> **Профиль бота:** ``{bot.user}``\n> **Версия бота:** ``2.4``\n> **Имя бота:** ``{bot.user.name}``\n> **ID бота:** ``{bot.user.id}``\n> **Владелец бота:** ``Biskvit#0623``\n> **Пинг бота:** ``{round(bot.latency)}ms``",
        color = 0xff0000)
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed)
          
@bot.event
async def on_ready():
  print("бот запущен, пожалуйста не закрывайте окно")
  guilds = await bot.fetch_guilds(limit = None).flatten()
  await bot.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'B!help', type= discord.ActivityType.watching))

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0x89965, title = 'Случайная картинка лисы') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0x89965, title = 'Случайная картинка кота') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0x89965, title = 'Случайная картинка собаки') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def repeat(ctx, *, arg=None):
    author = ctx.message.author
    #if arg == None:
        #embed = discord.Embed(color = 0x89965, title = 'Ошибка', description = 'Кроме команды B!repeat, укажите текст!') 
    await ctx.send(arg) #/say
        #await ctx.send(embed = embed) # Отправляем Embed


@bot.command(aliases = ['шар'])
async def question(ctx, *, question):
    await ctx.send(random.choice(['Да', 'Нет', 'Не думаю', 'Наверное', 'Точно нет', 'Может быть!']))



# Clear message
@bot.command()
@commands.has_permissions(administrator=True)
async def clear( ctx, amount : int ):
    await ctx.channel.purge( limit = amount + 1 )
 
    await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c))


@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, discord.ext.commands.errors.CommandNotFound): 
          await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, Команда не найдена! Для получения списка команд, введите B!help ', colour = discord.Color.red()))
     if isinstance(error, discord.ext.commands.MissingRequiredArgument):
          await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, Пожалуйста, укажите команду как написано в команде помощи (B!commands) ', colour = discord.Color.red()))
     if isinstance(error, discord.ext.commands.MissingPermissions):
          await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, Не достаточно прав ', colour = discord.Color.red()))


@bot.event
async def on_server_join(server):
  guilds = await bot.fetch_guilds(limit = None).flatten()
  await bot.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'за {len(guilds)} серверами.', type= discord.ActivityType.watching))
  print( 'Bot joined' )


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason = "Причина"):
    #await ctx.send(f'{member.mention} **забанен**')
    embed = discord.Embed(color = 0x89965, title = 'Бан участника', description = (f'{member.mention} **Забанен** по причине {reason} '))
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await member.send(f'Тебя выгнали с сервера {ctx.guild.name}')
    await member.ban(reason = reason)
    


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason = "Причина"):
    #await ctx.send(f'{member.mention} **забанен**')
    embed = discord.Embed(color = 0x89965, title = 'Кик участника', description = (f'{member.mention} **кикнут** по причине {reason} '))
    embed.set_footer(text = f"Команду использовал {ctx.author.name}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    await member.send(f'Тебя выгнали с сервера {ctx.guild.name}')
    await member.kick(reason = reason)

@bot.command()
async def calculator(ctx, *, primer = None):
	embed = None
	import random
	if not primer == None:
		try:
			primer = primer.replace("×", "*")
			primer = primer.replace("÷", "/")
			evalprimer = eval(primer)
			primer = primer.replace("/", "÷")
			primer = primer.replace("*", "×")
			embed = discord.Embed(
				title = "Калькулятор",
				description = f"> ``{primer} = {evalprimer}``",
				color = discord.Colour(random.randint(111111, 999999)))
		except:
			embed = discord.Embed(
				title = "Ошибка",
				description = "> Пример должен состоять только из цифр и математематических знаков.",
				color = 0xff0000)
	else:
		embed = discord.Embed(
			title = "Ошибка",
			description = "> Напишите пример.",
			color = 0xff0000)
	await ctx.reply(embed = embed)


@bot.command()
async def spinning_stick(ctx):
    loading = True
    text = ""
    message = await ctx.reply("-")
    while loading:
        text = "|"
        await message.edit(content = text)
        await asyncio.sleep(0.2)
        text = "/"
        await message.edit(content = text)
        await asyncio.sleep(0.2)
        text = "-"
        await message.edit(content = text)
        await asyncio.sleep(0.2)
        text2 = "\n"
        text2 = repr(text2)
        text2 = text2.replace("'", "")
        text2 = text2.replace("n", "")
        text = text2
        await message.edit(content = text)
    await asyncio.sleep(10)
    loading = False

  
@bot.command()
async def victormem(ctx):
    r = random.randint(1,1)
    print(r)
    
    if r == 1:
        await ctx.send(file=discord.File("korneplod1.jpg"))
        
    if r == 2:
        await ctx.send(file=discord.File("korneplod2.jpg"))

    if r == 3:
        await ctx.send(file=discord.File("korneplod3.jpg"))

    if r == 4:
        await ctx.send(file=discord.File("korneplod4.jpg"))

    if r == 5:
        await ctx.send(file=discord.File("korneplod5.jpg"))

    if r == 6:
        await ctx.send(file=discord.File("korneplod6.jpg"))

    if r == 7:
        await ctx.send(file=discord.File("korneplod7.jpg"))

    if r == 8:
        await ctx.send(file=discord.File("korneplod8.jpg"))

    if r == 9:
        await ctx.send(file=discord.File("korneplod9.jpg"))

    if r == 10:
        await ctx.send(file=discord.File("korneplod10.jpg"))

    if r == 11:
        await ctx.send(file=discord.File("korneplod11.jpg"))

    if r == 12:
        await ctx.send(file=discord.File("korneplod12.jpg"))

    if r == 13:
        await ctx.send(file=discord.File("korneplod13.jpg"))

    if r == 14:
        await ctx.send(file=discord.File("korneplod14.jpg"))

    if r == 15:
        await ctx.send(file=discord.File("korneplod15.jpg"))

    if r == 16:
        await ctx.send(file=discord.File("korneplod16.jpg"))

    if r == 17:
        await ctx.send(file=discord.File("korneplod17.jpg"))

    if r == 18:
        await ctx.send(file=discord.File("korneplod18.jpg"))

    if r == 19:
        await ctx.send(file=discord.File("korneplod19.jpg"))

    if r == 20:
        await ctx.send(file=discord.File("korneplod20.jpg"))

    if r == 21:
        await ctx.send(file=discord.File("korneplod21.jpg"))

    if r == 22:
        await ctx.send(file=discord.File("korneplod22.jpg"))

    if r == 23:
        await ctx.send(file=discord.File("korneplod23.jpg"))

    if r == 24:
        await ctx.send(file=discord.File("korneplod24.jpg"))

    if r == 25:
        await ctx.send(file=discord.File("korneplod25.jpg"))

    if r == 26:
        await ctx.send(file=discord.File("korneplod26.jpg"))

    if r == 27:
        await ctx.send(file=discord.File("korneplod27.jpg"))

    if r == 28:
        await ctx.send(file=discord.File("korneplod28.jpg"))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member,time):
    muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
    time_convert = {"s":1, "m":60, "h":3600,"d":86400}
    tempmute= int(time[0]) * time_convert[time[-1]]
    await member.add_roles(muted_role)
    embed = discord.Embed(title = "Мут участника", description= f"{member.display_name}#{member.discriminator} Успешно замьючен", color=discord.Color.green())
    await ctx.send(embed=embed, delete_after=5)
    await asyncio.sleep(tempmute)
    await member.remove_roles(muted_role)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    muted_role=discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(muted_role)
    embed = discord.Embed(title = "Размьют участника", description= f"{member.display_name}#{member.discriminator} Успешно размьючен", color=discord.Color.green())
    await ctx.send(embed=embed, delete_after=5)



@bot.command()
async def skeletmem(ctx):
    rs = random.randint(1,16)
    print(rs)
    if rs == 1:
        await ctx.send(file=discord.File("1.jpg"))
        
    if rs == 2:
        await ctx.send(file=discord.File("2.jpg"))

    if rs == 3:
        await ctx.send(file=discord.File("3.jpg"))

    if rs == 4:
        await ctx.send(file=discord.File("4.jpg"))

    if rs == 5:
        await ctx.send(file=discord.File("5.jpg"))

    if rs == 6:
        await ctx.send(file=discord.File("6.jpg"))

    if rs == 7:
        await ctx.send(file=discord.File("7.jpg"))

    if rs == 8:
        await ctx.send(file=discord.File("8.jpg"))

    if rs == 9:
        await ctx.send(file=discord.File("9.jpg"))

    if rs == 10:
        await ctx.send(file=discord.File("10.jpg"))

    if rs == 11:
        await ctx.send(file=discord.File("11.jpg"))

    if rs == 12:
        await ctx.send(file=discord.File("12.jpg"))

    if rs == 13:
        await ctx.send(file=discord.File("13.jpg"))

    if rs == 14:
        await ctx.send(file=discord.File("14.jpg"))

    if rs == 15:
        await ctx.send(file=discord.File("15.jpg"))

    if rs == 16:
        await ctx.send(file=discord.File("16.jpg"))
 

@bot.command()
async def help(ctx):
    embed = discord.Embed(color = 0x89965, title = 'Помощь по командам бота', description = 'Команды: \n\nB!repeat - бот повторит сообщение автора\n\nB!say (текст) - озвучить набранный вами текст\n\nB!question (текст) - задать вопрос боту \n\nB!victormem - прислать любой мем из серии: Виктор корнеплод\n\nB!skeletmem - прислать мем из серии: крутые скелеты\n\nB!ban (@участник) - забанить участника\n\nB!mute (@участник) (время (s, m, h, d) - Замучить участника\n\nB!unmute (@участник) - Размучить участника\n\n)B!clear (число сообщений) - очистить указанное количество сообщений\n\nB!kick (@участник) - кикнуть участника\n\nB!botinfo - информация о боте\n\nB!calculator (пример) калькулятор, пример использования: 2 * 2\n\nB!spinning_stick - палка, которая крутится\n\nB!fox - прислать рандомную картинку лисы\n\nB!cat - прислать рандомную картинку кота\n\nB!dog - прислать рандомную картинку собаки\n\nВерсия бота: 1.1 \n\nОзвучивание текста взято у Dima101130, Аватарку для бота рисовал [left-Shift]#1470') # Создание Embed'a
    await ctx.send(embed = embed)


@bot.command()
async def say(ctx,text):
    engine = pyttsx3.init()
    engine.save_to_file(text,"voice_line.mp3")
    engine.runAndWait()
    await ctx.send(file=discord.File("voice_line.mp3"))
bot.run('')
