from flask import Flask,render_template,url_for,request,redirect
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/create",methods=['POST','GET'])
def create():
    if request.method == 'POST':

        content = request.form['text']
        res = 'file created successfully..!'
        
        my_w = tk.Tk()
        my_w.geometry("400x300")
        my_w.title("www.savemyfile.com")
        my_font1=('times',18,'bold')

        l1 = tk.Label(my_w,text="Save File",width=30,font=my_font1)
        l1.grid(row=1,column=1)
        b1 = tk.Button(my_w,text="Save",command=lambda:save_file(), width=20)
        b1.grid(row=2,column=1)
        def save_file():
            filename = filedialog.asksaveasfilename(filetypes=[('text file','*.txt')],
                                                defaultextension='.txt',initialdir='C:\\Users\\patel\\OneDrive\\Desktop\\notepad')
    
            f = open(filename,'a')
            f.write(content)
            f.close()
            
        my_w.mainloop() 
        
        return render_template('main.html',res=res)
    
    return render_template('create.html')

@app.route("/choose",methods=['POST','GET'])
def choose():
    if request.method == "POST":
        my_w = tk.Tk()
        my_w.geometry("400x300")
        my_w.title("www.openfile.com")
        my_font1=('times',18,'bold')

        l1 = tk.Label(my_w,text="Open File",width=30,font=my_font1)
        l1.grid(row=1,column=1)
        b1 = tk.Button(my_w,text="Open",command=lambda:save_file(), width=20)
        b1.grid(row=2,column=1)
        def save_file():
            global fil,con
            fil = filedialog.askopenfilename(filetypes=[('text file','*.txt')],
                                                defaultextension='.txt',initialdir='C:\\Users\\patel\\OneDrive\\Desktop\\notepad')
    
            
            f = open(fil)
            con = f.read()
            f.close()
            
        my_w.mainloop()
        return render_template('edit.html',f = fil, con = con)
        
    return render_template('choose.html')

@app.route("/update",methods=['POST','GET'])
def update():
    if request.method == "POST":
        filename = request.form['file']
        content = request.form['text']
        f = open(filename,'w')
        f.write(content)
        f.close()
        res = 'file updated successfully..!'
        return render_template('main.html',res=res)

app.run(debug=True)