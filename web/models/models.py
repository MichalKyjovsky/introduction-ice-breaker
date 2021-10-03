

class Student:

    def __init__(self, first_name: str, last_name: str):
        super(Student, self).__init__()
        assert first_name and last_name
        self._first_name = first_name
        self._last_name = last_name


class Topic:

    def __init__(self, topic_name: str, topic_description: str):
        super(Topic, self).__init__()
        # Topic description may be empty as for initial version
        assert topic_name
        self._topic_name = topic_name
        self._topic_description = topic_description

