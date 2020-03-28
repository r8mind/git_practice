from stack import Stack,Node

print("Let's play Towers of Hanoi!!")

stacks =[]

left_stack = Stack('left')
middle_stack = Stack('middle')
right_stack = Stack('right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("\nEnter a number greater than or equal to 3\n"))

for i in range(num_disks,0,-1):
    left_stack.push(i)

num_optimal_moves = 2**(num_disks) - 1

print('\nThe fastest way you can solve this game is in {} moves'.format(num_optimal_moves))

def get_input():
    choices = [i.get_name()[0] for i in stacks]

    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]

            print(f'Enter {letter} for {name}')

        user_input = input('')
        if user_input in choices:
            for i in range(len(choices)):
                if user_input == choices[i]:
                    return stacks[i]

num_user_moves = 0
while right_stack.size != num_disks:
    print('\n\n\n...Current Stacks......\n')
    for i in range(num_disks):
        print(left_stack.print_items(num_disks)[i],'\t',middle_stack.print_items(num_disks)[i],'\t',right_stack.print_items(num_disks)[i])
    while True:
        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()

        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()

        if not from_stack.size:
            print('\n\nInvalid move. Try Again')
        
        elif not to_stack.size or from_stack.peek()<to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break

        else:
            print('\n\n Invalid Move Try Again')


print(f'\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}.')



        
        