from PyQt5.QtCore import pyqtSignal, QObject

MONTHS = {
    'январь' : {
        'number' : '1',
        'season' : 'зима'
    },
    'февраль' : {
        'number' : '2',
        'season' : 'зима'
    },
    'март' : {
        'number' : '3',
        'season' : 'весна'
    },
    'апрель' : {
        'number' : '4',
        'season' : 'весна'
    },
    'май' : {
        'number' : '5',
        'season' : 'весна'
    },
    'июнь' : {
        'number' : '6',
        'season' : 'лето'
    },
    'июль' : {
        'number' : '7',
        'season' : 'лето'
    },
    'август' : {
        'number' : '8',
        'season' : 'лето'
    },
    'сентябрь' : {
        'number' : '9',
        'season' : 'осень'
    },
    'октябрь' : {
        'number' : '10',
        'season' : 'осень'
    },
    'ноябрь' : {
        'number' : '11',
        'season' : 'осень'
    },
    'декабрь' : {
        'number' : '12',
        'season' : 'зима'
    }
}


class MonthInfo(QObject):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.number = ''
        self.season = ''

    def update_value(self, new_value: str):
        if new_value not in MONTHS:
            self.number = ''
            self.season = ''
        else:
            self.number = MONTHS[new_value]['number']
            self.season = MONTHS[new_value]['season']
