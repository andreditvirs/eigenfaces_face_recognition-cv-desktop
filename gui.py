from tkinter import *
import os

folder_path = 'D:\\Teknik Informatika\\CV\\Project Akhir\\'
in_path = folder_path+'testing\\'

def list_dir():
    listds = os.listdir(in_path)
    number_files = len(listds)
    os.chdir(in_path)
    arr = os.listdir()
    return arr

def show_info():
    os.chdir(folder_path)
    message_txt.delete(0.0, 'end')
    menu = menu_value_choice.get()
    name = str('"'+tkvar.get()+'"')
    if menu == 1:
        testing_name = testing.get()
        os.system('python add_testing.py %s'%testing_name)
        message_txt.insert(0.0, "Testing01 berhasil ditambahkan")        
    elif menu == 2:
        os.system('python t_eigen.py')
        message_txt.insert(0.0, "Training dataset selesai")
    elif menu == 3:
        os.system('python f_eigen.py')
        message_txt.insert(0.0, "Mengakhiri Webcam")
    elif menu == 4 :
        video_name = video_file.get()
        if video_name != '':
            os.system('python fv_eigen.py %s'%video_name)
            message_txt.insert(0.0, "Video tersimpan")
        else:
            message_txt.insert(0.0, "Anda belum memasukkan nama video")
    elif menu == 5:
        os.system('python manual_testing.py %s'%name)
        message_txt.insert(0.0, "Hasil ada di command line")
    else:
        message_txt.insert(0.0, "Anda belum memilih salah satu menu")

rootWindow = Tk()
video_file = StringVar()
testing = StringVar()
tkvar = StringVar(rootWindow)

mahasiswa = sorted(list_dir())
tkvar.set('Pilih Testing')

popupMenu = OptionMenu(rootWindow, tkvar, *mahasiswa)
# Label(rootWindow, text="Pilih Mahasiswa").grid(row=2, column=2)

rootWindow.resizable(height = None, width = None)
rootWindow.title("Face Recognition")

welcome_label = Label(rootWindow, text="Aplikasi Pengenalan Wajah\n Mahasiswa 2 D3 IT B", fg="gray",
                      font=("arial", 16,"bold"))
procedure_label = Label(rootWindow, text="Silahkan memilih menu yang diinginkan", fg="gray",
                      font=("arial", 14))
add_label = Label(rootWindow, text="Untuk menambahkan 3 foto training pada \nfolder NRP melalui webcam selama 15 detik", fg="gray",
                      font=("arial", 10))
testing_entry = Entry(rootWindow, textvariable=testing) # Untuk masukkan nama testing01
train_label = Label(rootWindow, text="Untuk melakukan training pada dataset \n(output = ekstraksi fitur, grayscale face)", fg="gray",
                      font=("arial", 10))
webcam_label = Label(rootWindow, text="Untuk melakukan pengenalan wajah \nsesuai ekstraksi fitur dengan webcam", fg="gray",
                      font=("arial", 10))
video_label = Label(rootWindow, text="Untuk melakukan pengenalan wajah \nsesuai ekstraksi fitur dari video file", fg="gray",
                      font=("arial", 10))
do_label = Label(rootWindow, text="Untuk melakukan pengenalan wajah \nsesuai ekstraksi fitur dari testing01", fg="gray",
                      font=("arial", 10))
message_label = Label(rootWindow, text="Message Box (Jangan diisi)", fg="gray",
                      font=("arial", 10))
att_label = Label(rootWindow, text="Tekan 'q' untuk mengakhiri menu program", fg="gray",
                      font=("arial", 10))
video_entry_label = Label(rootWindow, text="Masukkan nama file video disertai format \nvideo(contoh = example.mp4)", fg="gray",
                      font=("arial", 10))
video_entry = Entry(rootWindow, textvariable=video_file) # Untuk masukkan nama video

menu_value_choice = IntVar()
radio_button_a = Radiobutton(rootWindow, text="Add Testing01", variable=menu_value_choice,
                               font=("arial", 12), value=1)
radio_button_t = Radiobutton(rootWindow, text="Train Dataset", variable=menu_value_choice,
                               font=("arial", 12), value=2)
radio_button_f = Radiobutton(rootWindow, text="Face Recognition (Webcam)", variable=menu_value_choice,
                              font=("arial", 12), value=3)
radio_button_fv = Radiobutton(rootWindow, text="Face Recognition (Video File)", variable=menu_value_choice,
                              font=("arial", 12), value=4)
radio_button_d = Radiobutton(rootWindow, text="Face Recognition (Testing02)", variable=menu_value_choice,
                              font=("arial", 12), value=5)

message_txt = Text(rootWindow, width=36, height=1, wrap=WORD, fg="blue",
                   font=("arial", 12, "bold"))

lets_see_button = Button(rootWindow, text="Mulai", font=("arial", 12),
                         command=lambda: show_info())

# Setting the layout

rootWindow.grid_rowconfigure(0, minsize=20)

welcome_label.grid(row=1, columnspan=4)
procedure_label.grid(row=2, columnspan=4)

rootWindow.grid_rowconfigure(3, minsize=20)
radio_button_a.grid(row=4, column=1, sticky=W)
add_label.grid(row=5, column=1, sticky=W)
radio_button_t.grid(row=4, column=2, sticky=W)
train_label.grid(row=5, column=2, sticky=W)
testing_entry.grid(row=6, column=1)

radio_button_f.grid(row=7, column=1, sticky=W)
webcam_label.grid(row=8, column=1, sticky=W)
radio_button_fv.grid(row=7, column=2, sticky=W)
video_label.grid(row=8, column=2, sticky=W)
video_entry_label.grid(row=9, column=2, sticky=W)
video_entry.grid(row=10, column=2, sticky=N)

radio_button_d.grid(row=11, column=1, sticky=W)
do_label.grid(row=12, column=1, sticky=W)
popupMenu.grid(row=13, column=1, sticky=N)

rootWindow.grid_rowconfigure(14, minsize=20)
message_label.grid(row=15, columnspan=4)
message_txt.grid(row=16, columnspan=4, sticky=N, rowspan=1)

rootWindow.grid_rowconfigure(17, minsize=20)
lets_see_button.grid(row=18, columnspan=4)

att_label.grid(row=19, columnspan=4)
rootWindow.mainloop()