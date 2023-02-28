import smtplib as s 
ob=s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login("prabhunathkudile@gmail.com","password required")
subject="sending email using python"
body="sab moh maya hai.Tum aaye the khali hath jayoge khali hath."
message="Subject:{}\n\n{}".format(subject,body)
listOfAddress=["prabhunathkudile@gmail.com","zopatesagar@gmail.com"]
ob.sendmail("prabhunathkudile@gmail.com",listOfAddress,message)
ob.quit()
