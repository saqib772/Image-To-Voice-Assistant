from PIL import Image
import pytesseract
from googletrans import Translator
from gtts import gTTS
import os

def image_to_text(image_file):
    text = pytesseract.image_to_string(Image.open(image_file))
    return text
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text
def text_to_speech(text, filename):
    tts = gTTS(text, lang='en')
    tts.save(filename)
image_file = 'image.png'
target_language = 'es'
translated_text_file = 'translated_text.txt'
speech_file = 'speech.mp3'

# Extract text from image
text = image_to_text(image_file)

# Translate text
translated_text = translate_text(text, target_language)

# Save translated text to file
with open(translated_text_file, 'w') as f:
    f.write(translated_text)

# Convert text to speech
text_to_speech(translated_text, speech_file)

# Play speech
os.system('start ' + speech_file)
