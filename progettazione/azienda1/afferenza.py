import datetime

class Afferenza:
    _data: datetime.date

    def __init__(self, data: datetime.date):
        self._data = data

    def data(self) -> datetime.date:
        return self._data