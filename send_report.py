import yagmail
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Email report using credentials from .env
def send_email_report():
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    
    subject = "Automated Test Report"
    body = "Please find the attached test report."
    report_path = os.path.join(os.getcwd(), "reports", "report.html")

    try:
        # Initialize yagmail client with email and password from .env file
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        
        # Send email with report as attachment
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=body,
            attachments=report_path
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    send_email_report()
