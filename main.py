import os

WORD = "defenestration"


def main():
    assert 1 <= len(WORD) <= 24, "entry must be 1-24 characters"
    assert WORD.strip() == WORD and WORD.strip() != "", "entry must be non-blank"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
