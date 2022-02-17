import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
K = int(input())
gallery, rec_count = [], []
recommends = list(map(int, input().split()))

for i in range(K):

    if recommends[i] not in gallery and len(gallery) < N:
        gallery.append(recommends[i])
        rec_count.append(1)

    elif recommends[i] in gallery:
        for j in range(len(gallery)):
            if gallery[j] == recommends[i]:
                rec_count[j] += 1
                break

    elif recommends[i] not in gallery and len(gallery) == N:
        min_v = min(rec_count)

        for j in range(N):
            if rec_count[j] == min_v:
                gallery.pop(j)
                rec_count.pop(j)
                gallery.append(recommends[i])
                rec_count.append(1)
                break

print(' '.join(list(map(str, sorted(gallery)))))
