from flask import Flask, render_template

app = Flask(__name__)

currentLoc = ["00"]
x = "0"
y = "0"
'''
file = open("dlwodyd", "r")
newLoc = file.readlines()
file.close()
if currentLoc != newLoc[-1]:
    x = newLoc[-1][0]
    y = newLoc[-1][1]
'''

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)