import os

# Specify the full path to finetune.exe
finetune_path = "C:/Users/Mayra/Documents/BatLlama/Bat_llama.cpp/finetune.exe"

# Specify the model base path
model_base_path = "Bat_llama.cpp/models/mistral-7b-instruct-v0.2.Q2_K.gguf"

# Build the command
finetune_command = f"{finetune_path} --model-base {model_base_path}"

# Capture and print the output
try:
    # Use os.system to execute the command
    exit_code = os.system(finetune_command)

    # Check the exit code
    if exit_code == 0:
        print("Finetune command executed successfully.")
    else:
        print(f"Finetune command failed with exit code {exit_code}.")
except Exception as e:
    print("Error:", e)