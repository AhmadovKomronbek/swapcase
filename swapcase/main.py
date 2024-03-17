lower_later = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_later = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text = "Hello world"

a = []
for i in range(len(text)):
    a.append(text[i])
print(a)
for i in range(len(text)):
    if a[i] in lower_later:
        a[i] = a[i].upper()
    elif a[i] in upper_later:
        a[i] = a[i].lower()
result = "".join(a)
print(result)
