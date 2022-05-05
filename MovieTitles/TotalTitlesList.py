import json

import requests

def TotalTitleList(substr):
    queryurl = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr
    response = requests.get(queryurl)
    # Since we know the response is in JSON, hence response.json is convenient
    #print(response.json())
    #response_str = json.loads(response.text())
    # resp = json.loads(response_str)
    #fetchedjson = json.loads(response.read())
    totalpages = response.json()["total_pages"]
    i = 1
    totalmovies = response.json()["total"]
    totalmoviecounter = 0
    titles = []
    while i <= totalpages:
        queryurlloop = queryurl + "&page=" + str(i)
        responseloop = requests.get(queryurlloop)
        for x in range(responseloop.json()["per_page"]):
            if totalmoviecounter < totalmovies:
                listmovietitle = responseloop.json()["data"][x]["Title"]
                #print("Value of movie title when x value is:", x, "is:", listmovietitle)
                titles.append(listmovietitle)
                totalmoviecounter = totalmoviecounter + 1
        i = i + 1
    # return (titles.sort())
    titles.sort()
    finaltitles = titles.copy()
    return finaltitles