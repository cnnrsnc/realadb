new = open("newlog.txt", "a")

dozing = str("Doze")
doze = str("doze")
power = str("PowerManagerService")

with open("logcat1.txt", 'r') as lines:
    for newline in lines.readlines():
        if newline.count(doze) >= 1:
            new.writelines(newline)
        elif newline.count(power) >= 1:
            new.writelines(newline)
        elif newline.count(power) >= 1:
            new.writelines(newline)

lines.close()
