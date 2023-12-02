import requests
import zipfile
from pathlib import Path
import click

@click.command()
@click.argument('url')
@click.argument('target_folder') 
def download_and_extract_data(url, target_folder):
    """
    Download a zip file from the given URL and extract it to the specified folder.

    Parameters:
        - url (str): The URL of the zip file.
        - target_folder (str): The folder where the content should be extracted.

    Returns:
        None
    """
    request = requests.get(url)
    target_path = Path(target_folder)
    target_path.mkdir(parents=True, exist_ok=True)

    zip_file_path = target_path / Path(url.split("/")[-1])

    with open(zip_file_path, 'wb') as f:
        f.write(request.content)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(target_path)

    print(f"Data downloaded and extracted to {target_path}")

if __name__ == '__main__':
    download_and_extract_data()
    
# Use in terminal:
# python download_and_extract_data.py <url> <target_folder>

# Use in Jupyter:
# download data as zip and extract
#url = "https://archive.ics.uci.edu/dataset/186/wine+quality/wine+quality.zip"
#download_and_extract_data(url, "../data/raw")

#original code for download_and_extract_data(): 
# url = "https://archive.ics.uci.edu/dataset/186/wine+quality/wine+quality.zip"
# request = requests.get(url)
# with open("../data/raw/wine+quality.zip", 'wb') as f:
#     f.write(request.content)
# with zipfile.ZipFile("../data/raw/wine+quality.zip", 'r') as zip_ref:
#     zip_ref.extractall("../data/raw")