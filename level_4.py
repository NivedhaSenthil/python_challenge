import requests

nothing = "8022"
def get_nothing(x):
    if str(x).isdigit():
        return x

while(nothing):
    result = requests.post("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing)
    print result.text
    nothing = filter(lambda x:get_nothing(x),result.text.split(" "))[0]
