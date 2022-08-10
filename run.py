"""
Import section
"""
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style
from colorama import init
init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('click_pose')


def intro_click_pose():
    """
    Introduction of the application
    with greeting, instructions and purpose.
    """
    print(Style.BRIGHT)
    print(Fore.MAGENTA + 'Wellcome to Click Pose!\n')
    print(Fore.MAGENTA + 'Let the benefits of Yoga')
    print(Fore.MAGENTA + 'indulge your body, mind and soul!')
    print(Fore.CYAN + '\nEnter 1 to practice a STRETCH pose')
    print(Fore.CYAN + 'Enter 2 to practice a STRENGTH pose')
    print(Fore.CYAN + 'Enter 3 to practice a TORSION pose')
    print(Fore.CYAN + 'Enter 4 to practice a BALANCE pose\n')
    print(Fore.GREEN + "**Don't forget to leave your feedback")
    print(Fore.GREEN + "when finished" + "\U0001F64F\n")
    print(Fore.MAGENTA + "So, let's get started?")
    print(Fore.MAGENTA +
        "Unfold your yoga mat and take a deep breath!" + Fore.RESET)


def stretch_pose():
    """
    Function that displays the instructions
    to execute the stretch poses
    and its benefits.
    """
    print("You chose 1\n")

    stretch = SHEET.worksheet('stretch')

    stretch_list_1 = stretch.row_values(2)
    print(Fore.GREEN + stretch_list_1[0])
    print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + stretch_list_1[1])
    print()
    print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + stretch_list_1[2])
    print()

    return stretch_again_or_quit()


def stretch_again_or_quit():
    """
    Function to give the user another stretch pose
    """
    print(Fore.MAGENTA + "WOULD YOU LIKE TO PRACTICE")
    print(Fore.MAGENTA + "ANOTHER STRETCH POSE?\n")

    another_stretch = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n"
        + Fore.RESET).lower()
    print()

    if another_stretch == "y":
        stretch = SHEET.worksheet('stretch')

        stretch_list_2 = stretch.row_values(3)
        print(Fore.GREEN + stretch_list_2[0])
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + stretch_list_2[1])
        print()
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + stretch_list_2[2])
        print()

        return again_or_quit()

    elif another_stretch == "n":
        again_or_quit()

    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + another_stretch + Fore.RESET}.')
        print("You must type y or n.\n")
        return stretch_again_or_quit()


def strength_pose():
    """
    Function that displays the instructions
    to execute the strength poses
    and its benefits.
    """
    print("You chose 2\n")

    strength = SHEET.worksheet('strength')

    strength_list_1 = strength.row_values(2)
    print(Fore.GREEN + strength_list_1[0])
    print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + strength_list_1[1])
    print()
    print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + strength_list_1[2])
    print()

    return strength_again_or_quit()


def strength_again_or_quit():
    """
    Function to give the user another strength pose
    """

    print(Fore.MAGENTA + "WOULD YOU LIKE TO PRACTICE")
    print(Fore.MAGENTA + "ANOTHER STRENGTH POSE?")
    print(Fore.RESET)

    another_strength = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n"
        + Fore.RESET).lower()
    print()

    if another_strength == "y":
        strength = SHEET.worksheet('strength')

        strength_list_2 = strength.row_values(3)
        print(Fore.GREEN + strength_list_2[0])
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + strength_list_2[1])
        print()
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + strength_list_2[2])
        print()

        return again_or_quit()

    elif another_strength == "n":
        again_or_quit()

    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + another_strength + Fore.RESET}.')
        print("You must type y or n.\n")
        return strength_again_or_quit()


def torsion_pose():
    """
    Function that displays the instructions
    to execute the torsion poses
    and its benefits.
    """
    print("You chose 3\n")

    torsion = SHEET.worksheet('torsion')

    torsion_list_1 = torsion.row_values(2)
    print(Fore.GREEN + torsion_list_1[0])
    print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + torsion_list_1[1])
    print()
    print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + torsion_list_1[2])
    print()

    return torsion_again_or_quit()


