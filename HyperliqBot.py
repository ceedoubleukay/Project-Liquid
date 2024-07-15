''' Basic Buy and Sell BOT '''

# Importing necessary modules and functions
import keyfile as secrets  # Importing secrets from keyfile
from Functions import *  # Import all functions from Functions.py
from eth_account.signers.local import LocalAccount  # Import LocalAccount from eth_account
import eth_account  # Import eth_account module
import time  # Import time module for sleep functionality
import schedule  # Import schedule module for scheduling tasks

# Define constants
symbol = 'WIF'  # Symbol for the cryptocurrency (must be on hyperliquid)
order_size = 1  # Size of the order
leverage = 3  # Leverage for the order
max_positions = 1  # Maximum number of positions allowed

def bot():
    # Retrieve the secret key from the secrets file
    secret_key = secrets.metaKey
    # Create an account object using the secret key
    account = eth_account.Account.from_key(secret_key)

    # Get current positions and related information
    positions, in_position, position_size, position_symbol, entry_price, pnl_percentage, is_long, num_positions = getPositionandmaxPos(symbol, account, max_positions)
    print(f'These are my positions for {symbol}: {positions}')

    # Adjust leverage and position size based on the signal
    leverage, position_size = adjustleveragesizesignal(symbol, leverage, account)

    # Check if already in a position
    if in_position:
        print('In position, checking to sell')
        # Use killswitch to handle the position
        killswitch(symbol, account)
        return

    # Check for any open orders
    open_orders = Info(constants.TESTNET_API_URL, skip_ws=True).open_orders(account.address)
    if open_orders:
        print('Open order currently waiting to go through')
        return

    # Get the current ask and bid prices
    ask_price, bid_price, order_book_data = askBid(symbol)
    # Get the price of the 5th bid in the order book
    bid_price_5 = float(order_book_data[0][2]['px'])

    print(f'NOT in position, QUOTING a BUY @ {bid_price_5}')
    # Cancel all existing orders
    cancelAllOrders(account)
    print('Just cancelled ALL orders')

    # Place a limit buy order
    limitOrder(symbol, True, position_size, bid_price_5, False, account)
    print(f'Just placed an order for {position_size} at {bid_price_5}')

# Run the bot function
bot()
# Schedule the bot function to run every 5 seconds
schedule.every(5).seconds.do(bot)

# Keep the script running
while True:
    try:
        # Run any pending scheduled tasks
        schedule.run_pending()
        # Sleep for 10 seconds before checking again
        time.sleep(10)
    except Exception as e:
        # Print error message and sleep for 30 seconds if an exception occurs
        print('*** ERROR. SLEEPING FOR 30s')
        print(e)
        time.sleep(30)