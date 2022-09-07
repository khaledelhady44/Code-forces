no_students = int(input())
skills = input().split()

no_1 = skills.count("1")
no_2 = skills.count("2")
no_3 = skills.count("3")

min_teams = min(no_1, no_2, no_3)
print(min_teams)

for i in range(min_teams):
    print(skills.index("1") + 1, skills.index("2") + 1, skills.index("3") + 1)
    skills[skills.index("1")] = 4
    skills[skills.index("2")] = 4
    skills[skills.index("3")] = 4
