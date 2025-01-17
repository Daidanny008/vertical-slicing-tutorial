import argparse
def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("count", type=float, help = "The number of the items")
    parser.add_argument("price", type=float, help = "The price of the item")
    parser.add_argument(
        "--province", 
        type=str, 
        default = "Ontario", 
        choices=["Ontario", "Quebec"], 
        help = "The province where the tax is applied (default ON)"
        )
    args = parser.parse_args()
    count = args.count
    price = args.price

    if args.province == "Ontario":
        tax_rate = 1.13
    elif args.province == "Quebec":
        tax_rate = 1.14975

    # apply ON tax
    total = count * price * tax_rate

    # print tax
    print(f"The total price in {args.province} is {total:.2f}")

if __name__ == '__main__':
    main()