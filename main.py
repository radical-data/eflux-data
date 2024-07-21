import os
from src.scrape import scrape

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def main():
    start_page = 0
    end_page = 5
    scrape(start_page, end_page, output_folder)


if __name__ == "__main__":
    main()
