 citations.sort(reverse=True)  # Sort the array in descending order

    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index