from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

receita_df = pd.read_csv("receitas.csv", sep=";", encoding="utf-8")
category_all = receita_df["Categoria"].unique()


@app.route("/home", methods=["GET"])
def get_all_data():
    return jsonify(receita_df.to_dict(orient="records"))


@app.route("/category", methods=["GET"])
def get_data_category():
    return jsonify(category_all.tolist())


for category in category_all:
    endpoint_name = f"get_data_by_category_{category}"


    def get_data_by_category(category=category):
        data = receita_df[receita_df["Categoria"] == category].to_dict(orient="records")
        return jsonify(data)


    app.add_url_rule(f"/data/{category}", methods=["GET"], endpoint=endpoint_name, view_func=get_data_by_category)

if __name__ == "__main__":
    app.run(debug=True)
