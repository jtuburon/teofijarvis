import pyaudio
import speech_recognition as sr
import os

p = pyaudio.PyAudio()
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		recognized_text = r.recognize(audio).lower()
		words = recognized_text.split(" ");
		print words
		print("You said: " + recognized_text)
		if "shut" in words and "down" in words and"please" in words:
			os.system('sudo shutdown -P now')  
		elif "go" in words and "the" in words and "web" in words:
			os.system('su teo -c google-chrome-stable')  
		elif "hello" in words and "jarvis" in words:
			os.system('play jarvissaluda.wav')  			
		elif "why" in words and "spanish" in words:
			os.system('play whyinspanish.wav')  			
	except LookupError:
	    print("Could not understand audio")