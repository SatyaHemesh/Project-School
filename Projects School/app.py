from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = int(request.form['number'])
        if is_prime(number):
            result = f"{number} is a Prime Number."
        else:
            result = f"{number} is NOT a Prime Number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
