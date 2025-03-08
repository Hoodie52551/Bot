import discord
from discord.ext import commands

TOKEN = 'MTMwNzg0MDk3NTM5Mjg3MDQ3Mg.Gy3Wbz.Ua4j006l6A3QMbEy6N_nI2szN5uwySq21h6Ls0'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

stock = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def stock(ctx, action, *, item=None):
    if action == 'add':
        if item:
            if item not in stock:
                stock[item] = 0
            stock[item] += 1
            await ctx.send(f'Added 1 {item} to stock. Current stock: {stock[item]}')
        else:
            await ctx.send('Please specify an item to add.')

    elif action == 'remove':
        if item:
            if item in stock and stock[item] > 0:
                stock[item] -= 1
                await ctx.send(f'Removed 1 {item} from stock. Current stock: {stock[item]}')
            elif item not in stock:
                await ctx.send(f'{item} is not in stock.')
            else:
                 await ctx.send(f'There are no {item} in stock.')
        else:
            await ctx.send('Please specify an item to remove.')

    elif action == 'list':
        if stock:
            stock_list = "\n".join(f"{item}: {count}" for item, count in stock.items())
            await ctx.send(f'Current Stock:\n{stock_list}')
        else:
            await ctx.send('The stock is empty.')
    elif action == 'new':
        if item:
            if item not in stock:
                stock[item] = 0
                await ctx.send(f"Created new stock item: {item}. Initial stock: 0")
            else:
                await ctx.send(f"{item} already exists in the stock.")
        else:
            await ctx.send("Please specify an item to create.")

    else:
        await ctx.send('Invalid stock action. Use /stock add <item>, /stock remove <item>, /stock list, or /stock new <item>.')

bot.run(TOKEN)
