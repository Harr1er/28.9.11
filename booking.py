import requests
import json


class Booking:
    url = "https://restful-booker.herokuapp.com"

    def create_token(self, token):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(token)
        return requests.post(self.url + '/auth', headers=headers, data=data)

    def create_booking(self, token, booking):
        # Создание бронирования
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        data = json.dumps(booking)
        return requests.post(self.url + '/booking', headers=headers, data=data)

    def get_booking(self, token, bookingid):
        # Получение бронирования
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        return requests.get(self.url + f'/booking/{bookingid}', headers=headers)

    def get_list_of_bookings(self, token, filter):
        # Получение списка бронирований
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        return requests.get(self.url + f'/booking', headers=headers, params=filter)

    def update_booking(self, token, bookingid, booking):
        # Создание бронирования
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        data = json.dumps(booking)
        return requests.put(self.url + f'/booking/{bookingid}', headers=headers, data=data)

    def delete_booking(self, token, bookingid):
        # Получение бронирования
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        return requests.delete(self.url + f'/booking/{bookingid}', headers=headers)

my_booking = Booking()