from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="your_gemini_model")


system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser  # LCEL (LangChain Expression Language)

if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "Hello World"}))
    
    