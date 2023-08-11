import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

n_gpu_layers = 3
n_batch = 1512

llm = LlamaCpp(
    model_path="/mnt/Orin2SSD/LLAMA2/llama_test/llama-2-13b-chat.ggmlv3.q8_0.bin",
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    f16_kv=True,
    callback_manager=callback_manager,
    verbose=True,
    max_length=3024
)

class LLMApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create TextInput for displaying content
        self.text_input = TextInput(size_hint_y=0.8)
        self.layout.add_widget(self.text_input)

        # Create Button layout
        self.button_layout = BoxLayout(size_hint_y=0.2)

        # Create Load button
        self.load_button = Button(text='Load File')
        self.button_layout.add_widget(self.load_button)
        self.load_button.bind(on_release=self.show_filechooser)

        # Create Analyze button
        self.analyze_button = Button(text='Analyze')
        self.button_layout.add_widget(self.analyze_button)
        self.analyze_button.bind(on_release=self.analyze_content)

        self.layout.add_widget(self.button_layout)

        return self.layout

    def show_filechooser(self, instance):
        # Create FileChooser
        self.filechooser = FileChooserIconView()

        # Create BoxLayout
        box_layout = BoxLayout(orientation='vertical')

        # Add FileChooser to BoxLayout
        box_layout.add_widget(self.filechooser)

        # Create Select button
        select_button = Button(text='Select')
        select_button.bind(on_release=self.load_file)

        # Add Select button to BoxLayout
        box_layout.add_widget(select_button)

        # Create Popup
        self.popup = Popup(title='Choose a File',
                           content=box_layout,
                           size_hint=(0.9, 0.9))

        self.popup.open()

    def load_file(self, instance):
        try:
            # Get selected file path
            file_path = self.filechooser.selection[0]

            # Close the popup
            self.popup.dismiss()

            # Read the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Display content
            self.text_input.text = content

        except Exception as e:
            self.text_input.text = f"Failed to load file: {e}"

    def analyze_content(self, instance):
        # Get the content directly from the TextInput
        content = self.text_input.text

        # Prepend a prompt asking the model to explain the content
        full_prompt = "Explain the following code make it short:\n" + content

        # Prompt the model to get the answer
        result = llm(full_prompt)

        # Append the model's result to the existing content
        self.text_input.text += f"\n\nModel Result:\n{result}"

# Run the app
if __name__ == "__main__":
    LLMApp().run()
