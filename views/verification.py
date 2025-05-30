import lightbulb
import hikari
import miru

def verification_message(member, guild, channel, content) -> str:
    '''Logging message on a channel for mods'''
    message = (
        f'Wysłano wiadomość na kanale <#{channel.id}>.\n\n'
        f'{member.mention}: {content.content}\n'
    )
    return message


class AcceptButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SUCCESS, label="Akceptuj", emoji="✅")
        self.value = "accept"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        await ctx.respond(content=f"**Użytkownik został zaakceptowany.**", delete_after=5)
        self.view.stop()


class DenyButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.DANGER, label="Odrzuć", emoji="🚫")
        self.value = "deny"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        await ctx.respond(content=f"**Użytkownik został odrzucony.**", delete_after=5)
        self.view.stop()


class DeleteButton(miru.Button):
    def __init__(self) -> None:
        super().__init__(style=hikari.ButtonStyle.SECONDARY, label="Usuń", emoji="🗑️")
        self.value = "delete"

    async def callback(self, ctx: miru.ViewContext) -> None:
        self.view.answer = self.value
        await ctx.respond(content=f"**Wiadomość została usunięta.**", delete_after=5)
        self.view.stop()


class VerificationView(miru.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)  # No timeout for the view
        self.answer: str | None = None
        # Add the buttons to the view in the constructor
        self.add_item(AcceptButton())
        self.add_item(DenyButton())
        self.add_item(DeleteButton())