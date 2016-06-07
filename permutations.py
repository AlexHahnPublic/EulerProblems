def allPerms(string, start, end):
    current = 0
    if start == end-1:
        if not string in result:
            result.append(string)
    else:
        for current in range(start, end):
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            allPerms(''.join(x), start+1, end)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

def main(inp):
    global result
    result = []
    length = len(inp)
    allPerms(inp,0,length)
    return result


if __name__ == "__main__":
    import sys
    ans = main(str(sys.argv[1]))
    print ans




