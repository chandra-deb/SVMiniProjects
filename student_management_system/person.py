class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f'''
                Name: {self.name}
                Age: {self.age}
                Address: {self.address}
                '''
              )