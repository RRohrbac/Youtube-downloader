import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback= on_progress)
        video = ytObject.streams.get_highest_resolution()
        ytObject.streams
        title.configure(text = ytObject.title, text_color = "white")
        finishLabel.configure(text = "")
        video.download()
        finishLabel.configure(text = "Download Complete")  
    except:
        finishLabel.configure(text = "Download Error", text_color = "red")    
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text = per + '%')
    pPercentage.update()
    ProgressBar.set(float(percentage_of_completion) / 100)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#app window
app = customtkinter.CTk()
app.geometry("720x480")
app.title(("YouTube Downloader"))

#User Interface
title = customtkinter.CTkLabel(app, text="Paste Link Here")
title.pack(padx=10, pady=10)

#add link here
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable= url_var)
link.pack()

#download status
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#download
download = customtkinter.CTkButton(app, text="download", fg_color= "red", hover_color="#750d0c",
                                   border_color="white", border_width=1,
                                   command = startDownload)
download.pack(padx = 10, pady = 10)

#Downloading status
pPercentage = customtkinter.CTkLabel(app, text= "0%")
pPercentage.pack ()

ProgressBar = customtkinter.CTkProgressBar(app, progress_color= "red", width=400)
ProgressBar.set(0)
ProgressBar.pack(padx = 10, pady = 10)


#Run app
app.mainloop()
