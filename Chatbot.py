# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Uncomment the following lines to enable verbose logging
#import logging
#logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance	
chatbot = ChatBot(
    "Terminal",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="corpus-database"
    )
chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train("chatterbot.corpus.english")

chatbot.logger.info('Trained database generated successfully!')

print('Type something to begin...')

while True:
    try:
        bot_input = chatbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break