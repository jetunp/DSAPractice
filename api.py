import requests

def get_house_names_with_all_characters_from_book(book_num):
    responseBook = requests.get("https://anapioficeandfire.com/api/books/"+str(book_num))
    characterList=responseBook.json()['characters']
    housesSet = set()
    for character in characterList:
        responseCharacter = requests.get(character)
        allegiance = responseCharacter.json()['allegiances']
        print(allegiance)
        housesSet.update(allegiance)
    print('houses are: ',housesSet)
    resultSet = set()
    for house in housesSet:
        swornMemberPresent = True
        responseHouse = requests.get(house)
        swornMembers=responseHouse.json()['swornMembers']
        houseName = responseHouse.json()['name']
        # print('the list of swornMembers are: ',swornMembers)
        #for character in characterList:
        #     if character not in swornMembers:
        #         #print("what ius the sworn :",swornMember)
        #         swornMemberPresent = False
        #         break
        #     else:
        #         swornMemberPresent = True
        # if swornMemberPresent:
        #     print('the houses we want are: ',houseName)
        #     resultSet.add(houseName)
        check = any(swornMember in swornMembers for character in characterList)
        if check is True:
            print('the houses we want are: ',houseName)
        else:
            print('no match')
    print(len(housesSet))  
    print(len(resultSet))  
get_house_names_with_all_characters_from_book(5)