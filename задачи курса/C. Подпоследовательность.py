def check(substring, whole_line):
    pos = -1
    for i in substring:
        pos = whole_line.find(i, pos + 1)
        if pos == -1:
            return False
    return True


substring = input()
whole_line = input()
print(check(substring, whole_line))
