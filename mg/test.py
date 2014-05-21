

def play(chars):
    print("init minigame")
    scores = []
    for c in chars:
        x = int(raw_input("pick a number: "))
        scores.append(x)
    
    return scores

if __name__ == "__main__":
    res = play()
