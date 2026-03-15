def build_prompt(system_prompt, history, user_message):

    prompt = f"""
{system_prompt}

Conversation so far:
{history}

User: {user_message}

Assistant:
"""

    return prompt
