from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = "ABOUT PAGE"
    return render_template("index.html")


if __name__ == '__main__':
    print('PyCharm')
    app.run(debug=True)



