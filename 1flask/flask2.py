from unicodedata import name
from flask import Flask , redirect, url_for, request
app=Flask(__name__)

@app.route('/success/<f_name><l_name>')
def success(f_name, l_name):
    return "Welcome  %s   %s to Student Profile Page " %(f_name,  l_name)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        userf=request.form['fn']
        userl=request.form['ln']
        return redirect(url_for('success',f_name=userf, l_name=userl))
    else:
        userf=request.args.get('fn')
        userl=request.args.get('ln')
        return redirect(url_for('success', f_name=userf, l_name=userl))
        
if __name__=='__main__':
    app.run(debug=True)

    # "http://localhost:5000/login"
