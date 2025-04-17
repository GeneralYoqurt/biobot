import lightbulb

def welcome_message(member, guild, channel) -> str:
    '''Message sended privately to the user'''
    message = (
        f"Cześć {member.mention} witamy...\n\n"
        "Ojej! Weryfikacja! Spokojnie, to nic strasznego. Raz dwa i będzie po wszystkim.\n"
        "Masz dwie opcje:\n"
        f"1. Przedstawić się na <#{channel.id}>\n"
        "2. Założyć ticket i odpowiedzieć na pytania"
    )
    return message