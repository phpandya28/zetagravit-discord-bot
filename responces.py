import random
def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello, Welcome to ZetaGravit, Write Help if you want any Help'

    if p_message == 'help':
        return '`Write following words you may need help of : Event, Quiz, Ping_Team`'

    if p_message == 'event':
        return 'Write word which you want help of : About_Event, Date, Time, Material'

    if p_message == 'about_event':
        return 'ZetaGravit is organising a Quiz competition where host will ask you quesions based on Space and Astronomy from content available on ZetaGravit website or social media account'

    if p_message == 'date':
        return 'Event is on 8th of July, 2023'

    if p_message == 'time':
        return 'Timings is not yet decided, we will inform you when it is decided'

    if p_message == 'material':
        return 'You can refer zetagravit website or social media account for quiz preparation'

    if p_message == 'ping_team':
        return '@The_Team'

    if p_message == 'quiz':
        return 'We will soon provide sample quiz on discord'

    if p_message == 'roll':
        return str(random.randint(1, 10000000000000000000))

    