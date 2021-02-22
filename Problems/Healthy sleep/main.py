less = int(input())
most = int(input())
sleep = int(input())
if sleep < less:
    print("Deficiency")
elif sleep > most:
    print("Excess")
else:
    print("Normal")

