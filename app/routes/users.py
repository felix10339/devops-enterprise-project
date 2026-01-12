from flask import Blueprint, jsonify
from app.db import users_collection

users_bp = Blueprint("users", __name__)

@users_bp.route("/api/users", methods=["GET"])
def get_users():
    users = list(users_collection.find({}, {"_id": 0}))
    return jsonify(users)
