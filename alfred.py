# Importing necessary modules
import pyttsx3  # Fpr speaking functionality
import speech_recognition as sr  # To recognize user's voice
import datetime as dt  # To know date and time
import sounddevice as sd  # To remove audio errors
import wikipedia  # For fetching info from Wikipedia
import webbrowser as web  # For opening websites
import os  # For opening desktop files and applications
import sys  # For cross-platform functionalities
import subprocess  # To spawn new processes
import pywhatkit as pw  # For some specific functionalities like google search
import pyjokes  # For fetching jokes
import requests # For sending HTTP requests
import wolframalpha # For geopraphical, computational or GK questions
import random # For playing a random song from Music directory
import pyautogui # For taking screenshot
from bs4 import BeautifulSoup # For pulling news out of news website


# Setting the voice using Pyttsx3 and Espeak
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)


# Speak Function using Pyttsx3
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Wish Function
def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Alfred, at your service!")
    speak("I am Alfred, at your service!")


# Function for commanding Alfred using SpeechRecognition
def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        query = listener.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry, say that again please!")
        speak("Sorry, say that again please!")
        return "None"

    return query


# Note taking fucntion
def note(text):
    date = dt.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["/usr/bin/mousepad", file_name])


# Game playing Function
def game():

    print("Okay, I challenge you to a game of Rock-Paper-Scissor!")
    speak("Okay, I challenge you to a game of Rock-Paper-Scissor!")

    # Validation function
    def validate(hand):
        if hand < 0 or hand > 2:
            return False
        return True

    # Hand function
    def printHand(hand, name = 'Guest'):
        hands = ['Rock', 'Paper', 'Scissor']
        print(name + ' picked: ' + hands[hand])
        speak(name + 'picked' + hands[hand])

    # Judging function
    def judge(player, alfred):

        # Add control flow based on the comparison of player and computer
        if player == alfred:
            return 'It is a tie. You may try Again.'
        elif player == 0 and alfred == 1:
            return 'You lose. Better luck next time.'
        elif player == 1 and alfred == 2:
            return 'You lose. Better luck next time.'
        elif player == 2 and alfred == 0:
            return 'You lose. Better luck next time.'
        else:
            return 'Congratulations. You have won.'

    print('--- Starting the Rock-Paper-Scissor Game ---')
    speak('Starting the Rock Paper Scissor Game')
    speak('Please enter your name')
    playerName = takeCommand()

    print('Pick a hand: (0: Rock, 1: Paper, 2: Scissor)')
    speak("Pick a hand. Press 0 for Rock, 1 for Paper and 2 for Scissor.")
    speak("Please enter a number between 0 and 2.")
    playerHand = int(input('Please enter a number between 0 and 2: '))

    if validate(playerHand):
        alfredHand = random.randint(0,2)

        printHand(playerHand, playerName)
        printHand(alfredHand, 'Alfred')

        # Assign the return value of judge to the result variable
        result = judge(playerHand, alfredHand)

        # Print the result variable
        print(result)
        speak(result)

    else:
        print('Invalid Number...')
        speak("Invalid Number")


