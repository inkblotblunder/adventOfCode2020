import numpy
group_answers = []

with open ('./day6input.txt') as f:
    data = f.read()
    group_answers = data.split('\n\n')

# count number of questions answered
def part1(group_answers):
    answer_count = []
    for group in group_answers:
        individual_answers = group.split('\n')
        answer_set = set()
        for answer in individual_answers:
            for letter in answer:
                answer_set.add(letter)
        answer_count.append(len(answer_set))
    print(numpy.sum(answer_count))

# count number of questions everyone answered
def part2(group_answers):
    answer_count = []
    for group in group_answers:
        individual_answers = group.split('\n')
        group_answer_list = []
        for answer in individual_answers:
            individual_set = set()
            for letter in answer:
                individual_set.add(letter)
            group_answer_list.append(individual_set)
        group_intersection = set.intersection(*group_answer_list)
        answer_count.append(len(group_intersection))
    print(numpy.sum(answer_count))

part1(group_answers)
part2(group_answers)