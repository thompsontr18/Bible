import requests
from bs4 import BeautifulSoup
from googlesearch import search
import shutil
import time


def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))


def googlesearch(query):
    result = []
    for j in search(query, tld="com", stop=5, pause=2):
        if "https://www.bible.com/bible" in j and "-" not in j:
            result.append(j)
    return result[0]


def reading(bookchoice, chapterchoice):
    choice = bookchoice.title() + " " + str(chapterchoice)
    print("\n\n")
    print_center(choice + "\n\n")
    choice += " bible.com"
    url = googlesearch(choice)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    chapters = soup.findAll(
        "span", attrs={"class": "ChapterContent_content__dkdqo"})
    text = "	"
    for chapter in chapters:
        text += chapter.text
        text += " "
    text = text.replace("  ", " ")
    print(text)
    print("\n\n")
    time.sleep(1)
    while True:
        again = input("Would you like to continue to the next chapter? (Y/N) ")
        if (again == "Y" or again == "y") and chapterchoice == maximum:
            print("\n")
            print_center(f"This is the end of {bookchoice}")
            print("\n")
            nextbook = input("Would you like to move on to the next book? (Y/N) ")
            if bookchoice.title() == "Revelation" and (nextbook == "Y" or nextbook == "y"):
                print_center("Congratulations! You have finished reading the Bible!")
            res = int(list(biblebooks.keys()).index(bookchoice.title()))
            key = list(biblebooks)[res+1]
            print(key)
            reading(key, 1)
        if again == "Y" or again == "y":
            reading(bookchoice, chapterchoice + 1)
        elif again == "N" or again == "n":
            quit()
        else:
            print("Not a valid answer")



biblebooks = {'Genesis': 50,
              'Exodus': 40,
              'Leviticus': 27,
              'Numbers': 36,
              'Deuteronomy': 34,
              'Joshua': 24,
              'Judges': 21,
              'Ruth': 4,
              '1 Samuel': 31,
              '2 Samuel': 24,
              '1 Kings': 22,
              '2 Kings': 25,
              '1 Chronicles': 29,
              '2 Chronicles': 36,
              'Ezra': 10,
              'Nehemiah': 13,
              'Esther': 10,
              'Job': 42,
              'Psalms': 150,
              'Proverbs': 31,
              'Ecclesiastes': 12,
              'Song Of Solomon': 8,
              'Isaiah': 66,
              'Jeremiah': 52,
              'Lamentations': 5,
              'Ezekiel': 48,
              'Daniel': 12,
              'Hosea': 14,
              'Joel': 3,
              'Amos': 9,
              'Obadiah': 1,
              'Jonah': 4,
              'Micah': 7,
              'Nahum': 3,
              'Habakkuk': 3,
              'Zephaniah': 3,
              'Haggai': 2,
              'Zechariah': 14,
              'Malachi': 4,

              'Matthew': 28,
              'Mark': 16,
              'Luke': 24,
              'John': 21,
              'Acts': 28,
              'Romans': 16,
              '1 Corinthians': 16,
              '2 Corinthians': 13,
              'Galatians': 6,
              'Ephesians': 6,
              'Philippians': 4,
              'Colossians': 4,
              '1 Thessalonians': 5,
              '2 Thessalonians': 3,
              '1 Timothy': 6,
              '2 Timothy': 4,
              'Titus': 3,
              'Philemon': 1,
              'Hebrews': 13,
              'James': 5,
              '1 Peter': 5,
              '2 Peter': 3,
              '1 John': 5,
              '2 John': 1,
              '3 John': 1,
              'Jude': 1,
              'Revelation': 22}


while True:
    bookchoice = input("> Which book would you like to read? ")
    chapterchoice = int(input("> Which chapter would you like to read? "))
    maximum = biblebooks.get(bookchoice.title())
    if bookchoice.title() in biblebooks and chapterchoice > 0 and chapterchoice <= maximum:
        break
    else:
        print("Not a valid book/chapter combination.")



reading(bookchoice, chapterchoice)
