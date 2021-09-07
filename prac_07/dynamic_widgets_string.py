
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgets(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strings = ["Otta", "Mango", "Berlin", "Silvester"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets_string.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.strings:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgets().run()
