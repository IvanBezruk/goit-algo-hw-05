def generator_numbers(text):
    
    #Split text to separate word
    words = text.split()

    for word in words:
        #Remove all punctiations
        clean_word = word.rstrip(".,!?;:")

        #Check it is a valid number
        if clean_word.replace(".","").isdigit():
            yield float(clean_word)

def sum_profit(text, func):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")