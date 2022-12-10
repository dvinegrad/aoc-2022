with open('input.txt') as f:
    msg = f.read()

print(next(filter(lambda i: len(set(msg[i:i+4])) == 4, range(len(msg)))) + 4)