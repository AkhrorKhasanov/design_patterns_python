class WindowsButton:
    def render(self):
        return "Windows Button"


class WindowsCheckbox:
    def render(self):
        return "Windows Checkbox"


class MacButton:
    def render(self):
        return "Mac Button"


class MacCheckbox:
    def render(self):
        return "Mac Checkbox"


class WindowsFactory:
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory:
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


def create_ui(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


windows_factory = WindowsFactory()
create_ui(windows_factory)

print('-' * 10)

mac_factory = MacFactory()
create_ui(mac_factory)
