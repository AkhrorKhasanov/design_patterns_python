class Computer:
    def __init__(self, cpu, ram, storage, gpu):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"


class ComputerBuilder:
    def __init__(self):
        self.cpu = "Intel i5"
        self.ram = "8GB"
        self.storage = "256GB SSD"
        self.gpu = None

    def set_cpu(self, cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def add_gpu(self, gpu):
        self.gpu = gpu
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage, self.gpu)


builder = ComputerBuilder()
gaming_pc = builder.set_cpu("Intel i9").set_ram('32GB').set_storage('1TB SSD').add_gpu('NVIDIA RTX 4080').build()
print(gaming_pc)