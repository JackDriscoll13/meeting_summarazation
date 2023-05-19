import os
from pathlib import Path
from dotenv import load_dotenv

import re

import openai
from dataclasses import dataclass

@dataclass
class regex_in:
    string: str

    def __eq__(self, other: str | re.Pattern):
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        # TODO extend for search and match variants
        return other.fullmatch(self.string) is not None

# Clean up the a line of text, return None if its a timestamp or blank line
def cleanLine(line):
    match regex_in(line):
        case r'\d+ .*':
            #If its a speaker/heading tag
            firstremoved = re.sub('\d+ "','',line)
            nameonly = re.sub('" .*',':',firstremoved)
            return nameonly
        case r'[0-9][0-9].*': 
            return None
        case r'[A-Za-z].*': 
            return line

        case '': 
            return None
with open('julyaTranscript.vtt') as f:
    myr = f.read()
lines = myr.splitlines()

output = []
previous_speaker = ''
for line in lines: 
    newline = cleanLine(line)
    if newline != None: 
        if newline[-1] == ':':
            current_speaker = newline
            if current_speaker != previous_speaker:
                #print(newline) 
                previous_speaker = current_speaker
                output.append(newline)
        else: 
            #print(newline) 
            output.append(newline)
final = '\n'.join(output)




load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
aikey = os.getenv('OPENAI_API_KEY')
maindir = Path(os.getcwd()).parent






os.environ['REQUESTS_CA_BUNDLE'] = 'C:/Users/P3159331/Downloads/CharterRootCert.crt'



openai.api_key = aikey


# # Make resuest (completion) 
# response = openai.Completion.create(
#   engine="text-davinci-003",
#   prompt=f"Can you summarize the following transcript for me into detailed bullet points? I would like your response to be long and detailed:  \n {final[0:7000]}",
#   max_tokens=2000
# )

# Make request (chat)


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Can you summarize the following transcript for me into detailed bullet points?:  \n {final[0:7000]}"}],
    n = 1
)

print(response)

