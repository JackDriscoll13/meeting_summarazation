import openai

def get_responses(chunks, model):
    responses = [] 
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
    return responses


