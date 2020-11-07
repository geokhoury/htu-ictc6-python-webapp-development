# Dictionary Basics

# > Creating a dictionary
course = {
    'name': 'Python Web',
    'code': 'ICTC6',
    'number_of_hours': 180,
    'active': True
}

# # > Getting a key - Direct Memory Access
# print(f"The course title is: {course['name']}.")
# print(f"The course code is: {course['code']}.")
# # print(f"The course location is: {course['location']}.")      # This will raise a KeyError

# # > Getting a key - using the get() method
# print(f"The course title is: {course.get('name')}.")
# print(f"The course code is: {course.get('code')}.")

# # > Set default value for the key 'id'
# course.setdefault('id', course.get('code'))
# print(f"The course ID is: {course.get('id')}.")  # This will not raise an error

# # > Adding elements
# course['location'] = 'Online'
# course['id'] = 'ICTC6 Python Web'

# # > WWTP?
# print(course)

# # > Get the Length
# print(f"The dictionary contains {len(course)} items.")

# # > Copying a dictionary
# other_course = course.copy()
# other_course['name'] = "Introduction to Origami"
# other_course['id'] = "Origami 101"
# print(course)
# print(other_course)


# > Getting all items
items = list(course.items())              # Returns a list of tuples
print(f"The items are: {items}")

# > WWTP?
print(f"The course has {items[2][0]} : {items[2][1]}.")
print(f"The course has {items[0][0]} : {items[0][1]}.")

# > Getting all keys and values
keys = course.keys()
values = course.values()

print(f"The keys are: {keys}")      # returns a list of keys
print(f"The items are: {values}")   # returns a list of values


# # > Clearing a dictionary
# print(course)
# course.clear()
# print(course)  # {}
