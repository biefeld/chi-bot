# χ-bot 

χ-bot (pronounced chi-bot) is a text-to-speech (TTS) food ordering system written in python, with fuzzy string matching. This was initally a project completed during highschool, making use of the [pywin32](https://pypi.org/project/pywin32/) Windows API for TTS. To make it compatable with all OS, the TTS is now implemented using the [gTTS](https://pypi.org/project/gTTS/) and [playsound](https://pypi.org/project/playsound/) python libraries.

In future, realtime speech-to-text would be nice to implement, potentially using the [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) library.

## Requirements

χ-bot requires the following:
- [python](https://www.python.org/) 3.11+
- [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/) 0.18.0+, for fuzzy string matching
- [python-Levenshtein](https://pypi.org/project/python-Levenshtein/) 0.25.1+, to speed up fuzzywuzzy
- [gTTS](https://pypi.org/project/gTTS/) 2.5.1+, for generating TTS messages using the Google TTS API
- [playsound](https://pypi.org/project/playsound/) 1.3.0+, for outputting TTS messages.

Install the python libraries (assuming python & pip are installed) using:

```bash
pip install fuzzywuzzy gTTS playsound python-Levenshtein
```
An internet connection is also required to interact with the Google TTS API.

## How to Use

### Installation

To install χ-bot, clone this repo to your local machine.

```bash
git clone https://github.com/biefeld/chi-bot.git
```

### Running

To run χ-bot, execute the following commands:

```bash
#Navigate to chi-bot directory, if required
cd chi-bot

# Execute chi-bot
python3 chi-bot.py
```

Ensure your sound is turned up, otherwise there will be no TTS audio. Follow the prompts ouput by χ-bot to place orders, view the menu and view order history. When χ-bot is speaking, there will be a message in the terminal.

```
χ-bot is speaking...
```

Press `CTRL-C` at any time to exit the app.

## Config

The menu (courses, dishes) and order history are stored within the `db` directory. These files may be modified if you wish to add/edit/remove menu items or previous orders placed. Ensure that the `.json` format used by χ-bot is followed.

The TTS messages are stored within the hidden `.tts` directory, but will be erased after they are used.

Within `classes/TTS.py`, the `FLUSH_TERM` flag can be set to either true (default) or false. If the flag is true, the terminal will be cleared everytime χ-bot prompts the user. The flag can be set to false if the terminal should not be cleared.

Within `classes/TTS.py`, `classes/Menu.py` and `classes/Orders.py`, the `DIR` variable assists in locating the `.tts` and `db` directories. If these directories are moved/changes, this variable will have to be updated accordingly.
