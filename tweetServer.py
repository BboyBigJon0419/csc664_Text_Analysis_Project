from flask import Flask, render_template
#pip install flask
app = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)


