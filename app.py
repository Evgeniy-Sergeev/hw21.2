from flask import Flask, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/contacts", methods=["GET"])
def contacts():
    try:
        with open("templates/contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        return Response(html_content, content_type="text/html")
    except FileNotFoundError:
        return "Контактная страница не найдена", 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
