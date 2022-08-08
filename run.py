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


"""
Variables created to check proper connection with worksheets
"""
# stretch = SHEET.worksheet('stretch')
# data_stretch = stretch.get_all_values()
# print(data_stretch)

# strength = SHEET.worksheet('strength')
# data_strength = strength.get_all_values()
# print(data_strength)

# torsion = SHEET.worksheet('torsion')
# data_torsion = torsion.get_all_values()
# print(data_torsion)

# balance = SHEET.worksheet('balance')
# data_balance = balance.get_all_values()
# print(data_balance)

feedback = SHEET.worksheet('feedback')
data_feedback = feedback.get_all_values()
# print(data_feedback)


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

    all_stretches = []
    for ind in range(1, 4):
        all_col = stretch.col_values(ind)
        all_stretches.append(all_col[1:])

    name = all_stretches[0]
    instructions = all_stretches[1]
    benefits = all_stretches[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        print(Fore.GREEN + name)
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")

    return again_or_quit()


def strength_pose():
    """
    Function that displays the instructions
    to execute the strength poses
    and its benefits.
    """
    print("You chose 2\n")

    strength = SHEET.worksheet('strength')

    all_strengths = []
    for ind in range(1, 4):
        all_col = strength.col_values(ind)
        all_strengths.append(all_col[1:])

    name = all_strengths[0]
    instructions = all_strengths[1]
    benefits = all_strengths[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        print(Fore.GREEN + name)
        print(Fore.CYAN + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")

    return again_or_quit()


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

    return pose_type_choice()


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

    return pose_type_choice()


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
        pose_type_choice()
    elif again_quit == "n":
        print(Fore.GREEN + Style.BRIGHT + "\nSad to know that you")
        print("want to leave.\n")
        print("Please give a feedback, ")
        print("so we can now how much you enjoyed the app.\n")
        print(Fore.MAGENTA + "NAMASTE!" + "\U0001F64F\n")
        # leave_feedback()
    else:
        print()
        print(Fore.RED + "ERROR:" + Fore.RESET)
        print(f'You entered {Fore.RED + again_quit + Fore.RESET}.')
        print("You must type y or n.\n")
        return again_or_quit()


def main():
    """
    Main function that runs the applications functions
    """
    intro_click_pose()
    pose_type_choice()
    # again_or_quit()
    # leave_feedback()


main()
