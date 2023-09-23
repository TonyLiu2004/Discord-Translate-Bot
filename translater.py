import googletrans
from googletrans import Translator
from googletrans import LANGUAGES

valid_languages = []
for code,name in LANGUAGES.items():
    valid_languages.append(code)
    valid_languages.append(name)

def translate(userInput,lang):
    translator = googletrans.Translator()
    user_input = userInput

    user_language = lang
    if user_language in valid_languages:
        return translator.translate(user_input, dest=user_language).text
    else:
        return "Please enter a valid language. Use list for a list of languages."

def list():
    translated = ""
    for code,name in LANGUAGES.items():
        translated += (f"{name}: {code}\n")
    return translated
