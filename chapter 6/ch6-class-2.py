def dodajUListu(l):
    l.append(4)

def dodajBroj(b):
    b = b + 5

def dodajString(s):
    s = s + " shake"

def main():
    list = [1,2,3]

    stringic = "banana"
    broj = 1.4

    dodajUListu(list)
    dodajBroj(broj)
    dodajString(stringic)

    print(list) #[1,2,3,4]
    print(broj)#6.4
    print(stringic)#"banana shake"

main()