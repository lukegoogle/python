from collections import Counter

def minWindow(s: str, t: str) -> str:
    """Finds the minimum window substring of s that contains all characters in t.

    Uses the sliding window technique with two pointers and a frequency 
    dictionary to achieve linear time complexity.

    Args:
        s: The source string to search within.
        t: The target string containing characters to look for.

    Returns:
        The smallest substring of s containing all characters of t. 
        Returns an empty string if no such window exists.
    """
    if not t or not s:
        return ""

    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)
    required = len(dict_t)

    # Left and Right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t
    # are present in the current window in its required frequency.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):
        # Add one character from the right to the window
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If the frequency of the current character added equals to the
        # desired count in t then increment the formed count by 1.
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            char = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `Left` pointer 
            # is no longer a part of the window.
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            # Move the left pointer ahead, this helps in look for a new window.
            l += 1    

        # Keep expanding the window once we are done contracting.
        r += 1    

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]