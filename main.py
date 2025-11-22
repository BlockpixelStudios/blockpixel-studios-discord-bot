import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configuração dos intents
intents = discord.Intents.all()

# Criação do bot
bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

# Evento quando o bot fica online
@bot.event
async def on_ready():
    print(f'╔═══════════════════════════════════════╗')
    print(f'║  Blockpixel Studios Bot está Online!  ║')
    print(f'╚═══════════════════════════════════════╝')
    print(f'Bot: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'Servidores: {len(bot.guilds)}')
    print(f'═══════════════════════════════════════')
    
    # Status do bot
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="BOT oficial da Blockpixel Studios ♥️"
        ),
        status=discord.Status.online
    )
    
    # Carrega todos os cogs
    await load_cogs()

async def load_cogs():
    """Carrega todos os módulos (cogs) do bot"""
    cogs = [
        'cogs.info',
        'cogs.tickets',
        'cogs.moderation',
        'cogs.giveaways',
        'cogs.events',
        'cogs.verification'
    ]
    
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f'✅ {cog} carregado com sucesso!')
        except Exception as e:
            print(f'❌ Erro ao carregar {cog}: {e}')

# Comando de recarregar cogs (apenas para administradores)
@bot.command(name='reload')
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    try:
        await bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'✅ Módulo `{extension}` recarregado!')
    except Exception as e:
        await ctx.send(f'❌ Erro ao recarregar: {e}')

# Handler de erros global
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="❌ Sem Permissão",
            description="Você não tem permissão para usar este comando!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed, delete_after=5)
    
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="❌ Argumentos Faltando",
            description="Você esqueceu de fornecer alguns argumentos! Use `/ajuda` para mais informações.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed, delete_after=5)
    
    elif isinstance(error, commands.CommandNotFound):
        pass  # Ignora comandos não encontrados
    
    else:
        print(f'Erro não tratado: {error}')

# Inicia o bot
if __name__ == '__main__':
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f'❌ Erro ao iniciar o bot: {e}')
