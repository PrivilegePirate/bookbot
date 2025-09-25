def word_num(text: str) -> int:
    return len(text.split())

def word_counter(text: str) -> dict[str, int]:
    counts = {}
    for token in text.split():
        word = "".join(ch for ch in token.lower() if ch.isalpha())
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts

def char_counter(text: str) -> dict[str, int]:
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(counts_dict: dict[str, int]) -> list[dict]:
    return sorted(
        ({"item": k, "num": v} for k, v in counts_dict.items()),
        key=lambda d: d["num"],
        reverse=True
    )