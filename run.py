from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("startpage.html")

@app.route("/exchangerate")
def exchange():

    currency1=request.args.get("currency1","Please Enter")
    currency2=request.args.get("currency2","Please Enter")
    rate=float(request.args.get("exchangerate","1"))       ## 1 is the default value

    table1 = []
    table2=[]
    for x in range(1, 21):
        table1.append((x, round(x*rate,4)))
        table2.append((x,round(x/rate,3)))
    print(table1)
    print(table2)
    return render_template("rates.html", currency1=currency1,
                           currency2=currency2,
                           rate=rate,
                           table1=table1,
                           table2=table2)

