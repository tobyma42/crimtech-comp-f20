import math

def square_root(n):
<<<<<<< HEAD
    # Your code here!
=======
>>>>>>> 85faed6b0d6d59051e450b7af72d40c7dd657666
    if isinstance(n,int) and n >= 0:
        return math.sqrt(n)
    else:
        return -1
    return 0

def test():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root("hello") == -1
    assert square_root(-10) == -1
    print("Success!")

if __name__ == "__main__":
    test()
