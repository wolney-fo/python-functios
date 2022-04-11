import banknote_selector

def change_calculator(paid_amount, purchase_value):
    change_value = paid_amount - purchase_value
    
    if change_value <= 0.0:
        print('| Change: BRL0.00')
        return False
    else:
        print(f'| Change: BRL{change_value:.2f}\n')
        banknote_selector(change_value)
        return True
