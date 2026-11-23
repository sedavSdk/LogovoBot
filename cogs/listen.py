from discord.ext import commands
import configparser
import sys
sys.path.append("..")
from utils import doImage
import discord
from random import choice
from discord import app_commands

class CogListen(commands.Cog):
    def __init__(self, client):
        self.client = client
        config = configparser.ConfigParser()
        config.read('cogs.ini')

        self.leverId = config.getint('id', 'lever_id')

        self.systemId = config.getint('id', 'system_id')
        self.logovoId = config.getint('id', 'guild_id')
        self.poeId = config.getint('id', 'poe_channel_id')
        self.logovo = None
        self.system = None
        self.testId = config.getint('id', 'test_id')
        self.test = None
        self.poe = None


    @commands.command()
    async def setId(self, ctx, id : int):
        self.leverId = id
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.logovo = self.client.get_guild(self.logovoId)
        self.system = discord.utils.get(self.logovo.channels, id=self.systemId)
        self.test = discord.utils.get(self.logovo.channels, id=self.testId)
        self.poe = discord.utils.get(self.logovo.channels, id=self.poeId)
    
    @commands.Cog.listener()
    async def on_member_remove(self, mem):
        m=[" покинул нас...", " ушел и больше не вернулся", " нашел себе сервер получше", "съебал нахуй"]
        await self.system.send(content=f'{mem.name} {choice(m)}')
    
    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     if len(before.roles) < len(after.roles):
    #         new_role = next(role for role in after.roles if role not in before.roles)
    #         if new_role.name in ('Логовичанин'):

    #             url = after.avatar.url
    #             doImage(url)
    #             with open('результат.png', 'rb') as f:
    #                 picture = discord.File(f)
    #                 await self.test.send(file=picture)

    @app_commands.command(name="achive")
    @app_commands.choices(achive=[
    app_commands.Choice(name="Логовичанин", value="logovichanin"),
    app_commands.Choice(name="Донатер", value="gilda"),
    ])
    async def achive(self, interaction: discord.Interaction, user_name : str, achive : str):
        if "botMaster" in [role.name for role in interaction.user.roles] or interaction.user.name == "grokov":
            mem = discord.utils.get(self.logovo.members, name=user_name)
            if mem == None: 
                await interaction.response.send_message(content="Неправильный ник", ephemeral=True)
                return
            url = mem.avatar.url
            doImage(url, achive)
            with open('результат.png', 'rb') as f:
                picture = discord.File(f)
                await self.test.send(file=picture, content=f"{mem.mention}")
                await interaction.response.send_message(content="Сделано", ephemeral=True)
        else:
            await interaction.response.send_message(content="Права не имеешь!!!", ephemeral=True)

    @app_commands.command(name="secret_achive")
    async def s_achive(self, interaction: discord.Interaction, user_name : str, achive : str):
        if "botMaster" in [role.name for role in interaction.user.roles] or interaction.user.name == "grokov":
            mem = discord.utils.get(self.logovo.members, name=user_name)
            if mem == None: 
                await interaction.response.send_message(content="Неправильный ник", ephemeral=True)
                return
            url = mem.avatar.url
            doImage(url, achive)
            with open('результат.png', 'rb') as f:
                picture = discord.File(f)
                await self.test.send(file=picture, content=f"{mem.mention}")
                await interaction.response.send_message(content="Сделано", ephemeral=True)
        else:
            await interaction.response.send_message(content="Права не имеешь!!!", ephemeral=True)