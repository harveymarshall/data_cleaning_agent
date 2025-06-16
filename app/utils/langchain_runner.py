from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


from dotenv import load_dotenv
load_dotenv()

def get_cleaning_chain() -> LLMChain:
    """
    Create a LangChain for cleaning text using OpenAI's GPT model.
    """
    template = """
    You are a senior data engineer.

You have the following dataset profile:
{dataset_summary}

The user provided this context:
{context}
Suggest a data cleaning and preprocessing plan. Include:
- Columns to drop or keep
- Handling missing values
- Data type conversions
- Outlier handling
- Encoding steps
- Optional: pandas code for each step

Return your response with a step-by-step breakdown of how to clean the data with the optional cleaning code at the end.

"""

    prompt = PromptTemplate(
        input_variables=["dataset_summary", "context"],
        template=template
    )

    print(prompt)
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    return LLMChain(llm=model, prompt=prompt)


