import tkinter as tk
import winsound
import random
root=tk.Tk()
root.geometry('300x300+'+str((root.winfo_screenwidth()//2)-(root.winfo_width()//2))+'+'+str((root.winfo_screenheight()//2)-(root.winfo_height()//2)))
root.title('Breakout')
root.resizable(width='No', height='No')
root.attributes("-toolwindow", 1)
try:
    konfiguration=open('data/konfiguration', 'r')
    lesen=konfiguration.read()
    config=lesen.split(' ')
    fg=config[0]
    bg=config[1]
    ton=int(config[2])
    schwierigkeit=int(config[3])
    konfiguration.close()
except:
    konfiguration2=open('data/konfiguration', 'w')
    config2=konfiguration2.write('black white 1 0')
    konfiguration2.close()
    konfiguration=open('data/konfiguration', 'r')
    lesen=konfiguration.read()
    config=lesen.split(' ')
    fg=config[0]
    bg=config[1]
    ton=int(config[2])
    schwierigkeit=int(config[3])
    konfiguration.close()
x=0
y=0
def menü_auswahl_prüfen(event):
    global menü
    global einstell_menü
    global ton_menü
    global schwierigkeits_menü
    global farb_menü
    global winkel
    global x_ball
    global y_ball
    global ton
    global schwierigkeit
    global bg
    global fg
    global x_w
    global y_w
    global k1_l
    global k2_l
    global k3_l
    global k4_l
    global k5_l
    global k6_l
    global k7_l
    global k8_l
    global k9_l
    global k10_l
    global k11_l
    global k12_l
    global k13_l
    global k14_l
    global k15_l
    global k16_l
    global k17_l
    global k18_l
    global k19_l
    if menü==1:
        if x<=120:
            einstellungen.place_forget()
            hauptmenü.place_forget()
            spiel_starten.place_forget()
            winkel=random.randint(210, 330)
            while(winkel<=190) and (winkel >= 170):
                winkel=random.randint(210, 330)
            level_anzeige.config(text='Level '+str(level))
            level_anzeige.place(x=0, y=100, width=300, height=100)
            root.update()
            root.after(1000, None)
            level_anzeige.place_forget()
            root.after(0, winkel_drehen)
            root.after(0, ball_bewegen)
            winsound.PlaySound(None, winsound.SND_PURGE)
            menü=0
            x_ball=140
            y_ball=140
            x_w=0
            y_w=0
            if schwierigkeit==0:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
                k7_l=0
                k8_l=0
                k9_l=0
                k10_l=0
                k11_l=0
                k12_l=0
                k13_l=0
                k14_l=0
                k15_l=0
                k16_l=0
                k17_l=0
                k18_l=0
                k19_l=0
            elif schwierigkeit==1:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k7.place(x=0, y=20, width=25, height=20)
                k8.place(x=25, y=20, width=50, height=20)
                k9.place(x=75, y=20, width=50, height=20)
                k10.place(x=125, y=20, width=50, height=20)
                k11.place(x=175, y=20, width=50, height=20)
                k12.place(x=225, y=20, width=50, height=20)
                k13.place(x=275, y=20, width=25, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
                k7_l=1
                k8_l=1
                k9_l=1
                k10_l=1
                k11_l=1
                k12_l=1
                k13_l=1
                k14_l=0
                k15_l=0
                k16_l=0
                k17_l=0
                k18_l=0
                k19_l=0
            elif schwierigkeit==2:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k7.place(x=0, y=20, width=25, height=20)
                k8.place(x=25, y=20, width=50, height=20)
                k9.place(x=75, y=20, width=50, height=20)
                k10.place(x=125, y=20, width=50, height=20)
                k11.place(x=175, y=20, width=50, height=20)
                k12.place(x=225, y=20, width=50, height=20)
                k13.place(x=275, y=20, width=25, height=20)
                k14.place(x=0, y=40, width=50, height=20)
                k15.place(x=50, y=40, width=50, height=20)
                k16.place(x=100, y=40, width=50, height=20)
                k17.place(x=150, y=40, width=50, height=20)
                k18.place(x=200, y=40, width=50, height=20)
                k19.place(x=250, y=40, width=50, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
                k7_l=1
                k8_l=1
                k9_l=1
                k10_l=1
                k11_l=1
                k12_l=1
                k13_l=1
                k14_l=1
                k15_l=1
                k16_l=1
                k17_l=1
                k18_l=1
                k19_l=1
        else:
            einstellungen.place_forget()
            hauptmenü.place_forget()
            spiel_starten.place_forget()
            einstellungen_überschrifft.place(x=5, y=5, width=290, height=100)
            einstell_menü=1
            menü=0
            einstellungen_farbe.place(x=0, y=240, width=100, height=30)
            einstellungen_schwierigkeit.place(x=100, y=240, width=100, height=30)
            einstellungen_ton.place(x=200, y=240, width=100, height=30)
    elif einstell_menü==1:
        einstell_menü=2
        if x<=70:
            einstellungen_farbe_weis.place(x=15, y=240, width=30, height=30)
            einstellungen_farbe_blau.place(x=75, y=240, width=30, height=30)
            einstellungen_farbe_grün.place(x=135, y=240, width=30, height=30)
            einstellungen_farbe_gelb.place(x=195, y=240, width=30, height=30)
            einstellungen_farbe_schwarz.place(x=255, y=240, width=30, height=30)
            farb_menü=1
        elif x<=170:
            einstellungen_schwierigkeit_leicht.place(x=0, y=240, width=100, height=30)
            einstellungen_schwierigkeit_mittel.place(x=100, y=240, width=100, height=30)
            einstellungen_schwierigkeit_schwer.place(x=200, y=240, width=100, height=30)
            schwierigkeits_menü=1
        elif x<=240:
            einstellungen_ton_an.place(x=5, y=240, width=140, height=30)
            einstellungen_ton_aus.place(x=155, y=240, width=140, height=30)
            ton_menü=1
        einstellungen_farbe.place_forget()
        einstellungen_schwierigkeit.place_forget()
        einstellungen_ton.place_forget()
    elif farb_menü==1:
        if x<=30:
            bg='white'
            fg='black'
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            einstellungen_farbe_weis.config(relief='sunken')
            einstellungen_farbe_blau.config(relief='groove')
            einstellungen_farbe_grün.config(relief='groove')
            einstellungen_farbe_gelb.config(relief='groove')
            einstellungen_farbe_schwarz.config(relief='groove')
        elif x<=90:
            bg='#afeeee'
            fg='black'
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            einstellungen_farbe_weis.config(relief='groove')
            einstellungen_farbe_blau.config(relief='sunken')
            einstellungen_farbe_grün.config(relief='groove')
            einstellungen_farbe_gelb.config(relief='groove')
            einstellungen_farbe_schwarz.config(relief='groove')
        elif x<=150:
            bg='#ccffcc'
            fg='black'
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            einstellungen_farbe_weis.config(relief='groove')
            einstellungen_farbe_blau.config(relief='groove')
            einstellungen_farbe_grün.config(relief='sunken')
            einstellungen_farbe_gelb.config(relief='groove')
            einstellungen_farbe_schwarz.config(relief='groove')
        elif x<=210:
            bg='#ffffcc'
            fg='black'
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            einstellungen_farbe_weis.config(relief='groove')
            einstellungen_farbe_blau.config(relief='groove')
            einstellungen_farbe_grün.config(relief='groove')
            einstellungen_farbe_gelb.config(relief='sunken')
            einstellungen_farbe_schwarz.config(relief='groove')
        elif x<=300:
            bg='black'
            fg='white'
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            einstellungen_farbe_weis.config(relief='groove')
            einstellungen_farbe_blau.config(relief='groove')
            einstellungen_farbe_grün.config(relief='groove')
            einstellungen_farbe_gelb.config(relief='groove')
            einstellungen_farbe_schwarz.config(relief='sunken')
        root.config(bg=bg)
        ball.config(bg=bg)
        balken.config(bg=fg)
        hauptmenü.config(bg=bg)
        spiel_starten.config(bg=bg, fg=fg)
        einstellungen.config(bg=bg, fg=fg)
        einstellungen_überschrifft.config(bg=bg)
        einstellungen_farbe.config(bg=bg, fg=fg)
        einstellungen_schwierigkeit.config(bg=bg, fg=fg)
        einstellungen_schwierigkeit_leicht.config(bg=bg)
        einstellungen_schwierigkeit_mittel.config(bg=bg)
        einstellungen_schwierigkeit_schwer.config(bg=bg)
        einstellungen_ton.config(bg=bg, fg=fg)
        level_anzeige.config(bg=bg)
        einstellungen_ton_an.config(bg=bg)
        einstellungen_ton_aus.config(bg=bg)
    elif ton_menü==1:
        if x<=120:
            ton=1
            einstellungen_ton_an.config(fg=fg2)
            einstellungen_ton_aus.config(fg=fg)
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            winsound.PlaySound('data/Titel.WAV', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
        else:
            ton=0
            einstellungen_ton_an.config(fg=fg)
            einstellungen_ton_aus.config(fg=fg2)
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
            winsound.PlaySound(None, winsound.SND_PURGE)
    elif schwierigkeits_menü==1:
        if x<=70:
            schwierigkeit=0
            einstellungen_schwierigkeit_leicht.config(fg=fg2)
            einstellungen_schwierigkeit_mittel.config(fg=fg)
            einstellungen_schwierigkeit_schwer.config(fg=fg)
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
        elif x<=170:
            schwierigkeit=1
            einstellungen_schwierigkeit_leicht.config(fg=fg)
            einstellungen_schwierigkeit_mittel.config(fg=fg2)
            einstellungen_schwierigkeit_schwer.config(fg=fg)
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
        else:
            schwierigkeit=2
            einstellungen_schwierigkeit_leicht.config(fg=fg)
            einstellungen_schwierigkeit_mittel.config(fg=fg)
            einstellungen_schwierigkeit_schwer.config(fg=fg2)
            konfiguration2=open('data/konfiguration', 'w')
            config2=konfiguration2.write(fg+' '+bg+' '+str(ton)+' '+str(schwierigkeit))
            konfiguration2.close()
def zum_menü_gehen(event):
    global menü
    global einstell_menü
    global ton_menü
    global schwierigkeits_menü
    global farb_menü
    if (menü==0) and (einstell_menü==1):
        spiel_starten.place(x=5, y=240, width=145, height=30)
        einstellungen.place(x=150, y=240, width=145, height=30)
        hauptmenü.place(x=5, y=100, width=290, height=50)
        einstell_menü=0
        einstellungen_überschrifft.place_forget()
        einstellungen_farbe.place_forget()
        einstellungen_schwierigkeit.place_forget()
        einstellungen_ton.place_forget()
        menü=1
        if ton==1:
            winsound.PlaySound('data/Titel.WAV', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    elif (einstell_menü==0) and (menü==0):
        ball.place_forget()
        menü=1
        spiel_starten.place(x=5, y=240, width=145, height=30)
        einstellungen.place(x=150, y=240, width=145, height=30)
        hauptmenü.place(x=5, y=100, width=290, height=50)
        k1.place_forget()
        k2.place_forget()
        k3.place_forget()
        k4.place_forget()
        k5.place_forget()
        k6.place_forget()
        k7.place_forget()
        k8.place_forget()
        k9.place_forget()
        k10.place_forget()
        k11.place_forget()
        k12.place_forget()
        k13.place_forget()
        k14.place_forget()
        k15.place_forget()
        k16.place_forget()
        k17.place_forget()
        k18.place_forget()
        k19.place_forget()
        if ton==1:
            winsound.PlaySound('data/Titel.WAV', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
    elif einstell_menü==2:
        einstell_menü=1
        farb_menü=0
        ton_menü=0
        schwierigkeits_menü=0
        farb_menü=0
        einstellungen_farbe.place(x=0, y=240, width=100, height=30)
        einstellungen_schwierigkeit.place(x=100, y=240, width=100, height=30)
        einstellungen_ton.place(x=200, y=240, width=100, height=30)
        einstellungen_farbe_weis.place_forget()
        einstellungen_farbe_blau.place_forget()
        einstellungen_farbe_grün.place_forget()
        einstellungen_farbe_gelb.place_forget()
        einstellungen_farbe_schwarz.place_forget()
        einstellungen_ton_an.place_forget()
        einstellungen_ton_aus.place_forget()
        einstellungen_schwierigkeit_leicht.place_forget()
        einstellungen_schwierigkeit_mittel.place_forget()
        einstellungen_schwierigkeit_schwer.place_forget()
def winkel_drehen():
    global winkel
    global x_w
    global y_w
    if winkel%360 <= 45:
        x_w=45
        y_w=0-winkel%360
    elif winkel%360<=90:
        x_w=90-winkel%360
        y_w=-45
    elif winkel%360<=135:
        winkel=winkel%360-90
        x_w=0-winkel%360
        y_w=-45
    elif winkel%360<=180:
        x_w=-45
        y_w=(180-winkel%360)*(-1)
    elif winkel%360<=225:
        winkel=winkel%360-180
        x_w=-45
        y_w=(0-winkel%360)*(-1)
    elif winkel%360<=270:
        x_w=(270-winkel%360)*(-1)
        y_w=45
    elif winkel%360<=315:
        winkel=winkel%360-270
        x_w=(0-winkel%360)*(-1)
        y_w=45
    elif winkel%360<=360:
        x_w=45
        y_w=360-winkel%360
def ball_bewegen():
    global winkel
    global x_w
    global y_w
    global geschwindigkeit
    global x_ball
    global y_ball
    global level
    global k1_l
    global k2_l
    global k3_l
    global k4_l
    global k5_l
    global k6_l
    global k7_l
    global k8_l
    global k9_l
    global k10_l
    global k11_l
    global k12_l
    global k13_l
    global k14_l
    global k15_l
    global k16_l
    global k17_l
    global k18_l
    global k19_l
    global menü
    global x
    while(menü!=1):
        root.after(1, None)
        if (x_ball<=0) or (x_ball>=280):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            x_w=x_w*(-1)
        if  (y_ball>=280):
            level=1
            menü=1
            ball.place_forget()
            level_anzeige.config(text='Verloren')
            k1.place_forget()
            k2.place_forget()
            k3.place_forget()
            k4.place_forget()
            k5.place_forget()
            k6.place_forget()
            k7.place_forget()
            k8.place_forget()
            k9.place_forget()
            k10.place_forget()
            k11.place_forget()
            k12.place_forget()
            k13.place_forget()
            k14.place_forget()
            k15.place_forget()
            k16.place_forget()
            k17.place_forget()
            k18.place_forget()
            k19.place_forget()
            level_anzeige.place(x=0, y=100, width=300, height=100)
            root.update()
            root.after(2000, None)
            root.update()
            level_anzeige.place_forget()
            spiel_starten.place(x=5, y=240, width=145, height=30)
            einstellungen.place(x=150, y=240, width=145, height=30)
            hauptmenü.place(x=5, y=100, width=290, height=50)
            if ton==1:
                winsound.PlaySound('data/Titel.WAV', winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)
            break
        if (y_ball<=0):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            y_w=y_w*(-1)
        if (y_ball>=260) and (x_ball>=x-10) and (x_ball<=x+50):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            y_w=y_w*(-1)
        if (k1_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=-20) and (x_ball<=50):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k1.place_forget()
            k1_l=0
            y_w=y_w*(-1)
        elif (k2_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=30) and (x_ball<=100):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k2.place_forget()
            k2_l=0
            y_w=y_w*(-1)
        elif (k3_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=80) and (x_ball<=150):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k3.place_forget()
            k3_l=0
            y_w=y_w*(-1)
        elif (k4_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=130) and (x_ball<=200):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k4.place_forget()
            k4_l=0
            y_w=y_w*(-1)
        elif (k5_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=180) and (x_ball<=250):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k5.place_forget()
            k5_l=0
            y_w=y_w*(-1)
        elif (k6_l==1) and (y_ball<=20) and (y_ball>=-20) and (x_ball>=230) and (x_ball<=300):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k6.place_forget()
            k6_l=0
            y_w=y_w*(-1)
        elif (k7_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=-20) and (x_ball<=25):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k7.place_forget()
            k7_l=0
            y_w=y_w*(-1)
        elif (k8_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=5) and (x_ball<=75):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k8.place_forget()
            k8_l=0
            y_w=y_w*(-1)
        elif (k9_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=55) and (x_ball<=125):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k9.place_forget()
            k9_l=0
            y_w=y_w*(-1)
        elif (k10_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=105) and (x_ball<=175):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k10.place_forget()
            k10_l=0
            y_w=y_w*(-1)
        elif (k11_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=155) and (x_ball<=225):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k11.place_forget()
            k11_l=0
            y_w=y_w*(-1)
        elif (k12_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=205) and (x_ball<=275):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k12.place_forget()
            k12_l=0
            y_w=y_w*(-1)
        elif (k13_l==1) and (y_ball<=40) and (y_ball>=0) and (x_ball>=255) and (x_ball<=300):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k13.place_forget()
            k13_l=0
            y_w=y_w*(-1)
        elif (k14_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=-20) and (x_ball<=50):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k14.place_forget()
            k14_l=0
            y_w=y_w*(-1)
        elif (k15_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=30) and (x_ball<=100):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k15.place_forget()
            k15_l=0
            y_w=y_w*(-1)
        elif (k16_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=80) and (x_ball<=150):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k16.place_forget()
            k16_l=0
            y_w=y_w*(-1)
        elif (k17_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=130) and (x_ball<=200):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k17.place_forget()
            k17_l=0
            y_w=y_w*(-1)
        elif (k18_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=180) and (x_ball<=250):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k18.place_forget()
            k18_l=0
            y_w=y_w*(-1)
        elif (k19_l==1) and (y_ball<=60) and (y_ball>=20) and (x_ball>=230) and (x_ball<=300):
            if ton==1:
                winsound.PlaySound('data/ball.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
            k19.place_forget()
            k19_l=0
            y_w=y_w*(-1)
        if k1_l+k2_l+k3_l+k4_l+k5_l+k6_l+k7_l+k8_l+k9_l+k10_l+k11_l+k12_l+k13_l+k14_l+k15_l+k16_l+k17_l+k18_l+k19_l==0:
            level=level+1
            winkel=random.randint(210, 330)
            while(winkel>=290) and (winkel <= 250):
                winkel=random.randint(210, 330)
            level_anzeige.config(text='Level '+str(level))
            level_anzeige.place(x=0, y=100, width=300, height=100)
            root.update()
            root.after(1000, None)
            level_anzeige.place_forget()
            root.after(0, winkel_drehen)
            root.after(0, ball_bewegen)
            winsound.PlaySound(None, winsound.SND_PURGE)
            menü=0
            x_ball=140
            y_ball=140
            x_w=0
            y_w=0
            if schwierigkeit==0:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
            elif schwierigkeit==1:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k7.place(x=0, y=20, width=25, height=20)
                k8.place(x=25, y=20, width=50, height=20)
                k9.place(x=75, y=20, width=50, height=20)
                k10.place(x=125, y=20, width=50, height=20)
                k11.place(x=175, y=20, width=50, height=20)
                k12.place(x=225, y=20, width=50, height=20)
                k13.place(x=275, y=20, width=25, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
                k7_l=1
                k8_l=1
                k9_l=1
                k10_l=1
                k11_l=1
                k12_l=1
                k13_l=1
            elif schwierigkeit==2:
                k1.place(x=0, y=0, width=50, height=20)
                k2.place(x=50, y=0, width=50, height=20)
                k3.place(x=100, y=0, width=50, height=20)
                k4.place(x=150, y=0, width=50, height=20)
                k5.place(x=200, y=0, width=50, height=20)
                k6.place(x=250, y=0, width=50, height=20)
                k7.place(x=0, y=20, width=25, height=20)
                k8.place(x=25, y=20, width=50, height=20)
                k9.place(x=75, y=20, width=50, height=20)
                k10.place(x=125, y=20, width=50, height=20)
                k11.place(x=175, y=20, width=50, height=20)
                k12.place(x=225, y=20, width=50, height=20)
                k13.place(x=275, y=20, width=25, height=20)
                k14.place(x=0, y=40, width=50, height=20)
                k15.place(x=50, y=40, width=50, height=20)
                k16.place(x=100, y=40, width=50, height=20)
                k17.place(x=150, y=40, width=50, height=20)
                k18.place(x=200, y=40, width=50, height=20)
                k19.place(x=250, y=40, width=50, height=20)
                k1_l=1
                k2_l=1
                k3_l=1
                k4_l=1
                k5_l=1
                k6_l=1
                k7_l=1
                k8_l=1
                k9_l=1
                k10_l=1
                k11_l=1
                k12_l=1
                k13_l=1
                k14_l=1
                k15_l=1
                k16_l=1
                k17_l=1
                k18_l=1
                k19_l=1
        geschwindigkeit=(level*2)+(schwierigkeit*3)+5
        vor_x=x_w/1000*geschwindigkeit
        vor_y=y_w/1000*geschwindigkeit*(-1)
        x_ball=x_ball+vor_x
        y_ball=y_ball+vor_y
        ball.place(x=x_ball, y=y_ball, width=20, height=20)
        root.update()
def links(event):
    global x
    for i in range(0, 1):
        i=0
        if x>0:
            x=x-10
            balken.place(x=x, y=280)
            if x<=240:
                einstellungen_farbe.config(fg=fg)
                einstellungen_schwierigkeit.config(fg=fg)
                einstellungen_ton.config(fg=fg2)
                einstellungen.config(fg=fg2)
                spiel_starten.config(fg=fg)
            if x<=170:
                einstellungen_farbe.config(fg=fg)
                einstellungen_schwierigkeit.config(fg=fg2)
                einstellungen_ton.config(fg=fg)
            if x<=120:
                spiel_starten.config(fg=fg2)
                einstellungen.config(fg=fg)
            if x<=70:
                einstellungen_farbe.config(fg=fg2)
                einstellungen_schwierigkeit.config(fg=fg)
                einstellungen_ton.config(fg=fg)
            root.update()
def rechts(event):
    global x
    for i in range(0, 1):
        i=0
        if x<240:
            x=x+10
            balken.place(x=x, y=280)
            if x<=240:
                einstellungen_farbe.config(fg=fg)
                einstellungen_schwierigkeit.config(fg=fg)
                einstellungen_ton.config(fg=fg2)
                einstellungen.config(fg=fg2)
                spiel_starten.config(fg=fg)
            if x<=170:
                einstellungen_farbe.config(fg=fg)
                einstellungen_schwierigkeit.config(fg=fg2)
                einstellungen_ton.config(fg=fg)
            if x<=120:
                spiel_starten.config(fg=fg2)
                einstellungen.config(fg=fg)
            if x<=70:
                einstellungen_farbe.config(fg=fg2)
                einstellungen_schwierigkeit.config(fg=fg)
                einstellungen_ton.config(fg=fg)
            root.update()

x=120
level=1
fg2='#CC0000'
farb_menü=0
schwierigkeits_menü=0
ton_menü=0
menü=1
einstell_menü=0
root.bind('<Return>', menü_auswahl_prüfen)
balken=tk.Label(root, bg=fg, relief='groove')
level_anzeige=tk.Label(root, font=('Segoe Print', 30), bg=bg, fg=fg2)
ball=tk.Label(root, bg=bg, fg=fg2, text='\u26AB', font=('Arial', 20))
balken.place(x=120, y=280, width=60, height=5)
hauptmenü=tk.Label(root, bg=bg, fg=fg2, text='breakout', font=('Segoe Print', 30))
spiel_starten=tk.Label(root, fg=fg2, bg=bg, text='Spiel starten')
einstellungen=tk.Label(root, fg=fg, bg=bg, text='Einstellungen')
einstellungen_überschrifft=tk.Label(root, fg=fg2, bg=bg, text='Einstellungen', font=('Segoe Print', 20))
einstellungen_farbe=tk.Label(root, text='Farbe', bg=bg, fg=fg)
einstellungen_schwierigkeit=tk.Label(root, text='Schwierigkeit', bg=bg, fg=fg)
einstellungen_schwierigkeit_leicht=tk.Label(root, text='leicht', bg=bg, fg=fg)
einstellungen_schwierigkeit_mittel=tk.Label(root, text='mittel', bg=bg, fg=fg)
einstellungen_schwierigkeit_schwer=tk.Label(root, text='schwer', bg=bg, fg=fg)
einstellungen_ton=tk.Label(root, text='Ton', bg=bg, fg=fg)
einstellungen_ton_an=tk.Label(root, text='An', bg=bg, fg=fg)
einstellungen_ton_aus=tk.Label(root, text='Aus', bg=bg, fg=fg)
einstellungen_farbe_weis=tk.Label(root, bg='white', relief='groove')
einstellungen_farbe_blau=tk.Label(root, bg='#afeeee', relief='groove')
einstellungen_farbe_grün=tk.Label(root, bg='#ccffcc', relief='groove')
einstellungen_farbe_gelb=tk.Label(root, bg='#ffffcc', relief='groove')
einstellungen_farbe_schwarz=tk.Label(root, bg='black', relief='groove')
if bg=='white':
    einstellungen_farbe_weis.config(relief='sunken')
elif bg=='#afeeee':
    einstellungen_farbe_blau.config(relief='sunken')
elif bg=='#ccffcc':
    einstellungen_farbe_grün.config(relief='sunken')
elif bg=='#ffffcc':
    einstellungen_farbe_gelb.config(relief='sunken')
elif bg=='black':
    einstellungen_farbe_schwarz.config(relief='sunken')
else:
    bg='white'
    einstellungen_farbe_weis.config(relief='sunken')
if schwierigkeit==0:
    einstellungen_schwierigkeit_leicht.config(fg=fg2)
elif schwierigkeit==1:
    einstellungen_schwierigkeit_mittel.config(fg=fg2)
elif schwierigkeit==2:
    einstellungen_schwierigkeit_schwer.config(fg=fg2)
else:
    schwierigkeit=0
    einstellungen_schwierigkeit_leicht.config(fg=fg2)
if ton==0:
    einstellungen_ton_aus.config(fg=fg2)
elif ton==1:
    einstellungen_ton_an.config(fg=fg2)
else:
    ton=1
    einstellungen_ton_an.config(fg=fg2)
spiel_starten.place(x=5, y=240, width=145, height=30)
einstellungen.place(x=150, y=240, width=145, height=30)
hauptmenü.place(x=5, y=100, width=290, height=50)
root.bind('<Left>', links)
root.bind('<Right>', rechts)
root.bind('<Escape>', zum_menü_gehen)
k1=tk.Label(root, bg='dark grey', relief='groove')
k1_l=0
k2=tk.Label(root, bg='dark grey', relief='groove')
k2_l=0
k3=tk.Label(root, bg='dark grey', relief='groove')
k3_l=0
k4=tk.Label(root, bg='dark grey', relief='groove')
k4_1=0
k5=tk.Label(root, bg='dark grey', relief='groove')
k5_l=0
k6=tk.Label(root, bg='dark grey', relief='groove')
k6_l=0
k7=tk.Label(root, bg='dark grey', relief='groove')
k7_l=0
k8=tk.Label(root, bg='dark grey', relief='groove')
k8_l=0
k9=tk.Label(root, bg='dark grey', relief='groove')
k9_l=0
k10=tk.Label(root, bg='dark grey', relief='groove')
k10_l=0
k11=tk.Label(root, bg='dark grey', relief='groove')
k11_l=0
k12=tk.Label(root, bg='dark grey', relief='groove')
k12_l=0
k13=tk.Label(root, bg='dark grey', relief='groove')
k13_l=0
k14=tk.Label(root, bg='dark grey', relief='groove')
k14_l=0
k15=tk.Label(root, bg='dark grey', relief='groove')
k15_l=0
k16=tk.Label(root, bg='dark grey', relief='groove')
k16_l=0
k17=tk.Label(root, bg='dark grey', relief='groove')
k17_l=0
k18=tk.Label(root, bg='dark grey', relief='groove')
k18_l=0
k19=tk.Label(root, bg='dark grey', relief='groove')
k19_l=0
root.config(bg=bg)
root.mainloop()
