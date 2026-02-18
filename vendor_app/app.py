import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
DATA_FILE = "vendors.json"

# ---------- JSON ----------
def load_vendors():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_vendors(vendors):
    with open(DATA_FILE, "w") as f:
        json.dump(vendors, f, indent=4)

vendors = load_vendors()

# ---------- Routes ----------

@app.route('/')
def home():
    return render_template(
        "index.html",
        vendors=vendors,
        edit_vendor=None,
        edit_index=None
    )

@app.route('/add', methods=['POST'])
def add_vendor():
    vendors.append({
        "name": request.form['name'],
        "product": request.form['product']
    })
    save_vendors(vendors)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete_vendor(index):
    if 0 <= index < len(vendors):
        vendors.pop(index)
        save_vendors(vendors)
    return redirect('/')

@app.route('/edit/<int:index>')
def edit_vendor(index):
    if 0 <= index < len(vendors):
        return render_template(
            "index.html",
            vendors=vendors,
            edit_vendor=vendors[index],
            edit_index=index
        )
    return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update_vendor(index):
    if 0 <= index < len(vendors):
        vendors[index]['name'] = request.form['name']
        vendors[index]['product'] = request.form['product']
        save_vendors(vendors)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
