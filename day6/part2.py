with open('input.txt') as f:
    msg = f.read()

res = next(filter(lambda i: len(set(msg[i:i+14])) == 14, range(len(msg)))) + 14
print(res)