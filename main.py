import interactions

# A bot on Discord requires "intents." They help handle the computational burden and processing
# for specific data relative to a Gateway event or series.
# "ALL" is used as placeholder, but you should ideally only use those which you *need.*
intents = interactions.Intents.ALL

# The token is declared as a positional argument instead of being inputted through .start()
bot = interactions.Client("TOKEN HERE", intents=intents)

# This is a decorator that attaches onto asynchronous, callable signatures.
# The nomenclature is as follows: Gateway Event -> on_gateway_event.
# e.g. READY -> on_ready, MESSAGE_CREATE -> on_message_create

# Subsequently, on_ready may be called numerous times in the event the bot's connection to Discord
# must be reconnected, restarted or resumed. For a single-call action, please consider using on_start.
# Both of these special events will never require arguments. All other event handlers do.
@bot.event
async def on_ready():
    print("Bot is online!")


# Commanders are registered through this decorator. You may either explicitly perform the creation
# and registration of the application command through the decorator, or by modifying the name of the
# coroutine and argument signature.
@bot.command(
    name="copy",
    description="I will copy what you say!",
    options=[
        interactions.Option(
            type=interactions.OptionType.STRING,
            name="text",
            description="What you want me to say!",
            required=True,
        ),
    ],
)
async def copy(ctx: interactions.CommandContext, text: str):
    await ctx.send(text)

# interactions.py requires what's called a "runner call." This is the entry point to starting a bot connection.
# This *MUST* be at the EOF for contents.
bot.start()
