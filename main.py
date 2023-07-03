from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)

@app.route('/',methods={"GET","POST"})
@app.route('/register',methods={"GET","POST"})
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(name,email,password)
        return render_template('success.html')
    return render_template('register.html')


if __name__=="__main__":
    app.run(debug=True)