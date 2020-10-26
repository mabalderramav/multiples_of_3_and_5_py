def multiples_of_3_or_5_below(number):
    total_sum = 0
    for i in range(1, number):
        if (i % 3 == 0 or i % 5 == 0):
            total_sum = total_sum + i
    print(total_sum)


def run():
    multiples_of_3_or_5_below(10)
    multiples_of_3_or_5_below(100)
    multiples_of_3_or_5_below(200)
    multiples_of_3_or_5_below(300)
    multiples_of_3_or_5_below(400)
    multiples_of_3_or_5_below(500)
    multiples_of_3_or_5_below(600)
    multiples_of_3_or_5_below(700)
    multiples_of_3_or_5_below(800)
    multiples_of_3_or_5_below(900)
    multiples_of_3_or_5_below(1000)


if __name__ == '__main__':
    run()
