#Package import
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request 
 
#initialise app
app = Flask(__name__)

#decorator for homepage 
@app.route('/' )
def index():
    return render_template('index.html',
                           PageTitle = "Landing page")

 if __name__ == '__main__':
    app.run(debug = True)



d = {}
#Number of scoops, ounces of water, final volume
d["Elecare Infant"] = (1,2)
d["Puramino"] = (2,3,4), (5,6,7)
d["Pregestimil"] = (3,4)
d["Enfamil Gentlease"] = (4,5)
d["Enfamil Infant"] = (5,6)
d["Alfamino Infant"] = (4,4,4.5), (8,8,9), (20,25,27.5)

list_brand = []
for entry in d:
    list_brand.append(entry.upper())

while True:
    brand = input("What brand are you using? ")
    if brand.upper() in list_brand:
        break
    else:
        print("Invalid input. Please enter a valid brand.")

while True:
    count = 0
    scoops,water = input("What is current ratio?\nEnter the number of scoops of {} using decimals: ".format(brand)), input("Enter ounces of water: ")
    try:
        scoops = float(scoops)
        water = float(water)
        for ratio in d[brand]:
            if ratio[0]==scoops and ratio[1]==water:
                count +=1
                break
        if count==0:
            print("Invalid ratio. Please enter a valid ratio for {}".format(brand))
        elif count>0:
            break
    except:
        print("Invalid input. Please enter a number.")

while True:
    vol = input("Enter desired final volume of solution: ")
    try:
        vol = float(vol)
        break
    except:
        print("Invalid input. Please enter a number.")