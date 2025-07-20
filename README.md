
 # 🧪 Python Pytest Selenium Web UI Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Tested_with-Pytest-yellow?logo=pytest)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4-brightgreen?logo=selenium)](https://www.selenium.dev/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## 📌 About

This is a real-world Web UI Automation Framework built using **Python**, **Selenium 4**, and **Pytest** following the **Page Object Model (POM)** design.

It supports:

- Fixtures, parameterization, retry logic
- Screenshots on failure and logging
- HTML test reports
- Test data via Excel using `pandas` or `openpyxl`
- CI/CD ready for Azure Pipelines and GitHub Actions

---

## 📁 Folder Structure

```

.
├── tests/                  # Test cases
├── pages/                  # Page Object Model classes
├── utils/                  # Logger, data loader, helpers
├── test\_data/              # Excel or JSON data
├── reports/                # HTML reports and screenshots
├── conftest.py             # Pytest fixtures and config
├── requirements.txt        # Project dependencies
├── README.md               # Project overview

````

---

## 🚀 How to Run Tests

▶️ Run all tests with HTML report:


pytest -v --html=reports/result.html


▶️ Run in parallel (requires `pytest-xdist`):

pytest -v -n=2 --html=reports/result.html


---

## 🛠 Features

* ✅ Page Object Model (POM)
* ✅ Fixtures and parameterized testing
* ✅ Retry mechanism for flaky tests
* ✅ Screenshot + logging on failure
* ✅ HTML reports (pytest-html)
* ✅ Test data from Excel
* ✅ CI/CD integration ready

---

## 📦 Install Dependencies


pip install -r requirements.txt


---

## 🎯 Perfect For

* 🔹 SDET Interview Preparation (Google / Product-based Companies)
* 🔹 Web automation frameworks for real-world applications
* 🔹 Learning Pytest + Selenium in a structured way

---

## 🙋‍♂️ Author

Made with ☕, 🔥 & `pytest.mark.hustle` by [[Sharadrao Pawar](https://github.com/sharadraopawar)](https://github.com/sharadraopawar)





