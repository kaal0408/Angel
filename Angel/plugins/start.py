# By < @DIPESH_XD >
# // @Raizen //
from .. import Raizen
from telethon import events, custom, Button
Raizen_PIC = "https://telegra.ph/file/6010d4c56c0fc40654caa.mp4"
@Raizen.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await Raizen.send_file(event.chat_id,
                                  Raizen_PIC,
                                  caption=f"нεℓℓσ vяσ!!\n ι αм ρεяsσηαℓ αssιsтαηт σғ [𝘿𝙄𝙋𝙀𝙎𝙃](https://t.me/DIPESH_XD)",
                                  buttons=[
                                      (Button.inline(
                                          "ρℓυgιηs",
                                          data="mhelp"))]
                                  )

@Raizen.on(events.callbackquery.CallbackQuery(data="creator"))
async def creator(event):
    await event.edit(event.chat_id, "нεяε ιs мү мαsтεя υsεяηαмε @DIPESH_XD", show_alert=True)

########################################################################################################################################


@Raizen.on(events.callbackquery.CallbackQuery(data="mhelp"))
async def ommmmk(event):
    await event.edit("нεℓρ мεηυ",
                    buttons=[
                        [Button.inline("мαsтεя тσσℓs", data="ots")],
                        [Button.inline("тσσℓs", data="mhelpk")]
                    ])
                     
@Raizen.on(events.callbackquery.CallbackQuery(data="ots"))
async def oppppppppp(event):
    await event.edit("•/sed ғσя sε∂ ℓүғ.\n•/stop тσ sтσρ sε∂ ℓүғ.\n•/alive тσ cнεcк вσт ιs αℓιvε σя ησт.")

@Raizen.on(events.callbackquery.CallbackQuery(data="mhelpk"))
async def oooooookk(event):
    await event.edit("cσмιηg sσση💝")
           
