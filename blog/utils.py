import os
import json


def save_to_file(title, content, format_choice):
    directory = "blogs"
    os.makedirs(directory, exist_ok=True)  # Ensure directory exists

    if format_choice == "md":
        file_path = os.path.join(directory, f"{title.replace(' ', '_')}.md")
        with open(file_path, "w") as file:
            file.write(f"# {title}\n\n{content}")
    elif format_choice == "json":
        file_path = os.path.join(directory, f"{title.replace(' ', '_')}.json")
        with open(file_path, "w") as file:
            json.dump({"title": title, "content": content}, file)

    return file_path
