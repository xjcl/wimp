"""BA DA DAM DAM DA DA DAM - DAM -- DAM
    DA DAM DAM DA DA DA DAM DAM DAMM- DAMM- DAM
    DA DA NUNU NU NU... DADADADADANUNUNUNUNU
    DUM DUM -- DUM DUM (repeat)
    it's the mp7 mg theme okay!?
    """

def play(chars, mg):
    print("") # 'print()' prints '()'. wtf python.
    print(">>here go the rules")
    scores = mg.play(chars)
    maximum = max(scores)
    winners = [chars[i] for i, j in enumerate(scores) if j == maximum]
    return winners

#if __name__ == "__main__":
#    res = play()
