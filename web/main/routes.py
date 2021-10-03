from flask import render_template, url_for, redirect, jsonify, Blueprint
from ..utils.randomity import shuffle_students, shuffle_topics
from ..utils.assets_readers import get_student_dict, get_topics_dict

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
@main.route("/home", methods=["GET"])
def home():
    return render_template("main/main.html")


@main.route("/random_student", methods=["GET"])
def get_random_student():
    return jsonify(students=shuffle_students(get_student_dict()))


@main.route("/random_topic", methods=["GET"])
def get_random_topic():
    return jsonify(topics=shuffle_topics(get_topics_dict()))
