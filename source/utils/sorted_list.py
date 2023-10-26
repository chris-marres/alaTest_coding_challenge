from bisect import insort


class SortedList:
    def __init__(self):
        self._list = []

    def append(self, value):
        insort(self._list, value)

    def remove(self, value):
        self._list.remove(value)

    def __eq__(self, other: list) -> bool:
        return self._list == other

    def __getitem__(self, index):
        return self._list[index]

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        return str(self._list)

    def __repr__(self) -> str:
        return str(self._list)
