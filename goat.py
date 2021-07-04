def intersection_over_union(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


a = [float(x) for x in input().split()]
IoU = float(input())
sc = float(input())
for _ in range(int(input())):
    t = [float(x) for x in input().split()]
    t = [x if x % 1 != 0 else int(x) for x in t]
    if intersection_over_union(a, t) > IoU and t[-1] >= sc:
        print(*t)
# 50 60 430 230
# 0.3
# 0.6
# 2
# 210 60 430 230 0.9
# 429 60 600 230 0.9
