# app.py
from flask import Flask, render_template, request, jsonify
from graph import SocialGraph

app = Flask(__name__)
social_graph = SocialGraph()


@app.route("/")
def index():
    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True))


@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user = request.form.get("user")
        social_graph.add_user(user)
        message = f"User '{user}' added successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True), message=message)


@app.route("/remove_user", methods=["POST"])
def remove_user():
    try:
        user = request.form.get("user")
        social_graph.remove_user(user)
        message = f"User '{user}' removed successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True), message=message)


@app.route("/add_relationship", methods=["POST"])
def add_relationship():
    try:
        user1 = request.form.get("user1")
        user2 = request.form.get("user2")
        social_graph.add_relationship(user1, user2)
        message = f"Relationship added between '{user1}' and '{user2}' successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True), message=message)


@app.route("/remove_relationship", methods=["POST"])
def remove_relationship():
    try:
        user1 = request.form.get("user1")
        user2 = request.form.get("user2")
        social_graph.remove_relationship(user1, user2)
        message = f"Relationship removed between '{user1}' and '{user2}' successfully."
    except ValueError as e:
        message = str(e)

    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True), message=message)


@app.route("/clear", methods=["POST"])
def clear():
    social_graph.clear()
    message = "Graph cleared successfully."
    return render_template("index.html", graph=social_graph.to_json(),
                           matrix=social_graph.generate_matrix(str_=True), message=message)


@app.route("/graph_json")
def get_graph_json():
    return jsonify(social_graph.to_json())


if __name__ == "__main__":
    app.run(debug=True)
