import csv
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Function to send email
async def send_email(name, email):
    # Your email credentials
    email_sender = 'contato@revitalizeamb.com'
    email_password = 'Contato@123'

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email
    msg['Subject'] = 'Soluções Ambientais para Postos de Combustíveis: Protegendo o Meio Ambiente e seu Negócio'

    # Email body
    html_body = f"""\
      <html>
    <head>    
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://revitalizeamb.com/ArquivosDiversos/style.css">
        <script type="text/javascript" src="estudosLogica 2.js"></script>
    </head>
    
      <body>
        <div class = "div-body" style="padding: 1%; text-align: justify;font-family: Arial, Helvetica, sans-serif;">
            
            <div><img src="https://usercontent.one/wp/revitalizeamb.com/wp-content/uploads/2021/03/LOGO.png" 
                alt="RevitalizeAmbiental" 
                width="250">
            </div>
            <div><p><h1 style="text-align: center; margin: 5%;">Conheça nossos serviços</h1></p><br>
            </div>
                <p>A <b style="color: darkgreen;">Revitalize</b> <b>Consultoria Ambiental</b>. 
                Tem soluções sustentáveis e estratégias ambientais inteligentes para sua empresa. 
                Nosso objetivo é ajudar a <b>{name}</b> a alcançar a excelência ambiental, garantindo a conformidade regulatória e promovendo práticas de negócios 
                responsáveis.
                </p><br><br>

                <p><h2 style="text-align: center;">Nossos Serviços</h2></p><br>

                <p><b style="color: green;">Avaliação Ambiental</b>: Realizamos avaliações abrangentes para identificar e mitigar impactos ambientais em projetos de desenvolvimento;</p>
                <p><b style="color: green;">Gestão de Resíduos</b>: Desenvolvemos estratégias eficazes para reduzir, reutilizar e reciclar resíduos, minimizando o impacto ambiental e os custos operacionais;</p>
                <p><b style="color: green;">Licenciamento Ambiental</b>: Auxiliamos nossos clientes no processo de obtenção de licenças ambientais, garantindo conformidade com regulamentações locais juntamente com órgãos ambientais;</p>
                <p><b style="color: green;">Educação e Treinamento</b>: Oferecemos programas de treinamento personalizados para capacitar equipes a adotarem práticas sustentáveis e ambientalmente responsáveis;</p>
                <p><b style="color: green;">Consultoria Estratégica</b>: Prestamos consultoria estratégica para integrar a sustentabilidade aos negócios, identificando oportunidades de economia de recursos e aumento da eficiência operacional;</p>
                <p><b style="color: green;">Entre outros</b>: Podendo ser analisado caso a caso.</p>

                <p><h2 style="text-align: center;">Por que escolher a <a style="color: darkgreen;">Revitalize Ambiental</a></h2></p><br><br>
                <p><b style="color: darkgreen;">Experiência Comprovada</b>: Com mais de 7 anos de experiência, acumulamos um histórico comprovado de sucesso.</p>
                <p><b style="color: darkgreen;">Abordagem Personalizada</b>: Reconhecemos que cada cliente é único, .</p>
                <p><b style="color: darkgreen;">Inovação e Tecnologia</b>: Mantemo-nos atualizados com as últimas tendências e tecnologias ambientais.</p>
                <p><b style="color: darkgreen;">Resultados Tangíveis</b>: Nosso foco está em fornecer resultados mensuráveis.</p><br>


                <h3 style="text-align: center;">Juntos, podemos criar um futuro mais sustentável para as gerações presentes e futuras!</h3>
        </div>
                <div style="background-color: lightgray; padding: 1%;font-family: Arial, Helvetica, sans-serif; text-align: center;"> 
                    <div class="display: inline-block; text-align: center;">
                        <p><b>Para saber mais clique no botão!</b></p><br> 
                        <a href="https://api.whatsapp.com/send/?phone=5534998229616&text=Quero%20Saber%20Mais!&type=phone_number&app_absent=1" target="_blank">
                            
                            <img src="https://revitalizeamb.com/ArquivosDiversos/whatsapp_logo_icon_170905.png"  alt="whats" width="75px"></a>
                        </a>
                    </div>  
                    <h4 style="color: green;">Siga a Revitalize nas redes sociais</h4>
                        <p>Você vai se surpreender com os conteúdos originais sobre revitalização do nosso meio ambiente:</p>
                    <div style="display: inline-block;">
                        <a href="https://www.instagram.com/revitalizeambiental" target="_blank">
                            <img src="https://revitalizeamb.com/ArquivosDiversos/insta.png" alt="insta" width="60px"></a>
                    </div>
                    <div style="display: inline-block;">
                        <a href="https://linkedin.com/in/revitalizeambiental" target="_blank">
                            <img src="https://revitalizeamb.com/ArquivosDiversos/linkendin.png" alt="linkedin" width="60px"></a>                        
                    </div>
                        <p>Enviado por Revitalize</p>
                        <p>Av. Bahia, 1012 - 38406-000 - Uberlândia, MG, Brasil</p>
                        <a href=https://revitalizeamb.com target="_blank"><b>revitalizeamb.com</b></a>
                </div> 
 
      </body>
</html>
    """
    msg.attach(MIMEText(html_body, 'html'))

     # Add signature image attachment
    
    #filename = 'Assinatura - Revitalize.gif'  # Modify this with your signature image file
    #with open(filename, 'rb') as fp:
    #    img_data = fp.read()
    #img_part = MIMEImage(img_data)
    #img_part.add_header('Content-Disposition', 'inline', filename=filename)
    #img_part.add_header('Content-ID', '<signature_image>')
    #msg.attach(img_part)

    # Add attachment
    #filename = 'attachment.txt'  # Modify this with your attachment file
    #attachment = open(filename, 'rb')
    #part = MIMEBase('application', 'octet-stream')
    #part.set_payload((attachment).read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition', "attachment; filename= " + filename)
    #msg.attach(part)

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
            name = row['NOME']  # Change 'Name' to your column name for names
            email = row['EMAIL']  # Change 'Email' to your column name for emails
            tasks.append(send_email(name, email))
        await asyncio.gather(*tasks)

# Main function to run the script
async def main():
    csv_filename = 'EnvioEmMassaEmail.csv'  # Provide your CSV file path
    await read_csv(csv_filename)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())