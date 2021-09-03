from os import getenv
import traceback
import random
import discord

PREFIX = "yz "

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith(PREFIX + '你好'):
            await message.reply('你好~', mention_author=True)
        if message.content.startswith('难'):
            await message.channel.send('晴天好心情猜中了！')
        if message.content.startswith(PREFIX + '涩图'):
            await message.channel.send('https://nekos.life/lewd')
        if message.content.startswith(PREFIX + "晚安"):
            await message.reply('晚安~', mention_author=True)


token = getenv('DISCORD_BOT_TOKEN')
client = MyClient()



client.run(token)
