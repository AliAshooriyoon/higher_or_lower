import random

data = [
    {"name": "AliAshouriyoun", "folowwer": "14", "description": "Just a programmer"},
    {
        "name": "MrBeast",
        "folowwer": "422",
        "description": "Entertainment, challenges, and philanthropy",
    },
    {
        "name": "T-Series",
        "folowwer": "301",
        "description": "Bollywood music and film trailers",
    },
    {
        "name": "Cocomelon - Nursery Rhymes",
        "folowwer": "196",
        "description": "Animated nursery rhymes and kids' songs",
    },
    {
        "name": "SET India",
        "folowwer": "185",
        "description": "Hindi TV shows and entertainment",
    },
    {
        "name": "Vlad and Niki",
        "folowwer": "143",
        "description": "Kids' playtime and educational adventures",
    },
    {
        "name": "Kids Diana Show",
        "folowwer": "136",
        "description": "Kids' role-playing and toy unboxing",
    },
    {
        "name": "Like Nastya",
        "folowwer": "129",
        "description": "Kids' play and family-friendly content",
    },
    {
        "name": "Stokes Twins",
        "folowwer": "129",
        "description": "Comedy sketches and pranks",
    },
    {
        "name": "Zee Music Company",
        "folowwer": "119",
        "description": "Bollywood music videos",
    },
    {
        "name": "김프로KIMPRO",
        "folowwer": "116",
        "description": "Entertainment and vlogs",
    },
    {
        "name": "PewDiePie",
        "folowwer": "110",
        "description": "Gaming and commentary",
    },
    {
        "name": "WWE",
        "folowwer": "110",
        "description": "Wrestling highlights and shows",
    },
    {"name": "Goldmines", "folowwer": "106", "description": "Hindi dubbed movies"},
    {
        "name": "Sony SAB",
        "folowwer": "103",
        "description": "Hindi entertainment and TV shows",
    },
    {
        "name": "BLACKPINK",
        "folowwer": "98.4",
        "description": "K-pop music and performances",
    },
    {
        "name": "ChuChu TV Nursery Rhymes & Kids Songs",
        "folowwer": "97.2",
        "description": "Kids' educational songs",
    },
    {
        "name": "Alan's Universe",
        "folowwer": "95.8",
        "description": "Entertainment and animation",
    },
    {
        "name": "Zee TV",
        "folowwer": "93.4",
        "description": "Hindi TV dramas and shows",
    },
    {
        "name": "A4",
        "folowwer": "88.2",
        "description": "Russian entertainment and challenges",
    },
    {
        "name": "Alejo Igoa",
        "folowwer": "86.1",
        "description": "Spanish entertainment and vlogs",
    },
    {
        "name": "Baby Shark - Pinkfong Kids’ Songs & Stories",
        "folowwer": "82.7",
        "description": "Kids' songs and educational videos",
    },
    {
        "name": "BANGTANTV",
        "folowwer": "81.2",
        "description": "BTS K-pop music and content",
    },
    {
        "name": "5-Minute Crafts",
        "folowwer": "81",
        "description": "DIY and craft tutorials",
    },
    {
        "name": "Colors TV",
        "folowwer": "80.8",
        "description": "Hindi TV entertainment",
    },
    {
        "name": "ZAMZAM ELECTRONICS TRADING",
        "folowwer": "79.4",
        "description": "Electronics and entertainment",
    },
    {
        "name": "Toys and Colors",
        "folowwer": "78.3",
        "description": "Kids' play and toy reviews",
    },
    {
        "name": "HYBE LABELS",
        "folowwer": "78.2",
        "description": "K-pop music and artist content",
    },
    {
        "name": "T-Series Bhakti Sagar",
        "folowwer": "78.1",
        "description": "Hindi devotional music",
    },
    {
        "name": "Tips Official",
        "folowwer": "77.7",
        "description": "Bollywood music and songs",
    },
    {
        "name": "UR · Cristiano",
        "folowwer": "76.4",
        "description": "Sports and entertainment",
    },
    {
        "name": "Justin Bieber",
        "folowwer": "76",
        "description": "Pop music and artist content",
    },
    {
        "name": "KL BRO Biju Rithvik",
        "folowwer": "75.8",
        "description": "Malayalam lifestyle vlogs",
    },
    {
        "name": "Topper Guild",
        "folowwer": "73.9",
        "description": "Entertainment and challenges",
    },
    {
        "name": "Aaj Tak",
        "folowwer": "73.2",
        "description": "Hindi news and updates",
    },
    {
        "name": "Shemaroo Filmi Gaane",
        "folowwer": "72.9",
        "description": "Bollywood music videos",
    },
    {
        "name": "Infobells - Hindi",
        "folowwer": "70.7",
        "description": "Hindi kids' educational content",
    },
    {
        "name": "Mark Rober",
        "folowwer": "70.4",
        "description": "Science and educational experiments",
    },
    {
        "name": "El Reino Infantil",
        "folowwer": "69.8",
        "description": "Spanish kids' songs and stories",
    },
    {
        "name": "HAR PAL GEO",
        "folowwer": "69.4",
        "description": "Urdu TV dramas and entertainment",
    },
    {
        "name": "Fede Vigevani",
        "folowwer": "69.1",
        "description": "Spanish entertainment and vlogs",
    },
    {"name": "YRF", "folowwer": "68", "description": "Bollywood films and music"},
    {
        "name": "Canal KondZilla",
        "folowwer": "67.8",
        "description": "Brazilian funk music",
    },
    {
        "name": "Sony Music India",
        "folowwer": "67.2",
        "description": "Indian music and songs",
    },
    {
        "name": "Wave Music",
        "folowwer": "66.6",
        "description": "Bhojpuri music and videos",
    },
    {
        "name": "EminemMusic",
        "folowwer": "65.5",
        "description": "Rap music and artist content",
    },
    {
        "name": "ISSEI / いっせい",
        "folowwer": "65",
        "description": "Japanese entertainment",
    },
    {
        "name": "ARY Digital HD",
        "folowwer": "64.7",
        "description": "Urdu TV shows and dramas",
    },
    {
        "name": "Movieclips",
        "folowwer": "64.7",
        "description": "Film clips and trailers",
    },
    {
        "name": "YOLO AVENTURAS",
        "folowwer": "64.3",
        "description": "Spanish entertainment and challenges",
    },
    {
        "name": "Anaya Kandhal",
        "folowwer": "63.3",
        "description": "Hindi entertainment and kids' content",
    },
    {
        "name": "Dude Perfect",
        "folowwer": "61.4",
        "description": "Sports and comedy stunts",
    },
    {
        "name": "Taylor Swift",
        "folowwer": "61.3",
        "description": "Pop music and artist content",
    },
    {
        "name": "Bispo Bruno Leonardo",
        "folowwer": "60.6",
        "description": "Portuguese religious content",
    },
    {
        "name": "LooLoo Kids - Nursery Rhymes and Children's Songs",
        "folowwer": "60.6",
        "description": "Kids' nursery rhymes",
    },
    {
        "name": "Shemaroo",
        "folowwer": "59.7",
        "description": "Hindi entertainment and movies",
    },
    {
        "name": "Zhong",
        "folowwer": "59.5",
        "description": "Entertainment and comedy",
    },
    {
        "name": "PANDA BOI",
        "folowwer": "59.5",
        "description": "Comedy and entertainment",
    },
    {
        "name": "ToRung",
        "folowwer": "58.4",
        "description": "Vietnamese comedy videos",
    },
    {
        "name": "Ed Sheeran",
        "folowwer": "58.2",
        "description": "Pop music and artist content",
    },
    {
        "name": "Marshmello",
        "folowwer": "58.1",
        "description": "Electronic music and artist content",
    },
    {
        "name": "Billion Surprise Toys",
        "folowwer": "57.9",
        "description": "Kids' educational cartoons",
    },
    {
        "name": "आचार्य प्रशान्त - Acharya Prashant",
        "folowwer": "57.9",
        "description": "Hindi spiritual education",
    },
    {
        "name": "SonyMusicIndiaVEVO",
        "folowwer": "57.6",
        "description": "Indian music videos",
    },
    {
        "name": "Saregama Music",
        "folowwer": "57.4",
        "description": "Indian music and classics",
    },
    {
        "name": "Маша и Медведь",
        "folowwer": "57.2",
        "description": "Russian kids' animation",
    },
    {
        "name": "Mikecrack",
        "folowwer": "57",
        "description": "Spanish gaming content",
    },
    {
        "name": "JioHotstar Kids",
        "folowwer": "56.7",
        "description": "Hindi kids' entertainment",
    },
    {
        "name": "Billie Eilish",
        "folowwer": "56.5",
        "description": "Pop music and artist content",
    },
    {
        "name": "Ariana Grande",
        "folowwer": "56.3",
        "description": "Pop music and artist content",
    },
    {
        "name": "StarPlus",
        "folowwer": "56.1",
        "description": "Hindi TV shows and dramas",
    },
    {
        "name": "Get Movies",
        "folowwer": "56",
        "description": "Russian animation and films",
    },
    {
        "name": "Jess No Limit",
        "folowwer": "54.3",
        "description": "Indonesian gaming and entertainment",
    },
    {
        "name": "Alfredo Larin",
        "folowwer": "54.1",
        "description": "Spanish entertainment",
    },
    {
        "name": "JuegaGerman",
        "folowwer": "53.9",
        "description": "Spanish gaming and entertainment",
    },
    {
        "name": "ABS-CBN Entertainment",
        "folowwer": "53.5",
        "description": "Filipino TV shows and entertainment",
    },
    {
        "name": "LUCCAS TOON - LUCCAS NETO",
        "folowwer": "53.1",
        "description": "Portuguese kids' entertainment",
    },
    {
        "name": "Real fools shorts official",
        "folowwer": "52.8",
        "description": "Hindi comedy shorts",
    },
    {"name": "shfa", "folowwer": "52.7", "description": "Arabic kids' content"},
    {
        "name": "Juan De Dios Pantoja",
        "folowwer": "52.6",
        "description": "Spanish music and vlogs",
    },
    {
        "name": "Masha and The Bear",
        "folowwer": "52.4",
        "description": "English kids' animation",
    },
    {
        "name": "BETER BÖCÜK",
        "folowwer": "52.1",
        "description": "Turkish gaming content",
    },
    {
        "name": "Dangal TV Channel",
        "folowwer": "51.9",
        "description": "Hindi TV shows and dramas",
    },
    {"name": "HUM TV", "folowwer": "51.6", "description": "Urdu TV dramas"},
    {
        "name": "MrBeast 2",
        "folowwer": "51.4",
        "description": "Entertainment and challenges",
    },
    {
        "name": "shfa2 - شفا",
        "folowwer": "51.4",
        "description": "Arabic kids' content",
    },
    {
        "name": "Celine Dept",
        "folowwer": "51.2",
        "description": "Sports and entertainment",
    },
    {
        "name": "Ishtar Music",
        "folowwer": "51.1",
        "description": "Indian music videos",
    },
    {
        "name": "Bad Bunny",
        "folowwer": "50.7",
        "description": "Latin music and artist content",
    },
    {
        "name": "Fernanfloo",
        "folowwer": "49.3",
        "description": "Spanish gaming and entertainment",
    },
    {
        "name": "Dushyant kukreja",
        "folowwer": "49.2",
        "description": "Hindi comedy and entertainment",
    },
    {
        "name": "T-Series Bollywood Classics",
        "folowwer": "49.3",
        "description": "Classic Bollywood music",
    },
    {
        "name": "Maria Clara & JP",
        "folowwer": "48.9",
        "description": "Portuguese kids' entertainment",
    },
    {
        "name": "ABP NEWS",
        "folowwer": "48.8",
        "description": "Hindi news and updates",
    },
    {"name": "Shakira", "folowwer": "48.8", "description": "Latin pop music"},
    {
        "name": "MrBeast Gaming",
        "folowwer": "48.7",
        "description": "Gaming and challenges",
    },
    {
        "name": "Ricis Official",
        "folowwer": "48.7",
        "description": "Indonesian lifestyle and entertainment",
    },
    {
        "name": "IndiaTV",
        "folowwer": "48.5",
        "description": "Hindi news and updates",
    },
    {
        "name": "PowerKids TV",
        "folowwer": "48.2",
        "description": "Kids' animation and shows",
    },
    {
        "name": "Badabun",
        "folowwer": "47.6",
        "description": "Spanish entertainment and news",
    },
    {
        "name": "Felipe Neto",
        "folowwer": "47.5",
        "description": "Portuguese entertainment",
    },
]

