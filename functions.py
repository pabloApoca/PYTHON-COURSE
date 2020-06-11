def hello(name="Person"):
    print("Hello world " + name)


hello("Pablo")
hello("Martin")
hello()

def add(n1, n2):
    return n1 + n2

print(add(10, 30))
print(len("Hello"))


# lambda son funciones anonimas que resiben un numero de argunmento pero que solo resiven una expresion

add = lambda num1, num2: num1 + num2

print(add(10,50))

