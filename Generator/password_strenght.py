def evaluate_password_strength(password):
    if len(password) < 8:
        strength = "Invalid password. Minimum of 8 characters are a must."
    elif len(password) < 12:
        strength = "Could be better. Consider using more characters."
    elif len(password) < 18:
        strength = "Strong enough"
    else:
        strength = "Super strong"
    return strength



