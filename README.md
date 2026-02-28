# Python Learning & Development Repository

A comprehensive repository containing Python learning materials, assignments, and practical applications. This repository includes foundational Python concepts, object-oriented programming exercises, module development, and web applications using Streamlit.

---

## 📁 Repository Structure

```
PYTHON/
├── PY_Basics/                          # Python fundamentals
├── PY_Assignments/                     # Core assignment projects
│   ├── Modules_Assignments/            # Module & package development
│   └── [Assignment notebooks]
├── Stremlit_Assignment/                # Web application using Streamlit
├── app.py                              # Main application entry point
├── Requirements.txt                    # Python dependencies
└── README.md                          # This file
```

---

## 📚 Folder & File Documentation

### 🎓 **PY_Basics/** - Python Fundamentals

Tutorial notebooks introducing core Python concepts:

| File | Description |
|------|-------------|
| **PY_Intro.ipynb** | Introduction to Python - Basic syntax, printing, and first programs |
| **PY_Prerequist.ipynb** | Prerequisite concepts - Environment setup and installation guides |
| **PY_DataTypes.ipynb** | Data Types - Strings, integers, floats, lists, tuples, dictionaries, sets |
| **PY_Variables.ipynb** | Variables & Operators - Variable assignment, naming conventions, arithmetic & logical operators |

**Purpose:** These notebooks serve as foundational learning materials for beginners to understand Python fundamentals.

---

### 📋 **PY_Assignments/** - Assignment Projects & Data Files

Core assignment projects with supporting data files:

#### Assignment Notebooks:

| File | Description |
|------|-------------|
| **PY_Asmt1_DS.ipynb** | Data Structures - Arrays, lists, tuples, stacks, queues operations |
| **PY_Asmt2_CF.ipynb** | Control Flow - Conditional statements, loops (for/while), break/continue |
| **PY_Asmt3_Fu.ipynb** | Functions - Function definition, parameters, return values, recursion |
| **PY_Asmt4_FH.ipynb** | File Handling - Reading/writing files, file operations, CSV processing |
| **PY_Asmt6_EH.ipynb** | Exception Handling - Try/except blocks, custom exceptions, error management |
| **PY_Asmt7_OOPS.ipynb** | Object-Oriented Programming - Classes, inheritance, polymorphism, encapsulation, abstraction, magic methods |

#### Data Files:

| File | Description |
|------|-------------|
| **products_info.txt** | Product database containing product names, categories, and prices |
| **product_snapshot.txt** | Point-in-time product data snapshot for analysis |
| **discounted_prices.txt** | Product pricing with discount calculations applied |
| **sales_data.txt** | Sales transaction data for analysis and reporting |

**Purpose:** These assignments progressively teach Python concepts from basic data structures to advanced OOP principles with practical data files for exercises.

---

### 🔧 **PY_Assignments/Modules_Assignments/** - Module & Package Development

Practical exercises on creating and using Python modules and packages:

