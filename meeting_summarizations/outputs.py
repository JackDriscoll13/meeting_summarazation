import time



def summarize_usage(responses, start_time): 
    total_tokens, completion_tokens, prompt_tokens = 0
    
    for i in responses: 
        total_tokens += int(i['choices']['0']['usage']['total_tokens'])
        prompt_tokens += int(i['choices']['0']['usage']['prompt_tokens'])  
        completion_tokens += int(i['choices']['0']['usage']['completion_tokens'])
    
    print('\n Usage Summary: \nThe script took {0:0.1f} seconds.'.format(time.time() - start_time))
    print(f'Total tokens: {total_tokens}, prompt tokens: {prompt_tokens}, completion tokens: {completion_tokens}')
    # TODO: Add ai model, length of transcript, total time of transcript. Also will probaly want to put into a dictionary to do math with

def print_output(final_response, responses, start_time): 
    print('Final Response: \n')
    print(final_response)
    summarize_usage(responses, start_time)