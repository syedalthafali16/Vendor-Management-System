import json

def load_vendors():
    try:
        with open("vendors.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_vendors():
    with open("vendors.json", "w") as f:
        json.dump(vendors, f)


from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage (acts like database)
vendors = load_vendors()

#-----routes-----

# Home page
@app.route('/')
def home():
    return render_template('index.html', vendors=vendors)

# Add vendor
@app.route('/add', methods=['POST'])
def add_vendor():
    name = request.form['name']
    product = request.form['product']

    vendors.append({
        "name": name,
        "product": product
    })

    save_vendors()

    return redirect('/')

# Delete vendor
@app.route('/delete/<int:index>')
def delete_vendor(index):
    if 0 <= index < len(vendors):
        vendors.pop(index)
        save_vendors()
    return redirect('/')

#----- Run App -------
if __name__ == '__main__':
    app.run(debug=True)