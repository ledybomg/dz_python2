import json


class FileHandler:

    def __init__(self, path, name="Database"):
        self.path = path
        self.name = name
        self.object_structure = {"id": int,
                                 "name": str,
                                 "surname": str,
                                 "patronymic": str,
                                 "birth_date": str,
                                 "phone_number": str,
                                 "email": str,
                                 }

    def load_data(self):
        with open(self.path) as data_file:
            data = data_file.read()
            data = json.loads(data)
        return data

    def save_data(self, new_data):
        new_data = json.dumps(new_data, indent=2)
        with open(self.path, 'w') as data_file:
            data_file.write(str(new_data))

    def add_example(self):
        print(f"Adding new example to the {self.name} based on {self.path} file")
        new_object = {}
        for key, param_type in self.object_structure.items():
            print(f"Please, write {key} value:")
            while True:
                value = input()
                try:
                    value = self.object_structure[key](value)
                    break
                except Exception:
                    print("The exception handled while value type changing:")
                    print(Exception)
                    print("Please, try again.")
            new_object.update({key: value})
        data = self.load_data()
        data.append(new_object)
        self.save_data(new_data=data)
        print("done!")

    def delete_example(self, value, parameter="id"):
        delete_examples = self.find_example(value, parameter)
        data = self.load_data()
        for item in delete_examples:
            data.remove(item)
        self.save_data(new_data=data)
        print("done!")

    def change_example(self, value, parameter="id"):
        change_examples = self.find_example(value, parameter)
        print(change_examples)
        self.delete_example(value, parameter="id")
        changed_items = []
        for item in change_examples:
            print(f"Change the item {item}")
            new_object = {}
            for key, param_type in self.object_structure.items():
                print(f"Please, write {key} value:")
                while True:
                    value = input()
                    try:
                        value = self.object_structure[key](value)
                        break
                    except Exception:
                        print("The exception handled while value type changing:")
                        print(Exception)
                        print("Please, try again.")
                new_object.update({key: value})
            changed_items.append(new_object)
        data = self.load_data()
        for item in changed_items:
            data.append(item)
        self.save_data(new_data=data)
        print("done!")

    def find_example(self, value, parameter="id"):
        if parameter in self.object_structure.keys():
            data_type = self.object_structure[parameter]
            value = data_type(value)
            data = self.load_data()
            result_examples = []
            for item in data:
                if item[parameter] == value:
                    result_examples.append(item)
            return result_examples
        else:
            print(f"There's no such parameter in object structure.\n"
                  f"Choose one of these parameters to search:{self.object_structure}")

    def show_data(self):
        data = self.load_data()
        data = json.dumps(data, indent=2)
        print(data)


phone_book = FileHandler(path="phone_book.txt")
phone_book.change_example(value=4)

