from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
import os


def get_announcement_links(page):
    url = f"https://www.e-flux.com/v2/api/search?t[]=announcement&order=newest&page={page}"
    response = requests.get(url)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the announcement containers
    announcements = soup.find_all("div", class_="preview-search")

    # Extract links from each announcement
    links = [
        f"https://www.e-flux.com{announcement.find('a', class_='preview-search__title')['href']}"
        for announcement in announcements
    ]

    return links


def extract_eflux_id(link):
    return link.split("/")[4]


def scrape_announcement(link):
    # Make the request to the given link
    response = requests.get(link)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract title
    title_element = soup.find("h1", class_="article__header-title")
    title = title_element.get_text(strip=True) if title_element else "N/A"

    # Extract client (institution)
    client_element = soup.find("h2", class_="article__header-clients")
    client = client_element.get_text(strip=True) if client_element else "N/A"

    # Extract date
    date_element = soup.find("div", class_="announcement__date")
    date_str = date_element.get_text(strip=True) if date_element else "N/A"
    date = (
        datetime.strptime(date_str, "%B %d, %Y").isoformat()
        if date_str != "N/A"
        else "N/A"
    )

    # Extract categories
    category_elements = soup.find_all("h6", string="Category")
    categories = []
    for category_element in category_elements:
        for li in category_element.find_next_sibling("div").find_all("li"):
            categories.append(li.get_text(strip=True))

    # Extract subjects
    subjects = [
        sub.text
        for sub in soup.select('div.sidebar-list ul li span a[href*="search?s[]"]')
    ]

    # Extract participants
    participants_elements = soup.find_all("h6", string="Participants")
    participants = []
    for participants_element in participants_elements:
        for li in participants_element.find_next_sibling("div").find_all("li"):
            participants.append(li.get_text(strip=True))

    # Extract location and contact
    location_element = soup.find("div", class_="article__top-item")
    location = location_element.get_text(strip=True) if location_element else "N/A"

    # Extract description
    description_element = soup.find("div", class_="article__body")
    description = (
        description_element.get_text(strip=True) if description_element else "N/A"
    )

    # Extract images
    images = []
    image_elements = soup.find_all("img", class_="lazyimage")
    for img in image_elements:
        if "data-src" in img.attrs:
            images.append(img["data-src"])

    # Construct the data dictionary
    data = {
        "title": title,
        "link": link,
        "client": client,
        "posted_date": date,
        "categories": categories,
        "subjects": subjects,
        "participants": participants,
        "location": location,
        "description": description,
        "images": images,
    }

    return data


# Example usage:
link = "https://www.e-flux.com/announcements/617325/kenji-yanobebig-cat-bang/"
announcement_data = scrape_announcement(link)

# Save the data to a JSON file
with open("announcement_detail.json", "w", encoding="utf-8") as f:
    json.dump(announcement_data, f, indent=4, ensure_ascii=False)

print(announcement_data)


def scrape(start_page, end_page, output_folder):
    for page in range(start_page, end_page + 1):
        try:
            links = get_announcement_links(page)
            if not links:
                break

            for link in links:
                eflux_id = extract_eflux_id(link)
                announcement_data = scrape_announcement(link)
                announcement_data["eflux_id"] = eflux_id
                filename = os.path.join(output_folder, f"{eflux_id}.json")
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(announcement_data, f, indent=4, ensure_ascii=False)

        except requests.RequestException as e:
            print(f"Request error on page {page}: {e}")
            break
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break
