import random
import string


def input_word():
    return input("Input any word: ")


def compare_words():
    print("Input nothing for exit!")
    word = input_word()
    lst = [word]
    while len(word) != 0:
        lst.append(word)
        word = input_word()
    new_lst = []
    print('Here is the result!')
    for el in lst:
        if el not in new_lst:
            new_lst.append(el)
            print(el)


def lst_of_num_divisors(num: int):
    return [i for i in range(1, num // 2 + 1) if num % i == 0]


def is_perfect_number(num):
    """This function gets one parameter

    :param num:
    :return: is it perfect number or not
    """

    return sum([i for i in range(1, num) if num % i == 0]) == num


def zip(data1, data2):
    new_lst = []
    if len(data1) != len(data2):
        return "Lengths of data1 and data2 have to be the same!"
    for i in range(len(data1)):
        new_lst.append([data1[i], data2[i]])
    return new_lst


def is_palindrome():
    """this function asks the user the sentence and returns that sentence is palindrome or not
    """

    sentence = input("Input sentence: ").lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))
    lst_sentence = sentence.split(" ")
    for i in range(len(lst_sentence) // 2):
        if lst_sentence[i] != lst_sentence[-(i + 1)]:
            return False
    return True


def compare_numbers():
    average = 0
    num = input("Input number: ")
    sum, quan = 0, 0
    lst = []
    while num != "":
        sum += int(num)
        quan += 1
        lst.append(int(num))
        num = input("Input number: ")
    if quan > 0:
        average = sum / quan
    else:
        print("You input nothing")
    print(f"the arithmetic mean of the numbers you enter is {average}")
    print("Big then average number")
    print([el for el in lst if el > average])
    print("small then average number")
    print([el for el in lst if el < average])
    print("elements equal in average")
    print([el for el in lst if el == average])


def bingo_ticket():
    numbers = [i for i in range(1, 50)]
    ticket = []
    for i in range(6):
        num = random.choice(numbers)
        ticket.append(num)
        numbers.remove(num)
    ticket.sort()
    return ticket


def is_sorted(data):
    data1 = data.copy()
    data1.sort()
    for i in range(len(data)):
        if data[i] != data1[i]:
            return False
    return True


def is_user_input_sorted():
    lst = []
    number = input("Input number: ")
    while number != "":
        lst.append(int(number))
        number = input("Input number: ")
    if is_sorted(lst):
        print("The sequence of numbers entered is sorted")
    else:
        print("The sequence of numbers entered is not sorted")


def is_sublist(larger, smaller):
    if len(smaller) > len(larger):
        return False
    elif len(smaller) == 0:
        return True
    else:
        for el in smaller:
            if el not in larger:
                return False
    for i in range(len(larger)):
        if larger[i] == smaller[0]:
            j = 0
            while j < len(smaller):
                if larger[i + j] != smaller[j]:
                    return False
                else:
                    j += 1
            return True
