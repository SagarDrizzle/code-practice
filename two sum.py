#commit on 28 March 2025
'''
n= 10
row_lenght = 1

while n > 0 :
    print("#" , end= " ")

    for _ in range(row_lenght):
        print(n, end=" ")
        n = n-1
row_lenght += 1
'''

#  input input = "aabccddeee"  output = "2a1b2c2d3e"

input = "aabccddeee"
cur_char = input[0]
count = 1
output_list = [ ]
n= len(input)
for char in range (1 , n):
    if input[char] == cur_char :
        count = count +  1
    else:
        output_list.append(f"{count}{cur_char}")
        count = 1
        cur_char = input[char]
output_list.append(f"{count}{cur_char}")
output = ''.join(output_list)

print(output)













