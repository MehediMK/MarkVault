# ❓ Frequently Asked Questions (FAQs)

Welcome to the MarkVault FAQ section! Here, we answer some of the most commonly asked questions about using MarkVault. If you can’t find the answer you’re looking for, feel free to reach out to us.

---

## 💡 General Questions  

### 1. **What is MarkVault?**  

**MarkVault** is an open-source blogging platform that allows you to write, manage, and publish blog posts directly to your GitHub repository. It supports saving blogs in either Markdown or JSON formats and offers a simple interface for blog creation.

---

## 📝 Getting Started  

### 2. **How do I create a new blog post?**  

1. Navigate to the **Blog Creation Page** on your MarkVault site.  
2. Fill in the **Title**, **Content**, and select the desired **Format (Markdown/JSON)**.  
3. Click **Submit**, and the blog will be pushed to your GitHub repository.  

For more details, see the [Writing Blogs](usage.md) section.

---

### 3. **Can I edit or delete a blog post?**  

Currently, MarkVault does not support editing or deleting blogs from the UI. To edit or delete a blog:

1. Visit your GitHub repository.  
2. Locate the desired blog file (Markdown or JSON format).  
3. Edit the file using GitHub's editor, or delete it entirely.  

We plan to add editing and deletion features in future releases.

---

## 🔧 Configuration and Setup  

### 4. **How do I configure MarkVault to work with my GitHub repository?**  

MarkVault uses your GitHub credentials to push blogs directly to your repository. To configure it:

1. Set up the GitHub credentials in your `.env` file.
2. Add the repository URL where blogs will be pushed.
3. Ensure proper authentication and access tokens are configured.

For detailed instructions, check the [Configuration](configuration.md) page.

---

### 5. **Do I need to install anything before using MarkVault?**  

Yes! Before using MarkVault, ensure you have:

- Python 3.10 or higher installed.  
- A GitHub account and a repository for storing your blogs.  
- Dependencies installed via the `requirements.txt` file by running `pip install -r requirements.txt`.  

Once the environment is set up, you can start writing and managing your blogs.

---

## 🧑‍💻 Contributing  

### 6. **How can I contribute to MarkVault?**  

We welcome contributions to improve MarkVault! Here’s how you can get started:

1. Fork the project repository.
2. Make your changes or enhancements.
3. Submit a Pull Request to have your changes reviewed and merged.

For more detailed guidelines, check the [Contributing](contributing.md) page.

---

## 🚨 Troubleshooting  

### 7. **My blog is not appearing on the site. What do I do?**  

This can happen if there’s a delay in pushing to GitHub or if there’s an issue with your GitHub credentials.

**Troubleshooting steps:**

1. Check your GitHub repository to ensure the blog file has been pushed correctly.
2. Review the logs in your console for any error messages related to GitHub authentication.
3. Ensure the GitHub token is correctly set in the `.env` file.

If the issue persists, refer to the [Troubleshooting](troubleshooting.md) section.

---

### 8. **How do I fix a GitHub authentication error?**  

If you're getting authentication errors:

1. Verify that your GitHub access token is valid and has proper permissions.  
2. Check that the token is properly configured in the `.env` file.  
3. Make sure your GitHub repository is accessible and public or you have the necessary permissions.

For more details, check the [Configuration](configuration.md) page.

---

## 🔄 Updates and Future Features  

### 9. **Are there any upcoming features for MarkVault?**  

Yes! Some of the planned features for future releases include:

- Direct in-app editing and deletion of blogs.  
- User authentication for different roles (admin, author).  
- Support for other content formats like HTML or PDF.  
- A better UI for blog management.  

We’re constantly improving MarkVault, so check back for updates!

---

### 10. **Where can I find the latest release notes?**  

You can find the latest release notes and version history in the [GitHub Releases section](https://github.com/MehediMK/MarkVault/releases).

---

## 🔧 Still Need Help?

If you didn’t find the answer to your question here, feel free to contact us:

- Visit the [GitHub Issues page](https://github.com/MehediMK/MarkVault/issues) to report problems or ask questions.
- Join the **Discussions** section on GitHub to talk to the community and get help.

---

## 🚀 Start Using MarkVault Today!  

Once you have everything set up, you’re ready to create and manage your blogs! Explore the features, get involved, and contribute to the open-source community.