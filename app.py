from flask import Flask, render_template, request
from graph import SocialGraph

app = Flask(__name__)
social_graph = SocialGraph()

@app.route("/")
def index():
    return render_template("index.html", graph=str(social_graph))

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user = request.form.get("user")
        social_graph.add_user(user)
        message = f"User '{user}' added successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=str(social_graph), message=message)

@app.route("/add_relationship", methods=["POST"])
def add_relationship():
    try:
        user1 = request.form.get("user1")
        user2 = request.form.get("user2")
        social_graph.add_relationship(user1, user2)
        message = f"Relationship added between '{user1}' and '{user2}' successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=str(social_graph), message=message)

if __name__ == "__main__":
    app.run(debug=True)
