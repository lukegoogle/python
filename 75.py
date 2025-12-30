def sortColors(nums: list[int]) -> None:
    """Sorts an array of 0s, 1s, and 2s in-place.

    This implementation uses the Dutch National Flag algorithm with three 
    pointers (low, mid, high) to sort the array in a single pass.

    Args:
        nums: A list of integers where 0 represents red, 1 represents white, 
            and 2 represents blue.

    Returns:
        None. The array is modified in-place.
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # Swap current element with the low pointer
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # Element is in the correct middle section
            mid += 1
        else:
            # Swap current element with the high pointer
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Note: We don't increment mid here because the new nums[mid] 
            # swapped from high needs to be evaluated.