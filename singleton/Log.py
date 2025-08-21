class Log:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

a = Log()
b = Log()

a.logs.append("Сообщение 1")
print(b.logs)
print(a is b)