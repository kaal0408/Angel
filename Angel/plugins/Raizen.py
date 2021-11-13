from .. import Angel
from telethon import events, Button, client

ANGEL_USER = [2101760006]

@Angel.on(
    events.NewMessage(pattern="^/add ?(.*)", func=lambda e: e.sender_id in ANGEl_USER)
)
async def _(event):
  text = event.pattern_match.group(1)
  k = [[Button.text(text)]]
  await Angel.send_message(event.chat_id, f"ᴅᴏɴᴇ ʙɪᴛᴄʜ{text}")
  await event.reply("𝐫 𝐮 𝐜𝐫𝐚𝐳𝐲",
                    buttons=[
                        [Button.url("𝙼𝚢 𝙾𝚠𝚗𝚎𝚛", "t.me/Hayat_Murat_30")]
                    ])

########################################################################################################################################

                     
