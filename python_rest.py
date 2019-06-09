from flask import Flask, request
from deeppavlov.contrib.skills.similarity_matching_skill import SimilarityMatchingSkill

faq = SimilarityMatchingSkill(data_path="servs.csv",
                              x_col_name='Question',
                              y_col_name='Answer',
                              save_load_path='./model',
                              config_type='tfidf_autofaq',
                              edit_dict={},
                              train=True)
app = Flask(__name__)


@app.route("/search/<username>")
def search(username):
    answer = faq([username], [], [])

    if answer[1][0] < .3:
        return "Ну я же не Алиса"
    else:
        return answer[0][0]


if __name__ == '__main__':
    app.run(debug=True, port=31888)
