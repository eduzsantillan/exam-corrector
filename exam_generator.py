from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew
import os

os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model="mistral",
    base_url="http://localhost:11434" 
)

topics = """JDBC, MVC pattern,JSP, Servlets, Hibernate, JPA, J2EE, Testing"""
criteria = """Each question will be 5 points, consider the following : 
              clear and concise, covers the desired topic, has a practical and theoretical question"""


# Define the agent
java_instructor_1 = Agent(
    role="Java Instructor",
    goal="""Create questions for a java course""",
    backstory="""You are a skilled Java instructor with experience in generating exam questions. 
    You have strong knowledge of Java programming language and have taught Java courses in the past""",
    # verbose=True,
    llm=llm,
    allow_delegation=False,
    # tools=[tool]
)

java_instructor_2 = Agent(
    role="Java Instructor",
    goal="""validate questions for a java course""",
    backstory="""You are a skilled Java instructor with experience in generating exam questions. 
    You have strong knowledge of Java programming language and have taught Java courses in the past""",
    # verbose=True,
    allow_delegation=False,
    llm=llm,
    # tools=[tool]
)


spanish_translator = Agent(
    role="Spanish Translator",
    goal="""Translate the text provided from English to Spanish""",
    backstory="""You are a skilled Spanish translator with experience in translating text from English to Spanish""",
    # verbose=True,
    llm=llm,
    allow_delegation=False,
    # tools=[tool]
)

generate_exam = Task(
    description="""Generate exam with 4 questions where 2 questions should be practical and the other 2 practical with theory
        for a java course related to the followup topics:""" + topics,
    agent=java_instructor_1,
    expected_output="4 questions for a java exam ",
)

validate_exam = Task(
    description="""Validate the 4 questions match the criteria : """ + criteria +""" and all topics all covers among the 4 questions
    .Also, correct any if needed""",
    agent=java_instructor_2,
    expected_output="final 4 questions validated for a java exam ",
)

translate_exam = Task(
    description="""translate the exam it to spanish.""",
    agent=spanish_translator,
    expected_output="4 questions for a java exam translated into spanish""",
)

validate_exam.context = [generate_exam]
translate_exam.context = [validate_exam]


crew = Crew(
    agents=[java_instructor_1,java_instructor_2,spanish_translator],
    tasks=[generate_exam,validate_exam,translate_exam],
)

try:
    result = crew.kickoff()
    print("Final result: " + result)
except ValueError as e:
    print(f"Error during task execution: {e}")
