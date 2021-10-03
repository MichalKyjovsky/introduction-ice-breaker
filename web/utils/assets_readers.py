import csv
from pathlib import Path


def get_student_dict() -> list:
    pom = []

    with open(f"{Path(__file__).parent.absolute()}/../assets/students.csv", mode="rt+") as f:
        reader = csv.reader(f)
        header = reader.__iter__().__next__()

        for line in reader:
            pom.append(list(zip(header, line)))

        return [{student[0][0]: student[0][1], student[1][0]: student[1][1]} for student in pom]


def get_topics_dict() -> list:
    pom = []

    # TODO: REMOVE CODE DUPLICATE
    with open(f"{Path(__file__).parent.absolute()}/../assets/topics.csv", mode="rt+") as f:
        reader = csv.reader(f)
        header = reader.__iter__().__next__()

        for line in reader:
            pom.append(list(zip(header, line)))

        return [{topic[0][0]: topic[0][1], topic[1][0]: topic[1][1]} for topic in pom]
