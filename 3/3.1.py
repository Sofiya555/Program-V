class MyName:
    def __init__(self, name=None) -> None:
        self.name = name 
        if name is not None 
        else 
    self.anonymous_user().name 
        MyName.total_names += 1 
        self.my_id = self.total_names

    @property
    def whoami(self): 
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        return self.create_email()
    
    def create_email(self) -> str:
        return f"{self.name}ipynb

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!"):
        return f"You say: {message}"


print("Let's Start!")
names = ("Sofiya", "Petro", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
