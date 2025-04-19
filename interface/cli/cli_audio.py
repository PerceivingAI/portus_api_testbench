# interface/cli/cli_audio.py

from core.audio_engine import analyze_audio

def run_audio_mode():
    print("🎧 Audio analysis mode activated. Type /exit to return.\n")

    while True:
        file_path = input("📁 Enter path to audio file (.mp3, .wav, .flac): ").strip()

        if file_path.lower() == "/exit":
            print("👋 Exiting audio mode.\n")
            break

        prompt = input("📝 Instruction for the model (or press Enter for default): ").strip()
        if not prompt:
            prompt = "Describe the audio."

        print("⏳ Processing...\n")
        result = analyze_audio(file_path, prompt)
        print(f"\n🤖 Result:\n{result}\n")
