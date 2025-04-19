from core.docs_engine import analyze_pdf
from interface.cli.utils import handle_special_commands

def run_docs_mode():
    print("📄 Document analysis mode activated. Type /menu to return to menu, /exit to quit.\n")

    while True:
        file_path = input("📁 Enter path to .pdf file: ").strip()

        if not handle_special_commands(file_path):
            return

        prompt = input("📝 Instruction for the model (or press Enter for default): ").strip()
        if not prompt:
            prompt = "Summarize this document."

        print("⏳ Processing...\n")
        result = analyze_pdf(file_path, prompt)
        print(f"\n🤖 Result:\n{result}\n")
