from typing import Any


class iList(list):
    def __init__(self, lst=None):
        list.__init__(self, lst)
        if lst is None:
            lst = list()

    def __getitem__(self, n: int) -> Any:
        if len(self) == 0 or len(self) < n:
            return None
        return super().__getitem__(n)
