import time
from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import QRcode
from PIL import Image, ImageTk
import cv2
import facial_recognition
import threading

def get_button(window, text, color, command, fg='white'):
    button = ttk.Button(window,
                        text=text,
                        activebackground= 'black',
                        activeforeground='white',
                        fg= fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,

                        )
    return button

def get_img_label(window):
    label = ttk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label=ttk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label
def get_entry_text(window):
    inputtxt = ttk.Text(window,
                        height=2,
                        width=15,
                        font=("Arial", 32))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)

class App:
    def __init__(self):
        self.main_window =ttk.Tk()
        self.main_window.geometry("1200x520+350+100")


        self.login_button_main_window = get_button(self.main_window, 'capture', 'green', self.check_face)
        self.login_button_main_window.place(x=750, y=200)


        self.login_button_main_window = get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_main_window = get_button(self.main_window, 'register', 'green', self.register_new_user)
        self.register_new_user_main_window.place(x=750 , y=400)


        self.webcam_label = get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700,  height=500)

        self.add_webcam(self.webcam_label)

    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        decoded_frame =QRcode.QRcode.decoder(frame)
        #get_face = facial_recognition.recognition.stream(facial_recognition)
        #print(get_face)
        #facial_recognition.recognition.testRecognition(facial_recognition,'jamie foxx.png', frame)
        self.most_recent_capture_arr = decoded_frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)

        self.most_recent_capture_pil = Image.fromarray(img_)

        self.imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)


        self._label.imgtk = self.imgtk
        self._label.configure(image =self.imgtk)

        self._label.after(20, self.process_webcam)

    def login(self):
        self.login_button_main_window = ttk.Toplevel(self.main_window)
        self.login_button_main_window.geometry("1200x520+350+100")

        self.label_text1 = get_text_label(self.login_button_main_window, text="Email")
        self.label_text1.place(x=100 , y= 200)

    def register_new_user(self):
        self.register_new_user_main_window =ttk.Toplevel(self.main_window)
        self.register_new_user_main_window.geometry("1200x520+350+100")


    def start(self):
      self.main_window.mainloop()

    def threading(img):
        try:
            threading.Thread(target=img.check_face, args=(img,))
        except:
            print(" canot thread ")
    def check_face(self):
        frame = ImageTk.getimage(self.imgtk)
        print(" frame collected ")
        result = facial_recognition.recognition.testRecognition(facial_recognition, frame, 'face_database/oscar2.jpg')

        print(result)
        return result



if __name__ == "__main__":
    app =App()
    app.start()