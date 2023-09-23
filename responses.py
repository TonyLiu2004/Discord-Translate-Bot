import random
import translater

def getResponse(message: str) -> str:
    p_message = message.lower()

    if(p_message == '~hello'):
        return "Hello there!"
    
    if(p_message == '~roll'):
        return str(random.randint(1,6))

    if(p_message == '~help'):
        return '`HELP!`'

    if(p_message.startswith("~translate")):
        args = p_message.split()[1:]
        lang = args[0]
        user_input = ' '.join(args[1:])
        return translater.translate(user_input,lang)
    
    #return "idk man"