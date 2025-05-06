from typing import Literal
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return password_context.hash(password)

def validate_password(password: str) -> Literal[
    True, 
    "Password must be at least 8 characters long", 
    "Password must contain at least one digit", 
    "Password must contain at least one letter", 
    "Password must contain at least one special character"
]:
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char.isalpha() for char in password):
        return "Password must contain at least one letter"
    if not any(char in "!@#$%^&*()-_+=<>?{}[]|~`" for char in password):
        return "Password must contain at least one special character"
    return True