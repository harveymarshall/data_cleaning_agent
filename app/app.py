import streamlit as st
from utils.data_loader import load_uploaded_file
from utils.data_profiler import profile_data
from utils.langchain_runner import get_cleaning_chain

st.set_page_config(page_title="Data Cleaning Agent", layout="wide")

st.title("AI Data Cleaning Agent")
st.markdown("Upload a raw dataset and descrive the use case for the data - The Agent will suggest a plan to clean and prepare the data for your given use case.")

uploaded_file = st.file_uploader("Upload your dataset.", type=["csv", "xlsx", "xls", "parquet", "json"])
context = st.text_area("Describe your use case for how the dataset will be used. (e.g. This data will be passed to a classifier model)")

if uploaded_file and context:
    df = load_uploaded_file(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Dataset Profle Summary")
    summary = profile_data(df)
    st.text(summary)

    if st.button("Generate  Cleaning Suggestions"):
        with st.spinner("Generating Suggestions..."):
            chain = get_cleaning_chain()

            result = chain.invoke({"dataset_summary": summary, "context": context})

        st.subheader("Cleaning Plan and Suggested Cleaning Code")
        st.write(result["text"])
