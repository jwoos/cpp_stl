def answer(heights):
    heights_array = [0]
    water = 0
    max_left = 0
    max_right = 0

    for height in heights:
        
        next_index = heights.index(height) + 1
        before_index = heights.index(height) - 1
        

        if height > heights[next_index]:
            return "nothing"
        elif height < heights[next_index]:
