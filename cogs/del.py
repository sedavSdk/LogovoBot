from discord.ext import commands
from discord import app_commands
import datetime
import configparser
import sys
sys.path.append("..")
from utils import doImage
import discord
from random import choice

class CogDel(commands.Cog):
    def __init__(self, client):
        self.client = client
        config = configparser.ConfigParser()
        config.read('cogs.ini')
    
    @app_commands.command(name="delete", description='Удаляет сообщения в канале')
    @app_commands.describe(count="Сколько удалять")
    async def delete(self, interaction: discord.Interaction, count : int = 10):
        if "botMaster" in [role.name for role in interaction.user.roles]:
            await interaction.response.send_message(content="удалено", ephemeral=True)
            await interaction.channel.purge(limit=count)
        else:
            await interaction.response.send_message(content="Права не имеешь!!!", ephemeral=True)
        
