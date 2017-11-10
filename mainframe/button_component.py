from mainframe.array_type import ArrayType


class UIButton(ArrayType):

    def __init__(self, title):
        super().__init__()
        self.json['title'] = title

    def _set_url(self, url):
        return self._set_prop('url', url)

    def _set_payload(self, payload):
        return self._set_prop('payload', payload)

    def _set_type(self, button_type):
        return self._set_prop('type', button_type)

    def _set_title(self, title):
        return self._set_prop('title', title)

    def _set_prop(self, prop, value):
        self.json[prop] = value

        return self

    def _get_prop(self, prop):
        return self.json.get(prop)


class MessageButton(UIButton):

    def __init__(self, title):
        super().__init__(title)

    def _set_type(self, type):
        # if(!in_array(type, ["copy_url", "open_url", "open_modal", "post_payload"])) {
        #    throw new UIException('The type of a MenuButton must be either "copy_url", "open_url", "open_modal" or "post_payload"!')
        return self._set_type(type)

    def set_modal_title(self, title):
        # if(!in_array(self.getProp("type"), ["open_modal"])) {
        #    throw new UIException('To set a modal title, the type of the button must be either "open_modal"!')
        return self._set_prop('modalTitle', title)

    def set_payload(self, payload):
        return self._set_payload(payload)


class ModalButton(UIButton):

    def __init__(self, title):
        super().__init__(title)

    def set_type(self, type):
        # if(!in_array(type, ["copy_url", "open_url", "close_modal", "message_embed", "post_payload", "form_post"])) {
        #    throw new UIException('The type of a MenuButton must be either "copy_url", "open_url", "close_modal", "message_embed", "post_payload" or "form_post"!')
        return self._set_type(type)

    def set_style(self, style):
        return self._set_prop('style', style)

    def set_payload(self, payload):
        return self._set_payload(payload)

    def set_url(self, url):
        # if(!in_array(self.getProp("type"), ["copy_url", "open_url"])) {
        #    throw new UIException('To set an url, the type of the button must be either "copy_url" or "open_url"!')
        return self._set_url(url)


class MenuButton(UIButton):

    def __init__(self, title):
        super().__init__(title)

    def _set_type(self, type):
        # if(!in_array(type, ["copy_url", "open_url", "open_modal", "message_embed", "post_payload"])) {
        #    throw new UIException('The type of a MenuButton must be either "copy_url", "open_url", "open_modal", "message_embed" or "post_payload"!')
        return super()._set_type(type)

    def set_icon(self, icon):
        return super()._set_prop('icon', icon)

    def set_modal_title(self, title):
        # if(!in_array(self.getProp("type"), ["open_modal"])) {
        #    throw new UIException('To set a modal title, the type of the MenuButton must be either "open_modal"!')
        return self._set_prop('modalTitle', title)

    def set_payload(self, payload):
        return super()._set_payload(payload)
