
valid_password_count = 0
with open ('./day2input.txt') as f:
    for line in f:
        split_on_spaces = line.strip('\n').split(' ')
        
        password_policy = split_on_spaces[0].split('-')
        character_policy = split_on_spaces[1].strip(':')
        password = split_on_spaces[2]

        print("password policy: {}, char policy {}, pw: {}".format(password_policy, character_policy, password))

        #### Part 1
        # count = 0
        # minimum = int(password_policy[0])
        # maximum = int(password_policy[1])
        # for char in password:
        #     if (char == character_policy):
        #         count+=1
        # print("count: {}".format(count))
        # if count >= minimum and count <= maximum:
        #     valid_password_count+=1
        #### End part 1

        #### Part 2
        index_1 = int(password_policy[0]) - 1 
        index_2 = int(password_policy[1]) - 1
        if password[index_1] !=  password[index_2] and (password[index_1] == character_policy or password[index_2] == character_policy):
            valid_password_count+=1
        
print valid_password_count