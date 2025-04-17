# import requests
# import os
# import pandas as pd
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from langchain_core.prompts import PromptTemplate
# from langchain_groq import ChatGroq

SHEET_ID = "1Tv6vTnF9xCh7gQQGwb-XSGzULnV_ejgv60KTa6G5Kps"
SHEET_RANGE = "Sheet1!A:B"  # Adjust this if your sheet has a different name or range

# def get_email(name):
#     print("name is ",name)
#     creds = service_account.Credentials.from_service_account_file(
#         "/Users/kaushalgadhiya/Projects/My_Email_Agent/utils/credentials.json",  # Make sure your service account JSON is placed in your project root
#         scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
#     )
#     service = build("sheets", "v4", credentials=creds)
#     sheet = service.spreadsheets()
#     result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
#     values = result.get("values", [])

#     if not values:
#         raise ValueError("No data found in the Google Sheet")

#     df = pd.DataFrame(values[1:], columns=values[0])  # First row as header
#     df.columns = df.columns.str.strip()
#     print(df)

#     if "Name" not in df.columns or "Email" not in df.columns:
#         raise KeyError("Make sure your sheet has 'Name' and 'Email' columns")

#     # email = df[df["Name"].str.lower() == name.lower()]["Email"].values
#     email = df[df["Name"].str.strip().str.lower() == name.strip().lower()]["Email"].values
    
#     if len(email):
#         return email[0]
#     else:
#         raise ValueError("Email not found for the name: " + name)

# def generate_email(command):
#     prompt = f"""Extract the recipient name, subject, and generate a professional email based on the following command:
    
#     \"\"\"{command}\"\"\"
   
#     Please Follow strictyl format.Don't generate unnecessary text.
#     Format:
#     Recipient: <name> 
#     Subject: <subject>
#     Body:
#     <email body>
#     """

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={"model": "llama3.2", "prompt": prompt, "stream": False}
#     )
    
#     content = response.json()['response'].strip()
#     # print("Content:-", content)
#     print()

#     lines = content.splitlines()
#     recipient_name = ""
#     subject = ""
#     body = ""

#     # Extract recipient name
#     for i, line in enumerate(lines):
#         if line.lower().startswith("recipient:"):
#             recipient_name = line.split(":", 1)[1].strip()
#             recipient_line_idx = i
#             break

#     # Extract email using contact_lookup
#     recipient_email = get_email(recipient_name)

#     # Extract subject
#     for i, line in enumerate(lines):
#         if line.lower().startswith("subject:"):
#             subject = line.split(":", 1)[1].strip()
#             subject_line_idx = i
#             break

#     # Body starts after subject line
#     body_start_index = subject_line_idx + 1
#     body = "\n".join(lines[body_start_index:]).strip()
#     # Clean the body text
#     # Remove duplicate "Subject:" line in body, if exists
#     if body.lower().startswith("subject:"):
#         body = "\n".join(lines[body_start_index + 1:]).strip()
    
#     # Remove "Body:" prefix if it exists
#     if body.lower().startswith("body:"):
#         body = body[5:].strip()
#     print("OK")    
#     # Replace [Your Name] with Bansil Khokhar if it exists
#     body = body.replace("[Your Name]", "Kaushal Gadhiya")
#     print("OK")

#     # s

#     return recipient_name, recipient_email, subject, body


# # command = "Schedule my meeting with prince tomorrow 5 p.m."
# # recipient_name, recipient_email, subject, body = generate_email(command)

# # print("recipient_name :- ",recipient_name)
# # print("recipient_email :- ",recipient_email)
# # print("subject :- ",subject)
# # print("body :- ",body)


# groq_api_key = "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"
# llm = ChatGroq(api_key=groq_api_key, model_name="gemma2-9b-it")

# prompt_template = PromptTemplate(
#     input_variables=["command"],
#     template="""
# You are a highly skilled AI email assistant tasked with drafting clear, polite, and situationally appropriate emails based on the following instruction:

# Instruction:
# \"\"\"{command}\"\"\"

# Your response must strictly follow this structure:
# Recipient: <recipient name or placeholder>
# Subject: <email subject>
# Body:
# <well-structured email body>

# ## OBJECTIVE
#     Write a complete, ready-to-send email that fully addresses the user's purpose while maintaining a professional and friendly tone.

# ## INSTRUCTIONS
#     1. Carefully extract key details, intentions, and emotional tone from the user's voice instruction.
#     2. Write a clear, concise, and relevant subject line that accurately reflects the email's purpose.
#     3. Start with an appropriate professional greeting, considering the sender's relationship with the recipient.
#     4. Structure the body of the email into logically ordered, well-organized paragraphs.
#     5. Make the email sound thoughtful, warm, and human — not robotic or overly formal.
#     6. Use polite and direct language that is easy to understand, avoiding jargon and fluff.
#     7. Ensure proper grammar, correct spelling, and clear sentence construction.
#     8. Close the email with a courteous and fitting sign-off.

