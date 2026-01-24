class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

tom = Dog("Tom", "Dobermen")

tom.breed


class ApiConfig:
    def __init__(self, api_key, model="gpt-3.5", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens


dev_config = ApiConfig("dev-key", max_tokens = 50)

prod_config = ApiConfig("prod_key")

print(dev_config.max_tokens)
print(prod_config.max_tokens)
