class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        # Create a dictionary to map values in arr2 to their index
        order = {value: index for index, value in enumerate(arr2)}

        # Split arr1 into two lists: one for elements in arr2 and one for elements not in arr2
        in_arr2 = [x for x in arr1 if x in order]
        not_in_arr2 = [x for x in arr1 if x not in order]

        # Sort in_arr2 based on the order in arr2
        in_arr2.sort(key=lambda x: order[x])

        # Sort not_in_arr2 in ascending order
        not_in_arr2.sort()

        # Concatenate the two lists
        return in_arr2 + not_in_arr2
