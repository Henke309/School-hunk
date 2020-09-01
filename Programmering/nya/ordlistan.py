def check(ord):
    words = open("nya//nyaOrd.txt", "r")

    for word in words.readlines():
        if ord.lower() == word.strip():
            return True

    return False

if __name__ == '__main__':
    print(check("j dfdhjsdjf"))