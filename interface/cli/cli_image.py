import sys
from core.image_engine import analyze_image
from interface.cli.utils import handle_special_commands

def run_image_mode():
    print("🖼️  Image analysis mode activated. Type /exit to quit or /menu to return.\n")

    while True:
        file_path = input("📁 Enter path to image file (.jpg, .jpeg, .png): ").strip()
        if not handle_special_commands(file_path):
            break

        prompt = input("📝 Instruction for the model (or press Enter for default): ").strip()
        if not prompt:
            prompt = "Describe this image."

        print("⏳ Processing...\n")
        result = analyze_image(file_path, prompt)
        print(f"\n🤖 Result:\n{result}\n")
