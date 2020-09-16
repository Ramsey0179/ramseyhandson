from datetime import datetime

def convert_miliseconds(ms):
    segments = [{'number':3600000, 'text':' hour/s '},{'number':60000, 'text':' minute/s '},{'number':1000, 'text':' second/s '}]

    def makestr(segment):
        nonlocal ms
        temp = ms // segment['number']
        ms %= segment['number']
        return f"{temp and (str(temp) + segment['text']) or ''}"
 
    result = ""
    for segment in segments:
        result += makestr(segment)

    return f"{result or ('just ' + str(ms) + ' miliseconds') }"

def convert_miliseconds2(ms):
    segments = [{'div':3600000, 'remainder':24, 'text':' hour/s '},
                {'div':60000, 'remainder':60,'text':' minute/s '},
                {'div':1000, 'remainder':60,'text':' second/s '}]

    result = ""
    for segment in segments:
        value = (ms // segment['div']) % segment['remainder']
        result += f"{value and (str(value) + segment['text']) or ''}"

    return f"{result or ('just ' + str(ms) + ' miliseconds') }"

def convert_miliseconds3(ms):
    dtime = datetime.utcfromtimestamp(ms/1000).time() 
    result = ""
    result += f"{dtime.hour and (str(dtime.hour) + ' hour/s ') or ''}"
    result += f"{dtime.minute and (str(dtime.minute) + ' minute/s ') or ''}"
    result += f"{dtime.second and (str(dtime.second) + ' second/s ') or ''}"
    return f"{result or ('just ' + str(ms) + ' miliseconds') }"

def convert_miliseconds4(ms):
    result = ""
    saat = ms // 3600000
    if saat != 0:
        result += str(saat) + " hour/s " 
    dakika = (ms // 60000) % 60
    if dakika != 0:
        result += str(dakika) + " minute/s " 
    saniye = (ms // 1000) % 60
    if saniye != 0:
        result += str(saniye) + " second/s " 
    if result == "":
        result = "Just " + str(ms) + " miliseconds"
    return result

print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print('(To exit the program, please type "exit")')

while True:
    ms = input("Please enter the milliseconds (should be greater than zero) : ")
    if ms == "exit":
        print("Exiting the program... Good Bye")
        break
    if ms.isdigit():
        print(convert_miliseconds(int(ms)))
        print(convert_miliseconds2(int(ms)))
        print(convert_miliseconds3(int(ms)))
        print(convert_miliseconds4(int(ms)))
    else:
        print( "Not Valid Input !!!")