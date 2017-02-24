#!"C:\Python35\python.exe"

#第0001题，**作为Apple store app 独立开发者，你要搞限时促销， 为你的应用生成激活码（或者优惠券）， 使用Python生成200个激活码（或优惠券）
import random, string

forSelect = string.ascii_letters + "0123456789"

def generate(count, length):
    #count=200
    #length=20

    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
    
if __name__ =="__main__":
    generate(200, 20)


