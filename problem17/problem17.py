def letter_count(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif n == 30:
        return 'thirty'
    elif n == 40:
        return 'forty'
    elif n == 50:
        return 'fifty'
    elif n == 60:
        return 'sixty'
    elif n == 70:
        return 'seventy'
    elif n == 80:
        return 'eighty'
    elif n == 90:
        return 'ninety'
    elif n < 100:
        return letter_count(n - n % 10)+letter_count(n % 10)
    elif n % 100 == 0 and n < 1000:
        return letter_count(n // 100)+'hundred'
    elif n < 1000:
        return letter_count(n - n % 100)+'and'+letter_count(n % 100)
    elif n == 1000:
        return 'onethousand'
def main():
    sum = 0
    for i in range(1,1001):
        sum += len(letter_count(i))
        print(letter_count(i))
    print(sum)
if __name__ == '__main__':
    main()
