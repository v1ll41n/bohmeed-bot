import browser_cookie3
from fbchat import Client
from fbchat.models import *

class SendMessage(object):

   
    def __init__(self):
        
        self.cj = browser_cookie3.chrome()
    def Send(self,user,message):
        
        client = Client('<email>', '<password>', session_cookies=self.cj)

        users = client.searchForUsers(user)
        for u in users:
            print("User's ID: {}".format(u.uid))
            print("User's name: {}".format(u.name))
        #client.send(Message(text=message), thread_id=users[0].uid, thread_type=ThreadType.USER)


def main():

        sendmessage = SendMessage()
        sendmessage.Send('Kareem.Se1im','hello')




if __name__ == '__main__':
    main()
