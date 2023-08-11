#!/bin/bash

# Install Kivy
pip install kivy

# Install llama-cpp-python with CMAKE_ARGS and FORCE_CMAKE
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

# Download the specified file
wget https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/blob/main/llama-2-13b-chat.ggmlv3.q8_0.bin

# Notify user about completion
echo "Setup completed successfully!"


