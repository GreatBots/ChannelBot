from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**👋 Hey {},**

**💭 Welcome to {},** You can use me to manage channels with tons of features. Use below buttons to learn more.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Add Me To Your Channel", url="https://t.me/ChannelActionBot?start=group")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("About 🛡", callback_data="about")
        ],
        [InlineKeyboardButton("📣 Channel", url="https://t.me/MyOwnBots")],
        [InlineKeyboardButton("🗯 Support", url="https://t.me/DevsChats")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

**Available Commands ❓**

/about - About The Bot
/help - This Message
/start - Start the Bot

**Alternative Commands:**

/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

Channel : [Support](https://devschats.t.me)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Credits : [Thanks](https://graph.org/Credits-Of-ChannelActionBot-02-23)
          """
