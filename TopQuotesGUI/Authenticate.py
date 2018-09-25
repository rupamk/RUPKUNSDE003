from quotes import GoodRead


def Authenticate(email,password):
    obj = GoodRead()
    obj.set_base_url("https://www.goodreads.com/")
    obj.set_email(email)
    obj.set_password(password)
    obj.set_credential()

 if __name__ == '__main__':
     Authenticate()
