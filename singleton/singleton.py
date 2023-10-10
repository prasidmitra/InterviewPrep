import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = f"I am a singleton and my value is {value}"


if __name__ == "__main__":
    s1 = Singleton(1)
    print(s1.value)
    s2 = Singleton(2)
    print(s2.value)
    print(s1.value)
