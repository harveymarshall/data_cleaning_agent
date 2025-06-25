# data_cleaning_agent

AI Agent that takes a raw dataset and recommends steps for cleaning the data based on User context provided to the Agent.

# Installation

I have Dockerised this project and now simply to run you need to add a `.env` file to project root and fill it with your OPENAI_API_KEY.

Then you can run `docker-compose up -d` I have provided a sample data file in the data directory and an example API call below to call the container.

`curl http://localhost:8000/health` this should return a 200 response or "OK" of the container is up and running.

To call the agent with a role, dataset and context I have an example request below, This is just to test the endpoint and in the future or in production request would be made to this agent either by other agents or a UI making requests to the Agent.
