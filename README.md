# data_cleaning_agent

AI Agent that takes a raw dataset and recommends steps for cleaning the data based on User context provided to the Agent.

# Installation

I have used UV to manage the environment for this project.

To run your own version of this Agent you will need to install uv.

e.g. `bash brew install uv`

Once installed you can create a venv. Then use uv to install all the requirements in the pyproject.toml file.

`bash uv pip install -r pyproject.toml`

Once all requirements are installed create a new file called `.env` and add a variable called OPENAI_API_KEY and add in your own API key for the OpenAI models.

Once all these steps are completed you can run this command `bash python -m streamlit run ./app/app.py`
