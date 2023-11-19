from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', path_css="/static/css/style.css", path_img="https://re-feniks.ru/netcat_files/36/50/kak_izbavit_muzha_ot_igrovoj_zavisimosti_0.png")

@app.route('/calc')
def calc():
    n1 = 55
    n2 = 108
    return render_template('calc.html', 
                           num1=n1, 
                           num2=n2)


app.run(debug=True)
