import argparse
import poe

# If you want to use a default token, assign it to DEFAULT_TOKEN.
# Otherwise, leave it as None.
DEFAULT_TOKEN = None

# Create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Add the arguments
parser.add_argument('-m', '--message', type=str, default='Say "you need to write your message with -m or --message!" and nothing else',
                    help='a message to be sent')
parser.add_argument('-c', '--client', '-t', '--token', type=str, default=DEFAULT_TOKEN,
                    help='the client token')
parser.add_argument('--sage', action='store_true',
                    help='change the recipient from "beaver" to "capybara"')

# Parse the arguments
args = parser.parse_args()

# Create the client
client = poe.Client(args.client)

# Set the recipient based on the --sage argument
recipient = 'capybara' if args.sage else 'beaver'

# Send the message
message = args.message
for chunk in client.send_message(recipient, message):
    print(chunk['text_new'], end='', flush=True)
