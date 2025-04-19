# portus_manager.py

import argparse
import sys
from dotenv import load_dotenv

from interface.cli.cli_chat import run_chat_mode
from interface.cli.cli_audio import run_audio_mode
from interface.cli.cli_docs import run_docs_mode

load_dotenv()

def show_menu():
    while True:
        print("\nWelcome to Portus! Please select a Test:")
        print("1. Chat")
        print("2. Audio")
        print("3. Documents")
        print("4. Exit")
        choice = input("➤ Enter choice (1-4): ").strip()

        if choice == "1":
            run_chat_mode()
        elif choice == "2":
            run_audio_mode()
        elif choice == "3":
            run_docs_mode()
        elif choice == "4":
            print("👋 Exiting.")
            sys.exit(0)
        else:
            print("❌ Invalid selection. Please try again.")

def launch_portus():
    parser = argparse.ArgumentParser(description="Portus Modular Entry Point")
    parser.add_argument("--chat", action="store_true", help="Launch in chat mode")
    parser.add_argument("--audio", action="store_true", help="Launch in audio mode")
    parser.add_argument("--docs", action="store_true", help="Launch in docs mode")
    args = parser.parse_args()

    if args.chat:
        run_chat_mode()
    elif args.audio:
        run_audio_mode()
    elif args.docs:
        run_docs_mode()
    else:
        show_menu()
