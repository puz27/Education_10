from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        page_title = "MAIN"
        page_information = "INFORMATION ABOUT CANDIDATES"
        candidates = get_all(data_of_candidats)
        return render_template("index.html", page_title=page_title, page_information=page_information, candidates=candidates)


if __name__ == '__main__':
    print('PyCharm')
    app.run(debug=True)



