import openai
import meeting_summarizations

chunks = meeting_summarizations.main()
responses = []
for i in chunks:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Can you summarize the following transcript for me into detailed bullet points?:  \n {i}"}],
    n = 1
    )
    responses.append(response)

for i in responses: 
    print(i)