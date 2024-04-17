credits = 1

def check_credits():
    print('hi')
    global credits
    if credits > 0:
        return True
    else:
        return False

def update_credits():
    global credits
    if credits > 0:
        credits -= 1
        return True
    else:
        return False
