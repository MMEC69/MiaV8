from tkinter import *
from PIL import Image, ImageTk
import chatbot
from chatbot import get_message, bot_name
from itertools import count, cycle
import TTS_pyttx as pyttx3tts
import TTS_gtts as ttsg
import speech_recorder
from threading import *


FG_Msg_Box = '#FFB6C1' #pink
BG_Msg_Box = "#000000" #black
BG_Text_Box = "#000000" #black
BG_Window = '#FFB6C1' #pink

FONT = 'Helvetica 20'
FONT_BOLD = 'Helvetica 20 bold'

class MiaApplication:

    class ImageLabel(Label):
        #"""
        #A Label that displays images, and plays them if they are gifs
        #:im: A PIL Image instance or a string filename
        #"""

        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            frames = []

            try:
                for i in count(1):
                    frames.append(ImageTk.PhotoImage(im.copy()))
                    im.seek(i)
            except EOFError:
                pass
            self.frames = cycle(frames)

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(frames) == 1:
                self.config(image=next(self.frames))
            else:
                self.next_frame()

        def unload(self):
            self.config(image=None)
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.config(image=next(self.frames))
                self.after(self.delay, self.next_frame)

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Mia <3")

        icon1 = PhotoImage(file='icon\\mia_icon.png')
        #assigned the .png file to icon1 variable

        self.window.iconphoto(True, icon1)

        self.window.resizable(
            width=True,
            height=True
        )
        self.window.configure(
            width=735,
            height=750,
            bg=BG_Msg_Box
        )

        # text widget
        self.text_widget = Text(self.window,
                                width=20,
                                height=2,
                                bg=BG_Text_Box,
                                fg=FG_Msg_Box,
                                font=FONT,
                                padx=20,
                                pady=20,
                                bd=0
                                )
        self.text_widget.place(relheight=0.925,
                               relwidth=0.6800,
                               rely=0.,
                               relx=0
                               )
        self.text_widget.configure(cursor="arrow",
                                   state=DISABLED
                                   )

        # bottom label
        bottom_label = Label(self.window, bg=BG_Text_Box, height=48)
        bottom_label.place(relwidth=1, rely=0.9250)

        # message entry box
        self.msg_entry = Entry(
            bottom_label,
            bg="#454440", #sort of ash color
            fg=FG_Msg_Box,
            font=FONT,
            bd = 0,
            justify=LEFT
        )
        self.msg_entry.place(relwidth=1, relheight=0.0750, rely=0.0085, relx=0.001)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        self.msg_entry.bind('<Control-Shift_L>', self.record_me)

        #send button

        #open image
        #self.send_button_icon = Image.open("icon\\send3.png")

        #resize
        #self.send_button_icon_r = self.send_button_icon.resize((50, 50))

        #self.send_button_icon_rn = ImageTk.PhotoImage(self.send_button_icon_r)
        #send_button = Button(bottom_label,
        #                    text="S",
        #                     font=FONT_BOLD,
        #                     activeforeground=BG_Text_Box,
        #                     activebackground=BG_Msg_Box,
        #                     command=lambda: self._on_enter_pressed(None),
        #                     bd=0,
        #                     image=self.send_button_icon_rn
        #                     )

        #send_button.place(relx=0.9295,
        #                  rely = 0.0085,
        #                  relheight=0.0760,
        #                  relwidth=0.0755
        #                  )

        #mic button

        # open image
        #self.mic_button_icon = Image.open("icon\\microphone1.png")

        # resize
        #self.mic_button_icon_r = self.mic_button_icon.resize((50, 50))

        #self.mic_button_icon_rn = ImageTk.PhotoImage(self.mic_button_icon_r)
        #mic_button = Button(bottom_label,
        #                   text="M",
        #                    font=FONT_BOLD,
        #                    activeforeground=BG_Text_Box,
        #                    activebackground=BG_Msg_Box,
        #                    command=lambda: self._on_mic_pressed(None),
        #                    bd=0,
        #                    image=self.mic_button_icon_rn
        #                    )
        #mic_button.place(relx=0.8540,
        #                 rely=0.0085,
        #                 relheight=0.0760,
        #                 relwidth=0.0755
        #                  )

        # animated girl
        lbl = MiaApplication.ImageLabel(self.window, bd=0)
        lbl.place(
            relx=0.6600,
            rely=0.075
        )
        lbl.load("anime_girl_banner_for_mia\\anime_girl2.gif")

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        msg_returned_bot = self._insert_message(msg, "You")

        # pyttx3tts.pyttxs3_TTspeech(msg_returned_bot)
        ttsg.gTTS_TTspeech(msg_returned_bot)

    # =================================speech_recognition_implementation=============================
    def record_me(self, event):
        recorded_speech = speech_recorder.take_speech()
        self._insert_message(recorded_speech, "You")
        return "recorded"

    # ===============================end speech_recognition_implementation==========================

    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)

        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(cursor="arrow", state=DISABLED)


        msg_returned_bot = get_message(msg)
        msg2 = f"{bot_name}: {msg_returned_bot}\n\n"
        self.text_widget.configure(cursor="arrow", state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(cursor="arrow", state=DISABLED)


        self.text_widget.see(END)
        # This is to make sure chat is set to the bottom of the conversation

        return msg_returned_bot



if __name__ == "__main__":
    app = MiaApplication()
    app.run()



#something is not quite right