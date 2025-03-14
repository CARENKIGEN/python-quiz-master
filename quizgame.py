
import random
import time

def run_quiz():
    
    questions = [
        {
            "question": "What symbol is used for comments in Python?",
            "options": ["// comment", "/* comment */", "# comment", "-- comment"],
            "answer": 2  
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["String", "Integer", "Boolean", "Character"],
            "answer": 3
        },
        {
            "question": "How do you create a variable in Python?",
            "options": ["var name = value", "name := value", "name = value", "const name = value"],
            "answer": 2
        },
        {
            "question": "Which method is used to add an element to a list?",
            "options": ["add()", "append()", "insert()", "extend()"],
            "answer": 1
        },
        {
            "question": "What does the 'len()' function do?",
            "options": ["Checks if a list is empty", "Returns the length of an object", "Creates a new list", "Sorts a list"],
            "answer": 1
        }
    ]
    
    
    random.shuffle(questions)
    
    
    score = 0
    total_questions = len(questions)
    
    
    print("\n🎮 PYTHON QUIZ GAME 🎮")
    print("=" * 30)
    print("Test your Python knowledge!")
    print("=" * 30)
    
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}/{total_questions}:")
        print(q["question"])
        
        
        for j, option in enumerate(q["options"]):
            print(f"  {j+1}. {option}")
        
        
        while True:
            try:
                user_answer = int(input("\nYour answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
        
        
        if user_answer - 1 == q["answer"]:  # Convert 1-based to 0-based
            print("✅ Correct! Good job!")
            score += 1
        else:
            correct_option = q["options"][q["answer"]]
            print(f"❌ Wrong! The correct answer is: {correct_option}")
        
        
        time.sleep(1)
    
    
    print("\n" + "=" * 30)
    print(f"📊 FINAL SCORE: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"You got {percentage:.1f}% correct!")
    
    
    if percentage == 100:
        print("🏆 Perfect score! You're a Python master!")
    elif percentage >= 80:
        print("🌟 Great job! You know Python well!")
    elif percentage >= 60:
        print("👍 Good effort! Keep learning Python!")
    else:
        print("📚 Keep practicing! You'll get better with time!")
    
    return score, total_questions

def main():
    play_again = True
    
    while play_again:
        score, total = run_quiz()
        
        
        while True:
            again = input("\nWould you like to play again? (yes/no): ").lower()
            if again in ["yes", "y", "no", "n"]:
                break
            print("Please enter 'yes' or 'no'.")
        
        play_again = again in ["yes", "y"]
    
    print("\nThanks for playing the Python Quiz Game! Goodbye! 👋")

if __name__ == "__main__":
    main()