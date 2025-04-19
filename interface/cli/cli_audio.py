from portus_engine_module.engine_audio import analyze_audio
from interface.cli.utils import handle_special_commands

MENU_NAME = "Audio"
MENU_ORDER = 3

def run_audio_mode():
    print("🎧 Audio analysis mode activated. Type /menu to return or /exit to quit.\n")

    while True:
        file_path = input("📁 Enter path to audio file (.mp3, .wav, .flac): ").strip()
        if not handle_special_commands(file_path):
            break

        prompt = input("📝 Instruction for the model (or press Enter for default): ").strip()
        if not prompt:
            prompt = "Describe the audio."

        print("⏳ Processing...\n")
        result = analyze_audio(file_path, prompt)
        print(f"\n🤖 Result:\n{result}\n")
