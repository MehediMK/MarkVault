# 🛠️ Installation Guide  

Welcome to the **MarkVault** installation guide! This step-by-step guide will help you set up **MarkVault** on your system and get started with managing blogs using GitHub.  

---

## 🚀 Prerequisites  

Before installing MarkVault, make sure you have the following:  

🔹 **Python 3.10+** installed on your system.  
🔹 **Git** installed for repository management.  
🔹 A **GitHub account** with a repository for storing blog posts.  
🔹 A **GitHub Personal Access Token (PAT)** with `repo` permissions.  
🔹 **pip** (Python package manager) installed.  

---

## 📌 Step 1: Clone the Repository  

To install MarkVault, start by cloning the GitHub repository:  

```bash
git clone https://github.com/MehediMK/MarkVault.git
cd MarkVault
```

---

## 📌 Step 2: Create a Virtual Environment  

To keep dependencies isolated, create a virtual environment:  

```bash
python -m venv venv
```

Activate the virtual environment:  

- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS:**  
  ```bash
  source venv/bin/activate
  ```

---

## 📌 Step 3: Install Dependencies  

Now, install the required dependencies:  

```bash
pip install -r requirements.txt
```

This will install Django, PyGitHub, and other necessary packages.  

---

## 📌 Step 4: Configure Environment Variables  

MarkVault requires a `.env` file to store GitHub credentials.  

1️⃣ Copy the sample configuration file:  

```bash
cp sample.env .env   # For Linux/macOS
copy sample.env .env  # For Windows
```

2️⃣ Open `.env` and update the following variables with your **GitHub credentials**:  

```ini
GITHUB_ACCESS_TOKEN=your_personal_access_token
GITHUB_REPO_OWNER=your_github_username
GITHUB_REPO_NAME=your_repository_name
```

---

## 📌 Step 5: Apply Migrations (Optional)  

If you plan to extend MarkVault with a database, run:  

```bash
python manage.py migrate
```

Since MarkVault currently does not use a database, this step is **not mandatory**.  

---

## 📌 Step 6: Run the Development Server  

Now, start the Django server:  

```bash
python manage.py runserver
```

Visit **`http://127.0.0.1:8000/`** in your browser to access MarkVault.  

---

## 🎯 Next Steps  

🎉 Congratulations! You have successfully installed MarkVault. Now, proceed to:  

➡️ [Configuration Guide](configuration.md) – Set up additional options.  
➡️ [Writing Blogs](usage.md) – Learn how to create and sync blog posts.  
➡️ [Troubleshooting Guide](troubleshooting.md) – Fix common installation issues.  

---

## 🆘 Need Help?  

If you encounter any issues during installation, check the [FAQs](faq.md) or open an issue in the [GitHub Repository](https://github.com/MehediMK/MarkVault/issues).  

🚀 **Start blogging with MarkVault today!**  
