import tkinter as tk   # 画面を表示
import tkinter.filedialog as fd    #ファイルダイアログを使うモジュール
import PIL.Image    # 画像を扱うモジュール
import PIL.ImageTk  # tkinterで作成した画面上に画像を表示させるモジュール


# 画像をラベルに表示する関数  # ★

def dispLabel(image,path):
    imageData = PIL.ImageTk.PhotoImage(image)
    lbl.configure(image=imageData)
    lbl.image = imageData

    txtbox.delete(0, tk.END) 
    txtbox.insert(tk.END, path) 


# 画像を表示する関数
# 関数openFileの中で呼び出すので、openFileより上に書く
def dispPhoto(path):
    # 画像を読み込む
    newImage = PIL.Image.open(path).resize((400,300))

    dispLabel(newImage,path)



# 画像ファイルを開く関数
def openFile():
    fpath = fd.askopenfilename() #ファイルを開くためのダイアログが表示される

    # ファイルダイアログでキャンセルされた場合は、戻り値が空っぽ
    # fpathに値が入っている時だけ実行
    if fpath:
        dispPhoto(fpath)  # dispPhotoの呼び出し


# 回転させる関数
def rotatePhoto(): 
    rpath = txtbox.get()
    if rpath: # ★
        newImage = PIL.Image.open(rpath).resize((400,300)).rotate(30)

        dispLabel(newImage,rpath) # ★


# 白黒にする関数
def convPhoto(): 
    cpath = txtbox.get()
    if cpath:  # ★
        newImage = PIL.Image.open(cpath).resize((400,300)).convert("L")

        dispLabel(newImage,cpath) # ★


# 画面準備
root = tk.Tk()
root.title("画像読込アプリ")
root.geometry("500x450")

# テキストボックス　画像ファイルのパスを格納しておく　
txtbox=tk.Entry(width=30)
txtbox.place(x=150,y=50)

# ボタンの作成
btn = tk.Button(text="ファイルを開く",command=openFile)

btn_change = tk.Button(text="画像を変更する",command=openFile) 

btn_rotate = tk.Button(text="回転",command=rotatePhoto) 

btn_con = tk.Button(text="白黒",command=convPhoto)

# ボタンの配置
btn.place(x=150,y=20)

btn_change.place(x=150,y=80)
btn_rotate.place(x=250,y=80)
btn_con.place(x=300,y=80)




# ラベルの作成
lbl = tk.Label()

# ラベルの配置
lbl.place(x=50,y=120)

tk.mainloop()
