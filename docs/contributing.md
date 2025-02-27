# 🤝 Contributing to MarkVault

Thank you for considering contributing to **MarkVault**! We welcome contributions from developers of all skill levels and are excited to have you involved in the project. Whether you’re fixing a bug, adding a feature, or improving the documentation, we appreciate your help in making MarkVault a better project for everyone.

This guide will walk you through how to contribute to MarkVault. Please follow these guidelines to ensure a smooth and productive collaboration.

---

## 🎯 How to Contribute

### 1. **Fork the Repository**

Start by forking the **MarkVault** repository to your own GitHub account. This allows you to freely make changes and experiment without affecting the original codebase.

1. Go to the [MarkVault GitHub Repository](https://github.com/MehediMK/MarkVault).
2. Click on the **Fork** button at the top right corner of the page.
3. Select your GitHub account to create a fork of the project.

---

### 2. **Clone Your Fork**

Clone your forked repository to your local machine to start working on the project:

```bash
git clone https://github.com/<your-username>/MarkVault.git
```

Replace `<your-username>` with your GitHub username.

---

### 3. **Create a New Branch**

It’s essential to work on a new branch rather than directly on the `main` branch. This helps keep the codebase clean and allows for easier collaboration.

1. Navigate to the project directory:
   
   ```bash
   cd MarkVault
   ```

2. Create a new branch:

   ```bash
   git checkout -b feature/<your-feature-name>
   ```

   Replace `<your-feature-name>` with a descriptive name for your feature or bug fix.

---

### 4. **Make Your Changes**

Now, make your changes to the code, whether it’s fixing a bug, adding a feature, or improving documentation.

- **Code Changes:** Write clean and efficient code that follows the existing style and conventions used in the project. Make sure your code passes the existing tests (if applicable) and doesn’t break the build.
- **Documentation:** Update documentation files as needed to reflect the changes or provide additional context for users.

---

### 5. **Test Your Changes**

If you’ve made code changes, ensure they are working as expected:

- Run any existing tests.
- Add new tests if you’ve added features or fixed bugs that require them.
- Ensure the application works as intended by running it locally.

---

### 6. **Commit Your Changes**

After making your changes, commit them to your branch with a meaningful commit message:

```bash
git add .
git commit -m "Description of the changes you made"
```

Be sure to follow the standard commit message format:  
`<type>: <short description>`

Example:
```bash
git commit -m "feat: add new blog format support"
```

---

### 7. **Push Your Changes**

Push your changes to your forked repository on GitHub:

```bash
git push origin feature/<your-feature-name>
```

---

### 8. **Create a Pull Request**

Once your changes are pushed to GitHub, it’s time to open a pull request (PR).

1. Go to the [MarkVault GitHub Repository](https://github.com/MehediMK/MarkVault).
2. You should see an option to create a pull request from your recently pushed branch.
3. Fill in the PR description with a summary of the changes you made, why they are important, and any additional information.
4. Click **Create Pull Request**.

---

## 📝 PR Review Process

Once your PR is submitted, it will be reviewed by the maintainers. They may ask you to make further changes before merging the PR. Be patient during the review process and make sure to respond to feedback.

---

## 🔄 Syncing Your Fork

If you’ve been working on a feature for a while and the original repository has had changes (commits to the `main` branch), you may need to sync your fork with the latest updates.

To sync your fork, follow these steps:

1. Add the original repository as an upstream remote:

   ```bash
   git remote add upstream https://github.com/MehediMK/MarkVault.git
   ```

2. Fetch the latest changes from the original repository:

   ```bash
   git fetch upstream
   ```

3. Merge the changes into your local branch:

   ```bash
   git checkout main
   git merge upstream/main
   ```

4. Push the updates to your fork:

   ```bash
   git push origin main
   ```

---

## 👥 Communication

Effective communication is key to a successful collaboration. Whether you’re opening an issue, making a PR, or simply discussing an idea, please:

- Be respectful and constructive.
- Provide clear explanations for the changes you propose.
- If you’re reporting a bug or requesting a feature, give as much detail as possible to help us understand the problem or the enhancement.

---

## 📜 Code of Conduct

By contributing to MarkVault, you agree to follow our [Code of Conduct](code_of_conduct.md). We aim to foster a welcoming and inclusive community, where everyone can contribute and feel valued.

---

## ⚙️ Common Contribution Types

Here are a few common types of contributions we welcome:

### Bug Fixes
- Fix any issues or bugs found in the codebase.
- Write tests to ensure the bug is resolved.
- Help improve stability and performance.

### New Features
- Add new functionality that improves the user experience.
- Follow the project's coding standards and guidelines.
- Consider including documentation and tests for your feature.

### Documentation
- Improve the clarity of existing documentation.
- Add missing documentation for features, settings, or installation instructions.

### Code Quality
- Refactor existing code to improve readability and maintainability.
- Remove unnecessary code or redundant logic.

---

## 🙋‍♂️ Need Help?

If you have any questions or need help with contributing, don’t hesitate to reach out! You can ask for help on:

- **GitHub Issues:** Open a new issue and ask for assistance.
- **GitHub Discussions:** Join discussions on GitHub to talk to other contributors and users.
- **Community:** Feel free to reach out to us via email or the social channels listed on the [Contact page](contact.md).

---

## 🏆 Thank You for Contributing!

Your contribution is greatly appreciated, and we thank you for being part of the MarkVault project. Whether you’re fixing bugs, adding features, or improving documentation, every bit helps!