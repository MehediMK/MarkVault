### **Guidelines for Contributing to MarkVault**

Welcome, and thank you for considering contributing to **MarkVault**! Follow the steps below to make your contributions smooth and efficient.

---

#### **1. Prerequisites**
Before you start contributing:
- Ensure you have Python and Django installed.
- Familiarize yourself with Git and GitHub.
- Clone the repository:
  ```bash
  git clone https://github.com/MehediMK/MarkVault.git
  cd MarkVault
  ```

---

#### **2. Setting Up the Development Environment**
1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the server** to test the project:
   ```bash
   python manage.py runserver
   ```

---

#### **3. Contribution Workflow**
Follow the steps below to contribute your changes:

1. **Fork the Repository**:
   - Visit the repository [MarkVault](https://github.com/MehediMK/MarkVault.git) and click the "Fork" button.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/<your-username>/MarkVault.git
   cd MarkVault
   ```

3. **Create a New Branch**:
   - Always create a new branch for your changes to keep the `main` branch clean.
   ```bash
   git checkout -b feature/<your-feature-name>
   ```
   Example:
   ```bash
   git checkout -b feature/add-preview-functionality
   ```

4. **Make Your Changes**:
   - Write clean and modular code.
   - Follow the [PEP 8](https://peps.python.org/pep-0008/) coding style for Python.
   - Test your changes thoroughly before committing.

5. **Commit Your Changes**:
   - Use meaningful commit messages to describe what you've done.
   ```bash
   git add .
   git commit -m "Added preview functionality for blog creation"
   ```

6. **Push Your Changes**:
   ```bash
   git push origin feature/<your-feature-name>
   ```

7. **Open a Pull Request (PR)**:
   - Go to the original repository: https://github.com/MehediMK/MarkVault.git
   - Click on the "Pull Requests" tab and click "New Pull Request."
   - Select your branch and submit your pull request with a clear description.

---

#### **4. Code of Conduct**
By participating in this project, you agree to uphold the following:
- Be respectful and kind to others.
- Provide constructive feedback in code reviews.
- Ensure your contributions are free from plagiarism or copyright violations.

---

#### **5. Areas You Can Contribute**
Here are some ways you can contribute to MarkVault:
- **Bug Fixes**: Identify and fix bugs in the application.
- **Feature Enhancements**: Add new features or improve existing ones (e.g., UI improvements, Markdown rendering).
- **Documentation**: Improve the `README.md` file, add tutorials, or create guides.
- **Testing**: Add unit tests or improve test coverage for critical functionalities.
- **Refactoring**: Optimize the code for better performance and readability.

## Branch Protection Rules

To ensure a stable and secure codebase, the following branch protection rules are enforced:

### `main` Branch
- All changes must be submitted via pull requests.
- At least one review is required before merging.
- All status checks must pass.
- Direct pushes and force pushes are not allowed.
- Branch deletion is prohibited.

### `feature/*` Branches
- Pull requests are required for merging into `main`.
- Force pushes are allowed for development flexibility.
- Developers have write access to their feature branches.

If you encounter issues with these rules, please contact the repository maintainers.

---

#### **6. Code Style and Standards**
- Follow Python’s [PEP 8](https://peps.python.org/pep-0008/) guidelines.
- Use meaningful variable and function names.
- Add comments where necessary to explain complex code.
- Include docstrings for all methods and functions.
- Avoid hardcoding values; use environment variables or settings.

---

#### **7. Testing Your Changes**
- Write test cases for any new feature or bug fix.
- Run tests locally:
  ```bash
  python manage.py test
  ```

---

#### **8. Communication and Support**
If you have any questions or need clarification:
- Create an issue on GitHub.
- Add a detailed description of the issue or your feature request.
- Label your issue appropriately (e.g., `bug`, `enhancement`, `documentation`).

---

#### **9. Licensing**
By contributing to this project, you agree that your contributions will be licensed under the same license as the repository (include the license type here, e.g., MIT License).

---

#### **10. Thank You!**
Thank you for your interest in contributing to MarkVault! Your effort helps make this project better for everyone.
