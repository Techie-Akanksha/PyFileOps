# 🗂️ PyFileOps – File Manager using Python & Streamlit

<div align="center">

### A modern CRUD File Manager built with Python and Streamlit

Manage files through a clean web interface without using the command line.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# 📖 About

**PyFileOps** is a beginner-friendly CRUD (Create, Read, Update, Delete) application built using **Python** and **Streamlit**.

The application allows users to manage text files through an interactive graphical interface instead of using terminal commands.

This project demonstrates practical Python programming concepts including file handling, session state management, secure file operations, and responsive web UI development.

---

# ✨ Features

## ➕ Create Files

* Create new text files
* Add custom content
* Prevent duplicate filenames
* Empty filename validation

---

## 📖 Read Files

* View all available files
* Read file contents
* Display file size
* Clean code-style content viewer

---

## ✏️ Update Files

Supports three update operations:

* Rename files
* Append new content
* Overwrite existing content

---

## 🗑 Delete Files

* Select any file
* Confirmation before deletion
* Prevent accidental file removal

---

## 📁 Workspace Explorer

The sidebar displays

* Available files
* File sizes
* Auto-refresh after operations

---

## 🎨 Modern User Interface

* Gradient header
* Custom CSS styling
* Responsive layout
* Interactive buttons
* Success/Error notifications
* Modern typography

---

<!--# 🖼️ Screenshots

> Add screenshots after uploading the project.

 Example:

```
screenshots/
    home.png
    create.png
    read.png
    update.png
    delete.png
```

```markdown
![Home](screenshots/home.png)

![Create](screenshots/create.png)

![Read](screenshots/read.png)

![Update](screenshots/update.png)

![Delete](screenshots/delete.png)


```
---
 -->
# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Techie-Akanksha/PyFileOps.git
```

Move into the project

```bash
cd PyFileOps
```

---

## Install Dependencies

```bash
pip install streamlit
```

or

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run main.py
```

Open your browser

```
http://localhost:8501
```

---

# 📂 Project Structure

```
PyFileOps/
│
├── main.py
├── fm_workspace/
├── README.md
└── requirements.txt
```

---

# ⚙️ Tech Stack

* Python
* Streamlit
* pathlib
* HTML
* CSS

---

# 🧠 Python Concepts Used

This project demonstrates practical usage of

* Functions
* CRUD Operations
* File Handling
* pathlib
* Session State
* Conditional Statements
* Lists
* String Handling
* Custom CSS Integration
* UTF-8 File Encoding

---

# 🔒 Security Features

✔ Prevents Path Traversal using

```python
Path(name).name
```

✔ Files are stored only inside

```
fm_workspace/
```

✔ Duplicate filenames are prevented

✔ Empty filenames are rejected

✔ Delete confirmation prevents accidental deletion

---

# 📌 How the Application Works

### Create

Create a new file inside the workspace with custom content.

### Read

Select a file and display its contents inside a styled code viewer.

### Update

Users can

* Rename
* Append new content
* Completely overwrite existing content

### Delete

Users must confirm before permanently deleting a file.

---

# 📈 Future Improvements

Some features planned for future versions:

* File Upload
* Download Files
* Search Files
* Dark Mode
* Folder Support
* File Preview
* Syntax Highlighting
* File Metadata
* Activity Log
* Copy File
* Move File

---

# 🎯 Learning Outcomes

While building this project, I learned

* Building web applications using Streamlit
* Python file handling
* CRUD implementation
* State management with Streamlit
* Secure file operations using pathlib
* Creating responsive user interfaces
* Organizing Python projects

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 👩‍💻 Author

### Akanksha

GitHub

https://github.com/Techie-Akanksha

LinkedIn

www.linkedin.com/in/akanksha-deshmukh-b97372337

---

# ⭐ If you like this project

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates me to build more Python projects and continue improving my skills.
