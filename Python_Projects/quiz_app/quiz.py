class Question:
    """Models a single question entity, encapsulating its text, options, and answer."""
    def __init__(self, prompt, choices, explicit_answer):
        self.prompt = prompt
        self.choices = choices
        self.explicit_answer = explicit_answer

    def verify_answer(self, user_choice):
        """Compares user choice string directly with the encapsulated answer string."""
        return user_choice.strip().lower() == self.explicit_answer.strip().lower()


class QuizEngine:
    """Manages the operational lifecycle, score calculation, and state tracking of the quiz session."""
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.score = 0
        self.current_index = 0

    def contains_remaining_questions(self):
        """Boolean check to determine if elements still exist in the question collection."""
        return self.current_index < len(self.question_bank)

    def execute_next_question(self):
        """Extracts and steps through the upcoming item in the question array."""
        current_question = self.question_bank[self.current_index]
        self.current_index += 1
        
        print(f"\nQuestion {self.current_index}: {current_question.prompt}")
        for index, option in enumerate(current_question.choices, start=1):
            print(f"  {index}. {option}")
            
        while True:
            selection = input("\nSelect your response option index (1-4): ").strip()
            if selection in ["1", "2", "3", "4"]:
                # Map selected numerical choice directly to target text string
                selected_text = current_question.choices[int(selection) - 1]
                break
            print("[!] Invalid index validation choice. Select a value from 1 to 4.")

        if current_question.verify_answer(selected_text):
            print("[+] Evaluation: CORRECT.")
            self.score += 1
        else:
            print(f"[-] Evaluation: INCORRECT. True target: {current_question.explicit_answer}")

    def print_final_report(self):
        """Computes statistical final standings performance analytics metrics."""
        total = len(self.question_bank)
        percentage = (self.score / total) * 100 if total > 0 else 0
        
        print("\n" + "=" * 45)
        print("          QUIZ COMPILATION COMPLETE          ")
        print("=" * 45)
        print(f"Correct Answers Checked:  {self.score} / {total}")
        print(f"Final Score Scale:        {percentage:.2f}%")
        
        if percentage >= 80:
            print("Status Tier:             Elite System Proficiency")
        elif percentage >= 50:
            print("Status Tier:             Functional Operational Understanding")
        else:
            print("Status Tier:             System Performance Remediation Advised")
        print("=" * 45)


def main():
    """Initializes and builds objects to kick off execution inside Pydroid 3."""
    # Data layer setup: Instantiating specific items via the explicit model constructor
    raw_data = [
        Question(
            "Which built-in Python module leverages cryptographic secure pseudo-random numbers?",
            ["random", "secrets", "os", "hashlib"],
            "secrets"
        ),
        Question(
            "What type of error is raised if Python encounters an unexpected spacing structure?",
            ["IndexError", "ValueError", "IndentationError", "KeyError"],
            "IndentationError"
        ),
        Question(
            "What component of Python's 'ast' module helps analyze code blocks safely without running eval?",
            ["literal_eval", "parse", "dump", "walk"],
            "parse"
        )
    ]

    print("=" * 45)
    print("      OBJECT-ORIENTED COMPUTER SCIENCE QUIZ      ")
    print("=" * 45)
    
    # Initialize the engine orchestrator module by feeding it the structural objects bank
    quiz = QuizEngine(raw_data)
    
    while quiz.contains_remaining_questions():
        quiz.execute_next_question()
        
    quiz.print_final_report()


if __name__ == "__main__":
    main()
