# Similarity of instrumental melodies
A method to calculate pairwise similarity of monophonic melodies in Python.

Next to the scripts, it provides a .pkl representation of a corpus of 18th century popular melodies from the [Historiography of Musical Form](http://historiography-of-musical-form-through-mir.sbg.ac.at/) project.

# To start
Make a file, name it `config.py`. Define the following variables:
- `FILENAME`: name of the file (extension .pkl) in which the melodies are saved (a pickled list of pandas dataframes)
- `DATAPATH`: (optional, when parsing from music-xml) the directory in which music_xmls are stored. The script will recursively go through the subdirectories.

# Parse music files
music-xmls can be parsed with the music_conversion.py script. To run, execute `python music_conversion.py`. This will go through all music-xml files (monophonic) in `DATA_PATH` and save them in a pickle file (.pkl) defined in `FILENAME`.

# Calculate similarities with the Cardinality Score
Download [Docker](https://www.docker.com/get-started). Use a terminal application to navigate to this directory, then run `docker-compose up`. This should go through all melodies saved in `FILENAME`, and will generate two .csv files, `output.csv` with all similarities, and `filtered_output.csv`, which contains all similarities above a given threshold (by default, set at 0.2). IF the script should crash at any point, the remaining files are saved in `remaining_dfs.pkl`, which can be used to restart the script from where it left off.