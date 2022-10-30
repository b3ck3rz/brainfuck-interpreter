def blocks(code, length):
    opened = []
    block = {}
    for i in range(length):
        if code[i] == "[":
            opened.append(i)
        if code[i] == "]":
            block[opened.pop()] = i
    return block

code = "".join(i for i in input("Enter Brainfuck code: ") if i in '<>+-.,[]')
cells = [0 for _ in range(30000)]
pointer = 0
index = 0
length = len(code)
block = blocks(code, length)
result = ''

while pointer < length:
    symbol = code[pointer]
    if symbol == ">":
        index += 1
    elif symbol == "<":
        index -= 1
    elif symbol == "+":
        if cells[index] == 255: cells[index] = 0
        else : cells[index] += 1
    elif symbol == "-":
        if cells[index] == 0: cells[index] = 255
        else : cells[index] -= 1
    elif symbol == ".":
        result += chr(cells[index])
    elif symbol == ",":
        cells[index] = int(input("Enter a value: "))
    elif symbol == "[":
        start = pointer
        if cells[index] == 0 : pointer = block[pointer]
    elif symbol == "]":
        if cells[index] : pointer = start
    pointer += 1

print(f"Result: {result}")