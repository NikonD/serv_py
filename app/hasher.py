import argon2

# a = argon2.PasswordHasher()
# pas = "jojo1234"
# log = "admin"
# h_str = a.hash(pas + log)
# print('hashed')

# bool_ = a.verify(h_str , pas+log)
# print(bool_)
arg=argon2.PasswordHasher()

class PasswordManager(arg):

    def HashPass(self , str_pass_and_salt):
        print('password has been hashed')
        return arg.hash(str_pass_and_salt)
    
    def VerifyPass(self , str_hash ,  str_pass):
        return arg.verify(str_hash , str_pass)