| File | Description |
|------|-------------|
| **main.py** | Test script demonstrating the use of custom modules and packages |
| **Math_utils.py** | Custom module providing mathematical utility functions:<br>- `addo()` - Addition<br>- `subtract()` - Subtraction<br>- `square_root()` - Square root calculation with error handling |
| **string_utils.py** | Custom module for string manipulation operations:<br>- `capitalize_words()` - Capitalize first letter of each word<br>- `reverse_string()` - Reverse string content<br>- `word_count()` - Count words in a string |
| **shop_package/** | Python package for e-commerce calculations |
| **shop_package/__init__.py** | Package initialization file |
| **shop_package/billing.py** | Billing functionality |
| **shop_package/discount.py** | Discount calculation functions:<br>- `apply_discount()` - Apply percentage-based discounts<br>- `flat_discount()` - Apply fixed amount discounts |

**Purpose:** Learn to organize code into reusable modules and packages, understand package structure, and practice imports and namespacing.

---

### 🌐 **Stremlit_Assignment/** - Web Application Development

Web applications built with Streamlit framework for interactive data visualization and user interfaces:

| File | Description |
|------|-------------|
| **app_basic.py** | Basic Streamlit app demonstrating:<br>- Page title and headers<br>- User input widgets (text input)<br>- Button interactions<br>- Conditional output rendering |
| **app_dashboard.py** | Dashboard application for data visualization and analytics |
| **app_discount.py** | Discount calculator web app for computing product discounts |
| **app_product_form.py** | Product form application for data entry and product management |

**Purpose:** Build interactive web applications without frontend knowledge, create dashboards, and develop user-friendly data tools.

**How to Run:**
```bash
# Run any Streamlit app
streamlit run Stremlit_Assignment/app_basic.py
streamlit run Stremlit_Assignment/app_discount.py
streamlit run Stremlit_Assignment/app_product_form.py
```

---

### 📦 **Root Level Files**

| File | Description |
|------|-------------|
| **app.py** | Main application entry point - Simple demo application |
| **Requirements.txt** | Python package dependencies including:<br>- Data science: numpy, pandas, scikit-learn, matplotlib, seaborn<br>- Visualization: plotly, bokeh, dash<br>- Web frameworks: streamlit, flask, django<br>- ML frameworks: tensorflow, torch, xgboost, lightgboost, catboost<br>- Testing: pytest, coverage<br>- Code quality: flake8, mypy, sphinx |
| **README.md** | This documentation file |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd PYTHON
```

2. **Create a virtual environment:**
```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r Requirements.txt
```

---

## 📖 How to Use

### Learning Path (Recommended Order)

1. **Start with Basics:**
   - Begin with `PY_Basics/PY_Intro.ipynb`
   - Progress through data types and variables
   - Learn prerequisites if needed

2. **Core Assignments:**
   - Follow assignments in numerical order (PY_Asmt1 → PY_Asmt7)
   - Each builds on previous concepts
   - Run code cells to understand outputs

3. **Modules & Packages:**
   - Navigate to `PY_Assignments/Modules_Assignments/`
   - Run `python main.py` to see modules in action
   - Study the module structure

4. **Web Applications:**
   - Explore Streamlit apps in `Stremlit_Assignment/`
   - Run apps with streamlit command
   - Modify and experiment with the code

### Running Jupyter Notebooks

```bash
# Launch Jupyter Lab
jupyter lab

# Or Jupyter Notebook
jupyter notebook

# Navigate to desired notebook and run cells
```

### Running Python Scripts

```bash
# Run main module test
cd PY_Assignments/Modules_Assignments
python main.py

# Run Streamlit apps
streamlit run path/to/app.py
```

---

## 🎯 Key Topics Covered

### Python Fundamentals
- ✅ Data types and structures
- ✅ Variables and operators
- ✅ Control flow (if/else, loops)
- ✅ Functions and scope

### Intermediate Concepts
- ✅ File handling and I/O
- ✅ Exception handling and error management
- ✅ Modules and packages
- ✅ Code organization

### Advanced Topics
- ✅ Object-Oriented Programming (OOP)
  - Classes and objects
  - Inheritance and polymorphism
  - Encapsulation and abstraction
  - Magic methods and operator overloading
- ✅ Data analysis using pandas and numpy
- ✅ Data visualization using plotly and matplotlib

### Web Development
- ✅ Streamlit application development
- ✅ Interactive UI components
- ✅ Data dashboards

---

## 📊 Data Files Reference

### **products_info.txt**
- Contains product information
- Used in file handling and data analysis exercises
- Format: Product names, categories, prices

### **sales_data.txt**
- Sales transaction records
- Used for data analysis exercises
- Includes pricing and quantity information

### **discounted_prices.txt**
- Pre-calculated discounted prices
- Reference for discount calculation validation
- Output from discount calculation exercises

### **product_snapshot.txt**
- Point-in-time product inventory data
- Used for state verification exercises

---

## 🛠️ Technologies & Libraries

| Category | Libraries |
|----------|-----------|
| **Data Science** | numpy, pandas, scikit-learn |
| **Visualization** | matplotlib, seaborn, plotly, bokeh |
| **Web Frameworks** | streamlit, flask, django |
| **ML/DL** | tensorflow, torch, xgboost, lightgbm, catboost |
| **Testing** | pytest, coverage |
| **Code Quality** | flake8, mypy, sphinx |

---

## 📝 Assignment Summary

| Assignment | Topic | Key Concepts |
|-----------|-------|--------------|
| PY_Asmt1_DS | Data Structures | Lists, tuples, dictionaries, sets operations |
| PY_Asmt2_CF | Control Flow | Conditionals, loops, flow control |
| PY_Asmt3_Fu | Functions | Definition, parameters, recursion |
| PY_Asmt4_FH | File Handling | File I/O, reading/writing data |
| PY_Asmt6_EH | Exception Handling | Error handling, custom exceptions |
| PY_Asmt7_OOPS | OOP | Classes, inheritance, polymorphism, encapsulation |

---

## 🤝 Contributing

To contribute improvements or additional exercises:

1. Create a new branch for your feature
2. Add descriptive comments to your code
3. Follow PEP 8 style guidelines
4. Test your code thoroughly
5. Submit a pull request with clear description

---

## 📄 License

This repository is for educational purposes. Feel free to use, modify, and distribute for learning.

---

## 💡 Tips for Success

- Run code cells incrementally to understand outputs
- Experiment with modifying existing code
- Practice writing your own implementations
- Use these materials as reference while building projects
- Don't skip the data files - they're essential for understanding practical applications

---

## 🔗 Quick Links

| Task | Command |
|------|---------|
| Launch Jupyter | `jupyter lab` |
| Run Streamlit app | `streamlit run <app_name>.py` |
| Run module demo | `cd PY_Assignments/Modules_Assignments && python main.py` |
| Install dependencies | `pip install -r Requirements.txt` |
| Activate environment | `venv\Scripts\activate` |

---

## ❓ FAQ

**Q: What version of Python should I use?**
A: Python 3.7 or higher is recommended.

**Q: How do I run Jupyter notebooks?**
A: Use `jupyter lab` or `jupyter notebook` command and open the desired notebook file.

**Q: What if dependencies installation fails?**
A: Try `pip install --upgrade pip` first, then reinstall Requirements.txt.

**Q: Can I run these files on Windows/Mac/Linux?**
A: Yes! Python is cross-platform. All files work on Windows, macOS, and Linux.

---

## 📬 Contact & Support

For questions or issues, refer to the docstrings and comments within the code files.

---

**Last Updated:** February 2026  
**Repository Type:** Educational | Python Learning Materials
