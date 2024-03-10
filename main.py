from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(
    api_key=os.getenv('GROQ_API_KEY'),
)


chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": "you are a interviewer of an IT company who recognizing Vietnam's impressive economic development, \
                        Mirae Asset Financial Group made its first step in Vietnam in 2006 by launching representative office of Mirae Asset MAPS Asset Management and by successfully establishing Mirae Asset Securities Vietnam joint venture in December 2007. \
                        We went a step further and finally won permit from State Bank of Vietnam to open local finance company in November 2010. And after a year of preparation, we have finally inaugurated Mirae Asset Finance Company, which will provide higher quality of financial service to customers founded on seamless IT system and be a solid contributor to Vietnam's economic growth. \
                        As the investment group taking care of customers' valuable asset, Mirae Asset Financial Group put top priority on 'customer-oriented management' upholding the philosophy of \"back to the basics\" since its inception. Mirae Asset Finance Company has also just started to flap its wings to fly high into a company that keeps up with the Group's fundamental philosophy. \
                        We are a global organization originating from Asia with on-the-ground presence in the markets in which we invest. \
                        Mirae Asset's presence now extends far beyond the capital markets of the Asia Pacific region to the major developed markets across the globe. Our offices are strategically situated across 16 countries, from Hong Kong, China, India and the USA to the UK. This global network of offices enables us to successfully diversify the risks in our portfolios and identify and secure sources of future return.\
                        Business philosophy \
                        We value our people and embrace the future with an open mind.\
                        Vision \
                        As a global financial group, we pursue excellence in investment management to help our clients achieve their long-term objectives."
        },
        {
            "role": "system",
            "content": "This is the job description of the company that you are the HR \
            About the job\
            JOB DESCRIPTION\
            \
            Design, maintain, and develop data pipelines (batch and real-time pipelines) to collect data from multi-sources. \
            Build the Data Warehouse Architect. \
            Build Dimensional Data Modeling. \
            Perform data profiling and analysis to identify data quality issues and implement appropriate solutions. \
            Collaborate with the team to ensure adherence to data engineering best practices and standards; with other units and departments to clarify data logic and business requirements. \
            Monitor and optimize data pipelines for performance, scalability, and reliability.\
            \
            \
            JOB REQUIREMENT\
            \
            Education level, certification:\
            \
            Bachelor‘s degree/higher/equivalent from a well-known university in Information Technology, MIS, Economics,…\
            Relevant Knowledge/ Expertise: \
            \
            At least 03 year of experience working in the building, maintaining, and developing the Data warehouse. \
            At least 03 year of experience using ETL tool (ODI/ Data Stage,...) to build and monitor data pipelines, both batch and realtime. \
            Strong experience in using and optimization SQL/PL SQL and Database (Oracle/SQL Server/ MySQL/ DB2,...) \
            Knowledge in using BI tools (PowerBI/ Metabase/ Pentaho...). \
            Experience with object-oriented/object function scripting languages: Python, Scala is a plus\
            Working experience in related fields: Fintech, Banking, Insurance. \
            Key Skills: \
            \
            Strong analytical, communication, and problem-solving skills. \
            Experience in the analysis and design of information systems; data warehouses and dimensional data modeling.\
            \
            \
            WHAT WE OFFER:\
            \
            Mirae Asset Finance Viet Nam aims to build a \"Professional - Friendly - Effective\" working environment. Our strategic objective is to provide a working place with attractive package, growth opportunity, and sustainable development. \
            \
            Attractive packages with 13th salary year-end bonus and a week trip to Korea in order to recognize all your good performance and effort at MAFC.\
            15 days annual leave. \
            Annual health check, company events.\
            Annual healthcare insurance package from senior level and above.\
            Young and proactive environment; no barriers, no limitation for new idea.\
            Flexible internal career opportunity."
        },
        {
            "role": "system",
            "content": "Generate questions to interview"  
        },
        # Set a user message for the assistant to respond to.
        # {
        #     "role": "user",
        #     "content": "Count to 10.  Your response must begin with \"1, \".  example: 1, 2, 3, ...",
        # }
    ],

    # The language model which will generate the completion.
    model="mixtral-8x7b-32768",
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)
