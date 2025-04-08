
def validate_password(password:str):
    x=0
    y=0

    if len(password) >= 20:

        for i in password:
            if i.isupper() == True:
                x += 1

            elif i>=3:
                y += 1
                if i.isalnum() == True:
                        y += 1
                        if y>=4:
                   
                        
   

                            validate_password("pisellodurimo")
            
