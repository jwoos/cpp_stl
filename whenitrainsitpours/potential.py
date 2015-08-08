def answer(heights):
    max_height = max(heights)
    highest_index =  [i for i, j in enumerate(heights) if i == max_height]
    # loop backward and forward from highest height
    # compare current i
    for highest in highest_index:
        for height in heights:
            
