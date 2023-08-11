import os

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Borderbox(Widget):
    def __init__(self, **kwargs):
        super(Borderbox, self).__init__(**kwargs)
        self.bind(size=self.redraw, pos=self.redraw)

    def redraw(self, *args):
        self.canvas.clear()

        border_color = (0, 0, 0, 1)         # Black border color
        fill_color = (1, 1, 1, 1)  # Lighter gray fill color
        shadow_color = (0, 0, 0, 0.6)      # Adjusted shadow color

        border_width = 3  # Adjust the border width

        with self.canvas:
            # Draw shadow
            Color(*shadow_color)
            Rectangle(pos=(self.x + 6, self.y - 6), size=(self.width, self.height))

            # Draw border
            Color(*border_color)
            Rectangle(pos=(self.x, self.y), size=(self.width, self.height), width=border_width)

            # Draw fill
            Color(*fill_color)
            Rectangle(pos=(self.x + border_width, self.y + border_width),
                      size=(self.width - 2 * border_width, self.height - 2 * border_width))


class ModernWhiteApp(App):
    def build(self):
        layout = FloatLayout()

        # Construct image file paths based on the script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_analyzer_img_path = os.path.join(script_dir, 'file-upload.png')
        chatbot_assistant_img_path = os.path.join(script_dir, 'comment-alt.png')

        # Add the image with a specific size and position
        File_Analyzer_img = Image(source=file_analyzer_img_path,
                                  size_hint=(None, None), size=(100, 100),
                                  pos_hint={'x': 0.01, 'center_y': 0.69})
        layout.add_widget(File_Analyzer_img)

        # Add the label (text) below the image
        lbl_file = Label(text='File Analyzer', size_hint=(None, None), height=50, width=100,
                         pos_hint={'x': 0.02, 'center_y': 0.58},  # Positioning it just below the image
                         color=(0, 0, 0, 1), bold=True)
        layout.add_widget(lbl_file)

        Chatbot_Assistant_img = Image(source=chatbot_assistant_img_path, size_hint=(None, None),
                                      size=(100, 100),
                                      pos_hint={'x': 0.02, 'center_y': 0.36})
        layout.add_widget(Chatbot_Assistant_img)

        lbl_chat = Label(text='Chatbot Assistant', size_hint=(None, None), height=50, width=50,
                         pos_hint={'x': 0.06, 'center_y': 0.25}, color=(0, 0, 0, 1), bold=True)

        layout.add_widget(lbl_chat)

        border_box = Borderbox(size_hint=(0.8, 0.89), pos_hint={'x': 0.18, 'y': 0.06})
        layout.add_widget(border_box)

        return layout


if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    ModernWhiteApp().run()

