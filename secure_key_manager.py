import configparser
import os

def get_api_key(codeword):
    config = configparser.ConfigParser()
    
    base_dir = os.path.dirname(__file__)  # This makes the path absolute
    secret_file = os.path.join(base_dir, "alexa_key", ".secret_keys")

    print("Reading from:", secret_file)

    with open(secret_file, 'r') as f:
        content = f.read()
        print("File content loaded successfully (hidden for security).")

    config.read(secret_file)
    print("Sections found:", config.sections())

    try:
        key = config["openai"][codeword]
        print("✅ API Key Found:", key[:4] + "..." + key[-4:])
        return key
    except KeyError:
        raise ValueError(f" Codeword '{codeword}' not found in [openai].")

# 👇 This line is what actually runs the function
get_api_key("alexa-codeword")
