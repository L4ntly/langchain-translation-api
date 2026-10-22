from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="your_gemini_model")

messages = [
    SystemMessage(content="Translate the following from English to Spanish"),
    HumanMessage(content="Hello there, What's up with you?")
]


# model çıktısı -> str
parser = StrOutputParser()


chain = model | parser  # modelin çıktısı parser'a verilir

if __name__ == "__main__":
    print(chain.invoke(messages))
    
    