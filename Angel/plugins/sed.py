from .. import Raizen
from telethon import events, Button, client

Raizen_USER = [1801571739]

@Raizen.on(
    events.NewMessage(pattern="^/sed ?(.*)", func=lambda e: e.sender_id in Raizen_USER)
)
async def amdddd(event):
    text = event.pattern_match.group(1)
    k = [[Button.text(text)]]
    await Raizen.send_message(event.chat_id, "ʀᴀɪᴢᴇɴ 💝", buttons=k)
    
@Raizen.on(events.NewMessage(pattern="^/sed"))
async def start_all(event):
    if event.is_private:
        await event.reply("ᴜsᴇ ᴛʜɪs ᴄᴍᴅ ɪɴ ɢʀᴏᴜᴘ")
###################################################
@Raizen.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "ʜᴇʀᴇ ɪs ᴍʏ ᴍᴀsᴛᴇʀ ᴜsᴇʀɴᴀᴍᴇ  @DIPESH_XD")

#######################################################################################################################################
