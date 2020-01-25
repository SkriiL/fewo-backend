def fancy_price(price):
    arr = price.split('.')
    if len(arr) == 1:
            return arr[0] + ",00"
    elif len(arr) == 2:
        if len(arr[1]) == 1:
            return arr[0] + "," + arr[1] + "0"
        elif len(arr[1]) == 2:
            return arr[0] + "," + arr[1]


print(fancy_price("123.11"))