# interface/cli/cli_manager.py

import os
import importlib
from pathlib import Path
from collections import OrderedDict

CLI_FOLDER = Path(__file__).parent
EXCLUDED_FILES = {"utils.py", "__init__.py", "cli_manager.py"}


def discover_cli_modes():
    """
    Discovers all CLI modes and returns an OrderedDict sorted by MENU_ORDER then MENU_NAME.
    """
    mode_entries = []

    for file in os.listdir(CLI_FOLDER):
        if not file.endswith(".py") or file in EXCLUDED_FILES:
            continue

        module_name = file[:-3]  # Strip .py
        import_path = f"interface.cli.{module_name}"

        try:
            module = importlib.import_module(import_path)

            # Look for a run_*_mode function
            for attr in dir(module):
                if attr.startswith("run_") and attr.endswith("_mode"):
                    function = getattr(module, attr)

                    # Optional customizations
                    menu_name = getattr(module, "MENU_NAME", module_name.replace("cli_", "").capitalize())
                    menu_order = getattr(module, "MENU_ORDER", 9999)

                    mode_entries.append((menu_order, menu_name, function))
        except Exception as e:
            print(f"[cli_manager] ⚠️ Failed to import {import_path}: {e}")

    # Sort by MENU_ORDER, then MENU_NAME
    sorted_modes = sorted(mode_entries, key=lambda x: (x[0], x[1]))
    return OrderedDict((name, func) for _, name, func in sorted_modes)


cli_modes = discover_cli_modes()
