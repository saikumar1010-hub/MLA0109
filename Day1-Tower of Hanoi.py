def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Move top n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    # Move largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Number of disks
n = 3

print(f"\nTower of Hanoi solution for {n} disks:\n")
tower_of_hanoi(n, 'A', 'B', 'C')
