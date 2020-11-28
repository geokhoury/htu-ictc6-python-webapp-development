'''
6. Ask the user for a lowercase string (`s`) as input. Create a function called `check_palindrome(s)` which returns the longest substring which is palindrome.
    * **Input:** `"I love python.nohtyp evol I Python is never odd or even"`
    * **Return:** `"never odd or even"`
'''

def check_palindrome(sentence):
    text = str(sentence).replace(" ", "").lower()
    i = 0
    j = len(text) - 1

    while j > i:
        print(text[i], text[j])
        if text[i] == text[j]:
            i = i + 1
            j = j - 1
        else:
            return False
    return text

my_sentences = ["I love python.nohtyp evol I", "Never odd or even", "some text"]

for sentence in my_sentences:
    if check_palindrome(sentence):
        print(f"Found a Palindrome > '{sentence}'")