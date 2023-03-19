# python3


def build_heap(data,n):
    swaps = []
    
    for i in range(n//2,-1,-1):
        node = i
        
        while True:
            child = node*2+1
            # print(node,child)

            if child >= n:
                break
            if child+1 < n and data[child+1] < data[child]:
                child += 1
            if data[child] < data[node]:
                swaps.append((node,child))

                temp = data[node]
                data[node] = data[child] 
                data[child] = temp
                node = child
                # print(data)

                if node*2+1 >= n:
                    break
            else:
                break

    return swaps


def main():
    choice = input().strip().upper()
    
    if choice == "I":
        n = int(input())
        if n < 1 or n > 100000:
            print("Invalid input")
            main()
        data = list(map(int, input().split()))
    elif choice == "F":
        with open("./tests/04",'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))
    else: 
        print("Invalid input")
        main()

    assert len(data) == n
    swaps = build_heap(data, n)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    
    exit()


if __name__ == "__main__":
    main()
