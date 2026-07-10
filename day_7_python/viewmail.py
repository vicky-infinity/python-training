import imaplib

# Establish a secure connection to Gmail's IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Gmail credentials
# Replace these placeholders with your actual email address and App Password
email_address = "Enter your email"
app_password = "Enter the app password"

# Log in to the Gmail account
mail.login(email_address, app_password)

# Select the Inbox folder
mail.select("inbox")

# Search for emails whose subject contains "GLASS BOTTLE"
# The search returns matching email IDs
status, messages = mail.search(None, 'SUBJECT "GLASS BOTTLE"')

# Display the list of matching email IDs
print("Matching Email IDs:", messages)

# Specify the email ID you want to fetch
# Replace this with an ID from the search results if needed
email_id = b'6670'

# Fetch the complete email content (RFC822 format)
status, msg_data = mail.fetch(email_id, "(RFC822)")

# Print the fetch operation status
# Expected output: "OK" if successful
print("Fetch Status:", status)