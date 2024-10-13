import json

class Translator:
    def __init__(self, lang='en'):
        # Load translations from a JSON file
        self.translations = self.load_translations()
        self.lang = lang

    def load_translations(self):
        """Load translations from a JSON file."""
        try:
            with open('data/translations.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: translations.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")
            return []

    def translate(self, word):
        """Translate a given word to the specified language."""
        for entry in self.translations:
            if entry["word"].lower() == word.lower():
                # Check for a specific translation in the requested language
                if self.lang in entry["meaning"]["translations"]:
                    return entry["meaning"]["translations"][self.lang]
                # Return the English meaning if no specific translation is found
                return entry["meaning"].get("english", "Meaning not available.")
        
        return f"'{word}' not found in translations."  # Provide feedback if word is not found
