#program to contain hindi english words value and user lookup
dict = {
    "khana" : "eat",
    "dodna" : "run",
    "rona" : "cry",
    "angreji" : "English"
}

mean = input("enter the hindi words :\n")
print("The translation in english is : ",dict.get(mean))