import argparse
from core.chat_engine import chat_with_model
from config_manager import config, get_provider_name
from api_module.api_factory import get_client
from interface.cli.cli_chat import run_chat_mode
from interface.cli.cli_audio import run_audio_mode
from interface.cli.cli_embed import run_embedding_mode
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def show_menu():
    while True:
        print("\nSelect mode:")
        print("1. Chat")
        print("2. Audio")
        print("3. Embeddings")
        print("4. Exit")
        choice = input("➤ Enter choice (1-4): ").strip()

        if choice == "1":
            run_chat_mode()
        elif choice == "2":
            run_audio_mode()
        elif choice == "3":
            run_embedding_mode()
        elif choice == "4":
            print("👋 Exiting.")
            sys.exit(0)
        else:
            print("❌ Invalid selection. Please try again.")


def launch_portus():
    parser = argparse.ArgumentParser(description="Portus Modular Entry Point")
    parser.add_argument("--chat", action="store_true", help="Launch in chat mode")
    parser.add_argument("--audio", action="store_true", help="Launch in audio mode")
    parser.add_argument("--embed", action="store_true", help="Launch in embedding mode")
    args = parser.parse_args()

    if args.chat:
        run_chat_mode()
    elif args.audio:
        run_audio_mode()
    elif args.embed:
        run_embedding_mode()
    else:
        show_menu()
