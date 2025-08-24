class CPU:
    def freeze(self):
        print("CPU: Freeze")

    def jump(self, position):
        print(f"CPU: Jump to {position}")

    def execute(self):
        print("CPU: Execute")

class Memory:
    def load(self, position, data):
        print(f"Memory: Load data {data} at {position}")

class HardDrive:
    def read(self, sector, size):
        print(f"HardDrive: Read {size} bytes from sector {sector}")
        return "Boot data"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hd = HardDrive()

    def start(self):
        print("Kompyuter vklyuchaetsya...")
        self.cpu.freeze()
        data = self.hd.read(0, 1024)
        self.memory.load(0, data)
        self.cpu.jump(0)
        self.cpu.execute()
        print("Kompyuter rabotaet!")

computer = ComputerFacade()
computer.start()