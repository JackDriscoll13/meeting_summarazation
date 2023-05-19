# Third party imports
import openai

# Local imports
from clean_transcript import clean_transcript, clean_line
from openAIenv import setup_openai_env
from segregate_transcript import split_transcript
from select_openAI_model import get_model_selection
from openAI_responses import get_responses

def main(): 
    # Get path to transcript, and type of model we plan to use
    path_to_vtt = input('Please input the path to the vtt file: ')
    model = get_model_selection()
    # Set Up openai enviorment
    openai.api_key, openai.organization = setup_openai_env()
    #Read in transcript, split up transcript
    transcript = clean_transcript(path_to_vtt)
    chunks = split_transcript(transcript)
    for chunk in chunks: 
        print('----------------------------')
        print(chunk)
        print('----------------------------')
    # # Feed chunks one at a time into open ai get response
    #responses1 = get_responses(chunks, model)
    #print(responses1)
    return chunks
if __name__ == "__main__":
    main()