process = [
    ["P0",3,5],
    ["p1",2,4],
    ["p2",4,3],
    ["p3",1,2],
    ["p4",5,3]
]


process.sort(key=lambda x:x[1])
ct = []
tat = []
wt = []
current_time = 0
for i in process:
    name, at, bt = i

    if current_time < at :
        current_time = at

    current_time += bt
    ct.append(current_time)
    turnaround = current_time - at
    tat.append(turnaround)
    waiting = turnaround - bt
    wt.append(waiting)

print("P_id\taT\tBT\tCT\tTAT\tWT")

for i in range(len(process)):
    print(process[i][0], "\t", process[i][1], "\t", process[i][2], "\t", ct[i], "\t", tat[i], "\t", wt[i])

avg_tat = sum(tat) / len(tat)
print("avg_tat\t", avg_tat)
avg_wt = sum(wt) / len(wt)
print("avg_wt\t", avg_wt)
