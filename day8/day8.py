import copy 

input_instructions = []
with open ('./day8input.txt') as f:
    for line in f:
        processed_entry = line.strip().split(' ')
        input_instructions.append(processed_entry)

print input_instructions

VISITED = 'visited'

def execute(instructions):
    visit_instructions = copy.deepcopy(instructions)
    steps_run = 0
    accumulator = 0
    index = 0
    while index < len(visit_instructions):
        step = visit_instructions[index]
        if VISITED in step:
            break
        print("Index: {}, Step: {}".format(index, step))
            
        visit_instructions = step[0]
        argument = int(step[1])

        visit_instructions[index].append(VISITED)
        if instruction == 'nop':
                index += 1
        elif instruction == 'acc':
                accumulator += argument
                index += 1
        elif instruction == 'jmp':
                index += argument        
        
        if index == len(visit_instructions):
            print("Termination, accumulator: {}".format(accumulator))
            return True

    print("accumulator: {}".format(accumulator))
    return False

def part2(instructions):
    total_steps = len(instructions)
    didTerminate = False
    for i in range(total_steps):
        new_instructions = copy.deepcopy(instructions)
        print('new instr: {}'.format(new_instructions))
        step = new_instructions[i][0]
        print('step: {}'.format(step))
        if step == 'nop':
            new_instructions[i][0] = 'jmp'
            didTerminate = execute(new_instructions)
        elif step == 'jmp':
            new_instructions[i][0] = 'nop'
            didTerminate = execute(new_instructions)
        if didTerminate:
            return

# part 1:
execute(instructions)

part2(input_instructions)