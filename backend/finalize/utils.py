
class HandleError:
    def send_mail(traceback,e,fname,exc_type,exc_obj,exc_tb):
        from smtplib import SMTP,SMTPAuthenticationError,SMTPException
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        host = "smtp.gmail.com"
        port = 587
        username = "soubhagyakumar666@gmail.com"
        password = "SOubh@gy@519"
        from_email= username
        to_list=["soubhagyakumar666@gmail.com"]

        try:
            email_conn = SMTP(host, port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(username,password)

            the_msg = MIMEMultipart("alternative")
            the_msg['subject'] ="carrier-circle: Exceptions !"
            the_msg["from"]=from_email

            plain_txt = "testing the message"

            html_text = """\
                <!DOCTYPE html>
                <html lang="en">
                <body>


                <pre style="background:#e6e3e3;padding:5px;color:red;font-weight:bold;font-family:monospace;border-radius:5px;">
                <span style="color:white;background:black;padding:2px;">Traceback</span> {}
                <span style="color:white;background:black;padding:2px;">Error</span>  {}
                <span style="color:white;background:black;padding:2px;">File Name</span> {}
                <span style="color:white;background:black;padding:2px;">Type</span> {}
                <span style="color:white;background:black;padding:2px;">Exc_obj</span> {}
                <span style="color:white;background:black;padding:2px;">Line No.</span> {}
                </pre>


                </body>
                </html>

            """.format(traceback,e,fname,exc_type,exc_obj,exc_tb)

            part_1 = MIMEText(plain_txt,'plain')
            part_2 = MIMEText(html_text,"html")
            the_msg.attach(part_1)
            the_msg.attach(part_2)
            email_conn.sendmail(from_email,to_list,the_msg.as_string())
            email_conn.quit()
        except SMTPException:
            print("some thing went wrong")

    def make_error(traceback,e,fname,exc_type,exc_obj,exc_tb):
        HandleError.send_mail(traceback,e,fname,exc_type,exc_obj,exc_tb)
        return {
                "code":402,
                "error":e,
                "type":exc_type,
                "line":exc_tb,
                "fname":fname,
                "traceback":traceback
                }
