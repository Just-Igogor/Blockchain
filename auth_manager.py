import json
import hashlib
import os

class AuthManager:
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump({"users": []}, file)

    def load_users(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_users(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, login, password, eth_address):
        users_data = self.load_users()
        for user in users_data["users"]:
            if user["login"] == login:
                raise ValueError("Пользователь с таким логином уже существует.")
        
        hashed_password = self.hash_password(password)
        users_data["users"].append({
            "login": login,
            "password": hashed_password,
            "eth_address": eth_address
        })
        self.save_users(users_data)

    def validate_user(self, login, password):
        users_data = self.load_users()
        hashed_password = self.hash_password(password)
        for user in users_data["users"]:
            if user["login"] == login and user["password"] == hashed_password:
                return user["eth_address"]
        return None
