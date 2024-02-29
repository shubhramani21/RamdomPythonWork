from pytube import YouTube
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror, askokcancel
import threading

def download_video():
    try:
        #getting url form the entry
        video_link=url_entry.get()

        if(video_link==''):
            showerror(title='ERROR',message='Please Enter youtube URL link')

        else:
            def on_progress(stream,chank,bytes_remaining):
                #getting total size of the video
                total_size=stream.filesize

                def get_formatted_size(total_size,factor=1024,suffix='B'):

                    sizes=["", "K", "M", "G", "T", "P", "E", "Z"]
                    for unit in sizes:
                        if total_size<factor:
                            return f"{total_size:.2f}{unit}{suffix}"
                        total_size/=factor
                        
                    return f"{total_size:.2f}Y{suffix}"

                formatted_size=get_formatted_size(total_size)

                byte_downloaded=total_size-bytes_remaining

                percentage_completed = round(byte_downloaded / total_size * 100)

                progress_bar['value']=percentage_completed

                progress_label.config(text=str(percentage_completed)+'%,File size'+formatted_size)

                window.update()
            
            video=YouTube(video_link,on_progress_callback=on_progress)
            video.streams.get_highest_resolution().download()
            showinfo(title='Download Completed',message="Enjoy")

            progress_label.config(text='')
            progress_bar['value']=0

            

    except:
        # popup for displaying the error message
        showerror(title='Download Error', message='An error occurred while trying to ' \
                    'download the video\nThe following could ' \
                    'be the causes:\n->Invalid link\n->No internet connection\n'\
                     'Make sure you have stable internet connection and the video link is valid')
        # ressetting the progress bar and the progress label
        progress_label.config(text='')
        progress_bar['value'] = 0



def download_tread():
    t2=threading.Thread(target=download_video)
    t2.start()


########CREATES A WINDOW#############
window=Tk()

window.title("YouTube Video Downloader.")

window.geometry('500x460+430+180')

window.resizable(height=False , width=False)


########ADDIING WIGETS AND LOGO USING CANVAS#############
canvas=Canvas(window,width=500,height=400)

#########ADDING YOUTUBE IMAGE###########################
logo=PhotoImage(file='YouTube Logo Vector.png')

logo=logo.subsample(10,10)#Setting up the dimension

canvas.create_image(250,80,image=logo)#puts in the image


##################STYLE FOR THE WIGETS##########################

#style for the label
label_style=ttk.Style()
label_style.configure('TLabel',foreground='#000000', font=('OCR A Extended', 15))

#style for the entry
entry_style=ttk.Style()
entry_style.configure('TEntry',font=('Dotum',15))

#style for the button
button_style=ttk.Style()
button_style.configure('TButton',foreground='#000000', font='DotumChe')


##################CREATING LABEL##########################
url_label=ttk.Label(window,text='Enter  Video URL:',style='TLabel') #creating label
url_entry = ttk.Entry(window, width=76, style='TEntry')#creating entry

canvas.create_window(114,200,window=url_label)#adding label to canvas
canvas.create_window(250, 230, window=url_entry)#adding entry to canvas

###################CREATING PROGRESS BAR #######################
progress_label=Label(window,text='')
canvas.create_window(240,360,window=progress_label)

progress_bar=ttk.Progressbar(window,orient=HORIZONTAL,length=450,mode='determinate')
canvas.create_window(250,380,window=progress_bar)

download_button=ttk.Button(window,text="Download Video",style='TButton',command=download_tread)
canvas.create_window(240,410,window=download_button)

canvas.pack()
window.mainloop()