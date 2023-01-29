import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',130)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command=command.lower()
                if 'alexa' in command:
                    commandf=command.replace('alexa',' ')
                   
                    print(commandf)
                
            
                
                
            
            

    except:
        pass
    return commandf

def run_alexa():
    instruction=take_command()
    if "play" in instruction:
        song=instruction.replace('play'," ")
        talk("playing" +song)
        pywhatkit.playonyt(song)
    
    #time
    elif "time" in instruction:
        time1=datetime.datetime.now().strftime("%I:%M  %p")
        print(time1)
        talk("current time is " +time1)
    
    #date
    elif "date" in instruction:
        # date1=datetime.date.today()
        # date2=datetime.date.isoformat(date1)
        # print(date2)
        # talk("Todays date is"+date2)
        date1=datetime.datetime.now().strftime("%A %m %Y")
        #print(date1)
        talk("Current date is"+date1)

    #wikipedia
    elif "who is"  in instruction:
        instruction2=instruction.replace("who is" ," ")
        search=wikipedia.summary(instruction2,1)
        print(search)
        talk(search)
    
    #wedvow
    elif "stories" in instruction:
        talk("Wedvow stories is a wedding photo company founded by rahul mk and Midhun Lal Located in ottapalam opposite Lakshmi theatre")
   
    elif "are you single" in instruction:
        talk("no iam in relationship with wifi ")
    elif "are you there" in instruction:
        talk("yes Sarath ,how can i help you")

    #jokes
    elif "joke" in instruction:
        j=pyjokes.get_joke()
        print(j)
        talk(j)
    else:
        talk("pardon,say the command again")
    
    
    
while True:
    run_alexa()
    
        