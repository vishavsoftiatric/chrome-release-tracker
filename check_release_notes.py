import requests
from bs4 import BeautifulSoup
 
URL = "https://developer.chrome.com/release-notes"
HEADERS = {"User-Agent": "Mozilla/5.0"}
 
def fetch_titles():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
titles = [h2.text.strip() for h2 in soup.select("h2")]
    return titles
 
def main():
    new_titles = fetch_titles()
    with open("latest.txt", "r") as file:
old_titles = file.read().splitlines()
 
    if new_titles != old_titles:
        print("🚨 New Chrome Release Detected:", new_titles[0])
        with open("latest.txt", "w") as file:
            file.write("\n".join(new_titles))
    else:
        print("✅ No update found.")
 
if __name__ == "__main__":
    try:
        open("latest.txt", "x").close()  # Create the file if it doesn't exist
    except FileExistsError:
        pass
    main()
