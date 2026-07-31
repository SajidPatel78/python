class dog:
    kind = "canine"
    def __init__(self, name):
        self.name = name

d = dog("Fido")
e = dog("Buddy")

d.kind 
e.kind
print(d.name)
print(e.name)
print(d.kind)
