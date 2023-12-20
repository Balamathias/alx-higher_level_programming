# Python Classes

Mastering the concepts of OOP in python... Let me wrote some python code

```py
class User:

    __role = "user"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _set_role(self, role=None):
        self.__role = role if role is not None else "user"

    @statitmethod
    def get_username(self):
        return self.username

user = User("Matie", "****")

user._set_role(role="staff")
print(User.get_username)
```

### Python is cool!
