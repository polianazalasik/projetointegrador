from flask import Flask, render_template, request, redirect, url_for, session
from pessoa import Pessoa

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("Index.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", lista = Pessoa.select())

@app.route("/form_inserir_pessoas")
def mostrar_pessoas():
    return render_template("form_inserir_pessoas.html")

@app.route("/cadastrar")
def cadastrar_pessoas():
    nome =request.args.get("cpf")
    dia = request.args.get("dia")
    mes = request.args.get("mes")
    ano = request.args.get("ano")
    rg = request.args.get("rg")
    cpf = request.args.get("cpf")
    rua = request.args.get("rua")
    numero = request.args.get("numero")
    bairro = request.args.get("bairro")
    estado = request.args.get("estado")
    cidade = request.args.get("cidade")
    cep = request.args.get("cep")
    email = request.args.get("email")
    login = request.args.get("login")
    passs = request.args.get("passs")
    passconfirm = request.args.get("passconfirm")
    Pessoa(nome=nome, dia = dia, mes=mes, ano=ano, rg=rg, cpf=cpf, rua=rua, numero=numero, bairro=bairro, estado=estado, cidade=cidade, cep=cep, email=email, login=login, passs=passs, passconfirm=passconfirm)
    return listar_pessoas()

@app.route("/excluir_pessoas")
def excluir():
    cpf = request.args.get("cpf")
    for i in lista_global:
        if i.cpf == cpf:
            lista_global.remove(i)
            break
    return listar_pessoas()

@app.route("/form_alterar_pessoa")
def form_alterar():
    cpf = request.args.get("cpf")
    for p in lista_global:
        if p.cpf == cpf:
            return render_template("form_alterar_pessoa.html", pessoa = p)
    return "Pessoa não encontrada:" +cpf

@app.route("/alterar_pessoa")
def alterar_pessoa():
    procurar = request.args.get("cpf_original")
    cpf = request.args.get("cpf")
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    novo = Pessoa(cpf, nome, idade)
    for i in range(len(lista_global)):
        if lista_global[i].cpf == procurar:
            lista_global[i]= novo
            return redirect(url_for("listar_pessoas"))
    return "não achou" + procurar

@app.route("/login")
def login():
    login = request.args.get("login")
    senha = request.args.get("senha")
    if login == "admin" and senha == "123":
        session["usuario"] = login
        return redirect("/")
    else:
        return "erro no login e/ou senha"

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/album")
def album():
    return render_template("album.html")

@app.route("/alumbum1")
def alumbum():
    return render_template("alumbum1.html")

@app.route("/album2")
def album2():
    return render_template("album2.html")

@app.route("/album3")
def album3():
    return render_template("album3.html")

@app.route("/album4")
def album4():
    return render_template("album4.html")

@app.route("/album5")
def album5():
    return render_template("album5.html")

@app.route("/album6")
def album6():
    return render_template("album6.html")

@app.route("/album7")
def album7():
    return render_template("album7.html")

@app.route("/album8")
def album8():
    return render_template("album8.html")

@app.route("/album9")
def album9():
    return render_template("album9.html")

@app.route("/album10")
def album10():
    return render_template("album10.html")

@app.route("/album11")
def album11():
    return render_template("album11.html")

@app.route("/album12")
def album12():
    return render_template("album12.html")

@app.route("/form_compras")
def form_compras():
    return render_template("form_compras.html")

@app.route("/sucesso")
def fazer_sucesso():
    return render_template("sucesso.html")


app.config['SECRET_KEY'] = 'RYDYDYT'
app.run(host="0.0.0.0", debug=True)
