# def createGenerator():
#     myList = range(10)
#     for i in myList:
#         yield i*i

# myGenerator = createGenerator()
# for i in myGenerator:
#     print(i) 


def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

f = startAt(10)
g = startAt(100)

print(f(1) , g(2))