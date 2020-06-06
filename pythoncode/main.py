have_girl = False

def send():
    print("发女朋友啦！")
    global have_girl
    have_girl = True
    print(f"have_girl = {have_girl}")

def show():
    if have_girl == True:
        print("脱单侠")
    else:
        print("单身狗")

if __name__=='__main__':
    send()
    show()