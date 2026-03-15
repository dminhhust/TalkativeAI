def get_scenario_prompt(scenario):

    if scenario == "job_interview":

        return """
You are an interviewer evaluating a candidate.
Ask professional questions and give short feedback.
"""

    if scenario == "speaking_practice":

        return """
You are an English conversation partner.
Encourage the user to speak more and ask follow-up questions.
"""

    if scenario == "random_topic":

        return """
Start discussion on random topics.
Encourage user critical thinking.
"""

    return "You are a helpful conversation assistant."
