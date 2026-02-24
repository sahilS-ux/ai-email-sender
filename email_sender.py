import os
from google import genai
import smtplib
from dotenv import load_dotenv
load_dotenv()

class EmailSender:
    def __init__(self):
        self.api_key = os.environ.get("API_KEY")
        self.password= os.environ.get("PASSWORD")
        self.client = genai.Client(api_key=self.api_key)

    def generate_email(self, topic, friends_name, my_name):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction="You are an expert email writer. You only output emails in proper format. No explanations, no bullet points, no templates. Just the subject line and email body only.",
            ),
            contents=f"Write a casual friendly email to my friend named {friends_name} about {topic}. Sign it with my name {my_name}."
        )
        return response.text

    def send_email(self, my_email, to_email, my_name, content):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(my_email, self.password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f"Subject: Email from {my_name}\n\n{content}"
            )
