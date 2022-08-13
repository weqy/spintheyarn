import tkinter as tk
import random
from gtts import gTTS
import playsound # must run: pip install playsound==1.2.2 . latest versions WILL NOT WORK



root = tk.Tk()

entry1 = tk.Entry(root)

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Spin the Yarn / Storyteller')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

myNoun = ["best friend", "employer", "dog", "mother", "computer", "stuffed animal"]
myPlace = ["barber shop", "job interview", "pet store",
           "grocery store", "garage", "police station"]
myEnding = ["much better", "horrible", "amazing", "weird"]
myAdj = ["great", "even worse"]
myInterview = ["But, they never contacted me again", "I got the job"]

nounChoose = random.choice(myNoun)
placeChoose = random.choice(myPlace)
endingChoose = random.choice(myEnding)
interviewEnding = random.choice(myInterview)
adjChoose = random.choice(myAdj)

def story_choose():
    canvas1.delete("all")  # to clear the tk window
    label1 = tk.Label(root, text='Spin the Yarn / Storyteller')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    label2 = tk.Label(root, text='Which story number would you like?')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 80, window=label2)
    story1 = tk.Button(text='1', command=spin_the_yarn1, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 120, window=story1)
    story2 = tk.Button(text='2', command=spin_the_yarn2, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 150, window=story2)
    story3 = tk.Button(text='3', command=spin_the_yarn3, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 180, window=story3)

def spin_the_yarn1():
    canvas1.delete("all")  # to clear the tk window
    label1 = tk.Label(root, text='Spin the Yarn / Storyteller')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    my_story = tk.Label(root, text='One day, my ' + nounChoose + ' told me that I should get a haircut.\n' +
                                       " So, I went to the " + placeChoose + " to get one.\n"
                                       + " Then, I came back, and my " + nounChoose +
                                       " \ntold me that it looked " + adjChoose + ".")
    canvas1.create_window(200, 100, window=my_story)

    button1 = tk.Button(text='Read Text in US Accent', command=text_to_speech, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 200, window=button1)
    button2 = tk.Button(text='Read Text in UK Accent', command=text_to_speech_UK, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 230, window=button2)

    tts = gTTS(my_story.cget("text"))
    tts.save('story.mp3')

    tts_uk = gTTS(text=my_story.cget("text"), tld='co.uk', lang='en', slow=False)
    tts_uk.save('story_uk.mp3')

def text_to_speech():
    playsound.playsound('story.mp3')

def text_to_speech_UK():
    playsound.playsound('story_uk.mp3')

def spin_the_yarn2():
    canvas1.delete("all")  # to clear the tk window
    label1 = tk.Label(root, text='Spin the Yarn / Storyteller')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    my_story = tk.Label(root, text='Last week, my ' + nounChoose + ' told me I was fired from my job.\n'
                                                                       " I was very upset, so the next day I went to a "
                                       + placeChoose + " to get a new job.\n"
                                       + interviewEnding + ", and I felt " + endingChoose + ".")
    canvas1.create_window(200, 100, window=my_story)

    button1 = tk.Button(text='Read Text in US Accent', command=text_to_speech, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 200, window=button1)
    button2 = tk.Button(text='Read Text in UK Accent', command=text_to_speech_UK, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 230, window=button2)

    tts = gTTS(my_story.cget("text"))
    tts.save('story.mp3')

    tts_uk = gTTS(text=my_story.cget("text"), tld='co.uk', lang='en', slow=False)
    tts_uk.save('story_uk.mp3')

def spin_the_yarn3():
    canvas1.delete("all")  # to clear the tk window
    label1 = tk.Label(root, text='Spin the Yarn / Storyteller')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 25, window=label1)
    my_story = tk.Label(root, text='I was so scared when my ' + nounChoose + ' started barking like crazy!\n'
                                                                                 " I took my " + nounChoose + ' to the ' + placeChoose
                                       + " and everything was okay.\n I felt "
                                       + endingChoose + ".")
    canvas1.create_window(200, 100, window=my_story)
    tts = gTTS(my_story.cget("text"))
    tts.save('story.mp3')

    tts_uk = gTTS(text=my_story.cget("text"), tld='co.uk', lang='en', slow=False)
    tts_uk.save('story_uk.mp3')

    button1 = tk.Button(text='Read Text in US Accent', command=text_to_speech, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 200, window=button1)
    button2 = tk.Button(text='Read Text in UK Accent', command=text_to_speech_UK, bg='brown', fg='white',
                        font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 230, window=button2)



button1 = tk.Button(text='Generate Story!', command=story_choose, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 150, window=button1)

root.mainloop()
