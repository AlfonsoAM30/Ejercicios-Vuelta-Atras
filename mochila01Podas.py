from collections import deque


def bound(u, n, m, arr):
    if u[3] >= m:
        return 0
    profitBound = u[1]
    j = u[0] +1
    totWeight = int(u[3])
    while j < n and totWeight + int(arr[j][1]) <= m:
        totWeight += int(arr[j][1])
        profitBound += arr[j][2]
        j += 1
    if j < n:
        profitBound += int((w - totWeight) * arr[j][2] / arr[j][1])
    return profitBound


def solution(w, arr, n):
    arr.sort(reverse=True)
    q = deque()
    nodo_u = (-1, 0, 0, 0) #exploracion, beneficio, bound, cost
    q.append(nodo_u)
    max_profit = 0

    while q:
        nodo_u = q.pop()
        if nodo_u[0] == n-1:
            continue
        new_node_weight = nodo_u[3] + arr[nodo_u[0] + 1][1]
        new_node_profit = nodo_u[1] + arr[nodo_u[0] + 1][2]
        new_node_level = nodo_u[0] + 1
        node_v = (new_node_level, new_node_profit, bound((new_node_level, new_node_profit, 0, new_node_weight), n, w, arr), new_node_weight)

        if node_v[3] <= w and node_v[1] > max_profit:
            max_profit = node_v[1]

        if node_v[2] > max_profit:
            q.append(node_v)

        aux_level = nodo_u[0] + 1
        aux_profit = nodo_u[1]
        aux_weight = nodo_u[3]
        aux_node = (aux_level, aux_profit, 0, aux_weight)
        node_v = (nodo_u[0] + 1, nodo_u[1], bound(aux_node, n, w, arr), nodo_u[3])

        if node_v[2] > max_profit:
            q.append(node_v)

    return max_profit



if __name__ == '__main__':
    w = 15
    arr = [
        (10/2, 2, 10), (10/4, 4, 10), (12/6, 6, 12), (18/9, 9, 18)
    ]

    n = len(arr)
    print(solution(w, arr, n))





