import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/")
resp_dict = resp.json()


for i in range(len(resp_dict)):
    txt = open("titles.txt", "a+")
    txt.write(resp_dict[i]["title"]+"\n")
    txt.close()
    print(resp_dict[i]["title"])