class QuizQuestion:
    def __init__(self, question, options, correct_index):
        self.question = question
        self.options = options
        self.correct_index = correct_index


class QuizManager:
    def __init__(self):
        self.current_question = QuizQuestion(
            "Столица Франции?",
            ["Берлин", "Мадрид", "Париж", "Рим", "Лондон"],
            2
        )

    def get_question(self):
        return self.current_question



