import tkinter as tk
from tkinter import Label,Entry,Frame,Button
import datetime,time,winsound

#função que verifica o horario atual e coompara com o horario do alarme
def alarm():
    while True:
        set_alarm_time = f'{hora.get()}:{minuto.get()}:{segundo.get()}'
        time.sleep(1)
        current_time = datetime.datetime. now().strftime('%H:%M:%S')#pega o horario atual no formato hora:minuto:segundo
        print(current_time,set_alarm_time)
        if current_time == set_alarm_time:
            winsound.PlaySound('alarm.wav',winsound.SND_FILENAME)
            winsound.Beep(1000,10000)
            break

#criar a janela principal
janela = tk.Tk()
janela.title("Alarme")
janela.geometry("600x420")

#criar a parte visual e interativa
Label(janela,text='Alarme pythonico',font=('Helvetica',20,'bold'),pady=40).pack(pady=10)
Label(janela,text='Definir alarme:',font=('Helvetica',12)).pack(pady=5)

frame = Frame(janela)
frame.pack()
#criar menu drop down,stringvar serve para pegar o valor selecionado no menu drop down 
def option(value):
    opt = tk.StringVar(janela)
    options = [str(i).zfill(2) for i in range (value)] #cria a lista de opcoes por isso o for
    opt.set(options[0]) 
    tk.OptionMenu(frame,opt,*options).pack(side=tk.LEFT) # seus parametros sao o frame onde vai ser colocado, o stringvar e a lista de opcoes
    return opt
hora = option(24)
minuto = option(60)
segundo = option(60)
Button(janela,text='Definir',font=('Helvetica',12,),bg='blue',fg='white',command=alarm).pack(pady=20)
janela.mainloop()  