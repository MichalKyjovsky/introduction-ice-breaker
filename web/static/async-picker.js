document.getElementById("shuffle-btn").addEventListener("click", function () {
    if (student_database === undefined || student_database.students.length === 0) {
        get_random_student();
        get_random_topic();
    } else {
        let student = student_database.students.pop();
        let topics = topics_database.topics.pop();
        document.getElementById("student-name-box").textContent = student.first_name + " " + student.last_name;
        document.getElementById("topic-text-box").textContent = topics.topic_description;
    }
})

document.getElementById("shuffle-topics-btn").addEventListener("click", function () {
    if (topics_database === undefined || topics_database.topics.length === 0) {
        get_random_student();
        get_random_topic();
    } else {
        let topics = topics_database.topics.pop();
        document.getElementById("topic-text-box").textContent = topics.topic_description;
    }
})

let student_database = undefined;
let topics_database = undefined;

async function get_random_student() {
    fetch(`${window.origin}/random_student`)
        .then(response => response.json())
        .then(data => {
            student_database = data;
        })
}

async function get_random_topic() {
    fetch(`${window.origin}/random_topic`)
        .then(response => response.json())
        .then(data => {
            topics_database = data;
        })
}

