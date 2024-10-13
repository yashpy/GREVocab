import json
from translator import Translator
from interface import Interface
from model import Model

def find_by_word(word, vocab_list):
    for entry in vocab_list:
        if entry["word"].lower() == word.lower():
            return entry
    return None

def main():
    selectLanguage = Interface()
    lang = selectLanguage.get_user_language()
    translator = Translator(lang)
    
    input_word = selectLanguage.get_word()
    translated_word = translator.translate(input_word)
    print(f"Translated word: {translated_word}")

    model = Model()
    processed_output = model.query(translated_word)
    print(processed_output)

if __name__ == "__main__":
    main()