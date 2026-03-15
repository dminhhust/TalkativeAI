from app.redis_client import *
from app.services.scenario_services import *
from app.services.llm_service import *
from app.utils.prompt_builder import *
from app.models.message_model import *


def process_message(user_id, session_id, message, scenario):

    system_prompt = get_scenario_prompt(scenario)

    history = get_memory(session_id)

    prompt = build_prompt(system_prompt, history, message)

    response = generate_response(prompt)

    store_memory(session_id, f"User: {message}")
    store_memory(session_id, f"Assistant: {response}")

    save_message(session_id, "user", message)
    save_message(session_id, "assistant", response)

    return response
