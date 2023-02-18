import requests

def search_internships(role):
    url = f"https://api.github.com/search/issues?q={role}+label:internship"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])
        if len(items) > 0:
            print(f"Found {len(items)} internships for {role}:")
            for item in items:
                print(f"- {item['html_url']}: {item['title']}")
        else:
            print(f"No internships found for {role}.")
    else:
        print(f"Failed to search internships: {response.status_code} {response.reason}")

if __name__ == "__main__":
    role = input("Enter the role you want to search internships for: ")
    search_internships(role)
