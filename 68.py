from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """Formats text into fully justified lines of a given width.

        Args:
            words: A list of strings to be formatted.
            maxWidth: The maximum number of characters allowed per line.

        Returns:
            A list of strings representing the justified text.
        """
        res = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding this word (plus a space) exceeds maxWidth
            # len(current_line) represents the minimum spaces needed between words
            if current_length + len(word) + len(current_line) > maxWidth:
                # Process the completed line
                res.append(self._format_line(current_line, current_length, maxWidth, False))
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
            
        # Handle the very last line
        res.append(self._format_line(current_line, current_length, maxWidth, True))
        
        return res

    def _format_line(self, line: List[str], length: int, maxWidth: int, is_last: bool) -> str:
        """Helper to distribute spaces for a single line.

        Args:
            line: The list of words in the current line.
            length: The total length of the words without spaces.
            maxWidth: The target width.
            is_last: Boolean indicating if this is the last line of the text.

        Returns:
            A single justified string.
        """
        num_words = len(line)
        
        # Rule 1: Last line or single word line (Left Justified)
        if is_last or num_words == 1:
            s = " ".join(line)
            return s + " " * (maxWidth - len(s))
        
        # Rule 2: Middle lines (Fully Justified)
        total_spaces = maxWidth - length
        gap_count = num_words - 1
        
        # Calculate base spaces and extra spaces to be distributed from the left
        space_per_gap = total_spaces // gap_count
        extra_spaces = total_spaces % gap_count
        
        res = ""
        for i in range(gap_count):
            res += line[i]
            # Add base spaces + 1 extra space if i < extra_spaces
            res += " " * (space_per_gap + (1 if i < extra_spaces else 0))
            
        res += line[-1] # Add the last word
        return res