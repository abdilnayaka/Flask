from flask import Flask,render_template

app = Flask (__name__)

@app.route("/")
def index():
    return "Halo"

@app.route("/nama")
def nama():
    return "Halo nama"

@app.route("/nama/<string:nama>")
def getnama(nama):
    return "Halo {} Selamat datang" .format(nama)

@app.route("/mahasiswa")
def halmahasiswa():
    kelas = "1IA02"
    return render_template("mhs.html", kelas = kelas)

@app.route("/dosen")
def haldosen():
    alamat = ["Depok","Jakarta", "Bogor"]
    return render_template("dsn.html", alamat = alamat)

@app.route("/bootstrap")
def bs():
    return render_template("bs.html")

@app.route("/tabel")
def tabelmhs():
    return render_template("tabl.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
