import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        file_name, file_name_ext = os.path.splitext(self.photo_file_name)
        return file_name_ext


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        try:
            self.body_length, self.body_width, self.body_height = map(float, body_whl.split('x'))
        except ValueError:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            row_check = True
            if len(row) > 0:
                if row[0] == 'car':
                    file_name, file_name_ext = os.path.splitext(row[3])
                    if file_name_ext not in ['.jpg', '.jpeg', '.png', '.gif'] or row[1] == '':
                        row_check = False
                    if row_check:
                        try:
                            car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                        except ValueError:
                            pass
                elif row[0] == 'truck':
                    file_name, file_name_ext = os.path.splitext(row[3])
                    if file_name_ext not in ['.jpg', '.jpeg', '.png', '.gif'] or row[1] == '':
                        row_check = False
                    if row_check:
                        try:
                            car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                        except ValueError:
                            pass
                elif row[0] == 'spec_machine':
                    file_name, file_name_ext = os.path.splitext(row[3])
                    if file_name_ext not in ['.jpg', '.jpeg', '.png', '.gif'] or row[1] == '' or row[6] == '':
                        row_check = False
                    if row_check:
                        try:
                            car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
                        except ValueError:
                            pass
                else:
                    pass
    return car_list
