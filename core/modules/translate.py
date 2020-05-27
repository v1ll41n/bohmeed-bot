#Python 3.7.6

from googletrans import Translator



class TranslateNames(object):
    def __init__(self):
        
        self.translator = Translator()
        
    def translate(self,dic):
        ArDic=dic.copy()
        for n in dic :
            trans=self.translator.translate(dic[n], dest='ar',src='ar')
            ArDic[n]=trans.text
        return ArDic
        

        

#test the functionality
"""    
def main():
        EnDic = {
   "4234":"Kareem Seliem",
   "4444":"Diaa Mohamed"
   }
        trans = TranslateNames()
        Ardic=trans.translate(EnDic)
        print(Ardic)




if __name__ == '__main__':
    main()
"""
