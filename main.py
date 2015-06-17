import pyaudio
import speech_recognition as sr
import os

p = pyaudio.PyAudio()
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:                # use the default microphone as the audio source
		audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
	try:
		recognized_text = r.recognize(audio).lower()
		words = recognized_text.split(" ");
		print words
		print("You said: " + recognized_text)    # recognize speech using Google Speech Recognition	
		if "shut" in words and "down" in words and"please" in words:
			os.system('sudo shutdown -P now')  
		elif "go" in words and "the" in words and "web" in words:
			os.system('su teo -c google-chrome-stable')  
		elif "hello" in words and "jarvis" in words:
			os.system('play /home/teo/Documents/recognition/jarvissaluda.wav')  			
		elif "why" in words and "spanish" in words:
			os.system('play /home/teo/Documents/recognition/whyinspanish.wav')  			
	except LookupError:                            # speech is unintelligible
	    print("Could not understand audio")