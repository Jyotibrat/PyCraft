from datetime import datetime
import pytz

greetings = {
    "en": {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
    },
    "hi": {
        "morning": "सुप्रभात",
        "afternoon": "नमस्ते",
        "evening": "शुभ संध्या",
    }
}

def log_greeting(usr_nm, greeting):
    with open("greeting_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{datetime.now()}: {greeting} to {usr_nm}\n")

def greet_usr(usr_nm, lang="en", time_zn="Asia/Kolkata"):
    usr_time_zn = pytz.timezone(time_zn)
    current_time = datetime.now(usr_time_zn).time()

    if current_time.hour < 12:
        greeting = greetings[lang]["morning"]
    elif 12 <= current_time.hour < 18:
        greeting = greetings[lang]["afternoon"]
    else:
        greeting = greetings[lang]["evening"]

    print(f"{greeting}, {usr_nm}!")
    log_greeting(usr_nm, greeting)

def add_greeting_fixed(usr_names=None, new_greeting="Hello!"):
    if usr_names is None:
        usr_names = []
    usr_names.append(new_greeting)
    print(f"Usernames: {usr_names}")

def change_language():
    print("\nWhich language do you prefer?")
    print("1. English")
    print("2. Hindi")
    choice = input("Pick a number (1/2): ")

    if choice == "1":
        return "en"
    elif choice == "2":
        return "hi"
    else:
        print("Not a valid option. Sticking with English.")
        return "en"

def change_timezone():
    time_zn = input("What’s your timezone? (like Asia/Kolkata, Europe/London): ")
    try:
        pytz.timezone(time_zn)
        return time_zn
    except pytz.UnknownTimeZoneError:
        print("Hmm, that doesn't look like a valid timezone. Defaulting to Asia/Kolkata.")
        return "Asia/Kolkata"

def display_menu(usr_nm, lang, time_zn):
    while True:
        print("\nMenu:")
        print("1. Get Greeting")
        print("2. Change Language (English/Hindi)")
        print("3. Change Time Zone")
        print("4. Add Greeting with Mutable Default Argument")
        print("5. Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            greet_usr(usr_nm, lang, time_zn)
        elif choice == "2":
            lang = change_language()
        elif choice == "3":
            time_zn = change_timezone()
        elif choice == "4":
            print("\nDemonstrating fixed version:")
            add_greeting_fixed()
            add_greeting_fixed()
        elif choice == "5":
            cnfrm_exit = input("Are you sure you want to quit? (y/n): ")
            if cnfrm_exit.lower() == 'y':
                print("See you later!")
                break
            else:
                print("Continuing...")
        else:
            print("Oops! That's not a valid choice. Try again.")

def main():
    print("🌍 Hey there! Welcome to the Global Greetings Program!")
    usr_nm = input("What's your name? ")
    lang = "en"
    time_zn = "Asia/Kolkata"
    display_menu(usr_nm, lang, time_zn)

if __name__ == "__main__":
    main()