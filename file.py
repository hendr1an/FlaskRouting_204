from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render halaman login.html
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Ambil nama dari form
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')  # Ambil nama dari query string (jika GET)
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
