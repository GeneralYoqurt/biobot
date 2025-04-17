import lightbulb
import hikari
import miru

def verification_message(member, guild, channel, content) -> str:
    '''Logging message on a channel for mods'''
    message = (
        f'Wysłano wiadomość na kanale <#{channel.id}>.\n\n'
        f'{member.mention}: {content.content}\n'
    )

    
    button_verifi_accept = hikari.ButtonComponent(
        style=hikari.ButtonStyle.SUCCESS,   # Styl przycisku (PRIMARY, SECONDARY, SUCCESS, DANGER, LINK)
        label="Akceptuj",                # Tekst przycisku
        custom_id="button__verifi_accept",     # Unikalny identyfikator, który będzie używany do rozróżnienia przycisków
        is_disabled=False,  # Czy przycisk jest wyłączony (True) czy aktywny (False)
        emoji=hikari.Emoji.parse("<:accept:123456789012345678>"),  # Emoji do wyświetlenia na przycisku
        url=None,
        type=hikari.ComponentType.BUTTON  # Typ komponentu (BUTTON, SELECT_MENU, ACTION_ROW, itp.)
    )
    button_verifi_deny = hikari.ButtonComponent(
        style=hikari.ButtonStyle.DANGER,   # Styl przycisku (PRIMARY, SECONDARY, SUCCESS, DANGER, LINK)
        label="Odrzuć",                # Tekst przycisku
        custom_id="button__verifi_deny",     # Unikalny identyfikator, który będzie używany do rozróżnienia przycisków
        is_disabled=False,  # Czy przycisk jest wyłączony (True) czy aktywny (False)
        emoji=hikari.Emoji.parse("<:deny:123456789012345678>"),  # Emoji do wyświetlenia na przycisku
        url=None,
        type=hikari.ComponentType.BUTTON  # Typ komponentu (BUTTON, SELECT_MENU, ACTION_ROW, itp.)
    )
    button_verifi_delete = hikari.ButtonComponent(
        style=hikari.ButtonStyle.SECONDARY,   # Styl przycisku (PRIMARY, SECONDARY, SUCCESS, DANGER, LINK)
        label="Usuń",                # Tekst przycisku
        custom_id="button__verifi_delete",     # Unikalny identyfikator, który będzie używany do rozróżnienia przycisków
        is_disabled=False,  # Czy przycisk jest wyłączony (True) czy aktywny (False)
        emoji=hikari.Emoji.parse("<:delete:123456789012345678>"),  # Emoji do wyświetlenia na przycisku
        url=None,
        type=hikari.ComponentType.BUTTON  # Typ komponentu (BUTTON, SELECT_MENU, ACTION_ROW, itp.)
    )
    components = hikari.ActionRowComponent(components=[button_verifi_accept, button_verifi_deny, button_verifi_delete], type=hikari.ComponentType.ACTION_ROW)
    return message


class AcceptButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SUCCESS, label="Akceptuj", emoji="✅")
        self.value = "accept"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        for item in self.view.children:  # iterujemy po wszystkich przyciskach w widoku
            item.disabled = True
        await ctx.edit_response(components=self.view.build())
        self.view.stop()


class DenyButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.DANGER, label="Odrzuć", emoji="🚫")
        self.value = "deny"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        for item in self.view.children:
            item.disabled = True
        await ctx.edit_response(components=self.view.build())
        self.view.stop()


class DeleteButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SECONDARY, label="Usuń", emoji="🗑️")
        self.value = "delete"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        for item in self.view.children:
            item.disabled = True
        await ctx.edit_response(components=self.view.build())
        self.view.stop()


class VerificationView(miru.View):
    accept = AcceptButton()
    deny = DenyButton()
    delete = DeleteButton()

    def __init__(self) -> None:
        super().__init__()
        self.answer: str | None = None