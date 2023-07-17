 
# Quick POE Wrapper - Sage GPT-4 💬🤖

This repository contains a simple, yet powerful command-line interface (CLI) utility for sending prompts to either Sage or GPT-4 (default) on the chatbot platform Poe. The tool leverages the `poe` Python library to handle the communication with the Poe API. 📡🚀

## 🛠️ Installation

To run the CLI utility, you need Python 🐍 installed on your computer. The utility has been tested with Python 3.7 but should work with other 3.x versions as well.

First, clone this repository:

```bash
git clone https://github.com/levkropp/quick-poe-wrapper-sage-gpt4.git
cd quick-poe-wrapper-sage-gpt4
```

Then, install [poe-api](https://github.com/ading2210/poe-api)
## 🚀 Usage

The utility provides a collection of command line arguments to customize the way messages are sent to the Poe platform:

- `-m` or `--message`: This argument allows you to specify the message to be sent. If no message is provided, the default message 'Say "you need to write your message with -m or --message!" and nothing else' will be used. 💬

- `-c` or `--client` or `-t` or `--token`: This argument should be used to provide the client token. If no token is provided through the command line, the script will use the `DEFAULT_TOKEN` defined in the script itself.

- `--sage`: This flag changes the recipient from "beaver" (GPT-4) to "capybara" (Sage). 🔄

Here is an example of how to use these arguments:

```bash
python main.py --message "Tell me something about llamas!" --client YOUR_CLIENT_TOKEN --sage
```

This will send the message "Tell me something about llamas!" to Sage. 🦙💖

## 📄 Output

The utility prints out the response from the Poe platform directly to the standard output.  📤🖥️
