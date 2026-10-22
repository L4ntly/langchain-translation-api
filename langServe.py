from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes


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

chain = prompt_template | model | parser


# FastAPI app
app = FastAPI(
    title="Basic Translator App",
    version="1.0.0",
    description="Translation Chat Bot"
)


# Sunucuya bağlanma
add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    