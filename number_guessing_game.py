import time
import random

# tolgoomiin random toog tohiruulah
def random_too(range_num):
    return random.randint(1,range_num)

# useriin level tohirson index uudiig tohiruulah
def level_set(lvl):
    if lvl == 1:
        range_num = 50
        try_num = 10
        time_limit = 90
    elif lvl == 2:
        range_num = 100
        try_num = 7
        time_limit = 60
    elif lvl == 3:
        range_num = 200
        try_num = 5
        time_limit = 45
    return range_num, try_num, time_limit

# user toog taasan tohioldold score iig tootsooloh
def score(start_score, game_lvl, time_score,hint_count):
    if game_lvl == 1:
        user_score = start_score - time_score - hint_count*5
    elif game_lvl == 2:
        user_score = start_score - time_score*1.5 - hint_count*5
    elif game_lvl == 1:
        user_score = start_score - time_score*2 - hint_count*5
    return user_score

#user hint hussen vyd zuw hint hewleh
def hint(random_num, user_num):
    if user_num < random_num:
        hint_text = "tanii oruulsan too taah ystoi toonoos baga baina"
    else:
        hint_text = "tanii oruulsan too taah ystoi toonoos ih baina"
    return hint_text

#user iin score iig rank table iin hamt hewleh
def highscore(score_list, user_score):
    score_list.sort(reverse = True)
    deed_limit = len(score_list)
    if deed_limit >3:
        deed_limit = 3
    top3_flag = user_score in score_list[:deed_limit]
    if top3_flag:
        print("Bayar hurgii. ta TOP3 t orloo. tanii onoog tsenhereer haruulsan baigaa")
    else:
        print("Bayar hurgii. ta hojloo.tanii onoo bolon rank iig tsenhereer haruulsan baigaa")
    print("RANK|SCORE")
    if top3_flag:
        for i, score in enumerate(score_list[:deed_limit]):
            if score == user_score:
                print("\033[34m"+str(i+1)+"|"+str(score)+"\033[0m")
            else:
                print(str(i+1)+"|"+str(score))
    else:
        for i, score in enumerate(score_list[:3]):
            print(str(i+1)+"|"+str(score))
        print("\033[34m"+str(score_list.find(user_score)+1)+"|"+str(user_score)+"\033[0m")
    return 

user_name = input("Нэрээ оруулна уу?\n")
print(f"""Сайн байна уу?{user_name}Тоо таах тоглоомонд тавтай морил!
Уг тоглоомонд та сонгосон түвшингийнхээ дагуу тоо тааж тоглох юм. Хамгийн ихдээ 100 оноо авах боломжтой. Түвшингийн танилцуулга:
1.Хялбар(1-50 хооронд тоо таах, 10 оролдлого, 90 секунд, 1 секундэд 1 оноо хасагдана)
2.Дунд(1-100 хооронд тоо таах, 7 оролдлого, 60 секунд, 1 секундэд 1.5 оноо хасагдана)
3.Хэцүү(1-200 хооронд тоо таах, 5 оролдлого, 45 секунд, 1 секундэд 2 оноо хасагдана)
Тоглоомын явцад HINT авах боломжтой ба HINT авах бүрд 5 оноо хасагдана
""")
score_list = []

try:
    lvl = int(input("""Та тоглоомын түвшингээ сонгоно уу?
1.Хялбар
2.Дунд
3.Хэцүү
Зөвхөн түшингийн дугаар болох 1 тоог бичнэ үү
"""))
except:
    lvl = int(input("Zuwhun 1 eswel 2 eswel 3iin ali negiig oruulna uu\n"))
    
range_num, try_num, time_limit = level_set(lvl)

try:
    start_button = input("Togloom ehluuleh bol y garah bol n darna uu\n")
except:
    start_button = input("Zuwhun y eswel n darna uu\n")

while start_button=="Y" or start_button=="y":
    
    start_time =time.time()
    end_time =time.time()
    try_count = 0
    user_num = 0
    rand_num = random_too(range_num)
    user_numbers = []
    start_score = 100
    hint_count = 0
    time_limit_flag = 0
    try_flag = 0

    while end_time-start_time<time_limit and user_num!=rand_num and try_count<=try_num:

        if try_count <1:
            try:
                user_num = input(f"1 ees {range_num} hurtel toog oruulna uu\n")
            except:
                user_num = input("Zuwhun toon utga oruulna uu\n")
        else:
            try:
                user_num = input(f"1 ees {range_num} hurtel toog oruulna uu\nHerew hint awah bol H gej bichne uu")
            except:
                user_num = input("Zuwhun toon utga eswel H oruulna uu\n")

        end_time = time.time()
        if user_num == "H" or user_num == "h":
            print(hint(rand_num, user_numbers[-1]))
            hint_count = hint_count + 1
        else:
            user_num = int(user_num)
            user_numbers.append(user_num)
            try_count = try_count + 1
            user_score = score(start_score, lvl,end_time-start_time,hint_count)
            if user_num != rand_num:
                print(f"Ooops! tanii oruulsan too buruu baina. tanid {int(time_limit-end_time+start_time)} second, {try_num-try_count} oroldlogo uldlee")
            else:
                score_list.append(user_score)
                highscore(score_list,user_score)
    if end_time-start_time>=time_limit:
        print("\033[31m"+"Uuchlarai. Hugatsaanii hyazgaarlalt heterlee"+"\033[0m")
    elif try_count > try_num:
        print("\033[31m"+"Uuchlarai. Taah oroldlogiin too heterlee"+"\033[0m")
    try:
        start_button = input("Dahin togloh bol y garah bol n darna uu\n")
    except:
        start_button = input("Zuwhun y eswel n darna uu\n")

