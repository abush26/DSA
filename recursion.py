
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        # print(f"Move disk 1 from {source} to {target}")
        print(source,target)
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    # print(f"Move disk {n} from {source} to {target}")
    print(n , source,auxiliary)
    tower_of_hanoi(n-1, auxiliary, source, target)

num_disks = 3
tower_of_hanoi(num_disks, 'A', 'B', 'C')
