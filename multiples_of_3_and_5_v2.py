def divisible_by_under(limit, divs):
    return (i for i in range(limit) if any(i % div == 0 for div in divs))


def run():
    print(sum(divisible_by_under(10, (3, 5))))
    print(sum(divisible_by_under(100, (3, 5))))
    print(sum(divisible_by_under(200, (3, 5))))
    print(sum(divisible_by_under(300, (3, 5))))
    print(sum(divisible_by_under(400, (3, 5))))
    print(sum(divisible_by_under(500, (3, 5))))
    print(sum(divisible_by_under(600, (3, 5))))
    print(sum(divisible_by_under(700, (3, 5))))
    print(sum(divisible_by_under(800, (3, 5))))
    print(sum(divisible_by_under(900, (3, 5))))
    print(sum(divisible_by_under(1000, (3, 5))))


if __name__ == '__main__':
    run()
