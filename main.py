from tkinter import *
import random

DARK_GREY = "#272727"
# set the amount of time here 
TIME = 60

# opens word_list.txt reads file splits string into words, and creates list
with open("words_list.txt", mode="r", encoding="UTF-8") as file:
    words_in_file = file.read()
    LIST_OF_WORDS = words_in_file.split()


def countdown(time_left, chosen_words):

    # Update the time left and display it
    timer.config(text=str(time_left))

    # If time left is greater than 0, call countdown again after 1000ms (1 second)
    if time_left > 0:
        window.after(1000, countdown, time_left - 1, chosen_words)
    else:
        # Display "Time's up!" when the countdown finishes and applies changes to UI!
        timer.config(text="Time's up!")
        User_text_Entry.config(state="disabled")
        start_button.config(state="normal", width=120)
        text_for_user_to_type.config(highlightbackground="white")

        # Convert lists to sets and find the intersection(common items)
        user_typed_words = User_text_Entry.get()
        words_from_user = user_typed_words.split()

        # Find the intersection (common items)
        set_user = set(words_from_user)
        set_list_of_words = set(chosen_words)
        matching_correct_words_list = set_user & set_list_of_words
        correct_words_per_minute = len(matching_correct_words_list)

        # finds incorrectly spelt words (words that don't match set_list_of_words)
        misspelled_list = list(set(set_user) - set(set_list_of_words))

        # displays words per minute
        score.config(text=f"You typed words {correct_words_per_minute} per minute.", font=("Arial", 18, "bold"))
        score.pack()

        # if any incorrect words displays them
        if len(misspelled_list) > 0:
            # Join the words in the misspelled list into a string without square brackets
            misspelled_words_str = " ".join(misspelled_list)
            misspelled_words.config(text=f"misspelt words: {misspelled_words_str}")
            misspelled_words.pack()


def start(TIME):
    # configure widget to a functional state
    User_text_Entry.config(state="normal", width=140)

    # clears text in user entry field
    User_text_Entry.delete(0, END)

    #
    score.config(text="")

    # start_button disabled
    start_button.config(state="disabled", width=120)

    # change border to green when timer has started
    text_for_user_to_type.config(highlightbackground="green")

    # select new-words for test
    chosen_words = random.sample(LIST_OF_WORDS, 150)

    # display's new-words in the label widget for user to copy
    text_for_user_to_type.config(text=" ".join(chosen_words), foreground="white", font=("Arial", 15, "normal"), wraplength=675)

    # clear misspelled text
    misspelled_words.config(text="")

    # calls countdown timer
    countdown(TIME, chosen_words)


# creates UI for app
window = Tk()
window.title("Typing Speed Test")
window.geometry("1200x750")
window.config(bg=DARK_GREY)
window.iconbitmap('stopwatch-fill.ico')

# title
title = Label(text="Typing Speed Test", foreground="green", bg=DARK_GREY, font=("Arial", 35, "bold"), pady=20)
title.pack()

# timer label changes when button pressed to display time remaining
timer = Label(text="Are you ready?", foreground="white", bg=DARK_GREY, font=("Arial", 30, "bold"), pady=20)
timer.pack()

# displays words per minute label after function(timer) is completed
score = Label(text="score:", foreground="white", bg=DARK_GREY, font=("Arial", 28, "bold"), pady=15)

# displays text for user to type/copy
text_for_user_to_type = Label(height=15, width=75, bd=5, highlightbackground="white", highlightthickness=2, bg="black", text="press the start button!", fg="white")
text_for_user_to_type.pack()

# Entry field for user
User_text_Entry = Entry(width=88, justify='center')
User_text_Entry.pack(pady=10)
User_text_Entry.config(state="disabled")

# start button triggers Start function which triggers countdown
start_button = Button(text="Start timer", command=lambda: start(TIME), width=75, bg="green", fg="white")
start_button.pack()

# displays misspelled words
misspelled_words = Label(text="", foreground="red", bg=DARK_GREY, font=("Arial", 18, "bold"))

window.mainloop()
