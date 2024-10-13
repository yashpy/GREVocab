import json

class Translator:
    def __init__(self, lang='en'):
        with open('data/translations.json', 'r') as file:
            self.translations = json.load(file)
        self.lang = lang

    def translate(self, word):
        # Iterate through the list of words in the translations
        for entry in self.translations:
            if entry["word"].lower() == word.lower():
                # Return the translation if found
                if self.lang in entry["meaning"]["translations"]:
                    return entry["meaning"]["translations"][self.lang]
                # If no specific translation, return the English meaning
                return entry["meaning"]["english"]
        return word  # Return the word if no translation is found