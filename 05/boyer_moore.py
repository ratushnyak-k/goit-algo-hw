def boyer_moore_search(text, pattern):
    if not pattern:
        return 0

    def build_shift_table(pattern):
        table = {}
        length = len(pattern)
        for index in range(length - 1):
            table[pattern[index]] = length - index - 1
        return table

    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        char = text[i + len(pattern) - 1]
        i += shift_table.get(char, len(pattern))

    return -1