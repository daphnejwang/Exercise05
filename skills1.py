# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list=[]
    for num in some_list:
        if num % 2 != 0:
            odd_list.extend([num])
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list=[]
    for num in some_list:
        if num % 2 == 0:
            even_list.extend([num])
    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    length_greater_four = []
    for words in word_list:
        if len(words) >= 4:
            length_greater_four.extend([words])
    return length_greater_four

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    # i=0
    smallest_num = some_list[0]
    for num in some_list:
        if smallest_num > num:
            smallest_num = num
        # i += 1
    return smallest_num

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest_num = some_list[0]
    for num in some_list:
        if largest_num < num:
            largest_num = num
    return largest_num

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    half_val_list = []
    for num in some_list:
        half_num = float(num)/2
        half_val_list.extend([half_num])
    return half_val_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    word_len_list = []
    for words in word_list:
        len_word = len(words)
        word_len_list.extend([len_word])
    return word_len_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    count = 0
    for num in numbers:
        count += num
    return count

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    count = 1
    for num in numbers:
        count *= num
    return count

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    join_strings = ""
    for words in string_list:
        join_strings += words
    return join_strings

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    count = 0
    for num in numbers:
        count += num
        avg_int = count/len(numbers)
    return avg_int

some_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_list = ['Pooh', 'Tigger', 'Piglet', 'Owl']
numbers = [4, 18, 8, 5]
string_list = ['Tare', 'Panda', 'Hello', 'Kitty']

def main():
    print all_odd(some_list)
    print all_even(some_list)
    print long_words(word_list)
    print smallest(some_list)
    print largest(some_list)
    print halvesies(some_list)
    print word_lengths(word_list)
    print sum_numbers(numbers)
    print mult_numbers(numbers)
    print join_strings(string_list)
    print average(numbers)

if __name__ == "__main__":
    main()