import csv
import asyncio
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Function to send email with attachments and a signature
async def send_email(email, subject):
    # Your email credentials
    email_sender = 'contato@revitalizeamb.com'
    email_password = 'Contato@123'
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email
    msg['Subject'] = subject

    # Read HTML content from file
    with open('template.html', 'r') as f:
        html_body = f.read()

    # Replace placeholders in HTML content if necessary
    #html_body = html_body.replace('{{name}}', name)
    html_body = html_body.replace('{{subject}}', subject)

    # Attach HTML content to the message
    msg.attach(MIMEText(html_body, 'html'))

    # Add signature image attachment
    #filename = 'signature.png'  # Modify this with your signature image file
    #with open(filename, 'rb') as fp:
    #    img_data = fp.read()
    #img_part = MIMEImage(img_data)
    #img_part.add_header('Content-Disposition', 'inline', filename=filename)
    #img_part.add_header('Content-ID', '<signature_image>')
    #msg.attach(img_part)

    # Establish connection to SMTP server
    try:
        server = smtplib.SMTP('send.one.com', 587)
        server.starttls()
        server.login(email_sender, email_password)
        text = msg.as_string()
        server.sendmail(email_sender, email, text)
        print(f"E-mail enviado para {email}")        
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")
        server.quit()

# Read CSV file and extract data
async def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        tasks = []
        for row in reader:
            #name = row['NOME']  # Change 'Name' to your column name for names
            email = row['EMAIL']  # Change 'Email' to your column name for emails
            subject = row['ASSUNTO'] # Change 'Subject' to your column name for emails
            tasks.append(send_email(email, subject))
        await asyncio.gather(*tasks)

# Main function to run the script
async def main():
    csv_filename = 'EnvioEmMassaEmail.csv'  # Provide your CSV file path
    await read_csv(csv_filename)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
