def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = [0]  # Start with the keys in the first box (box 0).
    opened = [False] * n  # Initialize an array to track if each box is opened.

    while keys:
        current_box = keys.pop()  # Get the current box from the keys.
        opened[current_box] = True  # Mark the current box as opened.

        # Add any new keys found in the current box to the list of keys.
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                keys.append(key)

    # If all boxes are opened, the 'opened' list will have all True values.
    return all(opened)

# Example usage:
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

