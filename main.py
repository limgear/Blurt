import disnake
from disnake.ext import commands
from disnake import app_commands
from disnake import utils
from disnake.utils import get
from disnake import Game
import os
import math
import random
from asyncio import sleep
import time
import requests
from os import system
import asyncio
import json
import pyttsx3
import datetime

now = datetime.datetime.now()

bot = commands.Bot(command_prefix = None)

@bot.event
async def on_guild_join(guild: disnake.Guild):
  print (now.strftime("%d-%m-%Y %H:%M"))
  print('Бот добавлен на новый сервер!')  
  if guild.system_channel is not None:
        await guild.system_channel.send('Спасибо за то, что добавили меня на сервер! Введите /help для получения списка команд')
  elif guild.system_channel is None: 
        user = client.get_user(guild.owner.id)
        await user.send('Спасибо за то, что добавили меня на сервер! Введите /help для получения списка команд')

@bot.slash_command(name="fox",description="Бот парсит картинку лисы и присылает в чат")
async def fox(inter):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = disnake.Embed(color = 0x89965, title = 'Лиса')
    embed.set_image(url = json_data['link'])
    await inter.response.send_message(embed = embed)



@bot.slash_command(name="cat",description="Бот парсит картинку кота и присылает в чат")
async def cat(inter):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)
    embed = disnake.Embed(color = 0x89965, title = 'Кот')
    embed.set_image(url = json_data['link'])
    await inter.response.send_message(embed = embed)
    

@bot.slash_command(name="dog",description="Бот парсит картинку собаки и присылает в чат")
async def dog(inter):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)
    embed = disnake.Embed(color = 0x89965, title = 'Собака')
    embed.set_image(url = json_data['link'])
    await inter.response.send_message(embed = embed)

@bot.slash_command(pass_context=True,name="rep",description="Бот повторит сообщение участника")
async def rep(inter, *, arg=None):
    author = inter.author
    await inter.response.send_message(arg)

@bot.slash_command(pass_context=True,name="ball",description="Испытай удачу на предсказателе!")
async def ball(inter, *, question):
    await inter.response.send_message(random.choice(['Да', 'Нет', 'Не думаю', 'Наверное', 'Скорее всего нет', 'Может быть']))

@bot.slash_command(pass_context=True,name="clear",description="Удаляет указаное количество сообщений")
@commands.has_permissions(administrator=True)
async def clear( inter, amount : int ):
    await inter.channel.purge( limit = amount + 1 )
 
    await inter.response.send_message(embed = disnake.Embed(description = f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c))

@bot.event
async def on_command_error(inter, error):
     if isinstance(error, disnake.ext.commands.errors.CommandNotFound): 
          await inter.response.send_message(embed = disnake.Embed(description = f'{inter.author.name}, Команда не найдена! Для получения списка команд, введите B!help ', colour = disnake.Color.red()))
     if isinstance(error, disnake.ext.commands.MissingRequiredArgument):
          await inter.response.send_message(embed = disnake.Embed(description = f'{inter.author.name}, Отсутствует параметр (аргумент) ', colour = disnake.Color.red()))
     if isinstance(error, disnake.ext.commands.MissingPermissions):
          await inter.response.send_message(embed = disnake.Embed(description = f'{inter.author.name}, Не достаточно прав! ', colour = disnake.Color.red()))

@bot.event
async def on_server_join(server):
  guilds = await bot.fetch_guilds(limit = None).flatten()
  await bot.change_presence(status = disnake.Status.idle, activity= disnake.Activity(name=f'за {len(guilds)} серверами.', type= disnake.ActivityType.watching))

@bot.slash_command(pass_context=True,name="ban",description="Забанить пользователя")
@commands.has_permissions(ban_members=True)
async def ban(inter, member: disnake.Member, *, reason = "Причина"):
    embed = disnake.Embed(color = 0x89965, title = 'Бан участника', description = (f'{member.mention} **Забанен** по причине {reason} '))
    await inter.response.send_message(embed = embed)
    await member.send(f'Тебя забанили на сервере {inter.guild.name}')
    await member.ban(reason = reason)
    
@bot.slash_command(pass_context=True,name="kick",description="Кикнуть пользователя")
@commands.has_permissions(kick_members=True)
async def kick(inter, member: disnake.Member, *, reason = "Причина"):
    embed = disnake.Embed(color = 0x89965, title = 'Кик участника', description = (f'{member.mention} **кикнут** по причине {reason} '))
    await inter.response.send_message(embed = embed)
    await member.send(f'Тебя выгнали с сервера {inter.guild.name}')
    await member.kick(reason = reason)



@bot.slash_command(pass_context=True,name="calc",description="Калькулятор")
async def calc(inter, *, primer = None):
	embed = None
	import random
	if not primer == None:
		try:
			primer = primer.replace("×", "*")
			primer = primer.replace("÷", "/")
			evalprimer = eval(primer)
			primer = primer.replace("/", "÷")
			primer = primer.replace("*", "×")
			embed = disnake.Embed(
				title = 'Калькулятор',
				description = f'> ``{primer} = {evalprimer}``',
				color = disnake.Colour(random.randint(111111, 999999)))
		except:
			embed = disnake.Embed(
				title = "Ошибка",
				description = '> Пример должен состоять только из цифр и математематических знаков.',
				color = 0xff0000)
	else:
		embed = disnake.Embed(
			title = 'Ошибка',
			description = '> Напишите пример.',
			color = 0xff0000)
	await inter.response.send_message(embed = embed)

@bot.slash_command(name="help",description="Помощь по командам бота")
async def help(inter):
    embed = disnake.Embed(color = 0x89965, title = 'Помощь по командам бота', description = ' Команды: \n\n>rep - бот повторит сообщение автора' \
                          '\n\nsay (текст) - озвучить набранный вами текст' 
                          '\n\nball (текст) - сыграть в предсказатель'
                          '\n\nban (@участник) - забанить участника'
                          '\n\nclear (число сообщений) - очистить указанное количество сообщений'
                          '\n\nkick (@участник) - кикнуть участника'
                          '\n\ncalc (пример) калькулятор, пример использования: 2 * 2'
                          '\n\nfox - Картинка лисы'
                          '\n\ncat - Картинка кота'
                          '\n\ndog -  Картинка собаки'
                          '\n\nВерсия бота: 2.0'
                          '\n\nВместо префикса я использую слеш команды (/)'
                          '\n\nОзвучивание текста делал JustSomething, отдельное спасибо: left Shift, Хоттабыч')
    await inter.response.send_message(embed = embed)

@bot.slash_command(pass_context=True,name="say",description="Бот озвучит введённое вами слово")
async def say(inter,text):
    engine = pyttsx3.init()
    engine.save_to_file(text,"voice_line.mp3")
    engine.runAndWait()
    await inter.response.send_message(file=disnake.File("voice_line.mp3"))


@bot.event
async def on_ready():
    print("Бот готов!")
    await bot.change_presence(status = disnake.Status.idle, activity= disnake.Activity(name=f'/help', type= disnake.ActivityType.watching))

bot.run('')
