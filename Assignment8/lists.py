# give the colors that contain fruit
fruit = ["apple", "peas", "corn"]
x = {"red":["apple","firetruck"],"blue":["sky", "ocean"],"green":["peas"],"yellow":["sun", "corn"]}
y = [list(filter((lambda x: "apple" or "peas" or "corn" in x),x))]
print(y)


# match the outputs
s = [2*x+1 for x in range(0,13)]
print(s)
t = [x for x in range(0,13) if x%3]
print(t)
u = [2*x+1 for x in range(0,13) if x%3]
print(u)

# match the outputs
a = []
for i in range(1,9):
    if i%2==0:
        a.append(i**2-i+3)
print(a)
b = [(i**2-i+3) for i in range(1,9) if i%2 == 0]
print(b)

# match the outputs
c1 = []
for n in range(1,16):
    if n%2 == 0:
        c1.append(n**2)
    else:
        c1.append(n**3)
print(c1)
c2 = [(n**2) if n%2 == 0 else (n**3) for n in range(1,16)]
print(c2)

# This is technically transpose of a matrix
# But for now, just match output
e1 = [[1,2],[3,4],[5,6],[7,8]]
e2 = [[e1[j][i] for j in range(len(e1))] for i in range(len(e1[0]))]
print(e2)

# reverse the letters in the string
f1 = ["hello"]
f2 = [i[::-1] for i in f1]
print(f2)



# reverse the letters in the strings
g1 = ["hello","goodbye","merhaba"]
g2 = [i[::-1] for i in g1]
print(g2)
