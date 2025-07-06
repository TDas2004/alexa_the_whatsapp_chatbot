import configparser
import os

def get_api_key(codeword):
    config = configparser.ConfigParser()

    # Get absolute path to the jarvis_key folder
    base_dir = os.path.dirname(__file__)  # This gives the folder of the script
    secret_file = os.path.join(base_dir, "alexa_key", ".secret_keys")

    print("Reading from:", secret_file)

    with open(secret_file, 'r') as f:
        print("File content loaded successfully (not shown for security).")

    config.read(secret_file)
    print("Sections found:", config.sections())

    try:
        return config["openai"][codeword]
    except KeyError:
        raise ValueError(f"Codeword '{codeword}' not found in [openai].")

get_api_key("alexa-codeword")
