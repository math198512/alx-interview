def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track unlocked boxes
    unlocked[0] = True  # The first box is unlocked
    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)  # Get the current box to process

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)