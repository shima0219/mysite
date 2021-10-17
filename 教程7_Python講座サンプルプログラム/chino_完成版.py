

# 画面を作る
import tkinter as tk 
import tkinter.filedialog as fd 

import PIL.Image 
import PIL.ImageTk

# 機械学習で使うモジュール　①
import sklearn.datasets
import sklearn.svm # サポートベクターマシン　データを分類して境界線を引くためのアルゴリズム
import numpy


# 画像ファイルを数値リストに変換する関数
def imageToData(filename):
    # 画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS) 

    # 画像をラベルに表示
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage

    # 数値リストに変換する処理の追加　②
    numImage = numpy.asarray(grayImage,dtype = float)
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()
    
    return numImage

# 数字を予測する関数　③

def predictDigits(data):
    
    digits = sklearn.datasets.load_digits() # 学習用データを読み込む

    # 機械学習を行う
    clf = sklearn.svm.SVC(gamma = 0.001)    

    clf.fit(digits.data,digits.target)

    # 予測
    n = clf.predict([data])

    # 予測結果を表示する
    textLabel.configure(text = "この画像は" + str(n) + "です！")   


# ファイルダイアログを開く関数 
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        # 画像ファイルを数値リストに変換する
        data = imageToData(fpath)

        # ④
        # imageData関数で数値リスト化されたデータが返ってくる
        # 数字予測関数predictDigitsへデータを渡して、数字を予測        
        predictDigits(data)



root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root,text="ファイルを開く",command = openFile) 
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

# ⑤
# 予測結果を表示するラベル
textLabel = tk.Label(text="手描きの数字を認識します！")
textLabel.pack()

tk.mainloop()
