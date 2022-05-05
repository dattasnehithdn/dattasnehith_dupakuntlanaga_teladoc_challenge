from MovieTitles import TotalTitlesList

def RequestAllTitles():
    sub_string = input('Enter the substring of movie you would like to get the list: ')
    titles = TotalTitlesList.TotalTitleList(sub_string)
    print("Final sorted Movie titles having the substring: ", sub_string, "are:", titles)

movietitlesobj = RequestAllTitles()