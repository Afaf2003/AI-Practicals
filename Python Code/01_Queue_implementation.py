a = []

while True:
    print("Enter\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    c = int(input())
    if c == 1:
        x = int(input("Enter the number :"))
        a.append(x)
    elif c == 2:
        print("The Dequeue Element :"+a[0])
        a.pop(0)
    elif c == 3:
        print(a)
    else:
        exit()
