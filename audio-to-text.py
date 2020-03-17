# Library for Speech Recognition 
import speech_recognition as sr 

# Instance of the recogniser class.
r = sr.Recognizer()
# Making an instance of the Microphone 
with sr.Microphone()as source:
    # Script requests you say something :D
    print("Please Say Something: ")
    # mic captures audio
    audio=r.listen(source)
    try:
        # The output of audio is recongnised using Google speech recognition
        output=r.recognize_google(audio)
        # if audio was understood, it will be displayed with the statement "You said: " at the beginning of the statement. 
        print("You said: {}".format(output))
        # if audio not understood below statement will appear. 
    except:
        print("I didn't hear what you said, please try again")