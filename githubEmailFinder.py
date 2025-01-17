#!/usr/bin/env python3

#Python libraries
import requests
from tabulate import tabulate

#Color setup
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def checkGithubAPIStatut():
	"""
	This function check GitHub API statut : ONLINE / OFFLINE.
	"""
	response = requests.get('https://api.github.com')
	if response.status_code == 200:
		print("GitHub API is " + f"{bcolors.OKGREEN}{bcolors.BOLD}ONLINE{bcolors.ENDC}")
	else:
		print("GitHub API is " + f"{bcolors.FAIL}{bcolors.BOLD}OFFLINE{bcolors.ENDC}")

def checkGithubAPI():
	"""
	This function allows to search for the potential presence of mail in the public events pushed by your target on Github.
	"""
	#Looking for input from user and requests to the Github API without authentication
	AccountName = input("Please give me a github username: ")
	print("Looking for email(s) for the following github account: https://github.com/"+str(AccountName))
	response = requests.get('https://api.github.com/users/'+str(AccountName)+'/events/public')
	#Search for the email in the answer
	findEmailField = set(zip([email['author']['email'] for item in response.json() if item['payload'].get('commits')!=None for email in item['payload'].get('commits')], [username['author']['name'] for item in response.json() if item['payload'].get('commits')!=None for username in item['payload'].get('commits')]))
	my_list = list(set(findEmailField))
	if not my_list:
		print("No emails found")
	else:
		print("The email of your target can possibly be found in the list below: ")
		print(tabulate(my_list, headers = ['Email', 'Username']))

# Entry point of the script
def main():
	checkGithubAPIStatut()
	checkGithubAPI()

if __name__ == '__main__':
	main()
