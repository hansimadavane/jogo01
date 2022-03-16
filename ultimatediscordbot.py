# 'OTMyMzA4Mzg4ODU4MjAwMTg1.YeRF2Q.llz0e-DaF1eTtRVGT5HoiTTL6J4'

import discord

COMMAND_PREFIX = "!"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as boss {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.bot:
            return
        
    
        if message.content[0] == COMMAND_PREFIX:
            await message.channel.send("Hello from Bot!")

        elif message.content[0] != COMMAND_PREFIX:
            await message.channel.send("Hello from Hans! I will answer soon!")
 
        """else:
            await message.channel.send("Hello from Hans! I will answer soon!")"""

       
        

client = MyClient()
client.run('OTMyMzA4Mzg4ODU4MjAwMTg1.YeRF2Q.llz0e-DaF1eTtRVGT5HoiTTL6J4')


"""cmd_args = message.content.split(" ")
        cmd = cmd_args[0]
        args = list()
        if len(cmd_args) > 1:
            args = cmd_args[1]

        if cmd == "!hello":
            await message.channel.send(args)
        elif cmd == "!ping":
            await message.channel.send("pong ")"""
