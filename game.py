from tkinter import *
import pygame as gm

root = Tk()
root['bg'] = '#000000'
root.title('Фентези приключение')
root.geometry('1000x500')
root.resizable(width=False, height=False)
gm.init()


def login():
    gm.mixer.music.load("music/song1.mp3")
    gm.mixer.music.play(-1)
    
    frame_top = Frame(root, bg='#ffb700', bd=5)
    frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.45)

    info = Label(frame_top, text='Назови своё имя, путешественник!', bg='#ffb700', font=30)
    info.place(relx=0.25, relwidth=0.5, relheight=0.3)

    cityField = Entry(frame_top, bg='#868eff', border='1px', font='30px')
    cityField.place(rely=0.4, relwidth=1, relheight=0.15)

    btn = Button(frame_top, text='ВОЙТИ ЧЕРЕЗ ВРАТА!', command=lets_play)
    btn.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.15)

    frame_bottom = Frame(root, bg='#ffb700', bd=5)
    frame_bottom.place(relx=0.15, rely=0.65, relwidth=0.7, relheight=0.1)

    info = Label(frame_bottom, text='"COZY ROOM" studio  AND  "Банда хацкерів!!!!¡!!!!" unification\nPRESENT', bg='#ffb700', font=40)
    info.pack()


def lets_play():
    gm.mixer.music.load("music/song2.mp3")
    gm.mixer.music.play(-1)

    frame_top = Frame(root, bg='#000000', bd=5)
    frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.45)

    info = Label(frame_top, text='Назови своё имя, путешественник!', bg='#ffb700', font=30)
    info.place(relx=0.25, relwidth=0.5, relheight=0.3)

    cityField = Entry(frame_top, bg='#868eff', border='1px', font='30px')
    cityField.place(rely=0.4, relwidth=1, relheight=0.15)

    btn = Button(frame_top, text='ВОЙТИ ЧЕРЕЗ ВРАТА!', command=lets_play)
    btn.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.15)

    frame_bottom = Frame(root, bg='#000000', bd=5)
    frame_bottom.place(relx=0.15, rely=0.65, relwidth=0.7, relheight=0.1)

    info = Label(frame_bottom, text='"COZY ROOM" studio  AND  "Банда хацкерів!!!!¡!!!!" unification\nPRESENT', bg='#ffb700', font=40)
    info.pack()

login()

root.mainloop()
