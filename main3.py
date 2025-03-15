import smtplib

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = ""
SENDER_PASSWORD = "" 
RECEIVER_EMAIL = ""
SUBJECT = "Test Email"
BODY = "Hello, this is a test email sent from Python!"

# Create email message
message = f"Subject: {SUBJECT}\n\n{BODY}"

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Secure connection
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print(" Error:", e)
