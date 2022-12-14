from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/create",methods=['POST','GET'])
def create():
    if request.method == 'POST':
        filename = request.form['file']+".txt"
        content = request.form['text']
        res = filename+' file created successfully..!'
        
        f = open(filename,'a')
        f.write(content)
        f.close()
        return render_template('main.html',res=res)
    
    return render_template('create.html')

@app.route("/update")
def update():
    return "update"

app.run(debug=True)