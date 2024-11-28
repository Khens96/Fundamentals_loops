def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
    sum = 0
    for num in range(start, end + 1):
        sum += num
    return sum
    

def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """

    result = {
        'positive': [],
        'negative': [],
        'even': [],
        'odd': [],
    }

    for num in numbers:
        if num > 0:
            result['positive'].append(num)
        elif num < 0:
            result['negative'].append(num)
        if num % 2 == 0:
            result['even'].append(num)
        else:
            result['odd'].append(num)
    return result
    

def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    if n <= 0:
        return []
    

def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    triangle = []
    for n in range (rows):
        row = [1] * (n + 1)

        for k in range (1, n):
            row[k] = triangle[n - 1][k - 1] + triangle[n - 1][k]
    
        triangle.append(row)
    return triangle

def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    if n==1:
        print ("Move disk 1 from source",source,"to destination",target)
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print ("Move disk",n,"from source",source,"to destination",target)
    tower_of_hanoi(n-1, auxiliary, target, source)
        
n = 4
tower_of_hanoi(n,'A','B','C') 
            

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    return dna.find(sequence)
    dna = "ATGCGTACG"
    sequence = "GTA"
    index = find_dna_sequence(dna, sequence)
    print(index)


def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    return cleaned_string == cleaned_string[::-1]

def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    if len(input_string) <= 1:
        return [input_string]

    permutations = []
    for i in range(len(input_string)):
        remaining_string = input_string[:i] + input_string[i + 1:]

        for perm in generate_permutations(remaining_string):
            permutations.append(input_string[i] + perm)
    return permutations

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
    

def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.
    """

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    pass

if __name__ == "__main__":
    pass
