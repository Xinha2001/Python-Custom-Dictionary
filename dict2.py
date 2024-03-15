class KeyNotFoundException(Exception):
    def __init__(self, key):
        super().__init__(f"Key '{key}' not found.")

class dict2:
    def __init__(self):
        self._keys = []
        self._values = []

    def __setitem__(self, key, value):
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __getitem__(self, key):
        if key in self._keys:
            index = self._keys.index(key)
            return self._values[index]
        else:
            raise KeyNotFoundException(key)

    def __iter__(self):
        return iter(self._keys)

    def __len__(self):
        return len(self._keys)
