# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
from googletrans import Translator
# import Os module to start the audio file
import os 

fh = open("text.txt", "r")
myText = fh.read().replace("\n", " ")

translator = Translator()

# Language we want to use 
print("1 = English")
print("2 = French")
print("3 = Spanish")
print("4 = Exit")
print()
myChoice = int(input("Enter your choice: "))
if myChoice == 1:
   language = 'en'
   myText_trans = translator.translate(myText,dest='en')
   
elif myChoice == 2:
   language = 'fr'
   myText_trans = translator.translate(myText,dest='fr')
   
elif myChoice == 3:
   language = 'es'
   myText_trans = translator.translate(myText,dest='es')
    
   
elif myChoice == 4:
   exit()

output = gTTS(text=myText_trans.text, lang=language, slow=False)
output.save("output.wav")
fh.close()

# Play the converted file 
os.system("start output.wav")

