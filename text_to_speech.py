# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
from googletrans import Translator
# import Os module to start the audio file
import os 


mytext = input("Enter your text:")
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
   mytext_trans = translator.translate(mytext,dest='en')
   
elif myChoice == 2:
   language = 'fr'
   mytext_trans = translator.translate(mytext,dest='fr')
   
elif myChoice == 3:
   language = 'es'
   mytext_trans = translator.translate(mytext,dest='es')
    
   
elif myChoice == 4:
   exit()
      
myobj = gTTS(text=mytext_trans.text, lang=language, slow=False)
myobj.save("output.wav") 
# Play the converted file 
os.system("start output.wav") 