# while second_random_person == first_random_person:
# second_random_person = random.choice(data)


def runGame():
    contextPersons = [random.choice(data), random.choice(data)]
    correctAnswer = []
    stop = False

    def doStop():
        return True

    # print(contextPersons[0])
    def doQuestion():
        print("Do Question \n")
        contextPersons[1] = random.choice(data)
        while contextPersons[1] == contextPersons[0]:
            print("While the Same")
            contextPersons[1] = random.choice(data)
        person1 = contextPersons[0]
        person2 = contextPersons[1]

        return input(
            f"Welche hat hohere Folger \n A : {person1['name']} \n B: {person2['name']}  ? \n"
        )

    # ----------------------------------------------------------
    # ----------------------------------------------------------
    # selector = doQuestion()
    while stop == False:
        person1 = contextPersons[0]
        person2 = contextPersons[1]

        def selectorFunc():
            if correctAnswer != []:
                return doQuestion()
            else:
                # print("In Selector \n")
                return input(
                    f"Welche hat hohere Folger \n A : {person1['name']} \n B: {person2['name']}  ? \n"
                )

        # if correctAnswer != []:
        # contextPersons[0] = correctAnswer[0]
        selector = selectorFunc()
        if selector == "B":
            # print("if B \n")
            if person2["folowwer"] > person1["folowwer"]:
                print("Korrekt!")
                correctAnswer.insert(0, person2)
                contextPersons[0] = correctAnswer[0]
            elif person2["folowwer"] < person1["folowwer"]:
                print("Inkorrekt!")
                stop = doStop()
        elif selector == "A":
            # print("if A \n")
            if person1["folowwer"] > person2["folowwer"]:
                print("Korrekt!")
                correctAnswer.insert(0, person1)
                contextPersons[0] = correctAnswer[0]
            elif person1["folowwer"] < person2["folowwer"]:
                print("Inkorekkt")
                stop = doStop()


runGame()
