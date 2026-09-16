



def check_password(password):
    if len(password) >= 8:
        return "Strong enough"
    else:
        return "Too short"

print(check_password("python123"))