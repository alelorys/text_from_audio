import os
import tkinter
from gtts import gTTS
from tkinter import filedialog
from audio_to_text import audio_to_text
from text_to_audio import text_to_audio

status = None
content = ""
audio = None
path = ""
def open_files():
    file = filedialog.askopenfilename(initialdir="\\",
                                      title="Select a File",
                                      filetypes=(("Support files","*.txt*"),
                                                 ("and","*.mp3*")))
    file_name.configure(text=f"{file}")
    if file.endswith(".txt"):
        with open(file,'r',encoding="utf-8") as f:
            content = f.readlines()
            content = " ".join(content)
            show_text.insert(1.0, content)
    
    
def open_txt_file():
    global status
    open_files()
    status = 0

def open_audio_file():
    global path
    global status
    open_files()
    path = file_name.cget("text")
    status = 1


def convert_txt_audio():
    
    match status:
        case 0:
            global audio
            print("setting up for text to speech convertion")
            text = show_text.get("1.0","end")
            audio = text_to_audio(text=text,lang="pl")
            print("Convertion complete :)")
        case 1:
            global content
            content = audio_to_text(path)
            show_text.insert("1.0",content)

    
    
def save_file():
    file = filedialog.asksaveasfilename(initialfile="untitled1",
                                        filetypes=[("Text Files","*.txt"),("Audio Files","*.mp3")])
    extention = file.split(".")[-1]
    match extention:
        case "mp3":
            audio.save(file)
        case "txt":
            with open(file,'w',encoding="utf-8") as f:
                f.writelines(content)

app = tkinter.Tk()
app.title("Audio <> Text")
app.geometry("450x400")

file_name = tkinter.Label(app, text='nazwa pliku')
file_name.pack()
file_name.place(x=50,y=50)
show_text = tkinter.Text(app)
show_text.pack()
show_text.place(x=50,y=70, height=250,width=350)
audio_btn = tkinter.Button(app, text='audio to text',command=open_audio_file)
audio_btn.pack()
audio_btn.place(x=120,y=20)
text_btn = tkinter.Button(app,text='text to audio',command=open_txt_file)
text_btn.pack()
text_btn.place(x=200,y=20)

save_btn = tkinter.Button(app,text='Save',command=save_file)
save_btn.pack()
save_btn.place(x= 120, y=330)
convert_btn = tkinter.Button(app,text='Convert',command=convert_txt_audio)
convert_btn.pack()
convert_btn.place(x=170, y=330)

app.mainloop()

