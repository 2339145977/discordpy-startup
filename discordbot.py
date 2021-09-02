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

        if message.content.startswith(PREFIX + '我要一份涩图'):
            await message.reply('~hentai', mention_author=True)
        if message.content.startswith(PREFIX + 'hihao'):
            await message.reply('你好', mention_author=True)


token = getenv('DISCORD_BOT_TOKEN')
client = MyClient()



client.run(token)
