
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def main():
    x=sleep_in(False, False)
    print(x)
    x=sleep_in(True, False)
    print(x)
    x=sleep_in(False, True)
    print(x)
    x=sleep_in(True, True)
    print(x)

if __name__ == '__main__':
    main()







