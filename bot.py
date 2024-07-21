import json
import nextcord
from nextcord.ext import commands

from handlers.message_handler import handle_message
from handlers.slash_commands import register_slash_commands

from utils.languages import init as langs_init
import utils.sql as db

langs_init()
db.init()

intents = nextcord.Intents.default()
intents.message_content = True

def load_config():
    with open("config/config.json", "r") as f:
        return json.load(f)

config = load_config()


bot = commands.Bot(command_prefix=config['default-prefix'], intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    
    await handle_message(bot, message)

register_slash_commands(bot)

if config.get('production', False) == True:
    bot.run(config['tokens']['main'])
else:
    bot.run(config['tokens']['test'])