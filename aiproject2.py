import random
import tkinter as tk
from cProfile import label
import threading
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import array
import json
import win32com.client as wincl
import pyttsx3
import tkinter
from pygame import mixer
import speech_recognition as sr
import time
# ************************
# Scrollable Frame Class
# ************************
class ScrollFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master) # create a frame (self)
        self.canvas = tk.Canvas(self,width=1300, height=700, borderwidth=0, background="#ffffff")          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, background="#ffffff")                    #place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas
        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",tags="self.viewPort")            #add view port frame to canvas
        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.
    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame =ScrollFrame(self)
        self.img1=tk.PhotoImage(file="logo.png")
        tk.Label(self.scrollFrame.viewPort, image=self.img1,bg="#ffffff").pack(side="top", fill="x", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="PYROID: Learn Python", font=('Helvetica', 24, "bold"),bg="#ffffff",fg="#DC143C").pack(side="top", fill="x", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Master Python \n one step at a time", font=('Helvetica', 18, "bold"), bg="#ffffff",fg="#000000").pack(side="top", fill="x", pady=5)
        self.img2=tk.PhotoImage(file="ai6.png")
        tk.Label(self.scrollFrame.viewPort, image=self.img2, font=('Helvetica', 14, "bold"),bg="#ffffff",fg="#000000").pack(side="top", fill="x", pady=5)
        self.img3 = tk.PhotoImage(file="ai4.png")
        tk.Button(self.scrollFrame.viewPort, image=self.img3,command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)


class TitlePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="What We Will Learn!!!", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top",anchor="center", pady=5)
        self.img4 = tk.PhotoImage(file="index11.png")
        tk.Label(self.scrollFrame.viewPort, image=self.img4, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20,10),anchor="nw")
        self.img13 = tk.PhotoImage(file="index22.png")
        tk.Label(self.scrollFrame.viewPort, image=self.img13, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110,pady=(40,10), anchor="ne")
        self.img5 = tk.PhotoImage(file="btn11.png")
        self.img6 = tk.PhotoImage(file="btn22.png")
        self.img7 = tk.PhotoImage(file="btn33.png")
        self.img8 = tk.PhotoImage(file="btn44.png")
        self.img9 = tk.PhotoImage(file="btn55.png")
        self.img10 = tk.PhotoImage(file="btn66.png")
        self.img11 = tk.PhotoImage(file="btn77.png")
        self.img12 = tk.PhotoImage(file="btn88.png")
        tk.Button(self.scrollFrame.viewPort, image=self.img5 ,width=180,command=lambda: master.switch_frame(PageOne)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img6,width=180,command=lambda: master.switch_frame(PageTwo)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img7,width=180,command=lambda: master.switch_frame(PageThree)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img8,width=180,command=lambda: master.switch_frame(PageFour)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img9,width=180,command=lambda: master.switch_frame(PageFive)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img10,width=180,command=lambda: master.switch_frame(PageSix)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img11,width=180,command=lambda: master.switch_frame(PageSeven)).pack(side="top",anchor="center",pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.img12,width=180,command=lambda: master.switch_frame(PageEight)).pack(side="top",anchor="center",pady=0)
        frame= Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        self.my_thread = threading.Thread(target=master.switch_frame, args=(Quiz,))
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff",command=lambda:self.my_thread.start())
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2=Button(frame,image=self.img15,background="#ffffff",command=lambda: master.switch_frame(StartPage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
         self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff",command=self.quit )
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", expand=True)
#these are pages of main topics
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Introduction!!!", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1=tk.PhotoImage(file="ibtn1.png")
        self.image2 = tk.PhotoImage(file="ibtn2.png")
        self.image3 = tk.PhotoImage(file="ibtn3.png")
        self.image4 = tk.PhotoImage(file="ibtn4.png")
        self.image5 = tk.PhotoImage(file="ibtn5.png")
        self.image6 = tk.PhotoImage(file="ibtn6.png")
        self.image7 = tk.PhotoImage(file="ibtn7.png")
        self.image8 = tk.PhotoImage(file="ibtn8.png")
        self.image9 = tk.PhotoImage(file="ibtn9.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(ibtn1)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(ibtn2)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(ibtn3)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(ibtn4)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(ibtn5)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image6, width=180,command=lambda: master.switch_frame(ibtn6)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image7, width=180,command=lambda: master.switch_frame(ibtn7)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image8, width=180,command=lambda: master.switch_frame(ibtn8)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image9, width=180,command=lambda: master.switch_frame(ibtn9)).pack(side="top", anchor="center", pady=0)
        frame= Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        self.my_thread = threading.Thread(target=master.switch_frame, args=(Quiz,))
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: self.my_thread.start())
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2=Button(frame,image=self.img15,background="#ffffff",command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Decision Making & Loop", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn1.png")
        self.image2 = tk.PhotoImage(file="kbtn2.png")
        self.image3 = tk.PhotoImage(file="kbtn3.png")
        self.image4 = tk.PhotoImage(file="kbtn4.png")
        self.image5 = tk.PhotoImage(file="kbtn5.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn1)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn2)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn3)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn4)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn5)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
         self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Functions", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn6.png")
        self.image2 = tk.PhotoImage(file="kbtn7.png")
        self.image3 = tk.PhotoImage(file="kbtn8.png")
        self.image4 = tk.PhotoImage(file="kbtn9.png")
        self.image5 = tk.PhotoImage(file="kbtn10.png")
        self.image6 = tk.PhotoImage(file="kbtn11.png")
        self.image7 = tk.PhotoImage(file="kbtn12.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn6)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn7)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn8)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn9)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn10)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn11)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn12)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
         self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Collections Data Types", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn13.png")
        self.image2 = tk.PhotoImage(file="kbtn14.png")
        self.image3 = tk.PhotoImage(file="kbtn15.png")
        self.image4 = tk.PhotoImage(file="kbtn16.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn13)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn14)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn15)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn16)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Modules & Files", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn17.png")
        self.image2 = tk.PhotoImage(file="kbtn18.png")
        self.image3 = tk.PhotoImage(file="kbtn19.png")
        self.image4 = tk.PhotoImage(file="kbtn20.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn17)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn18)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn19)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn20)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Exception Handling", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn19.png")
        self.image2 = tk.PhotoImage(file="kbtn20.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn19)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn20)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Object Oriented Programming", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn21.png")
        self.image2 = tk.PhotoImage(file="kbtn22.png")
        self.image3 = tk.PhotoImage(file="kbtn23.png")
        self.image4 = tk.PhotoImage(file="kbtn24.png")
        self.image5 = tk.PhotoImage(file="kbtn25.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn21)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn22)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn23)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn24)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn25)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class PageEight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Introduction!!!", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        self.image10 = tk.PhotoImage(file="intro3.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image10, bg="#ffffff",fg="#DC143C").pack(side="right", padx=120, pady=(20, 10), anchor="nw")
        self.image11 = tk.PhotoImage(file="intro2 (2).png")
        tk.Label(self.scrollFrame.viewPort, image=self.image11, bg="#ffffff",fg="#DC143C").pack(side="left", padx=110, pady=(40, 10), anchor="ne")
        self.image1 = tk.PhotoImage(file="kbtn26.png")
        self.image2 = tk.PhotoImage(file="kbtn27.png")
        self.image3 = tk.PhotoImage(file="kbtn28.png")
        self.image4 = tk.PhotoImage(file="kbtn29.png")
        self.image5 = tk.PhotoImage(file="kbtn30.png")
        self.image6 = tk.PhotoImage(file="kbtn31.png")
        tk.Button(self.scrollFrame.viewPort, image=self.image1, width=180,command=lambda: master.switch_frame(kbtn26)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image2, width=180,command=lambda: master.switch_frame(kbtn27)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image3, width=180,command=lambda: master.switch_frame(kbtn28)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image4, width=180,command=lambda: master.switch_frame(kbtn29)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image5, width=180,command=lambda: master.switch_frame(kbtn30)).pack(side="top", anchor="center", pady=0)
        tk.Button(self.scrollFrame.viewPort, image=self.image6, width=180,command=lambda: master.switch_frame(kbtn31)).pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        self.my_thread = threading.Thread(target=master.switch_frame, args=(Quiz,))
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: self.my_thread.start())
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(TitlePage))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
 #quiz coding started please open data.json file before running it else you can do it direct with list(commented below)
class Quiz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        with open('./data.json', encoding="utf8") as f:
            data = json.load(f)
        # convert the dictionary in lists of questions and answers_choice
        self.questions = [v for v in data[0].values()]
        self.answers_choice = [v for v in data[1].values()]
        self.answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]
        self.user_answer = []
        self.indexes = []
        def gen(self):
            global indexes
            while (len(self.indexes) < 5):
                x = random.randint(0, 9)
                if x in self.indexes:
                    continue
                else:
                    self.indexes.append(x)
        def showresult(score):
            mixer.init()
            self.lblQuestion.destroy()
            self.r1.destroy()
            self.r2.destroy()
            self.r3.destroy()
            self.r4.destroy()
            self.labelimage = tk.Label(self,border=0)
            self.labelimage.pack(pady=(50, 30))
            self.labelresulttext = tk.Label(self,font=("Consolas", 20),)
            self.labelresulttext.pack()
            if score >= 20:
                verygood=mixer.Sound("verygood.wav")
                mixer.Sound.play(verygood)
                self.img = tk.PhotoImage(file="great.png")
                self.labelimage.configure(image=self.img)
                self.labelimage.image = self.img
                self.labelresulttext.configure(text="You Are Excellent !!")
            elif (score >= 10 and score < 20):
                verygood = mixer.Sound("verygood.wav")
                mixer.Sound.play(verygood)
                self.img = tk.PhotoImage(file="ok.png")
                self.labelimage.configure(image=self.img)
                self.labelimage.image = self.img
                self.labelresulttext.configure(text="You Can Be Better !!")
            else:
                self.img = tk.PhotoImage(file="bad.png")
                self.labelimage.configure(image=self.img)
                self.labelimage.image = self.img
                self.labelresulttext.configure(text="You Should Work Hard !!")
        def calc(self):
            global indexes,user_answer,answers
            x = 0
            score = 0
            for i in self.indexes:
                if self.user_answer[x] == self.answers[i]:
                    score = score + 5
                print(self.answers[i])
                x += 1

            print(score)
            showresult(score)
        self.ques = 1
        def selected():
            answer = mixer.Sound("answer.wav")
            sorry = mixer.Sound("sorry.wav")
            global radiovar, user_answer
            global lblQuestion, r1, r2,r3, r4
            global ques

            self.user_answer.append(self.x)
            print(self.user_answer)
            #self.x = self.radiovar.get()
            #self.user_answer.append(self.x)
            self.radiovar.set(-1)
            if self.ques < 5:
                self.lblQuestion.config(text=self.questions[self.indexes[self.ques]])
                self.r1['text'] = self.answers_choice[self.indexes[self.ques]][0]
                self.r2['text'] = self.answers_choice[self.indexes[self.ques]][1]
                self.r3['text'] = self.answers_choice[self.indexes[self.ques]][2]
                self.r4['text'] = self.answers_choice[self.indexes[self.ques]][3]
                self.ques += 1
                mixer.init()
                r = sr.Recognizer()
                r.dynamic_energy_threshold = False
                r.energy_threshold = 400
                with sr.Microphone() as source:
                    mixer.Sound.play(answer)
                    while True:
                        r.adjust_for_ambient_noise(source)
                        time.sleep(1.5)
                        try:
                            audio = r.listen(source, timeout=3, phrase_time_limit=3)
                            print("Recognizing...")
                            query = r.recognize_google(audio)
                            print(f"User said: {query}\n")
                            voice = query.lower()
                            if voice == '1' or voice == 'one' or voice=='a':
                                self.x = 0
                                my_thread7 = threading.Thread(target=selected, args=())
                                my_thread7.start()
                                break
                            elif voice == '2' or voice == 'to' or voice == 'two' or voice=='tu' or voice=='do' or voice=='b':
                                self.x = 1
                                my_thread7 = threading.Thread(target=selected, args=())
                                my_thread7.start()
                                break
                            elif voice == '3' or voice == 'three' or voice=='free' or voice=='c':
                                self.x = 2
                                my_thread7 = threading.Thread(target=selected, args=())
                                my_thread7.start()
                                break
                            elif voice == '4' or voice == 'for' or voice == 'four' or voice=='d':
                                self.x = 3
                                my_thread7 = threading.Thread(target=selected, args=())
                                my_thread7.start()
                                break
                            else:
                                mixer.Sound.play(sorry)
                        except sr.UnknownValueError:
                            # pygame.mixer.Sound.play(self.repeat_sound)
                            mixer.Sound.play(sorry)
                        except sr.RequestError:
                            mixer.Sound.play(sorry)
                            # pygame.mixer.Sound.play(self.requesterror_sound)
                        except Exception:
                            mixer.Sound.play(sorry)
            else:
                calc(self)
        def startquiz(self):
            global lblQuestion, r1, r2, r3,r4
            self.lblQuestion = tk.Label(self,text=self.questions[self.indexes[0]],font=("Consolas", 16),width=500,justify="center",wraplength=400,)
            self.lblQuestion.pack(pady=(100, 30))
            global radiovar
            self.radiovar = IntVar()
            self.radiovar.set(-1)
            self.r1 = tk.Radiobutton(self,text=self.answers_choice[self.indexes[0]][0],font=("Times", 12),value=0,variable=self.radiovar,command=selected,)
            self.r1.pack(pady=5)
            self.r2 = tk.Radiobutton(self,text=self.answers_choice[self.indexes[0]][1],font=("Times", 12),value=1,variable=self.radiovar,command=selected)
            self.r2.pack(pady=5)
            self.r3 = tk.Radiobutton(self,text=self.answers_choice[self.indexes[0]][2],font=("Times", 12),value=2,variable=self.radiovar,command=selected)
            self.r3.pack(pady=5)
            self.r4 = tk.Radiobutton(self,text=self.answers_choice[self.indexes[0]][3],font=("Times", 12),value=3,variable=self.radiovar,command=selected,)
            self.r4.pack(pady=5)
            mixer.init()
            answer = mixer.Sound("answer.wav")
            sorry= mixer.Sound("sorry.wav")
            r = sr.Recognizer()
            r.dynamic_energy_threshold = False
            r.energy_threshold = 400
            with sr.Microphone() as source:
                mixer.Sound.play(answer)
                while True:
                    r.adjust_for_ambient_noise(source)
                    time.sleep(1.5)
                    try:
                        audio = r.listen(source, timeout=3, phrase_time_limit=3)
                        print("Recognizing...")
                        query = r.recognize_google(audio)
                        print(f"User said: {query}\n")
                        voice = query.lower()
                        if voice == '1' or voice == 'one' or voice=='a':
                            self.x =0
                            my_thread7 = threading.Thread(target=selected, args=())
                            my_thread7.start()
                            break
                        elif voice == '2' or voice == 'to' or voice == 'two' or voice=='tu' or voice=='do' or voice=='b':
                            self.x = 1
                            my_thread7 = threading.Thread(target=selected, args=())
                            my_thread7.start()
                            break
                        elif voice == '3' or voice == 'three' or voice=='free' or voice=='c':
                            self.x = 2
                            my_thread7 = threading.Thread(target=selected, args=())
                            my_thread7.start()
                            break
                        elif voice == '4' or voice == 'for' or voice == 'four' or voice=='d':
                            self.x = 3
                            my_thread7 = threading.Thread(target=selected, args=())
                            my_thread7.start()
                            break
                        else:
                            mixer.Sound.play(sorry)

                    except sr.UnknownValueError:
                        # pygame.mixer.Sound.play(self.repeat_sound)
                        mixer.Sound.play(sorry)
                    except sr.RequestError:
                        mixer.Sound.play(sorry)
                        # pygame.mixer.Sound.play(self.requesterror_sound)
                    except Exception:
                        mixer.Sound.play(sorry)
        def startIspressed(self):
            self.labelimage.destroy()
            self.labeltext.destroy()
            self.lblInstruction.destroy()
            self.lblRules.destroy()
            self.btnStart.destroy()
            gen(self)
            my_thread = threading.Thread(target=startquiz, args=(self,))
            my_thread.start()


        def thread_check(self):
            mixer.init()
            welcome = mixer.Sound("welcome.wav")
            sorry = mixer.Sound("sorry.wav")
            self.img91 = tk.PhotoImage(file="quiz_factory.png")
            self.labelimage = tk.Label(self,image=self.img91,)
            self.labelimage.pack(pady=(40, 0))
            self.labeltext = tk.Label(self,text="Quiz Factory",font=("Comic sans MS", 26, "bold"),)
            self.labeltext.pack(pady=(10, 30))
            self.img92 = tk.PhotoImage(file="Frame.png")
            self.btnStart = tk.Button(self,image=self.img92,relief=FLAT,border=0,command=startIspressed,)
            self.btnStart.pack()
            self.lblInstruction = tk.Label(self,text="Read The Rules And\nClick Start Once You Are ready",font=("Consolas", 14,"bold"),justify="center",)
            self.lblInstruction.pack(pady=(10, 50))
            self.lblRules = tk.Label(self,text="This quiz contains 10 questions\nYou will get 20 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",width=100,font=("Times", 14),background="#000000",foreground="#FACA2F",)
            self.lblRules.pack()
            r = sr.Recognizer()
            r.dynamic_energy_threshold = False
            r.energy_threshold = 400
            with sr.Microphone() as source:
                mixer.Sound.play(welcome)
                while True:
                    r.adjust_for_ambient_noise(source)
                    time.sleep(1.5)
                    try:
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing...")
                        query = r.recognize_google(audio)
                        print(f"User said: {query}\n")
                        voice = query.lower()
                        if voice == 'start' or voice =='open':
                            my_thread7 = threading.Thread(target=startIspressed, args=(self,))
                            my_thread7.start()
                            break
                        else:
                            mixer.Sound.play(sorry)
                    except sr.UnknownValueError:
                        # pygame.mixer.Sound.play(self.repeat_sound)
                        mixer.Sound.play(sorry)
                    except sr.RequestError:
                        mixer.Sound.play(sorry)
                        # pygame.mixer.Sound.play(self.requesterror_sound)
                    except Exception:
                        mixer.Sound.play(sorry)
        #self.speak = wincl.Dispatch("SAPI.SpVoice")
        #self.speak.Speak("Welcome to quiz factory")
        self.my_thread = threading.Thread(target=thread_check, args=(self,))
        self.my_thread.start()
#these are the inside buttons of introduction(pageone)
class ibtn1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Getting Started", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="How to Get Started With Python?", font=('Helvetica', 18, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort, text="Python is a cross-platform programming language, meaning, it runs on multiple platforms like Windows, MacOS, Linux and has even been ported to the Java and .NET virtual machines. It is free and open source.Even though most of today’s Linux and Mac have Python preinstalled in it, the version might be out-of-date. So, it is always a good idea to install the most current version.", font=('Helvetica', 14),bg="#ffffff", wraplength = 500,pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="The Easiest Way to Run Python", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort, text="The easiest way to run Python is by using Thonny IDE. The Thonny IDE comes with the latest version of Python bundled in it. So you don't have to install Python separately.Follow the following steps to run Python on your computer.Download Thonny IDE.Run the installer to install Thonny on your computer.Go to File > New. Then save the file with .py extension. For example, hello.py, example.py etc.You can give any name to the file. However, the file name should end with .py Write Python code in the file and save it.", font=('Helvetica', 14),bg="#ffffff", wraplength = 500,pady=10,fg="#000000").pack(side="top", anchor="center")
        self.image12=tk.PhotoImage(file="hello.png")
        tk.Label(self.scrollFrame.viewPort, image=self.image12,bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Keywords and Identifiers", font=('Helvetica', 30, "bold"), bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Python Keywords", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Keywords are the reserved words in Python.We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structure of the Python language.In Python, keywords are case sensitive.There are 33 keywords in Python 3.7. This number can vary slightly in the course of time.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Identifiers", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Things to Remember", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Python is a case-sensitive language. This means, Variable and variable are not the same. Always name identifiers that make sense.While, c = 10 is valid. Writing count = 10 would make more sense and it would be easier to figure out what it does even when you look at your code after a long gap.Multiple words can be separated using an underscore, this_is_a_long_variable.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Statement, Indentation and Comments", font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Python Statement", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Instructions that a Python interpreter can execute are called statements. For example, a = 1 is an assignment statement. if statement, for statement, while statement etc. are other kinds of statements which will be discussed later.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Indentation", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Most of the programming languages like C, C++, Java use braces { } to define a block of code. Python uses indentation.A code block (body of a function, loop etc.) starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Comments", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Comments are very important while writing a program. It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out. You might forget the key details of the program you just wrote in a month's time. So taking time to explain these concepts in form of comments is always fruitful.In Python, we use the hash (#) symbol to start writing a comment.It extends up to the newline character. Comments are for programmers for better understanding of a program. Python Interpreter ignores comment. ",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Variables, Constants and Literals", font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Python Variables", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data which can be changed later throughout programming.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Constants", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.Non technically, you can think of constant as a bag to store some books and those books cannot be replaced once placed inside the bag.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Literals", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:\nNumeric Literals:\nNumeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types Integer, Float, and Complex.\nString literals:\nA string literal is a sequence of characters surrounded by quotes. We can use both single, double or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Data Types",font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Data types in Python", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Every value in Python has a datatype. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Numbers", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python.We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.\nIntegers can be of any length, it is only limited by the memory available.A floating point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is integer, 1.0 is floating point number.Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python List", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ].We can use the slicing operator [ ] to extract an item or a range of items from a list. Index starts form 0 in Python.Lists are mutable, meaning, value of elements of a list can be altered.", font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Tuple", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified.Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically.It is defined within parentheses () where items are separated by commas.\nt = (5,'program', 1+3j)\nWe can use the slicing operator [] to extract items but we cannot change its value.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Strings", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes. ",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn6(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Type Conversion and Type Casting",font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Type Conversion:", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion. Python has two types of type conversion.\nImplicit Type Conversion\nExplicit Type Conversion.",font=('Helvetica', 14,"bold"), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Implicit Type Conversion:", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.Lets see an example where Python promotes conversion of lower datatype (integer) to higher data type (float) to avoid data loss.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Explicit Type Conversion:", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.",
        font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn7(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Input, Output and Import",font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Python Input", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Up till now, our programs were static. The value of variables were defined or hard coded into the source code.To allow flexibility we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is where prompt is the string we wish to display on the screen. It is optional.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Output", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="We use the print() function to output data to the standard output device (screen).We can also output data to a file, but this will be discussed later. ",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Python Import", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="When our program grows bigger, it is a good idea to break it into different modules.A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension (.py.) Definitions inside a module can be imported to another module or the interactive interpreter in Python. We use the import keyword to do this.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Operators",font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="Arithmetic operators", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Comparison operators", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Comparison operators are used to compare values. It either returns True or False according to the condition.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Logical operators", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Logical operators are the and, or, not operators.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Bitwise operators", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.For example, 2 is 10 in binary and 7 is 111.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="Assignment operators", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="Assignment operators are used in Python to assign values to variables.a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class ibtn9(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Python Namespace and Scope",font=('Helvetica', 30, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=5)
        tk.Label(self.scrollFrame.viewPort, text="What is Name in Python?", font=('Helvetica', 18, "bold"),bg="#ffffff",fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="If you have ever read 'The Zen of Python(type import this in Python interpreter), the last line states, Namespaces are one honking great idea -- let's do more of those! So what are these mysterious namespaces? Let us first look at what name is.Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function, id().",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10,fg="#000000").pack(side="top", anchor="center")
        tk.Label(self.scrollFrame.viewPort, text="What is a Namespace in Python?", font=('Helvetica', 18, "bold"),bg="#ffffff", fg="#000000").pack(side="top", anchor="center", pady=0)
        tk.Label(self.scrollFrame.viewPort,text="So now that we understand what names are, we can move on to the concept of namespaces.To simply put it, namespace is a collection of names.In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.Different namespaces can co-exist at a given time but are completely isolated.A namespace containing all the built-in names is created when we start the Python interpreter and exists as long we don't exit.This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program. Each module creates its own global namespace.These different namespaces are isolated. Hence, the same name that may exist in different modules do not collide.Modules can have various functions and classes. A local namespace is created when a function is called, which has all the names defined in it. Similar, is the case with class. Following diagram may help to clarify this concept.",font=('Helvetica', 14), bg="#ffffff", wraplength=500, pady=10, fg="#000000").pack(side="top",anchor="center")
        frame = Frame(self)
        self.img14 = PhotoImage(file="quiz_factory1.png")
        self.img15 = PhotoImage(file="goback.png")
        self.img16 = PhotoImage(file="quit1.png")
        b1 = Button(frame, image=self.img14, width=180, background="#ffffff", command=lambda: master.switch_frame(Quiz))
        b1.pack(side=LEFT, padx=(140, 0), pady=2)
        b2 = Button(frame, image=self.img15, background="#ffffff", command=lambda: master.switch_frame(PageOne))
        b2.pack(side=LEFT, padx=(190, 0), pady=2)
        def quit(self):
            self.app.destroy()
        b4 = Button(frame, image=self.img16, width=180, background="#ffffff", command=self.quit)
        b4.pack(side=LEFT, padx=(200, 0), pady=2)
        frame.pack(side=BOTTOM, padx=(35, 35), fill=X)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
#these are the further button of title pages
class kbtn1(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn4(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn5(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn6(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn7(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn8(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn9(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn10(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn11(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn12(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn13(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn14(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn15(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn15(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn16(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn17(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn18(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn19(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn20(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn21(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn22(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn23(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.scrollFrame = ScrollFrame(self)
        tk.Frame.configure(self)
        tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
        self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn24(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x", pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn25(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn26(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x", pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn27(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn28(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn29(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn30(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",
                          command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
class kbtn31(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master)
                self.scrollFrame = ScrollFrame(self)
                tk.Frame.configure(self)
                tk.Label(self.scrollFrame.viewPort, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top",fill="x",pady=5)
                tk.Button(self.scrollFrame.viewPort, text="Go back to start page",command=lambda: master.switch_frame(TitlePage)).pack()
                self.scrollFrame.pack(side="top", fill="both", expand=True)
if __name__ == "__main__":
    app = SampleApp()
    app.title("Pydroid: Learn Python")
    app.geometry("1300x700")
    app.iconbitmap(default='ai1.ico')
    app.mainloop()
