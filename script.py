from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import moviepy.editor
import tkinter 


def main():
    plt = getgraph('tkt')

def getaudio():
    video = moviepy.editor.VideoFileClip("video.mp4")
    audio = video.audio
    audio.write_audiofile("Audio.mp3")

def getgraph(path):
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    input_data = read("1.wav")
    audio = input_data[1]
    plt.plot(audio[0:1000000000000000000000])
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    return plt
