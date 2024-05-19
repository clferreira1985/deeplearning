from langchain_openai import OpenAI
from Key_OpenAI import API_KEY

# Configure the OpenAI API key
openai_api_key = API_KEY

def entrance():
    return input("How do you feel today? ")

def classify_feeling(text):
    if "wonderful" in text or "perfect" in text:
        return "Positive"
    elif "bad" in text or "terrible" in text:
        return "Negative"
    else:
        return "Neutral"

def feeling(prompt):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct", openai_api_key=openai_api_key)
    output = llm.predict(prompt)
    result = classify_feeling(output)
    return result

if __name__ == "__main__":
    prompt = entrance()
    result = feeling(prompt)
    print(f"Input: {prompt}")
    print(f"Feeling: {result}")
