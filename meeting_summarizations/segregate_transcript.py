
def split_transcript(clean_transcript):
    """
    This function takes in a clean transcript of any length
    divides into equally sized chunks (which can be fed into openAI API)
    returns those chunks in a list
    """ 
    print('Dividing transcript into chunks...', end= ' ')
    chunks = []
    splitter = (len(clean_transcript)//7500)+1
    chunklen = len(clean_transcript)//splitter+1 
    for i in range(1, splitter+1):
        index1 = (i-1) * chunklen
        index2 = i * chunklen
        #print(f'index1: {index1} index2: {index2}')
        chunks.append(clean_transcript[index1:index2])
    print(f'Done \n Total Chunks: {splitter}, \n Chunk Length: {chunklen} chars')
    return chunks