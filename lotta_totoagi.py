import random#함수 랜덤을 뽑아주는 함수를 가져왔다
ar = [random.sample(range(1,46),6)]#일단 미리 사용자의 로또번호를 1~45까지 뽑는 수를 6번 반복함으로써 로또 번호를 추첨했다.
def areload(ar):#함수를 설정해주었다(이 함수는 위 코드를 반복함으로써 복권 코드를 바꿔주는 역할을 한다)
    
    ar = [random.sample(range(1,46),6)]    
    return ar
f = input("복권추첨기를 사용하시겠습니까? (y또는n)")#사용자의 입력을 받는다
if f == 'y':#그 입력으로 조건문을 거쳐서 갈래가 두가지로 나뉜다
    print("오늘의 행운번호는? ")#첫번째 사용한다고 하면 행운번호을 추첨한다,
    happy = [random.sample(range(1,46),6)]
    print(happy, end='\n')
    g = input("복권추첨기를 어떻게 사용하실 건가요 메크로라면 m 복권이라면 j를 눌러주세요 ")#그 번호를 매크로 사용할건지 일반 복권 사용인지 묻는다
    if(g == 'm'):#만약 메크로 모드라면 복권이 당첨될 때까지 사용자의 복권 번호를 돌리면서 맞을 때 까지한다!
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
    elif (g == 'j'):#만약 복권이라면 한번 하고는 끝이난다
        print (ar)
        if (happy == ar):
            print("당첨 축하합니다.")
        else:
            print("당첨에 실패했지만 괜찮아요 여기는 가상이예요")

        

else:#이때는 실수로 실행해서 종료한다.
    print("사용을 종료합니다.")
    print("사용을 종료합니다.")
    

