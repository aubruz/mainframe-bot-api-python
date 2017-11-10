from mainframe.child_component import ChildComponent


class Image(ChildComponent):

    def __init__(self, image_url, height, width):
        super().__init__()
        self._set_type("Image")
        self._add_props({
            "imageUrl": image_url,
            "height": height,
            "width": width
        })

    def allow_open_full_image(self):
        return self._add_props({"allowOpenFullImage": True})


class VideoLinkPreview(ChildComponent):

    def __init__(self, title):
        super().__init__()
        self._set_type("VideoLinkPreview")
        self._add_props({"title": title})

    def set_author(self, author):
        return self._add_props({"author": author})

    def set_url(self, url):
        return self._add_props({"url": url})

    def set_image_url(self, image_url):
        return self._add_props({"imageUrl": image_url})

    def set_image_width(self, width):
        return self._add_props({"imageWidth": width})

    def set_image_height(self, height):
        return self._add_props({"imageHeight": height})

    def set_domain_icon_url(self, domain_icon_url):
        return self._add_props({"domainIconUrl": domain_icon_url})

    def set_domain_name(self, domain_name):
        return self._add_props({"domainName": domain_name})

    def set_video_provider(self, video_provider):
        # if(video_provider !== 'youtube' && video_provider !== 'vimeo'){
        #    throw new UIException('Only youtube and vimeo are supported video provider.')
        return self._add_props({"videoProvider": video_provider})

    def set_video_id(self, video_id):
        # if(self.getProp('videoProvider') === null){
        #    throw new UIException('You need to specify a video provider.')
        return self._add_props({"videoId": video_id})

    def set_video_width(self, width):
        return self._add_props({"videoWidth": width})

    def set_video_height(self, height):
        return self._add_props({"videoHeight": height})

    def no_play_button(self):
        return self._add_props({"noPlayButton": True})


class MediaGallery(ChildComponent):

    def __init__(self):
        super().__init__()
        self._set_type("MediaGallery")
        self._must_have_children()

    def show_square_images(self):
        return self._add_props({"showSquareImages": True})

    def add_children(self, component):
        if isinstance(component, MediaItem):
            return self._add_children(component.get())
        # throw new UIException("Child of MediaGallery can only be a MediaItem")


class MediaItem(ChildComponent):

    def __init__(self, image_url):
        super().__init__()
        self._set_type("MediaItem")
        self._add_props({
            "imageUrl": image_url
        })

    def set_list_type(self, list_type):
        # if(!in_array(type, ["copy_url", "open_url", "open_modal", "message_embed", "post_payload"])) {
        #    throw new UIException('The type of a MediaItem must be either "copy_url", "open_url", "open_modal", "message_embed" or "post_payload"!')
        return self._add_props({"type": list_type})

    def set_width(self, width):
        return self._add_props({"width": width})

    def set_height(self, height):
        return self._add_props({"height": height})

    def set_payload(self, payload):
        # if(!in_array(self.getProp("type"), ["open_modal", "message_embed", "post_payload"])) {
        #    throw new UIException('To set a payload, the type of the MediaItem must be either "open_modal", "message_embed" or "post_payload"!')
        return self._add_props({"payload": payload})

    def set_url(self, url):
        # if(!in_array(self.getProp("type"), ["copy_url", "open_url"])) {
        #    throw new UIException('To set an url, the type of the MediaItem must be either "copy_url" or "open_url"!')
        return self._add_props({"url": url})

    def set_modal_title(self, title):
        # if(!in_array(self.getProp("type"), ["open_modal"])) {
        #    throw new UIException('To set a modal title, the type of the MediaItem must be "open_modal"!')
        return self._add_props({"modalTitle": title})

    def is_selected(self):
        return self._add_props({"isSelected": True})

    def set_selected_border_color(self, color):
        # if(self.getProp("isSelected") === null || self.getProp("isSelected") === false){
        #    throw new UIException("You need to set isSelected to True in order to use setSelectedBorderColor() in a MediaItem!")
        return self._add_props({"selectedBorderColor": color})

    def set_background_color(self, color):
        return self._add_props({"backgroundColor": color})


class AvatarList(ChildComponent):

    def __init__(self, avatars):
        super().__init__()
        self._set_type("AvatarList")
        self._add_props({
            "avatars": avatars
        })

    def add_avatarurl_(self, name):
        return self._add_props({"avatars": name}, True)

    def is_circle(self):
        return self._add_props({"isCircle": True})


class IconTextGroup(ChildComponent):

    def __init__(self, primary_text):
        super().__init__()
        self._set_type("IconTextGroup")
        self._add_props({"primaryText": primary_text})

    def set_secondary_text(self, text):
        return self._add_props({"secondaryText": text})

    def set_image_url(self, url):
        self._add_props({"imageUrl": url})


class LinkPreview(ChildComponent):

    def __init__(self, title, url):
        super().__init__()
        self._set_type("LinkPreview")
        self._add_props({
            "title": title,
            "url": url
        })

    def add_excerpt(self, excerpt):
        return self._add_props({"excerpt": excerpt})

    def add_image_url(self, url):
        return self._add_props({"imageUrl": url})

    def add_domain_icon_url(self, url):
        return self._add_props({"domainIconUrl": url})

    def add_domain_name(self, domain_name):
        return self._add_props({"domainName": domain_name})


class Author(ChildComponent):

    def __init__(self, display_name, username):
        super().__init__()
        self._set_type("Author")
        self._add_props({
            "displayName": display_name,
            "username":  username
        })

    def add_avatar_url(self, url):
        self._add_props({"avatarUrl" : url})
        return self

    def is_circle(self):
        self._add_props({"isCircle" : True})
        return self
