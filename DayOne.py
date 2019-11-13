lineList = [line.rstrip('\n') for line in open('one')]
# print(lineList)

result = 0
result_list = []
for i in lineList:
    result_list.append(result)
    result += int(i)
    if result in result_list:
        print(result)
print(result)


result = 0
result_list = []
should_continue = True
while should_continue:
    print("while loop")
    for i in lineList:
        print("for loop")
        result_list.append(result)
        result += int(i)
        if result in result_list:
            should_continue = False
            print(result)
print(result)
