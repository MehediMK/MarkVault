# ⚙️ Configuration Guide  

MarkVault allows you to configure essential settings to ensure smooth integration with GitHub and a seamless blogging experience. This guide will walk you through the necessary configuration steps.

---

## 📌 1. Environment Variables  

MarkVault relies on a `.env` file to securely store sensitive credentials and configuration values.  

### 🔹 Creating the `.env` File  

1️⃣ If you haven’t created the `.env` file yet, copy the sample configuration:  

```bash
cp sample.env .env   # For Linux/macOS
copy sample.env .env  # For Windows
```

2️⃣ Open the `.env` file in a text editor and update the necessary values.  

---

### 🔹 Required Environment Variables  

| Variable Name           | Description |
|-------------------------|-------------|
| `GITHUB_ACCESS_TOKEN`   | Your **GitHub Personal Access Token (PAT)** with `repo` permissions. |
| `GITHUB_REPO_OWNER`     | The **GitHub username** or organization name where the repository is hosted. |
| `GITHUB_REPO_NAME`      | The **repository name** where MarkVault will store blog posts. |

#### ✅ Example `.env` File:  

```ini
GITHUB_ACCESS_TOKEN=your_personal_access_token
GITHUB_REPO_OWNER=your_github_username
GITHUB_REPO_NAME=your_repository_name
```

⚠️ **Important:** Never share your `.env` file or commit it to GitHub.

---

## 📌 2. Configuring GitHub Access  

To enable MarkVault to push and fetch blog posts, ensure the following:  

✅ You have created a **GitHub Personal Access Token (PAT)**.  
✅ The token has **`repo` permissions** to read/write to your repository.  
✅ The repository is **public or private**, but your token must have access.  

---

## 📌 3. Changing File Format  

By default, MarkVault supports **Markdown (.md)** and **JSON (.json)** formats.  

### 📍 Modify Default File Format  

If you want to set a preferred format for blog posts, modify the `format_choice` option in `BlogForm` inside `forms.py`:  

```python
format_choice = forms.ChoiceField(
    choices=[('md', 'Markdown'), ('json', 'JSON')],
    widget=forms.RadioSelect,
    initial='md'  # Default format
)
```

🔹 Change `initial='json'` if you want JSON to be the default format.

---

## 📌 4. Setting Up Custom File Naming  

By default, MarkVault saves blog posts with the **title as the filename**, replacing spaces with underscores (`_`).  

If you need a different naming convention, modify the `prepare_content_to_save` function in `utils.py`:  

```python
file_name = f"{title.replace(' ', '-').lower()}.{format_choice}"
```

🔹 This will save files using hyphens (`-`) instead of underscores (`_`).  

---

## 📌 5. Running MarkVault on a Different Port  

By default, MarkVault runs on `http://127.0.0.1:8000/`. To change the port, use:  

```bash
python manage.py runserver 8080
```

🔹 This will start the server on `http://127.0.0.1:8080/`.  

---

## 🎯 Next Steps  

➡️ [Writing Blogs](usage.md) – Learn how to create and sync blog posts.  
➡️ [FAQs](faq.md) – Find answers to common configuration issues.  
➡️ [Troubleshooting](troubleshooting.md) – Debug potential errors.  

---

## 🆘 Need Help?  

If you run into any issues, check our [GitHub Issues](https://github.com/MehediMK/MarkVault/issues) or reach out in the **Discussions** section.  

🚀 **You're now ready to configure MarkVault and start blogging!** 
