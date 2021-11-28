from .. import Angel
from telethon import events, Button, client

Angel_USER = [2068551800]

@Angel.on(
    events.NewMessage(pattern="^/sed ?(.*)", func=lambda e: e.sender_id in Angel_USER)
)
async def amdddd(event):
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await Angel.send_message(event.chat_id, "Angel 💝", buttons=k)
    
@Angel.on(events.NewMessage(pattern="^/sed"))
async def start_all(event):
    if event.is_private:
        await event.reply("ᴜsᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ")
###################################################
@Angel.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "ʜᴇʀᴇ ɪs ᴍʏ ᴍᴀsᴛᴇʀ ᴜsᴇʀɴᴀᴍᴇ  @Hayat_Murat_30")

#######################################################################################################################################
