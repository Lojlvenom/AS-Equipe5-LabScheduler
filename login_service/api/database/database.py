from models.User import User

class Database():    
    def __init__(self):
        adm = User("adm","adm@email.com","adm123")
        self.user_list = [adm]

    def add_user(self,data):
        self.user_list.append(data)

    def listAll(self):
        return self.user_list
        
    #interface de busca
    def filter_user_by(self,filtro,pesquisa):
        
        if filtro == "name":
            if any(User for User in self.user_list if User.name == pesquisa):
                return User
            #else return error mensage
        
        if filtro == "email":
            if any(User for User in self.user_list if User.email == pesquisa):
                return User
            #else return error mensage
    
    def login(self, l_email,l_password):
        if any(User for User in self.user_list if User.email == l_email) and any(User for User in self.user_list if User.password == l_password):
            return True
        else: return False