import discord
from discord.ext import commands
from decouple import Config, RepositoryEnv
import os, sys
import importlib
import configparser

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

config = configparser.ConfigParser()
config.read('cogs.ini')
MY_GUILD = discord.Object(id=config['id']['guild_id'])

class MyClient(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(command_prefix='/', intents=intents)
        self.module_files = [f for f in os.listdir("cogs") if f.endswith(".py")]
    
    async def create_class_instance(self, module_name):
        try:
            module = importlib.import_module(f"cogs.{module_name}")
            for name, obj in module.__dict__.items():
                if isinstance(obj, type):
                    print(f"Creating an instance of {name} from {module_name}.py:")
                    await self.add_cog(obj(self))
        except Exception as e:
            print(f"Error in {module_name}.py: {str(e)}")

    async def setup_hook(self):
        for module_file in self.module_files:
            module_name = os.path.splitext(module_file)[0] 
            await self.create_class_instance(module_name)
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

    
 
client = MyClient(intents=intents)


@client.event
async def on_ready():
     print("setup comleted")



config = Config(RepositoryEnv('.env'))
client.run(config('TOKEN'))