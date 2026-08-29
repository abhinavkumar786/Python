n = int(input("total orders: "))
l = []

for i in range(n):
    on = int(input(f"order number {i+1}: "))
    l.append(on)

print("Orders:", l)

k = int(input("display order: "))
if k > n:
    print("Error: display order can't be greater than total orders")
else:
    l2 = l[:k]  # first k elements
    y = k

    while True:
        # Check for first negative number in l2
        neg_found = False
        for val in l2:
            if val < 0:
                print(val)
                neg_found = True
                break
        if not neg_found:
            print(0)

        # Slide window
        if y >= n:  # no more elements left
            break
        l2.pop(0)       # remove first element
        l2.append(l[y]) # add next element
        y += 1

        # this can be incorrect---->chatgpt
