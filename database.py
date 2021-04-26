# create record
# read record
# update record
# delete record
# crud
import os
import validation


file_path = 'C:/Users/MBA FOREX LEKKI/Desktop/Zuri Team/chuch/data/user_record/'

#filename = file_path

def create(account_number, first_name,last_name,email,password):


    user_data = first_name + "," + last_name + "," + email  + "," + password  + "," + str(0)

    if does_acount_number_exist(account_number):

        return False

    if does_email_exist(email):

        print("email already exists")

        return False
    
    complete_state = False

    try:
        
        f = open(file_path + str(account_number) + ".txt", "x")
  
    except FileExistsError:

        does_file_contain_data = read(file_path + str(account_number) + ".txt")

        if not does_file_contain_data:
            delete(account_number)

        

    else:

        f.write(str(user_data))
        complete_state = True
    
    finally:
        f.close()
        return complete_state
        





        
def read(user_account_number):
    is_user_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_user_account_number:
            f = open(file_path + str(user_account_number) + ".txt", "r")
        
        else:
            f = open(file_path + (user_account_number) ,"r")

    except FileNotFoundError:
        print("user does not exist")

    except FileExistsError:
        print("user details not found")

    except TypeError:
        print("invalid account number format")
    
    else:
        return f.readline()

    return False



def does_email_exist(email):

    all_users = os.listdir(file_path)
    
    for user in all_users:
        user_list = str.split(read(user), ',')
        
        if email in user_list:
            return True
    return False




def does_acount_number_exist(account_number):

    all_users = os.listdir(file_path)

    for user in all_users: 

        if user == str(account_number) + ".txt":
            return True

    return False 


# print(does_acount_number_exist(6193135869))      
    

def delete(user_account_number):

    is_delete_succesful = False

    if os.path.exists(file_path + str(user_account_number) + ".txt"):

        try:

            os.remove(file_path + str(user_account_number) + ".txt")
            is_delete_succesful = True

        except FileNotFoundError:
            print("user does not exist")

        finally:
            return is_delete_succesful





  

#create(6788156616,["chuch", "white", "chuch@gmail.com", "pass", 200])



















