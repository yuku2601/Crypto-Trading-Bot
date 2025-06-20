from bot import BasicBot
from config import API_KEY, API_SECRET

def main():
    bot = BasicBot(API_KEY, API_SECRET)
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None
    if order_type == 'LIMIT':
        price = input("Enter limit price: ")

    result = bot.place_order(symbol, side, order_type, quantity, price)
    if result:
        print("Order Success:", result)
    else:
        print("Order Failed")

if __name__ == "__main__":
    main()