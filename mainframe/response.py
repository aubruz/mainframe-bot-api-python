from mainframe.array_type import ArrayType


class UIPayload(ArrayType):

    def __init__(self, version=1):
        super().__init__()
        self.json['version'] = version
        self.json['buttons'] = []

    def add_button(self, button):
        self.json['buttons'].append(button.get())

        return self

    def set_render(self, component):
        self.json['render'].append(component.get())

        return self


class AuthenticationData(ArrayType):

    def __init__(self, url):
        super().__init__()
        self.json['url'] = url
        self.json['type'] = 'authentication'

    def add_payload(self, payload):
        self.json['payload'] = payload.get()

        return self


class BotResponse(ArrayType):

    def __init__(self, success=True):
        super().__init__()
        self.json['success'] = success

    def set_success(self, success):
        self.json['success'] = success

    def add_message(self, message):
        self.json['message'] = message

    def add_data(self, data):
        self.json['data'] = data.get()


class EmbedData(ArrayType):

    def __init__(self):
        super().__init__()
        self.json['type'] = 'embed'

    def set_ui(self, ui_payload: UIPayload):
        self.json['components'] = ui_payload.get()

        return self


class ModalData(ArrayType):

    def __init__(self, title=''):
        super().__init__()
        self.json['title'] = title
        self.json['type'] = 'modal'

    def set_ui(self, ui_payload: UIPayload):
        self.json['ui'] = ui_payload.get()

        return self

    def set_title(self, title):
        self.json['title'] = title

        return self
