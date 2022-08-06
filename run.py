"""
Import section
"""
import random
import gspread
from google.oauth2.service_account import Credentials
from colorama import init
init()
from colorama import Fore

"""
Scope borrowed from Code Institute
From Love Sandwiche's Walkthru Project
"""

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

torsion = SHEET.worksheet('torsion')
data_torsion = torsion.get_all_values()
# print(data_torsion)

balance = SHEET.worksheet('balance')
data_balance = balance.get_all_values()
# print(data_balance)

feedback = SHEET.worksheet('feedback')
data_feedback = feedback.get_all_values()
# print(data_feedback)


def intro_click_pose():
    """
    Introduction of the application
    with greeting, instructions and purpose.
    """
    print(Fore.MAGENTA + 'Wellcome to Click Pose!\n')
    print(Fore.MAGENTA + 'Let the benefits of Yoga')
    print(Fore.MAGENTA + 'indulge your body, mind and soul!')
    print(Fore.BLUE + '\nEnter 1 to practice a STRETCH pose')
    print(Fore.BLUE + 'Enter 2 to practice a STRENGTH pose')
    print(Fore.BLUE + 'Enter 3 to practice a TORSION pose')
    print(Fore.BLUE + 'Enter 4 to practice a BALANCE pose\n')
    print(Fore.GREEN + "**Don't forget to leave your feedback")
    print(Fore.GREEN + "when finished" + "\U0001F64F\n")
    print(Fore.MAGENTA + "So, let's get started?")
    print(Fore.MAGENTA + "Unfold your yoga mat and take a deep breath!")
    print(Fore.RESET)


def random_stretch():
    """
    Function that displays randomly the
    instructions to execute the stretch poses
    and its benefits.
    """
    print("You chose 1\n")

    stretch = SHEET.worksheet('stretch')

    all_stretches = []
    for ind in range(1, 6):
        all_col = stretch.col_values(ind)
        all_stretches.append(all_col[1:])

    name = all_stretches[0]
    instructions = all_stretches[1]
    benefits = all_stretches[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        
        print(Fore.GREEN + name)
        print("\n")
        print(Fore.BLUE + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")
    return pose_type_choice()
    

def random_strength():
    """
    Function that displays randomly the
    instructions to execute the strength poses
    and its benefits.
    """
    print("You chose 2\n")

    strength = SHEET.worksheet('strength')

    all_strengths = []
    for ind in range(1, 6):
        all_col = strength.col_values(ind)
        all_strengths.append(all_col[1:])

    name = all_strengths[0]
    instructions = all_strengths[1]
    benefits = all_strengths[2]

    for (name, instructions, benefits) in zip(name, instructions, benefits):
        
        print(Fore.GREEN + name)
        print("\n")
        print(Fore.BLUE + "INSTRUCTIONS: " + Fore.RESET + instructions)
        print("\n")
        print(Fore.MAGENTA + "BENEFITS: " + Fore.RESET + benefits)
        print("\n")

    return pose_type_choice()


def pose_type_choice():
    """
    Function that selects the user's choice
    """
    type_choice = input(Fore.BLUE + 
        'Please, make your choice (1, 2, 3 or 4)\n' + Fore.RESET)
    print(Fore.RESET)
    if type_choice == '1':
        random_stretch()
    elif type_choice == '2':
        random_strength()
    elif type_choice == '3':
        display_random_torsion()
    elif type_choice == '4':
        display_random_balance()
    else:
        print(f'You entered {Fore.RED + type_choice + Fore.RESET}.')
        print('You must choose 1, 2, 3, or 4\n')
        return pose_type_choice()

def display_random_torsion():
    """
    Function that displays randomly the 
    instructions to execute the torsion poses.
    """

def display_random_balance():
    """
    Function that displays randomly the 
    instructions to execute the balance poses.
    """

def main():
    """
    Main function that runs the applications functions
    """
    intro_click_pose()
    pose_type_choice()


main()