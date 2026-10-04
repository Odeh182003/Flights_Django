from .agent import run_ai_agent

def process_ai_query_task(user_query):
    # This executes asynchronously in the background qcluster process
    return run_ai_agent(user_query)