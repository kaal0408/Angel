from .. import Raizen
from telethon import events, Button, client

RAIZEN_USER = [1801571739]

@Raizen.on(
    events.NewMessage(pattern="^/add ?(.*)", func=lambda e: e.sender_id in RAIZEN_USER)
)
async def _(event):
  text = event.pattern_match.group(1)
  k = [[Button.text(text)]]
  await Raizen.send_message(event.chat_id, f"ᴅᴏɴᴇ ʙɪᴛᴄʜ{text}")
  await event.reply("ғᴜᴄᴋ ᴏғ ʙɪᴛᴄʜ",
                    buttons=[
                        [Button.url("𝙼𝚢 𝙾𝚠𝚗𝚎𝚛", "t.me/DIPESH_XD")]
                    ])

########################################################################################################################################

                     
