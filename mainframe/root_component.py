from mainframe.component import Component


class RootComponent(Component):

    def __init__(self):
        super().__init__()


class Form(RootComponent):

    def __init__(self):
        super().__init__()
        self._set_type('Form')
        self._must_have_children()

    def add_payload(self, payload):
        return super()._add_payload(payload)

    def add_data(self, key, value):
        return self._add_props({'data': {key: value}})


class Message(RootComponent):

    def __init__(self):
        super().__init__()
        self._set_type("Message")
        self._must_have_children()


class TextMessage(RootComponent):

    def __init__(self):
        super().__init__()
        self._set_type("TextMessage")
        self._must_have_children()


class Dialog(RootComponent):

    def __init__(self):
        super().__init__()
        self._set_type("Dialog")
        self._must_have_children()
