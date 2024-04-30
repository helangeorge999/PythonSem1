# Define a dictionary with questions as keys and answers as values
qa_dict = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the symbol for water?": "H2O",
    "What year did the Titanic sink?": "1912",
    "Who is the pro player of free fire?": "Helan George Adhikari"
}

# Function to ask a question and check the answer
def ask_question(question):
    # Check if the question is in the dictionary
    if question in qa_dict:
        # Print the question
        print(question)
        # Get the answer from the dictionary
        answer = qa_dict[question]
        # Ask the user for their answer
        user_answer = input("Your answer: ")
        # Check if the user's answer matches the correct answer
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", answer)
    else:
        print("Sorry, I don't know the answer to that question.")

# Ask the user for a question
user_question = input("Ask me a question: ")
# Call the function to ask the question and check the answer
ask_question(user_question)
