'''
7. Ask the user for two lowercase words (`w1`, `w2`) as input. Create a function called `create_anagram(w1, w2)`. The only allowed operation is to remove a character from any string. Find minimum number of characters to be deleted to make both the strings anagram.
   * **Input:** `w1= abbacyxz`
   * **Output:**  ``
'''


# Check if two strings are anagrams of each other


def count_characters(word):
    char_count = dict()

    for char in word:
        if char not in char_count.keys():
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count


def create_anagram(w1, w2):
    count_w1 = count_characters(w1)
    count_w2 = count_characters(w2)

    print(count_w1, count_w2)
    
    count = 0

    for k in count_w1.keys():
        if k in count_w2.keys():
            print(f"Common letter {k}")
            count += 1
    print(len(count_w1) - 2, len(count_w2) -2)
    return (count_w1, count_w2)

create_anagram("hello", "billion")
