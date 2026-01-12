from app.db import users_collection

print("Collections existantes :", users_collection.database.list_collection_names())
