import interactions

intents = interactions.Intents.ALL
bot = interactions.Client("TOKEN HERE", intents=intents)

@bot.event
async def on_ready():
    print("Bot is online!")


@bot.command(name="copy",
    description="I will copy what you say!",
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name= "text",
            description= "What you want me to say!",
            required=True
        )
    ]
    )
async def copy(ctx: interactions.CommandContext, text: str):
    channel = ctx.channel
    await channel.send(f"{text}")    
    message = await ctx.send("** **")
    await message.delete()


bot.start()
