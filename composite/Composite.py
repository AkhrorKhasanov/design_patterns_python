class File:
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(" " * indent + f"📄 {self.name}")


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print(" " * indent + f"📁 {self.name}")
        for child in self.children:
            child.show(indent + 2)


root = Folder("Root")
root.add(File("file1.txt"))
root.add(File("file2.txt"))

docs = Folder("Documents")
docs.add(File("resume.pdf"))
docs.add(File("notes.docx"))

root.add(docs)

root.show()