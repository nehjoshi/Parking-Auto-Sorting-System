from flask import Flask, render_template, request
from main import createArray, push, pop, QuickSort, getStack, Search
app = Flask(__name__)
stack = [[], [], [], [], [], '0']
initial = True

@app.route("/", methods=['GET', 'POST'])
def hello_world():

    global stack
    global initial

    if (request.method=="POST"):
        if (initial):
            print("STACK 5 is zero!!!")
            initial = False
            stack=[]
        
        number = int(request.form.get("input"))
        stack = push(stack, number)
        print("Number inputted: ", number)
        print(stack)

    if (len(stack)==1):
        return render_template("index.html", array5 = stack[0], array4 = [], array3 = [], array2 = [], array1 = [])
    elif (len(stack)==2):
        return render_template("index.html", array5 = stack[0], array4 = stack[1], array3 = [], array2 = [], array1 = [])
    elif (len(stack)==3):
        return render_template("index.html", array5 = stack[0], array4 = stack[1], array3 = stack[2], array2 = [], array1 = [])
    elif (len(stack)==4):
        return render_template("index.html", array5 = stack[0], array4 = stack[1], array3 = stack[2], array2 = stack[3], array1 = [])
    elif (len(stack)==5):
        return render_template("index.html", array5 = stack[0], array4 = stack[1], array3 = stack[2], array2 = stack[3], array1 = stack[4])

    return render_template("index.html", array5 = stack[0], array4 = stack[1], array3 = stack[2], array2 = stack[3], array1 = stack[4])

@app.route('/search', methods=['GET', 'POST'])
def search():
    print("Searching...")
    element = int(request.form.get("search"))
    if (Search(stack, element)):
        return render_template("search.html", found="Element is found")
    else:
        return render_template("search.html", found="Element is NOT found")

    
if (__name__ == "__main__"):
    app.run(debug=True, use_debugger=False, use_reloader=False)

