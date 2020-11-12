import random

from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        secret_number = request.cookies.get("secret_number")
        if not secret_number:
            secret_number = str(random.randint(1, 30))
            response = make_response(render_template("index.html", secret_number=secret_number))
            response.set_cookie("secret_number", secret_number)
        else:
            response = make_response(render_template("index.html", secret_number=secret_number))
        return response

    elif request.method == "POST":
        secret_number = int(request.cookies.get("secret_number"))
        guess = int(request.form.get("guess"))

        if guess == secret_number:
            response = make_response(render_template("success.html", secret_number=secret_number))
            response.set_cookie("secret_number", expires=0)
            return response
        else:
            return render_template("failure.html", secret_number=secret_number, guess=guess)


if __name__ == '__main__':
    app.run()
