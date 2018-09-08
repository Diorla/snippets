def vowel_counter():
    string = input("Enter the string you want to count\n")
    total = len(string)
    vowel = 0
    consonant = 0
    if(total <= 1):
        return "Text is empty"
    for i in string.lower():
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        elif i in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', \
                   'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
            consonant += 1
        # remove space
        elif i == " ":
            total -= 1
    others = total - vowel-consonant
    
    print("-"*50)
    print(f"vowel: {vowel}, consonant: {consonant}, others: {others}, total: {total}")
    return [vowel, consonant, others, total]


if __name__ == "__main__":
    vowel_counter()
    print("-"*50)
    input("Press enter to continue")
