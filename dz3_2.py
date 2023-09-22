import requests
import math

def gravitation(g,m1,m2,r):
    f=g*m1*m2 / math.pow(r,2)
    return f

m1 = 5.97600 * math.pow(10,24)
g = 6.6743 * math.pow(10,-11)

names = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
for i in range(len(names)):
    api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(names[i])
    response = requests.get(api_url, headers={'X-Api-Key': 'KheDR2ri0bbd/gV+p6hYbw==oSusQjtDdgpQcZAE'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    m2 = 1.898*10**27 * float((response.text[response.text.find('mass')+7:response.text.find('mass')+13]))
    r= float((response.text[response.text.find('year')+7:response.text.find('year')+15]))
    print(names[i],'-',gravitation(g,m1,m2,r))