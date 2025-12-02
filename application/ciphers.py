import base64

class CipherEngine:
    
    @staticmethod
    def caesar_encrypt(text, shift=3):
        """
        Caesar Cipher Encryption
        Shifts each letter by a fixed number of positions.
        """
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    @staticmethod
    def caesar_decrypt(text, shift=3):
        """Caesar Cipher Decryption"""
        return CipherEngine.caesar_encrypt(text, -shift)
    
    @staticmethod
    def atbash_transform(text):
        """
        Atbash Cipher - reverses the alphabet
        A↔Z, B↔Y, C↔X, etc.
        """
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr(90 - (ord(char) - 65))
                else:
                    result += chr(122 - (ord(char) - 97))
            else:
                result += char
        return result
    
    @staticmethod
    def base64_encode(text):
        """Base64 Encoding"""
        return base64.b64encode(text.encode()).decode()
    
    @staticmethod
    def base64_decode(text):
        """Base64 Decoding"""
        try:
            return base64.b64decode(text.encode()).decode()
        except Exception:
            return "Invalid Base64 string"
    
    @staticmethod
    def reverse_cipher(text):
        """Reverse Cipher - mirrors the text"""
        return text[::-1]
    
    @staticmethod
    def vigenere_encrypt(text, keyword="KEY"):
        """
        Vigenère Cipher Encryption
        Uses a keyword to create a polyalphabetic substitution.
        """
        result = ""
        keyword = keyword.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(keyword[key_index % len(keyword)]) - 65
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        return result
    
    @staticmethod
    def vigenere_decrypt(text, keyword="KEY"):
        """Vigenère Cipher Decryption"""
        result = ""
        keyword = keyword.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(keyword[key_index % len(keyword)]) - 65
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                key_index += 1
            else:
                result += char
        return result
    
    @staticmethod
    def rot13_transform(text):
        """ROT13 - Special case of Caesar cipher with shift of 13"""
        return CipherEngine.caesar_encrypt(text, 13)
    
    @staticmethod
    def morse_encode(text):
        """
        Morse Code Encoding
        Converts text to dots and dashes.
        """
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }
        return ' '.join(morse_dict.get(char.upper(), char) for char in text)
    
    @staticmethod
    def morse_decode(morse):
        """Morse Code Decoding"""
        morse_dict_rev = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
            '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
            '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
            '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
            '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9', '/': ' '
        }
        return ''.join(morse_dict_rev.get(code, '') for code in morse.split())
    
    @staticmethod
    def binary_encode(text):
        """Binary Encoding - converts text to 1s and 0s"""
        return ' '.join(format(ord(char), '08b') for char in text)
    
    @staticmethod
    def binary_decode(binary):
        """Binary Decoding"""
        try:
            return ''.join(chr(int(b, 2)) for b in binary.split())
        except Exception:
            return "Invalid binary string"