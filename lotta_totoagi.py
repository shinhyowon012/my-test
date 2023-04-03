import random

ar = [random.sample(range(1,46),6)]
def areload(ar):
    
    ar = [random.sample(range(1,46),6)]    
    return ar
f = input("복권추첨기를 사용하시겠습니까? (y또는n)")
if f == 'y':
    print("오늘의 행운번호는? ")
    happy = [random.sample(range(1,46),6)]
    print(happy, end='\n')
    g = input("복권추첨기를 어떻게 사용하실 건가요 메크로라면 m 복권이라면 j를 눌러주세요 ")
    if(g == 'm'):
        i = 0
        while (1):
            print(i)
            print(ar)
            if(happy == ar):
                print("복권 당첨 시도 {}",i)
                break
            else:
                i = i + 1
                ar = areload(ar)
    elif (g == 'j'):
        print (ar)
        if (happy == ar):
            print("당첨 축하합니다.")
        else:
            print("당첨에 실패했지만 괜찮아요 여기는 가상이예요")

        

else:
    print("사용을 종료합니다.")
    

