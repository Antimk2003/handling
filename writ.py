f = open("writing.txt","w")
f.write("Enjoy life today, yesterday is gone tomorrow may never come.")
f.close()

print("_________________________________")

f = open("writing.txt","a")
f.write("take your dreams seriously and work hard to get them\n")
f.close()

f = open("writing.txt","a")
a = f.write("take your dreams seriously and work hard to get them\n")
print(a)          # count cerecter
f.close()

# handle read and write both
f = open("and.txt","r+")
print(f.read())
f.write("good mornig")