# ## SPECIAL CONSIDERATIONS
#     - If the purpose includes meeting details, clearly mention the date, time, and location.
#     - If the email is a follow-up, acknowledge any prior conversation or email thread.
#     - If the message is urgent, communicate that politely and respectfully.
#     - If the email contains a request, be clear and specific about the desired action or response.
    
# Kaushal Gadhiya
# - Do not include placeholders like "[Your Name]" or extra explanations.

# Your output should only be the completed email in the specified format.
# """
# )

# chain = prompt_template | llm
# command = "I want to Schedule my meeting with prince tomorrow 5 p.m. about our heart deases project in conference room. I am project manager and prince is senior python developer."
# response = chain.invoke({"command": command})
# content = str(response.content).strip()
# print("Content:", content)



from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model_name="gemma2-9b-it")

prompt_template = PromptTemplate(
    input_variables=["command"],
    template="""
You are a highly skilled AI email assistant tasked with drafting clear, polite, and situationally appropriate emails based on the following instruction:

Instruction:
\"\"\"{command}\"\"\"

Your response must strictly follow this structure:
Recipient: <recipient name or placeholder>
Subject: <email subject>
Body:
<well-structured email body>

## OBJECTIVE
    Write a complete, ready-to-send email that fully addresses the user's purpose while maintaining a professional and friendly tone.

## INSTRUCTIONS
    1. Carefully extract key details, intentions, and emotional tone from the user's voice instruction.
    2. Write a clear, concise, and relevant subject line that accurately reflects the email's purpose.
    3. Start with an appropriate professional greeting, considering the sender's relationship with the recipient.
    4. Structure the body of the email into logically ordered, well-organized paragraphs.
    5. Make the email sound thoughtful, warm, and human — not robotic or overly formal.
    6. Use polite and direct language that is easy to understand, avoiding jargon and fluff.
    7. Ensure proper grammar, correct spelling, and clear sentence construction.
    8. Close the email with a courteous and fitting sign-off.

## SPECIAL CONSIDERATIONS
    - If the purpose includes meeting details, clearly mention the date, time, and location.
    - If the email is a follow-up, acknowledge any prior conversation or email thread.
    - If the message is urgent, communicate that politely and respectfully.
    - If the email contains a request, be clear and specific about the desired action or response.
    
Bansil Khokhar
- Do not include placeholders like "[Your Name]" or extra explanations.

Your output should only be the completed email in the specified format.
"""
)

chain = prompt_template | llm

def generate_email(command: str):
    try:
        response = chain.invoke({"command": command})
        content = str(response.content).strip()
        print("Content:", content)
        print()

        lines = content.splitlines()
        recipient_name = ""
        subject = ""
        body = ""

        # Extract recipient name
        for i, line in enumerate(lines):
            if line.lower().startswith("recipient:"):
                recipient_name = line.split(":", 1)[1].strip()
                recipient_line_idx = i
                break

        # Extract email address from the sheet
        recipient_email = get_email(recipient_name)

        # Extract subject
        for i, line in enumerate(lines):
            if line.lower().startswith("subject:"):
                subject = line.split(":", 1)[1].strip()
                subject_line_idx = i
                break

        # Extract body
        body_start_index = subject_line_idx + 1
        body = "\n".join(lines[body_start_index:]).strip()

        # Clean the body text
        # Remove "Body:" prefix if it exists
        if body.lower().startswith("body:"):
            body = body[5:].strip()
            
        # Replace [Your Name] with Bansil Khokhar if it exists
        body = body.replace("[Your Name]", "Bansil Khokhar")
        
        # print(f"\nRecipient Name: {recipient_name}")
        # print(f"Subject: {subject}")
        # print(f"Body:\n{body}")

        return recipient_name, recipient_email, subject, body

    except Exception as e:
        print(f"❌ Email generation failed: {str(e)}")
        return None, None, None, None

def get_email(name):
    print("name is ",name)
    creds = service_account.Credentials.from_service_account_file(
        "/Users/kaushalgadhiya/Projects/My_Email_Agent/utils/credentials.json",  # Make sure your service account JSON is placed in your project root
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"]
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
    values = result.get("values", [])

    if not values:
        raise ValueError("No data found in the Google Sheet")

    df = pd.DataFrame(values[1:], columns=values[0])  # First row as header
    df.columns = df.columns.str.strip()
    print(df)

    if "Name" not in df.columns or "Email" not in df.columns:
        raise KeyError("Make sure your sheet has 'Name' and 'Email' columns")

    # email = df[df["Name"].str.lower() == name.lower()]["Email"].values
    email = df[df["Name"].str.strip().str.lower() == name.strip().lower()]["Email"].values
    
    if len(email):
        return email[0]
    else:
        raise ValueError("Email not found for the name: " + name)

command = "I want to Schedule my meeting with prince tomorrow 5 p.m. about our heart deases project in conference room. I am project manager and prince is senior python developer."
recipient_name, recipient_email, subject, body = generate_email(command)
print("recipient_name :- ",recipient_name)
print("recipient_email :- ",recipient_email)
print("subject :- ",subject)
print("body :- ",body)