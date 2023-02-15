f = open("file.txt","r")
contend = f.read()
print(contend)
f.close()

print("______________________________-")


f = open("file.txt","r")
for line in f:
    print(line)
f.close()    

print("_______________________________")
f = open("file.txt","r")
print(f.readline())
print(f.readline())
f.close()

print("********************************")
f = open("file.txt","r")
print(f.readlines())
f.close()