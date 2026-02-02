n = 4
src = 'A'
des = 'B'
aux = 'C'

def move_disks(n, src, des, aux):
    if n == 1:
        print(f"Move disk 1 from {src} to {des}")
        return
    move_disks(n - 1, src, aux, des)
    print(f"Move disk {n} from {src} to {des}")
    move_disks(n - 1, aux, des, src)

move_disks(n, src, des, aux)
