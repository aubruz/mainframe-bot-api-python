from mainframe.components.child_component import ChildComponent


class Text(ChildComponent):

    def __init__(self):
        super().__init__()
        self._set_type("Text")
        self._must_have_children()


class TextButton(ChildComponent):

    def __init__(self):
        super().__init__()
        self._set_type("TextButton")
        self._must_have_children()

    def set_text_type(self, type):
        # if(!in_array(type, ["copy_url", "open_url", "open_modal", "post_payload"])) {
        #   throw new UIException('The type of a TextButton must be either "copy_url", "open_url", "open_modal" or "post_payload"!')
        return self._add_props({"type": type})

    def set_payload(self, payload):
        # if(!in_array(self.getProp("type"), ["open_modal", "post_payload"])) {
        #    throw new UIException('To set a payload, the type of the TextButton must be either "open_modal" or "post_payload"!')
        return self._add_props({"payload": payload})

    def set_url(self, url):
        # if(!in_array(self.getProp("type"), ["copy_url", "open_url"])) {
        #    throw new UIException('To set an url, the type of the TextButton must be either "copy_url" or "open_url"!')
        return self._add_props({"url": url})

    def set_modal_title(self, title):
        # if(!in_array(self.getProp("type"), ["open_modal"])) {
        #    throw new UIException('To set a modal title, the type of the TextButton must be "open_modal"!')
        return self._add_props({"modalTitle": title})


class TextHighlight(ChildComponent):

    def __init__(self):
        super().__init__()
        self._set_type("TextHighlight")
        self._must_have_children()

    def set_text_color(self, color):
        return self._add_props({"textColor": color})

    def set_highlight_color(self, color):
        return self._add_props({"highlightColor": color})


class TextInput(ChildComponent):

    def __init__(self, text_id, label):
        super().__init__()
        self._set_type("TextInput")
        self._add_props({
            "id": text_id,
            "label":  label
        })

    def set_prefix(self, prefix):
        return self._add_props({"prefix": prefix})

    def set_error_feedback(self, error):
        return self._add_props({"errorFeedback": error})

    def set_button_title(self, title):
        return self._add_props({"buttonTitle": title})

    def set_button_type(self, type):
        # if(type !== 'post_payload'){
        #    throw new UIException("The only possible value for buttonType in a TextInput Component is \"post_payload\"!")
        # if(self.getProp("buttonTitle") === null){
        #    throw new UIException('You must provide a title in order to set a type!')
        return self._add_props({"buttonType": type})

    def set_button_payload(self, payload):
        return self._add_props({"buttonPayload": payload})


class TextLink(ChildComponent):

    def __init__(self, url):
        super().__init__()
        self._set_type("TextLink")
        self._must_have_children()
        self._add_props({"url": url})

    def no_style(self):
        return self._add_props({"noStyle": True})

    def no_emojify(self):
        return self._add_props({"noEmojify": True})


class TextStyle(ChildComponent):

    def __init__(self, type):
        super().__init__()
        # if(!in_array(type, ["bold", "code", "italic", "strike"])) {
        #    throw new UIException('The type of a TextStyle must be either "bold", "code", "italic" or "strike"!')
        self._set_type("TextStyle")
        self._must_have_children()
        self._add_props({"type": type})


class TextSubtle(ChildComponent):

    def __init__(self):
        super().__init__()
        self._set_type("TextSubtle")
        self._must_have_children()
