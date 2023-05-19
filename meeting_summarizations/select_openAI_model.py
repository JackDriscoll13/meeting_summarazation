
def get_model_selection(): 
    model_to_use = input('What model would you like to use? \nEnter "1" for text-davinci-003 completion model OR \nEnter "2" for gpt-3.5-turbo chat model')
    match str(model_to_use): 
        case '1': 
            print('proceeding with text-davinci-003 completion model')
            return 'text-davinci-003'
        case '2': 
            print('proceeding with gpt-3.5-turbo chat model')
            return 'gpt-3.5-turbo'
        case _: 
            raise AttributeError('Invalid Input')