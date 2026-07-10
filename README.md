# Continuous Integration & Continuous Deployment (CI/CD) Pipeline

**This repository contains the automated pipeline solution developed for **Homework 15** within the i2i Academy training framework[cite: 15]. The project is designed strictly to demonstrate the core architecture of modern software delivery pipelines by isolating application logic, implementing automated testing tiers, and orchestrating cloud deployments.

---

## 🎯 Project Purpose
The primary purpose of this project is to eliminate manual intervention in the software development lifecycle by establishing a strict "gatekeeper" mechanism using GitHub Actions. 

By offloading validation tasks to an automated system, the pipeline guarantees that any code modification introduced to the repository is immediately checked for mathematical correctness and user interface stability before it can ever be considered ready for a production environment.

---

## 🔍 Scope of the Project
The scope of this project encompasses the creation of a lightweight telecom application environment and its corresponding multi-layered validation suite:

1. **Core Business Logic:** A dedicated module (`tax_calculator.py`) that implements internal functional computations, specifically simulating a 15% telecom tax calculation.
2. **Structural Unit Testing:** An isolated test script leveraging the `pytest` framework to verify that backend calculations return mathematically flawless results under designated inputs.
3. **Automated Frontend Validation:** A programmatic browser UI test utilizing `Selenium WebDriver` that launches a browser in the background to verify the availability and integrity of public web platforms.
4. **Cloud Orchestration:** A sequential workflow configuration (`ci-cd.yml`) that provisions virtualized environments and manages execution states dynamically based on the success of the test suites.

---

## 🛠️ Utilized Tools & Technological Stack

The automation architecture integrates the following industry-standard tools and technologies:

* **Python (v3.10):** The foundational programming language utilized to draft both the core application logic and the automated test configurations.
* **pytest Framework:** The test runner used to automatically scan the workspace, detect assertions, and report execution metrics.
* **Selenium WebDriver:** The browser automation framework used to programmatically simulate user interactions and validate frontend states.
* **Headless Chrome Browser:** A specialized configuration that allows Selenium to execute browser-based UI tests inside non-graphical cloud containers without requiring a physical monitor or graphical user interface (GUI).
* **GitHub Actions:** The native CI/CD platform used to ingest the workflow configuration, listen for repository events, and provision cloud runners.
* **Ubuntu Linux Runner:** The virtualized, clean operating system provided by the cloud infrastructure where the environment is constructed dynamically from scratch on every execution.

---

## ⚙️ Core Pipeline Architecture & Execution Workflow

The automated factory line is governed by the configuration file located at `.github/workflows/ci-cd.yml`. Upon detecting a code push event, the cloud runner executes the following sequential lifecycle stages:

```text
[Developer Push] ──> 🛠️ Stage A: Provisioning ──> 🧪 Stage B: Unit Test ──> 🌐 Stage C: UI Test ──> 🚀 Stage D: Deployment
