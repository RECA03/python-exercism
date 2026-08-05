actions = {0:'wink', 1:'double blink', 2:'close your eyes', 3:'jump', 4:'reverse'}

def commands(binary_str):
    #evaluate if the given number exists between 1 and 31
    if len(binary_str) > 5:
        raise ValueError("number must be between 1 and 31")
    
    #convert the binary string into a list of digits
    digit_list = list(binary_str)
    if "1" not in digit_list: #make the exception for any type of 0s that might be entered
        return []

    #reverse the digit list and create the handshake list
    digit_list.reverse()
    handshake = []

    for i, d in enumerate(digit_list):
        if d == '1':
            handshake.append(actions[i])
    
    #in case the hanshake will be reversed
    if handshake[-1] == "reverse":
        handshake.pop()
        handshake.reverse()
    
    return handshake

