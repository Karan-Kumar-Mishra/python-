# Dictionary in
d1= {}
    print(type(d1))

d2= {
"karan":"sultanpur"
    ,
"zack":"lucknow"
    ,
"jack":"california"
    ,
"mohan":
    {"name":"mohan"
        ,
"roll_number":"123"
,"address":"lucknow"
    },

}

print(d2)

print(d2["karan"])

print(d2["mohan"])

d2["Raj"]="kanpur"

          d2[1567]="84975"

                   print("After adding ")

                   print(d2)

                   del d2[1567]

                   del d2["jack"]

                   print("After deleteing ")

                   print(d2)

                   print("get function ")

                   print(d2.get("mohan"))

                   print("update function")

                   d2.update({"zack" : "z@ck"})

                   print(d2)

                   print("printing the key ")

                   print(d2.keys())

                   print("printing the iteam ")

                   print(d2.items())

