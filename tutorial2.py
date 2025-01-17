import argparse
def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help = "The price of the item")
    args = parser.parse_args()
    price = args.price

    # apply ON tax
    total = price * 1.13

    # print tax
    print(f"The total price is {total:.2f}")

if __name__ == '__main__':
    main()