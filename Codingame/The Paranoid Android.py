nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevators=[]
for i in range(nb_elevators):
    elevators.append([int(j) for j in input().split()])
    
elevators.sort()

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    try:
        if clone_pos < elevators[clone_floor][1] and direction == 'LEFT':
            print('BLOCK')
        elif clone_pos > elevators[clone_floor][1] and direction == 'RIGHT':
            print('BLOCK')
        else:
            print('WAIT')
    except:
        if clone_pos < exit_pos and direction == 'LEFT':
            print('BLOCK')
        elif clone_pos > exit_pos and direction == 'RIGHT':
            print('BLOCK')
        else:
            print('WAIT')