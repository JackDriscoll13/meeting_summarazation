
import re
from dataclasses import dataclass

def clean_transcript(vttFileName) -> str: 
    """
    This function takes a vtt file and cleans it,
    returning a final version of the transcript that doesn't have time blocks and signifantly reduces wasted space/characters.
    """
    with open(vttFileName) as f:
        myr = f.read()
    lines = myr.splitlines()

    output = []
    previous_speaker = ''
    for line in lines: 
        newline = clean_line(line)
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
    return final

# This data class is neccesary for using regex in combination with match
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
def clean_line(line):
    """
    This function uses regex to classify and clean each line of the vtt transcript
    """
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