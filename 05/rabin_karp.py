def rabin_karp_search(text, pattern):
    if not pattern:
        return 0

    d = 256
    q = 101
    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    h = 1
    p = 0
    t = 0

    for _ in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return -1