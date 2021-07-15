#監聽鍵盤，阻塞式
#https://codingnote.cc/zh-tw/p/114319/，蠻詳細的
#https://pynput.readthedocs.io/en/latest/keyboard.html，官網

from pynput import keyboard
import os

#內建函式
def on_press(key):
    #用key.char取得文字型輸入
    try:
        if key.char == 'a': #按a鍵強制結束
            os._exit(1)
        else:
            print(key.char)
       
    #特殊鍵由keyboard.Key處理，
    except AttributeError:
        if key == keyboard.Key.space:
                myprogram()
def myprogram():
    print('start')
        

#這裡是監聽鍵盤的程式，無限循環
while True:
    with keyboard.Listener(
        on_press = on_press,
        ) as listener:
        listener.join()

