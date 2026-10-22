from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


# .env içindekileri dosyaya aktarma
load_dotenv()  

# Gemini modeli ile iletişim
model = ChatGoogleGenerativeAI(model="your_gemini_model")


messages = [
    SystemMessage(content="Translate the following from English to Spanish"),
    HumanMessage(content="Hello there, What's up with you?")
]


if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content[0]["text"])
