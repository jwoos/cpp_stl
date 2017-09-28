def answer(heights):
    max_left = 0
    max_right = 0
    right = len(heights) - 1
    left = 0
    water = 0

    while left < right:
        if max_left < heights[left]:
            max_left = heights[left]
        if max_right < heights[right]:
            max_right = heights[right]
        if max_right >= max_left:
            water += max_left - heights[left]
            left += 1
        else:
            volume += max_right - heights[right]
            water -= 1
    return water
