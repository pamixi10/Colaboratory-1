QUESTION=[
    "サザエさんの旦那は？>>",
    "カツオの妹は？>>",
    "タラちゃんはカツオから見てどんな関係？>>",
    "特別問題です!猫の名前は？>>"
    ]
R_ANS=["マスオ","ワカメ","甥","たま"]
R2_ANS=["ますお","わかめ","おい","タマ"]

a=0
for i in range(3):
    print(QUESTION[i])
    ans=input()
    if R_ANS[i] in ans or R2_ANS[i] in ans:
        print("正解です")
        a=a+1
        if a==3:
            ans2=input(QUESTION[3])
            if R_ANS[3] in ans2 or R2_ANS[3] in ans2:
                 print("大正解です!!")
    else:
        print("不正解です")
        