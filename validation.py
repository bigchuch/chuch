def account_number_validation(accountNumber):
    if accountNumber: 

        try:
            int(accountNumber)

            if len(str(accountNumber)) == 10:
                return True
            
        except ValueError:
            return False  
                
        except TypeError:
            return False


    return False  