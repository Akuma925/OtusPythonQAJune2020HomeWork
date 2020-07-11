import csv
import json


class BiblioClass:

    def c_res(self):
        list_book = []
        list_user = []
        with open('data/users.json', "r") as json_file:
            data_user = json.load(json_file)
        with open('data/books.csv', 'r') as csv_file:
            data_book = csv.DictReader(csv_file)
            for item in data_book:
                list_book.append(item)
        it = iter(list_book)
        if len(data_user) < len(list_book):
            for item in data_user:
                book_it = next(it)
                res = dict(name=item['name'], gender=item['gender'], address=item['address'],
                           book=[dict(title=book_it['Title'], author=book_it['Author'], height=book_it['Height'])])
                list_user.append(res)
        elif len(data_user) > len(list_book):
            for item in data_user:
                book_it = next(it)
                if next(it) is not None:
                    res = dict(name=item['name'], gender=item['gender'], address=item['address'],
                               book=[dict(title=book_it['Title'], author=book_it['Author'], height=book_it['Height'])])
                else:
                    res = dict(name=item['name'], gender=item['gender'], address=item['address'],
                           book=[dict()])
                list_user.append(res)
        r = list_user
        with open('data/result.json', "w") as file:
            s = json.dumps(list_user, indent=4)
            file.write(s)
        print("SUCCSESS")


b = BiblioClass()
b.c_res()

