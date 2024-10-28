from flask import Flask,render_template, request, redirect, url_for

app = Flask("Форма зворотнього зв'язку")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        print(f"Ім'я {name}\nПовідомлення: {message}")

        return render_template('success.html',name = name)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)