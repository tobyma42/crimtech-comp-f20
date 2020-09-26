def rm_smallest(d):
    # Your code here!
    values = []
    if bool(d) == True:
        for x in d:
            values.append(d[x])
        values.sort()
        for x in d:
            if d[x] == values[0]:
                y = x
        del d[y]
    else:
        return d
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()
