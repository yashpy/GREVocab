from flask import Flask, app, jsonify, request
from translator import Translator
from interface import Interface
from model import Model

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def main():
    lang = request.json.get('language')
    translator = Translator(lang)
    input_word = request.json.get('input_word')
    
    # Translate the input word
    translated_word = translator.translate(input_word)
    
    # Create an instance of the Model class to process the translated word
    model = Model()
    
    # Query the model with the translated word
    processed_output = model.query(translated_word)
    
    # Return the processed output as a JSON response
    return jsonify({
        'translated_word': translated_word,
        'processed_output': processed_output
    })

if __name__ == "__main__":
    app.run(debug=True, port=3000)