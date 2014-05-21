"""BA DA DAM DAM DA DA DAM - DAM -- DAM
    DA DAM DAM DA DA DA DAM DAM DAMM- DAMM- DAM
    DA DA NÜNÜ NÜ NÜ... DADADADADANÜNÜNÜNÜNÜ
    DUM DUM -- DUM DUM (repeat)
    it's the mp7 mg theme okay!?
    """

def play(chars, mg):
    print("here go the rules")
    print(">>rules")
    scores = mg.play(chars)
    maximum = max(scores)
    winners = [chars[i] for i, j in enumerate(a) if j == maximum]
    return winners

if __name__ == "__main__":
    res = play()
