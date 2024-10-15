from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "Which sentence is grammatically correct?",
                "options": ["She go to school.", "She goes to school.", "She going to school.", "She gone to school."],
                "correct_answer": 2
            },
            {
                "question": "Choose the correct form of the verb: 'I ____ reading a book.'",
                "options": ["is", "am", "are", "were"],
                "correct_answer": 2
            },
            {
                "question": "What is the past tense of 'run'?",
                "options": ["runs", "runned", "ran", "running"],
                "correct_answer": 3
            },
            {
                "question": "Select the correct plural form of the word 'child'.",
                "options": ["childs", "child", "childes", "children"],
                "correct_answer": 4
            }
        ]

        self.layout = BoxLayout(orientation='vertical')

        self.question_label = Label(text=self.questions[self.current_question]["question"], font_size='20sp')
        self.layout.add_widget(self.question_label)

        self.option_buttons = []
        for i in range(4):
            btn = Button(text=self.questions[self.current_question]["options"][i], on_press=self.check_answer)
            self.layout.add_widget(btn)
            self.option_buttons.append(btn)

        self.result_label = Label(text="", font_size='18sp')
        self.layout.add_widget(self.result_label)

        return self.layout

    def check_answer(self, instance):
        correct_answer = self.questions[self.current_question]["correct_answer"]
        chosen_option = self.option_buttons.index(instance) + 1

        if chosen_option == correct_answer:
            self.score += 1
            self.result_label.text = "Correct!"
        else:
            self.result_label.text = f"Wrong! The correct answer is option {correct_answer}"

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_final_score()

    def update_question(self):
        self.question_label.text = self.questions[self.current_question]["question"]
        for i, btn in enumerate(self.option_buttons):
            btn.text = self.questions[self.current_question]["options"][i]
        self.result_label.text = ""

    def show_final_score(self):
        self.layout.clear_widgets()
        final_score_label = Label(text=f"Your final score is {self.score}/{len(self.questions)}", font_size='24sp')
        self.layout.add_widget(final_score_label)

if __name__ == '__main__':
    QuizApp().run()