def torsion_again_or_quit():
    """
    Function to give the user another torsion pose
    """

    print(Fore.MAGENTA + "WOULD YOU LIKE TO PRACTICE")
    print(Fore.MAGENTA + "ANOTHER TORSION POSE?\n")

    another_torsion = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n"
        + Fore.RESET).lower()
    print()

    if another_torsion == "y":
        torsion = SHEET.worksheet('torsion')

        torsion_list_2 = torsion.row_values(3)
        print(Fore.GREEN + torsion_list_2[0])
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + torsion_list_2[1])
        print()
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + torsion_list_2[2])
        print()

        return again_or_quit()

    elif another_torsion == "n":
        again_or_quit()

    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + another_torsion + Fore.RESET}.')
        print("You must type y or n.\n")
        return torsion_again_or_quit()


def balance_pose():
    """
    Function that displays the instructions
    to execute the balance poses
    and its benefits.
    """
    print("You chose 4\n")

    balance = SHEET.worksheet('balance')

    balance_list_1 = balance.row_values(2)
    print(Fore.GREEN + balance_list_1[0])
    print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + balance_list_1[1])
    print()
    print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + balance_list_1[2])
    print()

    return balance_again_or_quit()


def balance_again_or_quit():
    """
    Function to give the user another balance pose
    """

    print(Fore.MAGENTA + "WOULD YOU LIKE TO PRACTICE")
    print(Fore.MAGENTA + "ANOTHER BALANCE POSE?\n")

    another_balance = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n"
        + Fore.RESET).lower()
    print()

    if another_balance == "y":
        balance = SHEET.worksheet('balance')

        balance_list_2 = balance.row_values(3)
        print(Fore.GREEN + balance_list_2[0])
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + balance_list_2[1])
        print()
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + balance_list_2[2])
        print()

        return again_or_quit()

    elif another_balance == "n":
        again_or_quit()

    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + another_balance + Fore.RESET}.')
        print("You must type y or n.\n")
        return balance_again_or_quit()


def pose_type_choice():
    """
    Function that selects the user's choice
    """
    type_choice = input(Fore.CYAN + Style.BRIGHT +
        '\nPlease, make your choice (1, 2, 3 or 4)\n' + Fore.RESET)
    print(Fore.RESET)

    if type_choice == '1':
        stretch_pose()
    elif type_choice == '2':
        strength_pose()
    elif type_choice == '3':
        torsion_pose()
    elif type_choice == '4':
        balance_pose()
    else:
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + type_choice + Fore.RESET}.')
        print('You must choose 1, 2, 3, or 4\n')
        return pose_type_choice()


def again_or_quit():
    """
    User can chooe to practice som more
    or to quit the app.
    """
    print(Fore.MAGENTA + "DO YOU WANT TO PRACTICE SOME MORE YOGA?\n")
    again_quit = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n"
        + Fore.RESET).lower()

    if again_quit == "y":
        print(Fore.MAGENTA + '\nEnter 1 to practice a STRETCH pose')
        print(Fore.MAGENTA + 'Enter 2 to practice a STRENGTH pose')
        print(Fore.MAGENTA + 'Enter 3 to practice a TORSION pose')
        print(Fore.MAGENTA + 'Enter 4 to practice a BALANCE pose\n')
        pose_type_choice()
    elif again_quit == "n":
        print(Fore.GREEN + Style.BRIGHT + "\nSad to know that you")
        print("want to leave.\n")
        print("Please give a feedback, so we")
        print("can know how much you enjoyed the app.\n")
        get_user_feedback()
    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + again_quit + Fore.RESET}.')
        print("You must type y or n.\n")
        return again_or_quit()


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)


def get_user_feedback():
    """
    Fuction to get the feedback from the user
    """
    feedback_row = []
    print(Fore.GREEN + "Type a number between 1 and 5")
    print("Being '1' very bad and '5' excellent\n")

    user_feedback = input(Fore.CYAN
        + "Your rating here, please: \n" + Fore.RESET)
    print()
    if '1' <= user_feedback <= '5':
        print(Fore.MAGENTA + "Thanks for your feedback!")
        print("Hope to see you again!\n")
        print(Fore.MAGENTA + "NAMASTE!" + "\U0001F64F\n")
        feedback_row.insert(0, user_feedback)
    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + user_feedback + Fore.RESET}.')
        print("You must type a number between 1 and 5.\n")
        get_user_feedback()
    update_worksheet(feedback_row, 'feedback')
    feedback_row = []


def main():
    """
    Main function that runs the applications functions
    """
    intro_click_pose()
    pose_type_choice()


main()
