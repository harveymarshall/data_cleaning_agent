from ..services.langchain_runner import get_cleaning_chain
from ..services.profile_data import profile_data

def invoke_llm(file, role, context):
    summary = profile_data(file)
    chain = get_cleaning_chain()
    result = chain.invoke({"role": role, "dataset_summary": summary, "context": context})
    return {"Result": result["text"]}
