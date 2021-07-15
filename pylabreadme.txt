pylab和pyplot的区别是，
前者将numpy导入了其命名空间中。
这样会使pylab表现的和matlab更加相似。
现在来说我们经常使用pyplot，
因为pyplot相比pylab更加纯粹。

安裝matplotlib，就會有pylab，而不是單獨安裝pylab

==中文支援不佳


==color參數，圖形和文字都可以用
        1. x11/css4
        white-w, color='w'
        red-r
        green-g
        blue-b
        cyan-c
        magenta-m
        yellow-y
        black-k

        2. '#rrggbb'
        color='#ff0000', 是紅色

        3. (r,g,b)數值在[0,1]
        color=(1,0,0), 是紅色

        4. (r,g,b,a) a=0完全透明，a=1完全不透明
        
==圖表上的名稱標示
pylab.title("my graph")
pylab.xlabel("x name")
pylab.ylabel("y name")

==顯示部份範圍
pylab.xlim(-5,5)
pylab.ylim(-2,2) 
取代上面二式如下  
pylab.axis((-5,5,-2,2))，一次設定x和y軸，用list和tuple都可以，(x1,x2,y1,y2)

pylab.axis('off')，x和y軸線隱藏，axis()只能接受一個參數

==axes和axis
整個圖檔顯示的部份叫做figure
畫在x, y軸範圍之內的圖叫做 axes
x座標和y座標叫做 axis

