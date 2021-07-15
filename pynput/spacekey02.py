#監聽鍵盤，阻塞式，所以程式會無限循環，一直監聽鍵盤
#https://codingnote.cc/zh-tw/p/114319/，蠻詳細的
#https://pynput.readthedocs.io/en/latest/keyboard.html，官網

from pynput import keyboard
import os

#這是pynput的內建函式，在這裡判斷space按下就執行myprogram
def on_press(key):
    if key == keyboard.Key.space:
        myprogram()

#遊戲程式在這裡
def myprogram():
    print('start the game')
    #把你的程式寫在這裡
    
    os._exit(1) #結束程式，否則要用ctrl + break來結束程式
        

#主程式是監聽鍵盤的程式，無限循環
while True:
    with keyboard.Listener(
        on_press = on_press,
        ) as listener:
        listener.join()


