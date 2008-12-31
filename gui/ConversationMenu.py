import Menu

import gettext

_ = gettext.gettext

class ConversationMenu(Menu.Menu):
    '''a class that represent the menu to customize the widgets that are shown
    on a given conversation'''

    def __init__(self, conversation):
        '''constructor'''
        Menu.Menu.__init__(self)

        self.set_image_visible = conversation._set_image_visible
        self.set_header_visible = conversation._set_header_visible
        self.set_toolbar_visible = conversation._set_toolbar_visible

        self.show_images = Menu.CheckBox(_('Show _images'), 
            conversation.image_visible)
        self.show_header = Menu.CheckBox(_('Show _header'), 
            conversation.header_visible)
        self.show_toolbar = Menu.CheckBox(_('Show _toolbar'), 
            conversation.toolbar_visible)

        self.show_images.signal_connect('toggled', self._on_show_images_toggled)
        self.show_header.signal_connect('toggled', self._on_show_header_toggled)
        self.show_toolbar.signal_connect('toggled', 
                self._on_show_toolbar_toggled)

        self.append(self.show_images)
        self.append(self.show_header)
        self.append(self.show_toolbar)

    def _on_show_images_toggled(self, checkbox, value):
        '''called when the show images is toggled'''
        self.set_image_visible(checkbox.toggled)

    def _on_show_header_toggled(self, checkbox, value):
        '''called when the show headers is toggled'''
        self.set_header_visible(checkbox.toggled)

    def _on_show_toolbar_toggled(self, checkbox, value):
        '''called when the show toolbars is toggled'''
        self.set_toolbar_visible(checkbox.toggled)
