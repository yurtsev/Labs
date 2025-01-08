class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        return 'пароль успешно заменен!'

    def check_password(self, password_input):
        if self.__password == password_input:
            return True
        return False


Yura = UserAccount('yurtsev', 'yurkaburka@mail.ru', '759')

password_input = input(f'введите пароль для входа в аккаунт {Yura.username}')
print(Yura.check_password(password_input))

new_password = input(f'задайте новый пароль для входа в аккаунт {Yura.username}')
print(Yura.set_password(new_password))

#----------task 2-----------


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'макрка {self.make} модель {self.model}'

class Car (Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'макрка {self.make} модель {self.model} топливо {self.fuel_type}'

v1 = Vehicle('toyota', 'trueno')
c1 = Car('Nissan', 'teana', '95')
print(v1.get_info())
print(c1.get_info())