import json

# File path for the config file
CONFIG_FILE = "config.json"

def load_config():
    """Load the configuration from a JSON file."""
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty config if no file is found

def save_config(config):
    """Save the configuration to a JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
