def get_answer(quest, option1='Y', option2='N'):
    while True:
        try:
            answer = input(quest)
            assert answer == option1 or answer == option2
            if answer == option1:
                return True
            else:
                return False
        except AssertionError:
              print(f"'{answer}' is not a valid answer")
