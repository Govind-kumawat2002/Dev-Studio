# from flask import Flask, request, redirect

# app = Flask(__name__)

# @app.route('/contact', methods=['POST'])
# def contact():
#     print(request.form)   # data aa raha hai
#     return redirect("/index.html")

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/contact', methods=['POST'])
def contact():
    print(request.form)
    return redirect(request.referrer)  # SAME page

if __name__ == '__main__':
    app.run(port=5000, debug=True)
