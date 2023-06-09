# Third party imports
import openai

# python imports
import time

# Local imports
from clean_transcript import clean_transcript, clean_line
from openAIenv import setup_openai_env
from segregate_transcript import split_transcript
from helpers import get_model_selection, concatenate_final_prompt, clean_final_response
from openAI_responses import get_responses, get_final_response, test_connection
from outputs import print_output

def main(): 
    start_time = time.time()
    
    # Get path to transcript, and type of model we plan to use
    path_to_vtt = input('Please input the path to the vtt file: ')
    model = get_model_selection()
    # Set Up openai enviorment
    openai.api_key, openai.organization = setup_openai_env()

    #Read in transcript, split up transcript
    transcript = clean_transcript(path_to_vtt)
    chunks = split_transcript(transcript)

    # # Feed chunks one at a time into open ai get response, join all responses together
    responses1 = get_responses(chunks, model)
    final_notes = concatenate_final_prompt(responses1, model)

    # Get final response,
    final_response = get_final_response(final_notes, model)
    final_response_clean = clean_final_response(final_response, model)
    responses1.append(final_response)

    print_output(final_response_clean,responses1,start_time, model)


    # Output final response into styled html file
    
if __name__ == "__main__":

    main()