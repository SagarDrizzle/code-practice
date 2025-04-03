# Here are string related coding problem staement

# i am pushing something on 10-03-2025 13:13

class Solutions:
    def findelements(self, arr, n):
        missing_duplicate = [0, 0]
        print("pass")
        actual_arrelement = set(arr)
        genrated_expectedelement = set(range(1, n + 1))

        Cal_missing_elements = list(genrated_expectedelement - actual_arrelement)
        print(Cal_missing_elements)

        if Cal_missing_elements:
            missing_duplicate[0] = Cal_missing_elements[0]
            print(missing_duplicate)

        elementsCount = {}

        for element in arr:

            if element in elementsCount:
                elementsCount[element] += 1
            else:
                elementsCount[element] = 1

        print(elementsCount)

        Duplicate_elements = [key for key, value in elementsCount.items() if value > 1]

        missing_duplicate[1] = Duplicate_elements[0]

        return missing_duplicate


arr = [1, 2, 2, 4]
n = 5

solutions = Solutions()
print("Final o/p")
print(solutions.findelements(arr, n))