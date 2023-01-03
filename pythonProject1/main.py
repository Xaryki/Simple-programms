def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in range(len(sentence)):
        if sentence[i] in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(get_count("kata"))
