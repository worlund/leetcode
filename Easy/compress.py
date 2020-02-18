from typing import List


def compress(chars: List[str]) -> int:
    if len(chars) == 1:
        return 1

    pos = 0
    i = 0
    curr = ""
    counter = 0
    while i < len(chars):
        a = 1
        if curr == "":
            curr = chars[i]
            counter += 1
            i += 1
        elif chars[i] == curr:
            del chars[i]
            counter += 1
        else:
            curr = ""
            if counter > 1:
                counterStr = str(counter)
                for c in counterStr:
                    chars.insert(pos + 1, c)
                    pos += 1
            pos += 1
            i = pos
            counter = 0

    if counter > 1:
        counterStr = str(counter)
        for c in counterStr:
            chars.insert(pos + 1, c)
            pos += 1

    return len(chars)

test = compress(["a","a","b","b","c","c","c"])

