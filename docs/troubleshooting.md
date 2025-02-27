# 🛠️ Troubleshooting

While working with **MarkVault**, you may encounter some issues. This page provides guidance on common problems and their solutions to help you resolve them quickly. If you’re unable to find a solution here, feel free to open an issue or ask for help in the community.

---

## 🚨 Common Issues and Solutions

### 1. **GitHub Authentication Failure**
   **Problem:** You’re unable to authenticate with GitHub while pushing or pulling data.
   **Solution:**
   - Ensure that your GitHub credentials (username and personal access token) are correctly set in your `.env` file.
   - If you recently updated your GitHub token, make sure it’s reflected in the configuration.
   - Double-check the repository permissions to ensure your token has access to the repository.

   ```bash
   # Example .env configuration
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_personal_access_token
   ```

### 2. **Slow Push/Pull to GitHub**
   **Problem:** Pushing or pulling content to/from GitHub takes too long.
   **Solution:**
   - Check the size of the file you're trying to push. Large files or multiple commits can slow down the process.
   - Ensure your internet connection is stable and fast.
   - If the issue persists, try splitting large files into smaller chunks or simplifying your commit history.

### 3. **Missing or Incorrect File Format**
   **Problem:** The file format is not correctly saved (Markdown or JSON).
   **Solution:**
   - Make sure that the correct format is selected when writing a blog. You can select either Markdown (`.md`) or JSON (`.json`) in the blog creation form.
   - Check that the content is properly formatted in the specified format. For instance, a Markdown file should have a header with `#` before the title, and JSON should have properly structured key-value pairs.

### 4. **Error: `File Not Found` when Viewing Blogs**
   **Problem:** The blog data does not appear on the blog list page.
   **Solution:**
   - Ensure that the files are correctly pushed to the GitHub repository.
   - Check if the GitHub repository is public or private. If it’s private, ensure the GitHub token has the correct permissions to access it.
   - Verify that the `fetch_from_github` function in your application is correctly retrieving the files from GitHub.

### 5. **Server Error (500) on Blog Creation**
   **Problem:** A 500 error occurs when creating a new blog.
   **Solution:**
   - Check the server logs to identify any specific issues with your Django project, such as missing dependencies or configuration issues.
   - Ensure that all required packages and modules are installed correctly in your environment.
   - Review the `push_to_github` and `prepare_content_to_save` functions for any issues with file handling or GitHub API interactions.

---

## 🛠️ Debugging Steps

If the above solutions do not resolve your issue, try these debugging steps:

1. **Check Logs**: Always check the error logs for more detailed information. In Django, you can find logs in the terminal or the `logs/` directory (if configured).
2. **Update Dependencies**: Make sure all your project dependencies are up to date:
   ```bash
   pip install -r requirements.txt
   ```
3. **Rebuild the Virtual Environment**: If the issue is related to the environment, try rebuilding it:
   ```bash
   rm -rf venv/
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Test GitHub API Access**: Test GitHub access with a simple script to ensure your credentials are correct:
   ```python
   from github import Github

   g = Github("your_github_token")
   user = g.get_user()
   print(user.login)
   ```

---

## ❓ Need Further Assistance?

If you’ve followed the troubleshooting steps and are still facing issues, don’t hesitate to:

- Open an issue on the [GitHub Issues page](https://github.com/MehediMK/MarkVault/issues).
- Reach out to the community via [insert contact method, such as Discord, Slack, or email].
- Provide details of the error, including logs, steps to reproduce, and your system configuration.

We’re happy to assist you and help resolve any issues!

---

## 🔧 Related Resources

- [GitHub Documentation](https://docs.github.com/en/github)
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Markdown Guide](https://www.markdownguide.org/)
- [JSON Guide](https://www.json.org/json-en.html)