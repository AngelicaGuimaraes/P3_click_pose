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
stretch = SHEET.worksheet('stretch')
data_stretch = stretch.get_all_values()
# print(data_stretch)

strength = SHEET.worksheet('strength')
data_strength = strength.get_all_values()
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
    print(Fore.GREEN + "Don't forget to leave your feedback")
    print(Fore.GREEN + "when finished" + "\U0001F64F\n")
    
intro_click_pose()