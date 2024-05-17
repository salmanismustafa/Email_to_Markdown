import os
import imapclient
import email
from email.policy import default
import subprocess
from datetime import datetime

def fetch_emails(sender):
    email_user = os.getenv('EMAIL_USER')
    email_pass = os.getenv('EMAIL_PASS')
    
    print(f"Connecting to email server as {email_user}")
    try:
        server = imapclient.IMAPClient('imap.gmail.com', ssl=True)
        server.login(email_user, email_pass)
        print("Logged in to email server")

        server.select_folder('INBOX')
        print(f"Searching for emails from {sender}")

        # Search for emails from the specific sender
        search_criteria = ['FROM', sender]
        messages = server.search(search_criteria)
        print(f"Found {len(messages)} emails from {sender}")

        for uid, message_data in server.fetch(messages, 'RFC822').items():
            msg = email.message_from_bytes(message_data[b'RFC822'], policy=default)
            print(f"Fetched email with UID {uid}")
            yield msg

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            server.logout()
            print("Logged out from email server")
        except:
            print("Failed to logout from email server")

def email_to_markdown(msg):
    subject = msg['subject']
    from_ = msg['from']
    date = msg['date']
    
    print(f"Converting email to Markdown: {subject}")

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = msg.get_payload(decode=True).decode()

    markdown_content = f"# {subject}\n\n*From: {from_}*\n*Date: {date}*\n\n---\n\n{body}"
    return markdown_content

def save_markdown(markdown_content, filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        print(f"Saving Markdown content to {filename}")
        with open(filename, 'w') as f:
            f.write(markdown_content)
    except Exception as e:
        print(f"Failed to save Markdown file {filename}: {e}")

def git_commit_and_push():
    try:
        print("Committing and pushing changes to Git repository")
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Add new email content'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Changes pushed to Git repository")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

if __name__ == "__main__":
    email_sender = os.getenv('EMAIL_SENDER')
    
    if not email_sender:
        print("EMAIL_SENDER environment variable is not set.")
    else:
        print(f"Starting script to fetch emails from {email_sender}")

        for msg in fetch_emails(email_sender):
            try:
                markdown_content = email_to_markdown(msg)
                date_str = datetime.strptime(msg['date'], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
                sanitized_subject = msg['subject'].replace(" ", "_").replace("/", "_")
                filename = f"emails/{date_str}-{sanitized_subject}.md"
                save_markdown(markdown_content, filename)
                git_commit_and_push()
            except Exception as e:
                print(f"An error occurred while processing email: {e}")

        print("Script completed successfully")

