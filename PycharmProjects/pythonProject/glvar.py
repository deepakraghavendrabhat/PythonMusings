# x = "global x"

def test(z):
     # global x
    x = "local x"

    print(x)

test('local z')
# print(z)

