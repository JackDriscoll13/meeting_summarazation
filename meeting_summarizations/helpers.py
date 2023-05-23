
def get_model_selection(): 
    model_to_use = input('What model would you like to use? \nEnter "1" for text-davinci-003 completion model OR \nEnter "2" for gpt-3.5-turbo chat model\n')
    match str(model_to_use): 
        case '1': 
            print('proceeding with text-davinci-003 completion model')
            return 'text-davinci-003'
        case '2': 
            print('proceeding with gpt-3.5-turbo chat model')
            return 'gpt-3.5-turbo'
        case _: 
            raise AttributeError('Invalid Input')

def concatenate_final_prompt(responses, model):
    if model == 'gpt-3.5-turbo':
        text_only = [response['choices'][0]['message']['content'] for response in responses]
    elif model == 'text-davinci-003':
        text_only = [response['choices'][0]['text'] for response in responses]
    return '\n'.join(text_only)

def clean_final_response(final_response, model): 
    if model == 'gpt-3.5-turbo':
        final_response_clean = final_response['choices'][0]['message']['content']
    elif model == 'text-davinci-003':
        final_response_clean = final_response['choices'][0]['text']
    return final_response_clean