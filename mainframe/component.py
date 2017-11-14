from mainframe.array_type import ArrayType


class Component(ArrayType):

    def __init__(self):
        super().__init__()
        self.can_have_children = False
        self.must_have_children = False
        self.json['type'] = ''
        self.json['props'] = {}

    def _can_have_children(self):
        self.can_have_children = True
        self.json['props']['children'] = []

        return self

    def _must_have_children(self):
        self._can_have_children()
        self.must_have_children = True

        return self

    def _set_type(self, component_type):
        self.json['type'] = component_type
        return self

    def _add_props(self, props: dict, append=False):
        for property_key, property_value in props.items():
            if append:
                if self.json['props'].get(property_key) is None:
                    self.json['props'][property_key] = []
                self.json['props'][property_key].append(property_value)
            elif isinstance(property_value, dict) and len(property_value):
                for key, value in property_value.items():
                    self.json['props'][property_key] = {key: value}
            else:
                self.json['props'][property_key] = property_value

        return self

    def _get_prop(self, prop):
        return self.json['props'].get(prop)

    def add_children(self, component):
        if self.can_have_children:
            if isinstance(component, Component):
                self._add_props({'children': component.get()}, True)
            else:
                self._add_props({'children': component}, True)

        return self
