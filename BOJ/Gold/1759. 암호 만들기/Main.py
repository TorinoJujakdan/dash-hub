L, C = map(int, input().split())
arr = list(map(str, input().split()))
result = []
v = ["a", "e", "i", "o", "u"]
arr.sort()


def recur(cnt, prev):   
    v_cnt = 0
    c_cnt = 0 
    if cnt == L:
        for i in range(L):
            if result[i] in v:
                v_cnt += 1
            else:
                c_cnt += 1
                if c_cnt >= 2 and v_cnt >= 1:
                    print("".join(result))
                    return
    
    for i in range(prev, C):
        result.append(arr[i])
        recur(cnt + 1, i + 1)
        result.pop()

recur(0, 0)