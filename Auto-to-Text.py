import os 
import speech_recognition as sr
from tqdm import tqdm

with open("APT-KEY") as f:
    GOOGLE_CLOUD_SPEED_CREDENTIALS = f.read()

r = sr.Recognizer()
files = sorted(os.listdir('parts/'))
