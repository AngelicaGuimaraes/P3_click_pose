"""
Import section
"""
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
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

    another_stretch = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n")
    print(Fore.RESET)

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
    print(Fore.MAGENTA + "ANOTHER STRENGTH POSE?\n")

    another_strength = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n")
    print(Fore.RESET)

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

    all_torsions = []
    for ind in range(1, 4):
        all_col = torsion.col_values(ind)
        all_torsions.append(all_col[1:])

    name = all_torsions[0]
    instructions = all_torsions[1]
    benefits = all_torsions[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        print(Fore.GREEN + name)
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")

    return again_or_quit()


def balance_pose():
    """
    Function that displays the instructions
    to execute the balance poses
    and its benefits.
    """
    print("You chose 4\n")

    balance = SHEET.worksheet('balance')

    all_balances = []
    for ind in range(1, 4):
        all_col = balance.col_values(ind)
        all_balances.append(all_col[1:])

    name = all_balances[0]
    instructions = all_balances[1]
    benefits = all_balances[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        print(Fore.GREEN + name)
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")

    return again_or_quit()


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
    again_quit = input(Fore.CYAN + "Type Yes 'y' or No 'n'\n" + Fore.RESET).lower()

    if again_quit == "y":
        print(Fore.MAGENTA + '\nEnter 1 to practice a STRETCH pose')
        print(Fore.MAGENTA + 'Enter 2 to practice a STRENGTH pose')
        print(Fore.MAGENTA + 'Enter 3 to practice a TORSION pose')
        print(Fore.MAGENTA + 'Enter 4 to practice a BALANCE pose\n')
        pose_type_choice()
    elif again_quit == "n":
        print(Fore.GREEN + Style.BRIGHT + "\nSad to know that you")
        print("want to leave.\n")
        print("Please give a feedback, ")
        print("so we can now how much you enjoyed the app.\n")
        print(Fore.MAGENTA + "NAMASTE!" + "\U0001F64F\n")
        leave_feedback()
    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + again_quit + Fore.RESET}.')
        print("You must type y or n.\n")
        return again_or_quit()


def leave_feedback():
    """
    Funtion for the user to leave a feedbacks
    """
    feedback = SHEET.worksheet('feedback')    
    user_feedback = int(input('Your rating: \n'))
    new_feedback = feedback.append(user_feedback)



    while True:
            try:
                user_feedback = int(input('Your rating: \n'))
                break
            except ValueError:
                print('You must enter a number between 1 and 5')
                continue
    if 1 <= user_feedback <= 5:
        user_feedback = int(user_feedback)
        total_rating = SHEET.worksheet('feedback').cell(cell.row, (cell.col - 2)).value
        total_rating = int(total_rating)
        new_rating = (user_feedback + total_rating)
        SHEET.worksheet('jokes').update_cell(cell.row, (cell.col - 2), new_rating)
        total_number_of_ratings = SHEET.worksheet('jokes').cell(cell.row, (cell.col - 1)).value
        total_number_of_ratings = int(total_number_of_ratings)
        new_total_ratings = (total_number_of_ratings + 1).SHEET.worksheet('jokes').update_cell(cell.row, (cell.col - 1), new_total_ratings)
        # pose_end()
    else:
        print('You must enter a number between 1 and 5')
        enter_rating()
    # enter_rating()


def main():
    """
    Main function that runs the applications functions
    """
    intro_click_pose()
    pose_type_choice()
    stretch = SHEET.worksheet('stretch')
    leave_feedback()


main()
