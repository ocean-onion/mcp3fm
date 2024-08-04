from flask_bcrypt import Bcrypt
from .compat import safe_str_cmp

class CustomBcrypt(Bcrypt):
    def check_password_hash(self, pw_hash, password):
        return safe_str_cmp(pw_hash, password)

bcrypt = CustomBcrypt()
