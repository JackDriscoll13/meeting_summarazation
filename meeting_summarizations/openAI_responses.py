import openai
from spinner import Spinner
def get_responses(chunks, model):
    """
    Takes in a list of transcript chunks and loops through them, appending a list of responses 
    """
    responses = [] 
    print('Generating inital responses based on each chunk -> ', end ='')
    with Spinner():
        match model:    
            case 'text-davinci-003': 
                for transcriptChunk in chunks: 
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=f"Can you summarize the following transcript for me into detailed bullet points? I would like your response to be long and detailed:  \n {transcriptChunk}",
                        max_tokens=2000
                    )
                    responses.append(response)
            case 'gpt-3.5-turbo':
                for transcriptChunk in chunks: 
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": f"Can you summarize the following transcript for me into detailed bullet points?:  \n {transcriptChunk}"}],
                        n = 1
                    )
                    responses.append(response)  
    print('done.')         
    return responses


def get_final_response(text, model):
    """Gets one final response from model""" 
    print('Generating final response ->', end = '')
    with Spinner():
        match model: 
            case 'text-davinci-003': 
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Can you rewrite these notes into concise, non-redundant meeting notes/action items? Please write your response in bulleted format: \n {text}",
                    max_tokens=2000
                )
            case 'gpt-3.5-turbo':
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Can you rewrite these notes into concise, non-redundant meeting notes andaction items? Please write your detailed response in bulleted format:  \n {text}"}],
                    n = 1
                )
    print('Done')                 
    return response

def test_connection(): 
    print('Testing connection... davinci completion model..')
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Suggest three names for a platypus that is a superhero.",
    max_tokens=100
    )
    return response