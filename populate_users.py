from flask import Flask, render_template, jsonify, request
from app.db import users_collection

app = Flask(__name__)

# Page d'accueil
@app.route("/")
def home():
    return render_template("index.html")

# API pour récupérer les utilisateurs
@app.route("/api/users")
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return jsonify(users)

# API pour ajouter un utilisateur
@app.route("/api/users/add", methods=["POST"])
def add_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Nom et email requis"}), 400
    # Vérifie si l'utilisateur existe déjà
    if users_collection.count_documents({"email": email}) > 0:
        return jsonify({"error": "Email déjà utilisé"}), 400
    users_collection.insert_one({"name": name, "email": email})
    return jsonify({"message": "Utilisateur ajouté avec succès"}), 201

if __name__ == "__main__":
    app.run(debug=True)