# Functionalities of Alfred
def runAlfred():
    print("Tell me how can I help you...")
    speak("Tell me how can I help you.")
    query = takeCommand().lower()

    # Identity
    if 'who are you' in query:
        print("I am Alfred, your personal assistant! As of now, I am programmed to open a few websites, play music from your device, play songs on YouTube, search on Google, fetch info from Wikipedia, give you the present time, enlighten you on the current weather conditions around the world, read out today's news headlines from BBC, answer some geographical as well as computational questions, locate places in Google Maps, take screenshots, save your notes, play Rock-Paper-Scissor with you and entertain you with one-liner jokes.")

        speak("I am Alfred, your personal assistant! As of now, I am programmed to open a few websites, play music from your device, play songs on YouTube, search on Google, fetch info from Wikipedia, give you the present time, enlighten you on the current weather conditions around the world, read out today's news headlines from BBC, answer some geographical as well as computational questions, locate places in Google Maps, take screenshots, save your notes, play Rock Paper Scissor with you and entertain you with one-liner jokes.")

    # Logic for executing tasks based on query

    # Fetch info from Wikipedia
    elif 'wikipedia' in query:
        speak('Searching Wkipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2, auto_suggest=False)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    # To take notes
    elif 'take note' in query:
        print("What should I note?")
        speak("What should I note?")
        strNote = takeCommand()
        note(strNote) # Calling the note taking fucntion defined earlier
        print("Your words have been noted.")
        speak("Your words have been noted.")

    # Browser actions using WebBrowser
    elif 'open youtube' in query:
        web.open('youtube.com')

    elif 'open google' in query:
        web.open('google.com')

    elif 'open whatsapp' in query:
        web.open('web.whatsapp.com')

    elif 'open reddit' in query:
        web.open('reddit.com')

    elif 'open spotify' in query:
        web.open('open.spotify.com')

    elif 'open telegram' in query:
        web.open('web.telegram.org')

    elif 'open colab' in query:
        web.open('colab.research.google.com')

    elif 'open mail' in query:
        web.open('mail.google.com')

    elif 'open facebook' in query:
        web.open('facebook.com')

    elif 'open linkedin' in query:
        web.open('linkedin.com')

    elif 'open drive' in query:
        web.open('drive.google.com')
    
    elif 'open github' in query:
        web.open('github.com')

    elif 'twitter' in query:
        web.open('twitter.com')

    elif 'canva' in query:
        web.open('canva.com')

    elif 'open keep' in query:
        web.open('keep.google.com')

    elif 'open meet' in query:
        web.open('meet.google.com')

    elif 'open map' in query or 'open maps' in query:
        web.open('maps.google.com')

    elif 'open code' in query:
        web.open('onlinegdb.com')

    # Locate a place in Google Maps using WebBrowser
    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        print("Locating" + location + " " + "in Google Maps")
        speak("Locating" + location + " " + "in Google Maps")
        web.open("https://www.google.co.in/maps/place/" + location + "")

    # Playing a particular song on YouTube using PyWhatKit
    elif 'play song' in query:
        song = query.replace('play', '')
        print('Playing' + song)
        speak('Playing' + song)
        pw.playonyt(song)

    # Google Search using PyWhatKit
    elif 'search' in query:
        strSearch = query.replace('search', '')
        print('Searching on Google...')
        speak('Searching on Google!')
        pw.search(strSearch)

    # OS actions
    elif 'play music' in query:
        music_dir = '/home/noobchirag69/Music'
        songs = os.listdir(music_dir)
        num = random.randint(0, len(songs))
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        print('Playing music from the Music directory...')
        speak('Playing music from the Music directory...')
        subprocess.call([opener, os.path.join(music_dir, songs[num])])

    # Time using DateTime
    elif 'the time' in query:
        strTime = dt.datetime.now().strftime("%I:%M %p")
        print(f"The time is {strTime}\n")
        speak(f"The time is {strTime}\n")

    # Jokes using PyJokes
    elif 'joke' in query:
        print(pyjokes.get_joke())
        speak(pyjokes.get_joke())

    # For fetching News using Requests and BeautifulSoup
    elif 'news' in query:
        url = 'https://www.bbc.com/news'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')[:6]
        unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']
        
        print("According to BBC...")
        speak("According to BBC")
        
        for m in list(dict.fromkeys(headlines)):
            if m.text.strip() not in unwanted:
                print(m.text.strip())
                speak(m.text.strip())

    # For questions
    elif 'ask' in query:
        print('Please ask your question. I will try my best to answer.')
        speak('Please ask your question. I will try my best to answer.')
    
    # For computational questions
    elif 'calculate' in query:
        app_id = "L4YQ8E-PL486JPL4L"
        client = wolframalpha.Client('L4YQ8E-PL486JPL4L')
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print(answer)
        speak(answer)

    # For Geographical questions
    elif 'what is' in query or 'who is' in query:
        app_id = "L4YQ8E-PL486JPL4L"
        client = wolframalpha.Client('L4YQ8E-PL486JPL4L')
        res = client.query(query)
        answer = next(res.results).text

        try:
            print(answer)
            speak(answer)
        except Exception as e:
            print("Sorry, No results!")
            speak("Sorry, no results!")

    # Taking Screenshot
    elif 'screenshot' in query:
        screen = pyautogui.screenshot()
        imageName = str(dt.datetime.now()).replace(":", "-") + "-image.png"
        screen.save(imageName)
        print('Screenshot has been taken.')
        speak('Screenshot has been taken.')

    # Weather
    elif 'weather' in query:
        api_key = "60e6a50272af81d3cffa81bc0dadf7f9"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        print('Please mention the city.')
        speak('Please mention the city.')
        city = takeCommand()
        complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
        api_link = requests.get(complete_url)
        api_data = api_link.json()
        degreeSign = u"\N{DEGREE SIGN}"

        if api_data["cod"] != "404":
            temperature = ((api_data['main']['temp']))
            weatherDescription = api_data['weather'][0]['description']
            humidity = api_data['main']['humidity']
            windSpeed = api_data['wind']['speed']
            pressure = api_data['main']['pressure']

            print("According to the Weather API, " + city + " is experiencing" 
                "\nTemperature of " + str(temperature) + " " + degreeSign + "C" 
                "\nPressure of "+ str(pressure) + " hPa" 
                "\nHumidity of " + str(humidity) + " %" 
                "\nWind Speed of " + str(windSpeed) + " m/s" 
                "\nWeather Description: " + str(weatherDescription).upper())
            
            speak("According to the Weather API" + city + "is experiencing")
            speak("Temperature of " + str(temperature) + "degree Celcius" 
                "\nPressure of " + str(pressure) + "hectopascal" 
                "\nHumidity of " + str(humidity) + "percent"
                "\nWind Speed of " + str(windSpeed) + "meter per second" 
                "\nThe weather describes " + str(weatherDescription))
             
        else:
            print("Sorry, city Not Found.")
            speak("Sorry, city Not Found.")

    # Game
    elif 'game' in query:
        game()

    # Exit
    elif 'stop' in query:
        print("Thank you. Alfred signing off!")
        speak("Thank you. Alfred signing off!")
        exit()

# Main Function
if __name__ == "__main__":
    clear = lambda: os.system('clear')

    clear() # Function to clear out every command before the execution
    wishMe() # Wish the user at the beginning

    while True:
        runAlfred()