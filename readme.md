
This `README.md` file provides an overview of the application, installation instructions, usage guidelines, and script details. You can add more sections or modify existing ones based on your requirements


# Email to Markdown Converter

This application fetches emails from a specified sender, converts them to Markdown format, and publishes them on your personal website via Git.

## Features

- Fetches emails from a specified sender using IMAP.
- Converts email content to Markdown format.
- Saves the converted emails as Markdown files.
- Automatically commits and pushes the changes to your Git repository.

## Prerequisites

- Python 3.6+
- An email account (Gmail recommended)
- Git installed on your machine

## Installation

1. **Clone the Repository**

   git clone https://github.com/salmanismustafa/Email_to_Markdown.git
   cd your-repo

    Set Up Environment Variables

    Configure the following environment variables:

    For Unix-based systems (Linux, macOS), add these to your .bashrc, .bash_profile, or .zshrc:

 

export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-password"
export EMAIL_SENDER="specific-sender@example.com"

For Windows:

    Open the Start Search, type in "env", and select "Edit the system environment variables".
    In the System Properties window, click on the "Environment Variables" button.
    Click "New" to add a new user or system variable.
    Add EMAIL_USER as the variable name and your-email@gmail.com as the value.
    Add EMAIL_PASS as the variable name and your-password as the value.
    Add EMAIL_SENDER as the variable name and specific-sender@example.com as the value.

Install Required Packages

sh

    pip install imapclient
    pip install markdownify

Usage

    Run the Script

    sh

    python your_script_name.py

    Output
        The script will fetch emails from the specified sender, convert them to Markdown format, and save them in the emails directory.
        The new Markdown files will be committed and pushed to your Git repository.

Script Details
fetch_emails(sender)

Connects to the email server and fetches emails from the specified sender.
email_to_markdown(msg)

Converts the fetched email to Markdown format.
save_markdown(markdown_content, filename)

Saves the converted Markdown content to a file.
git_commit_and_push()

Commits and pushes the changes to the Git repository.
Example

Here’s what you might see in the terminal when you run the script:

sh

$ python your_script_name.py
Connecting to email server as your-email@gmail.com
Logged in to email server
Searching for emails from specific-sender@example.com
Found 2 emails from specific-sender@example.com
Fetched email with UID 123
Converting email to Markdown: Important Update
Saving Markdown content to emails/2024-05-17-Important_Update.md
Committing and pushing changes to Git repository
Changes pushed to Git repository
Fetched email with UID 124
Converting email to Markdown: Another Update
Saving Markdown content to emails/2024-05-17-Another_Update.md
Committing and pushing changes to Git repository
Changes pushed to Git repository
Logged out from email server
Script completed successfully

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    imapclient for making IMAP easy to use.
    markdownify for converting HTML to Markdown.
