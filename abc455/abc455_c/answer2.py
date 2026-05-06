from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)

hash_map = defaultdict(int)

for a in A:
    hash_map[a] += a

sorted_keys = sorted(hash_map, key=hash_map.get, reverse=True)

for i in range(min(K, len(sorted_keys))):
    total -= hash_map[sorted_keys[i]]

print(total)
