def twosum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    possible = {}
    solution = None

    for i, x in enumerate(nums):
        if possible.get(x) is not None:
            solution = [i, possible.get(x)]
            break

        possible[target - x] = i

    return solution

if __name__ == "__main__":
    print(twosum([2, 7, 11, 15], 9))
