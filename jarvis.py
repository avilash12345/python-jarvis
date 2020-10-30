import pyttsx3
import datetime
import speech_recognition as sr
 #import pyaudio
 import wikipedia
import webbrowser
import os




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices[0].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening!")

	speak("I am Jarvis sir. please tell me how may i help you")	


def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone()==source:
		print("Listening.....")
		r.pause_threshold=1
		audio = r.listen(source)

	try:
		print("Recognizing.....")
		query = r.recognize_google(audio, language='en-in')
		print(f'User said:{query}\n')

	except Exception as e:
		#print(e)
		print('say that again please.....')
		return "None"
		return query



if __name__ == '__main__':
		#speak("hello lipan dogi good morning")	
		wishme()
		while True:
		    query = takeCommand().lower()
# logic jarvis command
            if 'wikipedia' in query:
            	speak('searching wikipedia...')
            	query = query.replace('wikipedia'.'')
            	results=wikipedia.summery(query, sentences=2)
            	speak("Accordind to wikipedia")
            	speak(results)
            	print(results)

            elif 'open youtube' in query:

                webbrowser.open("youtube.com")

            elif 'open google' in query:

                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:

                webbrowser.open("stackoverflow.com")        

            elif 'play music' in query:

                 music_dir="C:\\Users\\JHUNU777\\Music"  
                 songs = os.listdir(music_dir)  
                 print(songs)
                 os.startfile(os.path.join(music_dir,songs[0]))

            elif 'the time' in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is{strtime}")    