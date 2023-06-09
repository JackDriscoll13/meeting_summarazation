import time



def summarize_usage(responses, start_time, model): 
    total_tokens, completion_tokens, prompt_tokens = 0, 0, 0
    
    for i in responses: 
        #if model == 'gpt-3.5-turbo':
        total_tokens += int(i['usage']['total_tokens'])
        prompt_tokens += int(i['usage']['prompt_tokens'])  
        completion_tokens += int(i['usage']['completion_tokens'])
        # elif model == 'text-davinci-003': 
        #     total_tokens += int(i['usage']['total_tokens'])
        #     prompt_tokens += int(i['usage']['prompt_tokens'])  
        #     completion_tokens += int(i['usage']['completion_tokens'])                   
    
    print('\nUsage Summary: \nThe script took {0:0.1f} seconds.'.format(time.time() - start_time))
    print(f'Total tokens: {total_tokens}, prompt tokens: {prompt_tokens}, completion tokens: {completion_tokens}')
    # TODO: Add ai model, length of transcript, total time of transcript. Also will probaly want to put into a dictionary to do math. Aso maybe calculate expected cost of the pull

def print_output(final_response, responses, start_time, model): 
    print('Final Response: \n')
    print(final_response)
    summarize_usage(responses, start_time, model)