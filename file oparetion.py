def file():
    f = open("MY_file.txt","w")
    line1= input("your selt:")
    line2 =input("text:")
    new = "\n"
    f.write(line1)
    f.write(new)
    f.close()
file()
