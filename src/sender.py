import resend
from config import RESEND_API_KEY, RECIPIENT_EMAIL

# Configure Resend
resend.api_key = RESEND_API_KEY


def send_email(subject: str, body: str):
    """
    Send an email using Resend.
    """

    if not RESEND_API_KEY:
        raise ValueError("RESEND_API_KEY is missing.")

    if not RECIPIENT_EMAIL:
        raise ValueError("RECIPIENT_EMAIL is missing.")

    try:
        response = resend.Emails.send({
            "from": "YouTube Trends <onboarding@resend.dev>",
            "to": [RECIPIENT_EMAIL],
            "subject": subject,
            "html": f"""
            <html>
                <body>
                    <h2>YouTube Trending Videos</h2>
                    <pre style="font-family:Arial, sans-serif; white-space:pre-wrap;">
{body}
                    </pre>
                </body>
            </html>
            """
        })

        print("✅ Email sent successfully!")
        print("📨 Resend Response:")
        print(response)

        return response

    except Exception as e:
        print("❌ Email sending failed!")
        print(e)
        raise
