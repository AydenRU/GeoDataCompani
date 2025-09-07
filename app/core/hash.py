from passlib.context import CryptContext


my_hash = CryptContext(
    schemes=['bcrypt'],
    deprecated="auto",
    bcrypt__rounds=12
)