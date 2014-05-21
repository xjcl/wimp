
class Test(object):
    def __init__(self):
        pass
    def play(self, chars):
        print(">>init minigame")
        scores = []
        for c in chars:
            x = int(raw_input("pick a number, "+str(c)+": "))
            scores.append(x)
        return scores

#if __name__ == "__main__":
#    t = Test()
