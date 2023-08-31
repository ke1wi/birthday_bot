
class Student:
    
    name: str
    birthday: str
    tag: str
    
    def __init__(self, name, birthday, tag) -> None:
        self.name = name
        self.birthday = birthday
        self.tag = tag
