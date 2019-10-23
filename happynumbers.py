
def get_happiness_state(num):
    res = num

    while (res > 1):
        digits = [int(d) for d in str(res)]
        count = 0

        for i in digits:
            if count == 0: 
                res = i**2
                count += 1
                continue
            res = res + (i**2)
            count += 1
        print(res)
    return 1
    return True if (res == 1) else False