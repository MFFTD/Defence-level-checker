import os
import csv
import glob
import requests

class DefenceLevelChecker:
    def __init__(self):
        self.count: int = 0

    def get_current_folder_path(self) -> str:
        return os.getcwd()

    def construct_csv_folder_path(self, current_working_directory_path: str) -> str:
        return os.path.join(current_working_directory_path, 'csv_folder')

    def construct_csv_files_path(self, csv_folder_path: str) -> str:
        return os.path.join(csv_folder_path, '*')

    def sort_files_by_creation_time(self, csv_files_path: str) -> list[str]:
        return sorted(glob.iglob(csv_files_path), key=os.path.getctime, reverse=True)

    def get_latest_file(self, sorted_files: list[str]) -> str:
        return sorted_files[0]

    def read_csv(self, latest_file: str) -> list[str]:
        with open(latest_file, newline='') as csvfile:
            usernames = list(csv.reader(csvfile))
            usernames: str = usernames[0]
            if usernames[-1] == '':
                usernames.pop()
        return usernames

    def scrape(self, usernames: list[str]) -> list[str]:
        for username in usernames:
            request_response = requests.get(f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={username}')
            rows = request_response.text.split('\n')
            self.check_defence_levels(username, rows)

    def check_defence_levels(self, username: str, rows: list[str]) -> None:
        if len(rows) >= 3: # 3rd row contains the data for defence
            defence_row = rows[2] # index for the defence data row
            defence_values = defence_row.split(',') # the row contains rank, level, total xp
            if len(defence_values) >= 2:
                defence_level = int(defence_values[1]) # get the element that contains defence level
                if defence_level > 25:
                    self.count += 1
                    print(f'{self.count}. Defence level for "{username}": {defence_level}.')

    def main(self) -> None:
        current_working_directory_path = self.get_current_folder_path()
        csv_folder_path = self.construct_csv_folder_path(current_working_directory_path)
        csv_files_path = self.construct_csv_files_path(csv_folder_path)
        sorted_files = self.sort_files_by_creation_time(csv_files_path)
        latest_file = self.get_latest_file(sorted_files)
        usernames = self.read_csv(latest_file)
        self.scrape(usernames)

if __name__ == "__main__":
    checker = DefenceLevelChecker()
    checker.main()
    