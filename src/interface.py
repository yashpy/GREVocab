class Interface:
    def get_user_language(self):
        lang = input("Enter your preferred language (Spanish/French/German): ")
        return lang

    def get_word(self):
        return input("Enter a word to translate: ")