import os
import json


# def save_to_file(title, content, format_choice):
#     directory = "blogs"
#     os.makedirs(directory, exist_ok=True)  # Ensure directory exists

#     if format_choice == "md":
#         file_path = os.path.join(directory, f"{title.replace(' ', '_')}.md")
#         with open(file_path, "w") as file:
#             file.write(f"# {title}\n\n{content}")
#     elif format_choice == "json":
#         file_path = os.path.join(directory, f"{title.replace(' ', '_')}.json")
#         with open(file_path, "w") as file:
#             json.dump({"title": title, "content": content}, file)

#     return file_path


def prepare_content_to_save(title, content, format_choice):
    file_name = "draft.md"
    
    if format_choice == "md":
        file_name = f"{title.replace(' ', '_')}.md"        
        content = f"# {title}\n\n{content}"
            
    elif format_choice == "json":
        file_name = f"{title.replace(' ', '_')}.json"
        content = json.dumps({"title": title, "content": content}, indent = 4) 

    return file_name, content