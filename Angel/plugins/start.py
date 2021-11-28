# By < @DIPESH_XD >
# // @Raizen //
import re
from .. import Angel
from telethon import events, custom, Button
Angel_PIC = "https://telegra.ph/file/0a85a39c40572d8266a06.mp4"
@Angel.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Angel.send_file(event.chat_id,
                                  Angel_PIC,
                                  caption=f"нεℓℓσ vяσ!!\n ι αм ρεяsσηαℓ αssιsтαηт σғ [Hayat_Murat](https://t.me/status_galery_30)",
                                  buttons=[
                                      (Button.inline(
                                          "ρℓυgιηs",
                                          data="mhelp"))]
                                  )

@Angel.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "нεяε ιs мү мαsтεя υsεяηαмε @Hayat_Murat_30", show_alert=True)

########################################################################################################################################


@Angel.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    await event.edit("нεℓρ мεηυ",
                    buttons=[
                        [Button.inline("мαsтεя тσσℓs", data="ots")],
                        [Button.inline("тσσℓs", data="mhelpk")]
                    ])
                     
@Angel.on(events.callbackquery.CallbackQuery(data="ots"))
async def oppppppppp(event):
    await event.edit("•/sed ғσя sε∂ ℓүғ.\n•/stop тσ sтσρ sε∂ ℓүғ.\n•/alive тσ cнεcк вσт ιs αℓιvε σя ησт.")

@Angel.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("cσмιηg sσση💝")
           
