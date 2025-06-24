from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

def get_cleaning_chain() -> LLMChain:
    """
    Create a LangChain for cleaning text using OpenAI's GPT model.

    Args:
        variables: A list of variables to be used with the PromptTemplate

    Returns:
        LLMChain: A LLMChain instance loaded with a model and the formatted prompt
    """
    with open("../prompts/prompt.txt", "r") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["role", "dataset_summary", "context"],
        template=template
    )

    print(prompt)
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    return LLMChain(llm=model, prompt=prompt)


