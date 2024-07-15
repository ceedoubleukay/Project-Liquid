
# Project Liquid

A basic Hyperliquid bot that buys and sells at a desired market cap.

[ SKELETON ] - DOES NOT implement any indicators or algorithmic calculations, is used instead as a tool to assist with these algorithms.

[ WORKFLOW ] - Makes a BUY/LONG order, once the order has been placed it will SELL/SHORT the order with no time or price limits. ( These come with the algorithms )


## NOTES
- Functions.py file is a HIDDEN file that is not displayed in the project. It is essentially backpacking off of HyperLiquids-sdk functionality.
    - The reason for this is due to your current use-case. You may be using a different exchange and therefore the functions/functionality WILL NOT WORK
    - A good suggestion would be to use the ccxt library here 👉 https://docs.ccxt.com/#/ as it will cover most of your functionality needs.

## TODO

- Add/Implement indicator calculations for more refined algorithms.
- Reformat the bot to make it more readily efficient and interchangable, for example:
    - You have an algorithm in a seperate script that will call a 'BUY' or 'SELL' function with certain parameters. This will help/assist you in having to plug in your algorithm into the main script.