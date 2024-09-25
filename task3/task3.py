import timeit

class BoyerMoore:
    def search(self, text, pattern):
        m = len(pattern)
        n = len(text)
        bad_char = {}
        
        for i in range(m):
            bad_char[pattern[i]] = i
            
        s = 0
        while s <= n - m:
            j = m - 1
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1
            if j < 0:
                return s
            else:
                s += max(1, j - bad_char.get(text[s + j], -1))
        return -1

class KMP:
    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, text, pattern):
        lps = self.compute_lps(pattern)
        i = j = 0
        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                return i - j
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

class RabinKarp:
    def search(self, text, pattern):
        d = 256
        q = 101
        m = len(pattern)
        n = len(text)
        p = 0  # hash value for pattern
        t = 0  # hash value for text
        h = 1
        
        for i in range(m - 1):
            h = (h * d) % q
        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for i in range(n - m + 1):
            if p == t:
                for j in range(m):
                    if text[i + j] != pattern[j]:
                        break
                if j == m - 1:
                    return i
            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t += q
        return -1

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm.search(text, pattern), number=1000)

def main():
    # Читання текстових файлів
    with open('task3/article1.txt', 'r', encoding='ISO-8859-1') as file:
        text1 = file.read()
    with open('task3/article2.txt', 'r', encoding='ISO-8859-1') as file:
        text2 = file.read()

    algorithms = {
        "Boyer-Moore": BoyerMoore(),
        "KMP": KMP(),
        "Rabin-Karp": RabinKarp()
    }

    patterns = {
        "existing": "підрядок",  # Вкажіть реальний підрядок
        "non_existing": "вигаданий_підрядок"
    }

    for text_num, text in zip(["Article 1", "Article 2"], [text1, text2]):
        print(f"\n{text_num} results:")
        for name, algorithm in algorithms.items():
            for pattern_name, pattern in patterns.items():
                time_taken = measure_time(algorithm, text, pattern)
                print(f"{name} - {pattern_name}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()