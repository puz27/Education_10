from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    page_name = "MAIN PAGE"
    return render_template("index.html", page_name=page_name)


if __name__ == '__main__':
    print('PyCharm')
    app.run(debug=True)



