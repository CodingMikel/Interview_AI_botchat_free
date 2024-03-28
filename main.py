import streamlit as st
import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

def generate_questions(conversation, memory, groq_chat, job_description):
    job_description_summary = JOB_DESCRIPTION
    response = conversation.run(f"Consider the following job description summary:\n{job_description_summary}\nGenerate 1 interview questions for a Data Engineer position.")
    memory.save_context({'input': f"Consider the following job description summary:\n{job_description_summary}\nGenerate 1 interview questions for a Data Engineer position."}, {'output': response})
    st.write("HR Bot:", response)

def main():
    st.title("Groq Chat App")

    # Add customization options to the sidebar
    st.sidebar.title('Select an LLM')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama2-70b-4096']
    )
    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)

    memory = ConversationBufferWindowMemory(k=conversational_memory_length)

    groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name=model)

    conversation = ConversationChain(llm=groq_chat, memory=memory)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input': message[0]['human']}, {'output': message[0]['AI']})

    generate_questions(conversation, memory, groq_chat, JOB_DESCRIPTION)

    user_answer = st.text_area("Answer a question:")
    if user_answer:
        response = conversation(user_answer)
        message = [
            {"AI": response["response"], "human": user_answer},
            {
                "role": "system",
                "content": "You are continuing the interview conversation with the candidate.",
            },
        ]
        st.session_state.chat_history.append(message)
        st.write("Chatbot:", response["response"])

        # Check if it's the endpoint of the interview
        if should_end_interview(response):
            st.write("Interview endpoint reached. Thank you!")

def should_end_interview(response):
    end_phrases = ["Thank you for your time", "We have completed the interview", "This concludes the interview"]
    for phrase in end_phrases:
        if phrase.lower() in response["response"].lower():
            return True
    return False


JOB_DESCRIPTION = """
Job Description:\
- Design, maintain, and develop data pipelines (batch and real-time pipelines) to collect data from multi-sources. \
- Build the Data Warehouse Architect. \
- Build Dimensional Data Modeling. \
- Perform data profiling and analysis to identify data quality issues and implement appropriate solutions. \
- Collaborate with the team to ensure adherence to data engineering best practices and standards; with other units and departments to clarify data logic and business requirements. \
- Monitor and optimize data pipelines for performance, scalability, and reliability. \
\
Job Requirements:\
- Bachelor‘s degree/higher/equivalent from a well-known university in Information Technology, MIS, Economics,…\
- At least 3 years of experience working in the building, maintaining, and developing the Data warehouse.\
- At least 3 years of experience using ETL tool (ODI/ Data Stage,...) to build and monitor data pipelines, both batch and real-time.\
- Strong experience in using and optimization SQL/PL SQL and Database (Oracle/SQL Server/ MySQL/ DB2,...).\
- Knowledge in using BI tools (PowerBI/ Metabase/ Pentaho...).\
- Experience with object-oriented/object function scripting languages: Python, Scala is a plus.\
- Working experience in related fields: Fintech, Banking, Insurance.\
- Strong analytical, communication, and problem-solving skills.\
- Experience in the analysis and design of information systems; data warehouses and dimensional data modeling.",
"""

if __name__ == "__main__":
    main()