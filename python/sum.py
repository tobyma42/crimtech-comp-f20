def sum(lst, n):
    # Your code here!
    sums = []

    for x in lst:
        lst.remove(x)
        for y in lst:
            sums.append(x + y)
    if n in sums:
        return True

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()
