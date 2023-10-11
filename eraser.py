
import tkinter
from tkinter import filedialog
import os
import sys
import pathlib
import time
import shutil
from send2trash import send2trash



def kaynakDosyaSec ():
    global kaynakdir
    root= tkinter.Tk()
    root.withdraw()
    curdir=os.getcwd()
    kaynakdir=filedialog.askdirectory(parent=root, initialdir=curdir, title="Kaynak Dosya Seç")
    return kaynakdir
def hedefDosyaSec ():
    global hedefdir
    root= tkinter.Tk()
    root.withdraw()
    curdir=os.getcwd()
    hedefdir=filedialog.askdirectory(parent=root, initialdir=curdir, title="Hedef Dosya Seç")
    return hedefdir
def listele ():
    #dosya seçme
    kaynakDosyaSec()
    hedefDosyaSec()
    #dosya toplama
    print("Kaynak Klasör Listeleniyor...")
    kaynakDosyalar=pathlib.Path(kaynakdir)
    kayDosLis=kaynakDosyalar.rglob("*")
    print("Hedef Klasör Listeleniyor...")
    hedefDosyalar=pathlib.Path(hedefdir)
    hedDosLis=hedefDosyalar.rglob("*")
    global klist
    klist=[]
    global hlist
    hlist=[]
    #liste hazırlama
    for k in kayDosLis:
        if k.is_file():
            klist.append(k)
    
    for h in hedDosLis:
        if h.is_file():
            hlist.append(h)
            
    a=0
    for i in klist:
        for j in hlist:
            try:
                if i.name==j.name and i.stat().st_size==j.stat().st_size:
                    print(j.name)
                    send2trash(j)
                    a=a+1
            except:
                print("Hata oluştu")        
    print("{} Adet Dosya Çöp Kutusuna Taşındı".format(a))            
    time.sleep(5)            
                
   
listele()
