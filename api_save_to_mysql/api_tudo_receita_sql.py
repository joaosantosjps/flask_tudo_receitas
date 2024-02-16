from flask import Flask, jsonify
import mysql.connector
import os

connetc_sql = mysql.connector.connect(
    user=os.getenv("mysqluser"),
    password=os.getenv("mysqlkey"),
    host=os.getenv("mysqlhost"),
    database="tudo_receita_sql"
)

app = Flask(__name__)
my_cursor = connetc_sql.cursor()


@app.route("/home", methods=["GET"])
def get_all_data():
    my_cursor.execute("SELECT * FROM receitas;")
    my_receitas = my_cursor.fetchall()
    receitas = list()

    for receita in my_receitas:
        receitas.append(
            {
                "ID": receita[0],
                "Categoria": receita[1],
                "Título": receita[2],
                "Link": receita[3],
                "Dificuldade": receita[4],
                "Quantidade": receita[5],
                "Tempo": receita[6]
            }
        )

    return jsonify(receitas)


@app.route("/category", methods=["GET"])
def get_data_by_category():
    my_cursor.execute("SELECT DISTINCT Categoria FROM `receitas`;")
    category_all = my_cursor.fetchall()
    return jsonify(category_all)


@app.route("/data/<category>", methods=["GET"])
def view_for_category(category):
    my_cursor.execute(f"SELECT * FROM receitas WHERE Categoria='{category}';")
    view_category = my_cursor.fetchall()
    list_category = list()

    for categorys in view_category:
        list_category.append(
            {
                "ID": categorys[0],
                "Categoria": categorys[1],
                "Título": categorys[2],
                "Link": categorys[3],
                "Dificuldade": categorys[4],
                "Quantidade": categorys[5],
                "Tempo": categorys[6]
            }
        )

    return jsonify(list_category)


if __name__ == "__main__":
    app.run(debug=True)
