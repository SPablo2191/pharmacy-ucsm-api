import random
import string

def generate_invoice_code(length=8):
    """Generates a random invoice code of given length."""
    # generate a random string of uppercase letters and digits
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return code