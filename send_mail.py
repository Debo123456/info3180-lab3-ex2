import smtplib

def send_mail(from_name, from_addr, subject, msg):
    
    errors = False
    
    to_addr = 'danieldawson496@gmail.com'
    
    to_name = 'Daniel Dawson'
    
    message = """
    From: {} <{}>\r\n
    To: {} <{}>\r\n
    Subject: {}\r\n
    {}
    """
    message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
    # Credentials (if needed)
    username = ''
    password = ''
    
    # The actual mail send
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to_addr, message_to_send)
    except:
        errors = True
    server.quit() 
    
    if errors == True:
        return False
    else:
        return True