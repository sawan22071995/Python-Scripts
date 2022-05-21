# program to temprature celcious to farenheit

def tempratur_farenheit(celcious):
    return (celcious * (9/5)) + 32
    
cel = int(input("enter the temprature in celcious:"))
fer = tempratur_farenheit(cel)
print(f"The Temprature of {cel}'C celcious in farenheit is : {fer}'F ")
