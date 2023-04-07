def prepare_data(arg):
    """Метод подготовки тестовых данных"""

    if arg == 'booking':
        data = {
                'firstname': 'Nata',
                'lastname': 'New',
                'totalprice': 100,
                'depositpaid': True,
                "bookingdates": {
                    'checkin': "2023-03-20",
                    'checkout': "2023-03-30"
                },
                'additionalneeds': 'sea view'
        }
    elif arg == 'full_change_booking':
            data = {
                'firstname': 'Natalia',
                'lastname': 'Newton',
                'totalprice': 150,
                'depositpaid': True,
                "bookingdates": {
                    'checkin': "2023-03-20",
                    'checkout': "2023-03-30"
                },
            }
    elif arg == 'part_change_booking':
            data = {
                'totalprice': 350,
                "bookingdates": {
                    'checkout': "2023-03-25"
                },
            }
    elif arg == 'token':
        data = {
                "username": "admin",
                "password": "password123"
        }
    elif arg == 'filter':
        data = {
                "firstname": "John"
        }
    return data