# BananHack

**BananHack** is a program designed to automate a martingale betting strategy on the Bananobet website to win Banano Coin.

## Disclaimer

This software is intended for use as a gambling aid. The martingale strategy is not 100% reliable. It is crucial to only gamble with funds you can afford to lose. Gambling can be addictive, and this tool does not guarantee profit. Use it at your own risk.

## Prerequisites

Before running BananHack, ensure you have the following installed on your system:

- Firefox Browser (Version 94.0.2 or higher)
- Python (Version 3.10 or higher)
- Python Modules: Selenium & Pynput

## Installation

Install the required Python libraries, using the requirements file, by running the following command:

`pip install -r requirements.txt`

## Usage

Follow these steps to run BananHack:

1. Navigate to the BananHack directory:

`cd path/to/Bananhack`

2. Execute the main script:

`python main.py`

3. Launch the web connection to the site by clicking the "open website" button.
4. Log in with your Bananobet account.
5. Click on the betting field (bet) on the site and press TAB.
6. Return to the Bananhack window.
7. Enter the desired number of rolls. This is the number of games to play before the script stops automatically. The default value is 10. This setting allows you to control how many betting rounds you want the script to execute.
8. Enter the maximum number of consecutive losses. This setting determines the stopping point for the script if a certain number of consecutive losses is reached. The default value is 15. If the script encounters this number of consecutive losses, it will stop to prevent further loss, acting as a safeguard.
9. Click on the yellow magic button!

**Important**: Do not touch the keyboard/mouse during the game session.