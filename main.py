from C_Prinzip import apply_c_principle
import os

def open_and_apply(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        german_text = file.read()

    result_text = apply_c_principle(german_text)

    base_name, extension = os.path.splitext(input_file_path)
    output_file_path = base_name + "_TEST" + extension

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(result_text)

# Example usage
input_file_path = r"Texts\Weltraumerkundung.txt"  # Provide the actual file path

open_and_apply(input_file_path)