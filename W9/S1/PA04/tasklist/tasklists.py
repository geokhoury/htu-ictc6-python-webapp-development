from status import Status       # Remember to import status and priority from the provided files
from priority import Priority

# task lists

tasklists = {
    1: {
        "name": "Python list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            1,
            2,
            3
        ],
        "tags": ['python', 'programming', 'fullstack']
        },
    2: {
        "name": "Home list",
        "last_updated": "2012-04-23T18:25:43.511Z",
        "created_at": "2012-04-23T18:25:43.511Z",
        "tasks": [
            4,
            5
        ],
        "tags": ['python', 'programming', 'fullstack']
    }
}

# tasks

tasks = {
    1: {
        "name": "learn flask blueprints",
        "last_updated": "2020-04-23T18:25:43.511Z",
        "created_at": "2020-04-23T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Etiam sit amet massa nec urna hendrerit gravida et sed ipsum."
    },
    2: {
        "name": "learn Python enums",
        "last_updated": "2012-04-20T18:25:43.511Z",
        "created_at": "2012-04-20T18:25:43.511Z",
        "status": Status.IN_PROGRESS,
        "priority": Priority.MEDIUM,
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    },
    3:  {
        "name": "revise OOP concepts",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Ut eget elit interdum neque faucibus viverra."
    },
    4:  {
        "name": "clean keyboard",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Donec fermentum lacus ultrices mauris pretium, sit amet placerat felis dictum."
    },
    5:  {
        "name": "water plants",
        "last_updated": "2020-04-25T18:25:43.511Z",
        "created_at": "2020-04-25T18:25:43.511Z",
        "status": Status.DONE,
        "priority": Priority.HIGH,
        "description": "Nam imperdiet ligula quis ligula rhoncus, et vehicula sem consectetur."
    }
}

print(tasklists)
print(tasks)