#15 - Suliguin, Jose Santiago T.
9 - Balingkilat
SG2 - Activity 3
August 14, 2026 

Year = int(input("Enter your bith year: "))
print("")

#Sorting out valid years from invalid years
if Year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
    exit()
    
Zodiac_Class = Year % 12

#Classifying Years into Signs
if Zodiac_Class == 0:
    print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    # Years of the monkey have no remainder
    
elif Zodiac_Class == 1:
    print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    # Years of the rooster have a remainder of 1
    
elif Zodiac_Class == 2:
    print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    # Years of the dog have a remainder of 2
    
elif Zodiac_Class == 3:
    print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")
    # Years of the pig have a remainder of 3
    
elif Zodiac_Class == 4:
    print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
    # Years of the rat have a remainder of 4
    
elif Zodiac_Class == 5:
    print("Your Chinese Zodiac Sign is: Ox (牛 / Niú)")
    # Years of the ox have a remainder of 5
    
elif Zodiac_Class == 6:
    print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    # Years of the tiger have a remainder of 6
    
elif Zodiac_Class == 7:
    print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    # Years of the rabbit have a remainder of 7
    
elif Zodiac_Class == 8:
    print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    # Years of the dragon have a remainder of 8
    
elif Zodiac_Class == 9:
    print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    # Years of the snake have a remainder of 9
    
elif Zodiac_Class == 10:
    print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    # Years of the horse have a remainder of 10
    
elif Zodiac_Class == 11:
    print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    # Years of the goat have a remainder of 11
    
    
