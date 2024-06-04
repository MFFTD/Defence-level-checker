# Defence-level-checker

Defence-level-checker is used alongside with RuneLite plugin "Clan List Exporter", which exports player names of a friends chat/clan chat -channel into a csv file.

## Requirements
- Python 3.6 or higher

## Usage

1. Export the friends chat/clan chat -channel names to a csv file using RuneLite plugin Clan List Exporter. The plugin is found in plugin hub.
2. Navigate to your `.runelite` folder and get the csv file(s) from `clanlistexports` folder and move them to this project's `csv_files` folder.
3. Run the Python script:
    ```bash
    cd path/to/project/folder
    python3 scrape.py
    ```

Replace `path/to/project/folder` with the actual path to your project folder.

