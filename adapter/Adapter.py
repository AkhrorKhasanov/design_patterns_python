class OldPrinter:
    def old_print(self, text):
        print("Printing from old printer:", text)

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        self.old_printer.old_print(text)


old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

adapter.print("Hello, World!")