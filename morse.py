import kivy
import RPi.GPIO as GPIO
import logging
import time

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import Label

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  # GPIO 18
GPIO.output(12, GPIO.LOW)

COUNT = 0.5

LETTERS = {
    'a': '.-',
    'b': '-...', 
    'c': '-.-.', 
    'd': '-..', 
    'e': '.', 
    'f': '..-.', 
    'g': '--.', 
    'h': '....', 
    'i': '..', 
    'j': '.---', 
    'k': '-.-', 
    'l': '.-..', 
    'm': '--', 
    'n': '-.', 
    'o': '---', 
    'p': '.--.', 
    'q': '--.-', 
    'r': '.-.', 
    's': '...', 
    't': '-', 
    'u': '..-', 
    'v': '...-', 
    'w': '.--', 
    'x': '-..-', 
    'y': '-.--', 
    'z': '--..', 
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.', 
}

class TextInput():
    def on_text(self):
        logging.error("f")

class Morse(RelativeLayout):
    pass

class MorseApp(App):
    def build(self):
        GPIO.output(12, GPIO.HIGH)
        time.sleep(3 * COUNT)
        GPIO.output(12, GPIO.LOW)
        return Morse()
    
    def morse_lights(self):
        text = self.root.ids.textInput.text
        letters = list(text)
        logging.warning(letters)
        for letter in letters:
            if letter.lower() in LETTERS.keys():
                morse_letter = LETTERS[letter.lower()]
                self.morse_output(morse_letter)
            else:
                # Every non letter or number treated as a space.
                time.sleep(4 * COUNT) # Extra 4 count to make a 7 count between each word.
            time.sleep(2 * COUNT) # 3 count between each letter - need an extra 2
                
    def morse_output(self, letter):
        logging.info(letter)
        ds = list(letter)
        for d in ds:
            if d == '.':
                GPIO.output(12, GPIO.HIGH)
                time.sleep(COUNT)
            if d == '-':
                GPIO.output(12, GPIO.HIGH)
                time.sleep(3 * COUNT)
            GPIO.output(12, GPIO.LOW)
            time.sleep(COUNT)
        logging.warning("finished letter")
        
    def count_letters(self):
        text = self.root.ids.textInput.text
        if len(text) > 12:
            self.root.ids.textInput.text = ''.join(list(text)[:12])

            
morse = MorseApp()
morse.run()

GPIO.cleanup()
