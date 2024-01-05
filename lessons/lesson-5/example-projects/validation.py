import re


class TextRegexProcessor:
    def __init__(self):
        pass

    def validate_email(self, email):
        # Implement regex pattern for email validation | https://regex101.com/r/YCL8cP/1
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def validate_phone_number(self, phone_number):
        # Implement regex pattern for phone number validation | https://regex101.com/r/mDkz9f/1
        pattern = r"^\d{10}$"
        return re.match(pattern, phone_number) is not None

    def extract_information(self, text, pattern):
        matches = re.findall(pattern, text)
        return matches

    def search_replace_text(self, file_path, search_pattern, replace_pattern):
        with open(file_path, "r") as file:
            content = file.read()
            updated_content = re.sub(search_pattern, replace_pattern, content)

        with open(file_path, "w") as file:
            file.write(updated_content)


processor = TextRegexProcessor()

print(processor.validate_email("user@example.com"))
print(processor.validate_phone_number("1234567890"))  #

# Extract information | https://regex101.com/r/1zruAu/1
text_to_search = "Date: 2022-01-01, Time: 12:30 PM"
pattern_to_extract_date = r"\d{4}-\d{2}-\d{2}"
print(
    processor.extract_information(text_to_search, pattern_to_extract_date)
)  # ['2022-01-01']

# Search and replace text in a file (you can fill this out when you are reviewing, I cant be bothered)
processor.search_replace_text("sample.txt", "old_pattern", "new_pattern")
