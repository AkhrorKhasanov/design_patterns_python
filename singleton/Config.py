class Config:
    _instance = None


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {
                "DB_HOST": "localhost",
                "DB_PORT": 5432,
                "DEBUG": True,
            }
        return cls._instance


    def get(self, key):
        return self.settings[key]

    def set(self, key, value):
        self.settings[key] = value


a = Config()
b = Config()

print(a is b)
print(a.get("DB_HOST"))
b.set("DEBUG", False)
print(a.get("DEBUG"))