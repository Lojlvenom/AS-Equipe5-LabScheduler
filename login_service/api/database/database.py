from api.models.User import User

class Database():    
    def __init__(self):
        
        self.user_list = []

    def add_user(self,data):
        self.user_list.append(data)
        
    #interface de busca
    def filter_user_by(self,filtro,pesquisa):
 
        if filtro == "name":
            for i in range(len(self.user_list)):
                if self.user_list[i].name == pesquisa:
                    return self.user_list[i]  
                    
        if filtro == "email":
            for i in range(len(self.user_list)):
                if self.user_list[i].email == pesquisa:
                    return self.user_list[i] 
    
    def login(self, l_email,l_password):
        
        for i in range(len(self.user_list)):
            
            if self.user_list[i].email == l_email and self.user_list[i].password == l_password:

                return self.user_list[i]
        
db = Database()