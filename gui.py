from tkinter import *
import os

def show_info():
    message_txt.delete(0.0, 'end')
    menu = menu_value_choice.get()
    if menu == 1:
        os.system('python t_eigen.py')
        message_txt.insert(0.0, "Training dataset selesai")
    elif menu == 2:
        os.system('python f_eigen.py')
        message_txt.insert(0.0, "Mengakhiri Webcam")
    elif menu == 3 :
        video_name = video_file.get()
        if video_name != '':
            os.system('python fv_eigen.py %s'%video_name)
            message_txt.insert(0.0, "Video tersimpan")
        else:
            message_txt.insert(0.0, "Anda belum memasukkan nama video")
    else:
        message_txt.insert(0.0, "Anda belum memilih salah satu menu")

rootWindow = Tk()
video_file = StringVar()

rootWindow.resizable(height = None, width = None)
rootWindow.title("Face Recognition")

welcome_label = Label(rootWindow, text="Aplikasi Pengenalan Wajah\n Mahasiswa 2 D3 IT B", fg="gray",
                      font=("arial", 16,"bold"))
procedure_label = Label(rootWindow, text="Silahkan memilih menu yang diinginkan", fg="gray",
                      font=("arial", 14))
train_label = Label(rootWindow, text="Untuk melakukan training pada dataset \n(output = ekstraksi fitur, grayscale face)", fg="gray",
                      font=("arial", 10))
webcam_label = Label(rootWindow, text="Untuk melakukan pengenalan wajah \nsesuai ekstraksi fitur dengan webcam", fg="gray",
                      font=("arial", 10))
video_label = Label(rootWindow, text="Untuk melakukan pengenalan wajah \nsesuai ekstraksi fitur dari video file", fg="gray",
                      font=("arial", 10))
message_label = Label(rootWindow, text="Message Box (Jangan diisi)", fg="gray",
                      font=("arial", 10))
att_label = Label(rootWindow, text="Tekan 'q' untuk mengakhiri menu program", fg="gray",
                      font=("arial", 10))
video_entry_label = Label(rootWindow, text="Masukkan nama file video disertai format \nvideo(contoh = example.mp4)", fg="gray",
                      font=("arial", 10))
video_entry = Entry(rootWindow, textvariable=video_file) # Untuk masukkan nama video

menu_value_choice = IntVar()
radio_button_t = Radiobutton(rootWindow, text="Train Dataset", variable=menu_value_choice,
                               font=("arial", 12), value=1)
radio_button_f = Radiobutton(rootWindow, text="Face Recognition (Webcam)", variable=menu_value_choice,
                              font=("arial", 12), value=2)
radio_button_fv = Radiobutton(rootWindow, text="Face Recognition (Video File)", variable=menu_value_choice,
                              font=("arial", 12), value=3)

message_txt = Text(rootWindow, width=36, height=1, wrap=WORD, fg="blue",
                   font=("arial", 12, "bold"))

lets_see_button = Button(rootWindow, text="Mulai", font=("arial", 12),
                         command=lambda: show_info())

# Setting the layout

rootWindow.grid_rowconfigure(0, minsize=20)

welcome_label.grid(row=1, columnspan=4)
procedure_label.grid(row=2, columnspan=4)

rootWindow.grid_rowconfigure(3, minsize=20)
radio_button_t.grid(row=4, column=1, sticky=W)
train_label.grid(row=5, column=1, sticky=W)
radio_button_f.grid(row=4, column=2, sticky=W)
webcam_label.grid(row=5, column=2, sticky=W)
radio_button_fv.grid(row=4, column=3, sticky=W)
video_label.grid(row=5, column=3, sticky=W)
video_entry_label.grid(row=6, column=3, sticky=W)
video_entry.grid(row=7, column=3, sticky=N)

rootWindow.grid_rowconfigure(8, minsize=20)
message_label.grid(row=9, columnspan=4)
message_txt.grid(row=10, columnspan=4, sticky=N, rowspan=1)

rootWindow.grid_rowconfigure(11, minsize=20)
lets_see_button.grid(row=12, columnspan=4)

att_label.grid(row=13, columnspan=4)
rootWindow.mainloop()