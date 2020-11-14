# Runtime Functions

x = 4

# 0 <-- False
# Any other integer <-- True
 
if x:
    y = 2
    def hello():
        print('Hello, World!')
        print(f"y = {y}")
else:
    def hello():
        print('Hello, Universe!')

hello()
# Prints Hello, Universe!