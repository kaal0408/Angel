from .. import Angel
from telethon import events, Button
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

@Angel.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  Angel_PIC = "https://telegra.ph/file/0a85a39c40572d8266a06.mp4"
  but = [[Button.url("ãððð§ð£ððð­ãâ¤ï¸ð¥", "t.me/Hayat_Murat_30")]]
  pm_caption = "â¢**Éª á´á´ á´ÊÉªá´ á´ á´Ê á´á´sá´á´Ê**\n\n"
  pm_caption += "â¢**á´Ê sÊsá´á´á´ Éªs á´á´ÊÒá´á´á´ÊÊ Êá´É´É´ÉªÉ¢**\n\n"
  pm_caption += "â¢ á´Êá´á´á´ á´Ê sÊsá´á´á´ â\n\n"
  pm_caption += "â¢ ðððð ð ððððððð: 1.1\n"
  pm_caption += "â¢ ðððððððð ððððððð â {version.__version__}\n"
  pm_caption += (
        "â¢ ð¾ðððððððð ð½ð â [ãððð§ð£ððð­ãâ¤ï¸ð¥](t.me/Hayat_Murat_30)\n\n"
    )
  pm_caption += f"â¢ ð¾ððð¼ððð â [ãððð§ð£ððð­ãâ¤ï¸ð¥](t.me/Hayat_Murat_30)\n"
  await Angel.send_file(event. chat_id, file=Angel_PIC, captions=pm_caption, buttons=but, link_preview=False)
