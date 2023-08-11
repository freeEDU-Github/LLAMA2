import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from langchain.llms import LlamaCpp
from langchain import PromptTemplate
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

Window.size = (400, 300)


class TextDisplayApp(App):

    def build(self):
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # The TextInput for displaying text
        self.text_display = TextInput(readonly=True, background_color=[1, 1, 1, 1], foreground_color=[0, 0, 0, 1],
                                      size_hint_y=0.9)
        main_layout.add_widget(self.text_display)

        # Layout for user input and button
        input_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=44)

        self.text_input = TextInput(hint_text="Enter your text here", size_hint_x=0.8)
        input_layout.add_widget(self.text_input)

        self.button = Button(text="Send", size_hint_x=0.2)
        self.button.bind(on_press=self.display_text)
        input_layout.add_widget(self.button)

        main_layout.add_widget(input_layout)

        return main_layout

    def display_text(self, instance):
        question = self.text_input.text
        answer = self.ask_llm(question)
        self.text_display.text = f"Question: {question}\n\nAnswer: {answer}"

    def ask_llm(self, question):
        prompt_template = "{question}\n\nAnswer:"

        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

        n_gpu_layers = 3
        n_batch = 1512

        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Construct the model path based on the script directory
        model_path = os.path.join(script_dir, "llama-2-13b-chat.ggmlv3.q8_0.bin")

        llm = LlamaCpp(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_batch=n_batch,
            f16_kv=True,
            callback_manager=callback_manager,
            verbose=True,
        )

        response = llm(prompt_template.format(question=question))
        # Extract answer from the response. This step may vary depending on how the LLM outputs its response.
        # Assuming the answer is simply contained in the response:
        return response.strip()  # Make sure to strip any extra whitespace


if __name__ == "__main__":
    TextDisplayApp().run()
