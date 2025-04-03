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

<<<<<<< Updated upstream
=======
print("################### End of Progarmme #############")

###### max frequnr char in string i/p = sagar o/p = a

ip_str = "sagar"

dict_ip = { }

for char in ip_str:
    dict_ip[char] = dict_ip.get(char,0)+1

max_fre_char = max(dict_ip, key=dict_ip.get)

print(max_fre_char, dict_ip[max_fre_char])

print( #################### End of Program ################################## )

class Solution:
    def findelements(self, arr, n):
        missing_duplicate = [0, 0]  # [Duplicate, Missing]
        num_set = set()

        # Identify duplicate number
        for num in arr:
            if num in num_set:
                missing_duplicate[0] = num  # Duplicate found
            else:
                num_set.add(num)

        # Identify missing number
        for i in range(1, n + 1):
            if i not in num_set:
                missing_duplicate[1] = i  # Missing found

        return missing_duplicate


# Example Usage
arr = [1, 2, 2, 4, 5]  # n=5, expected missing=3, duplicate=2
n = len(arr)
solution = Solution()
print(solution.findelements(arr, n))  # Output: [2, 3]

print( #################### End of Program ################################## )

'''

nested_list = [1, [2, 3], [4, 5], 6,[ 7, 8, 9]]

def flatten_list(nested):
    flat_list = [ ]
    for item in nested:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


nested_list = [1, [2, 3], [4, 5], 6, [7, 8, 9]]
output = flatten_list(nested_list)

print(output)


>>>>>>> Stashed changes












