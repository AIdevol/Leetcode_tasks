class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
            result = []
            line = []
            line_length = 0

            for word in words:
                if line_length + len(word) + len(line) > maxWidth:
                    # Justify the current line and start a new line
                    spaces_to_add = maxWidth - line_length
                    if len(line) == 1:
                        result.append(line[0] + ' ' * spaces_to_add)
                    else:
                        spaces_between_words = spaces_to_add // (len(line) - 1)
                        extra_spaces = spaces_to_add % (len(line) - 1)
                        justified_line = ''
                        for i in range(len(line) - 1):
                            justified_line += line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
                        justified_line += line[-1]
                        result.append(justified_line)

                    # Start a new line
                    line = [word]
                    line_length = len(word)
                else:
                    # Add the word to the current line
                    line.append(word)
                    line_length += len(word)

            # Justify the last line (left-justified)
            result.append(' '.join(line).ljust(maxWidth))

            return result
