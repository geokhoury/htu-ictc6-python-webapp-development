# # > WWTP?

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally: 
#     print("d")

# # > WWTP?

# try:
#     print("a")
#     raise Exception("doom") 
# except:
#     print("b")
# else:
#     print("c")
# finally: 
#     print("d")

# > WWTP?

def f():
    try:
        print("a")
        return 
    except:
        print("b")
    else:
        print("c")
    finally:
        print("d")

f()