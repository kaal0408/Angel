from .. import Angel
from telethon import events, Button
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

@Angel.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  Angel_PIC = "https://telegra.ph/file/0a85a39c40572d8266a06.mp4"
  but = [[Button.url("「𝐌𝐚𝐧𝐣𝐞𝐞𝐭」❤️🥀", "t.me/Hayat_Murat_30")]]
  pm_caption = "•**ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍʏ ᴍᴀsᴛᴇʀ**\n\n"
  pm_caption += "•**ᴍʏ sʏsᴛᴇᴍ ɪs ᴘᴇʀғᴇᴄᴛʟʏ ʀᴜɴɴɪɢ**\n\n"
  pm_caption += "• ᴀʙᴏᴜᴛ ᴍʏ sʏsᴛᴇᴍ ✗\n\n"
  pm_caption += "• 𝙎𝙈𝙀𝙓 𝙓 𝙑𝙀𝙍𝙎𝙄𝙊𝙉: 1.1\n"
  pm_caption += "• 𝙏𝙀𝙇𝙀𝙏𝙃𝙊𝙉 𝙑𝙀𝙍𝙎𝙄𝙊𝙉 ☞ {version.__version__}\n"
  pm_caption += (
        "• 𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔 ☞ [「𝐌𝐚𝐧𝐣𝐞𝐞𝐭」❤️🥀](t.me/Hayat_Murat_30)\n\n"
    )
  pm_caption += f"• 𝘾𝙍𝙀𝘼𝙏𝙊𝙍 ☞ [「𝐌𝐚𝐧𝐣𝐞𝐞𝐭」❤️🥀](t.me/Hayat_Murat_30)\n"
  await Angel.send_file(event. chat_id, file=Raizen_PIC, captions=pm_caption, buttons=but, link_preview=False)
