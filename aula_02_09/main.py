import argparse

from revision import (
    activity1,
    activity2,
    activity3,
    activity4,
    activity5,
    activity6,
    activity7,
    activity8,
    activity9,
    activity10,
    activity11,
    activity12,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--activity", type=int, required=True)

    args = parser.parse_args()
    activity = args.activity

    if activity == 1:
        activity1()

    elif activity == 2:
        activity2()

    elif activity == 3:
        activity3()

    elif activity == 4:
        activity4()

    elif activity == 5:
        activity5()

    elif activity == 6:
        activity6()

    elif activity == 7:
        activity7()

    elif activity == 8:
        activity8()

    elif activity == 9:
        activity9()

    elif activity == 10:
        activity10()

    elif activity == 11:
        activity11()

    elif activity == 12:
        activity12()


if __name__ == "__main__":
    main()
