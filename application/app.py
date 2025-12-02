from flask import Flask, render_template, request, jsonify
from application.ciphers import CipherEngine


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Cipher metadata
CIPHERS = {
    'caesar': {
        'name': 'Caesar Cipher',
        'description': 'The ancient shift cipher used by Julius Caesar himself. Each letter shifts by a fixed number.',
        'historical': 'Used by Julius Caesar in 58 BC to protect military messages.',
        'difficulty': 'Beginner'
    },
    'vigenere': {
        'name': 'Vigenère Cipher',
        'description': 'A polyalphabetic cipher using a keyword. Once considered unbreakable, the "le chiffre indéchiffrable".',
        'historical': 'Created in 1553, resisted breaking for 300 years.',
        'difficulty': 'Intermediate'
    },
    'atbash': {
        'name': 'Atbash Cipher',
        'description': 'Biblical cipher where A↔Z, B↔Y, reversing the alphabet. Featured in The Da Vinci Code.',
        'historical': 'Originally used for Hebrew alphabet, dates to 500 BC.',
        'difficulty': 'Beginner'
    },
    'morse': {
        'name': 'Morse Code',
        'description': 'Dots and dashes that revolutionized long-distance communication via telegraph.',
        'historical': 'Invented by Samuel Morse in 1836, saved countless lives.',
        'difficulty': 'Beginner'
    },
    'base64': {
        'name': 'Base64 Encoding',
        'description': 'Modern encoding used across the internet to safely transmit binary data as text.',
        'historical': 'Developed for MIME email protocol in 1987.',
        'difficulty': 'Intermediate'
    },
    'binary': {
        'name': 'Binary Code',
        'description': 'The fundamental language of computers. Every character becomes 1s and 0s.',
        'historical': 'Foundation of all digital computing since the 1940s.',
        'difficulty': 'Beginner'
    },
    'rot13': {
        'name': 'ROT13',
        'description': 'A special Caesar cipher with 13-letter shift. Its own inverse - encrypt twice to decrypt.',
        'historical': 'Used in Usenet forums to hide spoilers and puzzles.',
        'difficulty': 'Beginner'
    },
    'reverse': {
        'name': 'Reverse Cipher',
        'description': 'Simple but effective - write your message backwards. Leonardo da Vinci used this in his notebooks.',
        'historical': 'Da Vinci\'s mirror writing filled thousands of notebook pages.',
        'difficulty': 'Beginner'
    }
}

@app.route('/')
def index():
    return render_template('index.html', ciphers=CIPHERS)

@app.route('/cipher/<cipher_type>')
def cipher_page(cipher_type):
    if cipher_type not in CIPHERS:
        return "Cipher not found", 404
    return render_template('cipher.html', cipher_type=cipher_type, cipher_info=CIPHERS[cipher_type], all_ciphers=CIPHERS)

@app.route('/api/transform', methods=['POST'])
def transform():
    data = request.json
    cipher_type = data.get('cipher_type')
    text = data.get('text', '')
    operation = data.get('operation', 'encrypt')
    key = data.get('key', 'KEY')
    shift = int(data.get('shift', 3))
    
    engine = CipherEngine()
    result = ""
    
    try:
        if cipher_type == 'caesar':
            result = engine.caesar_encrypt(text, shift) if operation == 'encrypt' else engine.caesar_decrypt(text, shift)
        elif cipher_type == 'atbash':
            result = engine.atbash_transform(text)
        elif cipher_type == 'base64':
            result = engine.base64_encode(text) if operation == 'encrypt' else engine.base64_decode(text)
        elif cipher_type == 'reverse':
            result = engine.reverse_cipher(text)
        elif cipher_type == 'vigenere':
            result = engine.vigenere_encrypt(text, key) if operation == 'encrypt' else engine.vigenere_decrypt(text, key)
        elif cipher_type == 'rot13':
            result = engine.rot13_transform(text)
        elif cipher_type == 'morse':
            result = engine.morse_encode(text) if operation == 'encrypt' else engine.morse_decode(text)
        elif cipher_type == 'binary':
            result = engine.binary_encode(text) if operation == 'encrypt' else engine.binary_decode(text)
        
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)