"""
Fetch and display the latest email from a Gmail Inbox using IMAP.

Requirements:
1. Enable 2-Step Verification on your Google account.
2. Generate a Gmail App Password.
3. Replace EMAIL_ADDRESS and APP_PASSWORD with your credentials.
"""

import imaplib
import email

# User credentials
EMAIL_ADDRESS = "Enter the email"
APP_PASSWORD = "Enter app Password"

# Connect to Gmail IMAP server securely
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to Gmail
mail.login(EMAIL_ADDRESS, APP_PASSWORD)

# Open Inbox
mail.select("inbox")

# Retrieve all email IDs from Inbox
status, data = mail.search(None, "ALL")

# Store email IDs as a list
mail_ids = data[0].split()

# Select the newest email
latest_email_id = mail_ids[-1]

# Download the complete email content
status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

# Get raw email data
raw_email = msg_data[0][1]

# Parse raw email into an EmailMessage object
message = email.message_from_bytes(raw_email)

# Print email details
print(f"Subject: {message['Subject']}")
print(f"From: {message['From']}")