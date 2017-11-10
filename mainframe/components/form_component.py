from mainframe.components.child_component import ChildComponent


class CheckboxGroup(ChildComponent):

    def __init__(self, title):
        super().__init__()
        self._set_type("CheckboxGroup")
        self._must_have_children()
        self._add_props({"title": title})


class CheckboxItem(ChildComponent):

    def __init__(self, checkbox_id, label):
        super().__init__()
        self._set_type("CheckboxItem")
        self._add_props({
            "id": checkbox_id,
            "label":  label
        })


class Dropdown(ChildComponent):
    def __init__(self, dropdown_id, label):
        super().__init__()
        self._set_type("Dropdown")
        self._add_props({
            "id": dropdown_id,
            "label": label,
            "options": []
        })

    def disable(self):
        return self._add_props({"disabled": True})

    def set_placeholder(self, placeholder):
        return self._add_props({"placeholder": placeholder})

    def add_options(self, options):
        if isinstance(options, str):
            return self._add_props({"options": options}, True)
        elif isinstance(options, list):
            for key, value in options:
                self._add_props({
                    "options": {
                        "label": value,
                        "value": key
                    }}, True)
        return self


class ListItem(ChildComponent):


    def __init__(self):
        super().__init__()
        self._set_type("ListItem")
        self._must_have_children()

    def set_list_type(self, list_type):
        #if(!in_array(type, ["copy_url", "open_url", "open_modal", "message_embed", "post_payload"])) {
        #    throw new UIException('The type of a ListItem must be either "copy_url", "open_url", "open_modal", "message_embed" or "post_payload"!')
        return self._add_props({"type": list_type})

    def set_payload(self, payload):
        #if(!in_array(self.getProp("type"), ["open_modal", "message_embed", "post_payload"])) {
        #    throw new UIException('To set a payload, the type of the ListItem must be either "open_modal", "message_embed" or "post_payload"!')
        return self._add_props({"payload": payload})

    def set_url(self, url):
        #if(!in_array(self.getProp("type"), ["copy_url", "open_url"])) {
        #    throw new UIException('To set an url, the type of the ListItem must be either "copy_url" or "open_url"!')
        return self._add_props({"url": url})

    def set_modal_title(self, title):
        #if(!in_array(self.getProp("type"), ["open_modal"])) {
        #    throw new UIException('To set a modal title, the type of the ListItem must be "open_modal"!')
        return self._add_props({"modalTitle": title})

    def add_children(self, component):
        #if(component instanceof Author || component instanceof AvatarList || component instanceof LinkPreview ||
        #    component instanceof IconTextGroup || component instanceof Image || component instanceof Text ||
        #     component instanceof VideoLinkPreview) {
        return self._add_children(component.get())
        #throw new UIException("The childs of a ListItem must be an instance of Author, AvatarList, IconTextGroup, Image, LinkPreview, Text or VideoLinkPreview!")


class ListComponent(ChildComponent):
    def __init__(self):
        super().__init__()
        self._set_type("ListComponent")
        self._must_have_children()

    def add_children(self, list_item: ListItem):
        return self._add_children(list_item.get())


    class MultiLineInput(ChildComponent):
        def __init__(self, id, label):
            super().__init__()
            self._set_type("MultiLineInput")
            self._add_props({
                "id": id,
                "label": label
            })

        def set_error_feedback(self, error):
            return self._add_props({"errorFeedback": error})


class MultiSelect(ChildComponent):

    def __init__(self, id, label):
        super().__init__()
        self._set_type("MultiSelect")
        self._add_props({
            "id": id,
            "label": label,
            "options": []
        })

    def disable(self):
        return self._add_props({"disabled": True})

    def add_options(self, options):
        if isinstance(options, str):
            return self._add_props({"options": options}, True)
        elif isinstance(options, list):
            for key, value in options:
                self._add_props({
                    "options": {
                        "label": value,
                        "value": key
                    }}, True)
        return self


class RadioButtonSelect(ChildComponent):
    def __init__(self, radio_button_id, button_title):
        super().__init__()
        self._set_type("RadioButtonSelect")
        self._add_props({
            "id": radio_button_id,
            "title": button_title,
            "options": []
        })

    def add_options(self, options):
        if isinstance(options, str):
            return self._add_props({"options": options}, True)
        elif isinstance(options, list):
            for key, value in options:
                self._add_props({
                    "options": {
                        "label": value,
                        "value": key
                    }}, True)
        return self
