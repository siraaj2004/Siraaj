import requests
from config import RESEND_API_KEY, RECIPIENT_EMAIL


def send_email(subject, html_content):
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "from": "onboarding@resend.dev",
            "to": [RECIPIENT_EMAIL],
            "subject": subject,
            "html": html_content
        }
    )

    print("Email Status:", response.status_code)
    print("Response:", response.text)

    return response.status_code
