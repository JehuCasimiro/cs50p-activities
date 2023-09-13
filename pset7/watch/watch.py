import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # search the raw link from the iframe src & extract the link from the iframe
    if matches := re.search(r'(?:src=")(https?://(?:www\.)?youtube\.com/(?:embed)/([a-zA-Z0-9_-]+))(?:")', s, re.IGNORECASE):
        extracted_link = matches.group(1)
        # search for the link only and extract the youtube id
        if id := re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", extracted_link):
            extracted_id = id.group(1)

            # return the shorten url
            return f"https://youtu.be/{extracted_id}"

    return None

if __name__ == "__main__":
    main()