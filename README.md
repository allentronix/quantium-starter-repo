# Quantium Pink Morsel Sales Visualiser

A data analytics and visualisation project that processes sales data for Soul Foods' Pink Morsels and creates an interactive Dash dashboard to analyse sales performance before and after a price increase.

The project demonstrates data processing, visualisation, automated testing, and test automation using Python.

---

## Project Overview

Soul Foods wanted to understand:

> "Were sales higher before or after the Pink Morsel price increase on 15th January 2021?"

To answer this business question, the project:

1. Processes raw CSV transaction data
2. Filters data to only include Pink Morsels
3. Calculates total daily sales
4. Generates a cleaned dataset
5. Builds an interactive dashboard
6. Adds automated tests to verify application functionality

---

## Features

### Data Processing

- Combines multiple CSV files into a single dataset
- Filters only Pink Morsel products
- Calculates sales using:

```
Sales = Quantity × Price
```

- Produces a formatted output file:

```
Sales, Date, Region
```

---

### Dash Visualisation

The dashboard includes:

- Sales trend line chart
- Date-based sales analysis
- Region filtering using radio buttons:
  - North
  - East
  - South
  - West
  - All regions

---

### Automated Testing

A test suite was created using Dash Testing and Pytest.

The tests verify:

- Header is displayed
- Sales visualisation is present
- Region selector is available

Run tests with:

```bash
python -m pytest
```

---

### Test Automation

A Bash script was created to automatically:

1. Activate the virtual environment
2. Run the test suite
3. Return:
   - Exit code `0` if tests pass
   - Exit code `1` if tests fail

Run:

```bash
./run_tests.sh
```

---

## Technologies Used

- Python 3.9
- Pandas
- Dash
- Plotly
- Pytest
- Selenium
- Bash scripting
- Git & GitHub

---

## Project Structure

```
quantium-starter-repo
│
├── app.py                 # Dash dashboard application
├── process_data.py        # CSV processing script
├── output.csv             # Cleaned sales dataset
├── run_tests.sh           # Automated test runner
│
├── tests
│   └── test_app.py        # Dash application tests
│
└── venv                   # Python virtual environment
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd quantium-starter-repo
```

Create and activate virtual environment:

```bash
python3.9 -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install pandas
pip install "dash[testing]"
```

---

## Running the Application

Process the data:

```bash
python process_data.py
```

Start the dashboard:

```bash
python app.py
```

Open:

```
http://127.0.0.1:8050/
```

---

## Running Tests

Run the test suite:

```bash
python -m pytest
```

Expected output:

```
3 passed
```

---

## Key Learning Outcomes

Through this project, I gained experience with:

- Data cleaning and transformation using Pandas
- Building interactive dashboards with Dash
- Creating automated UI tests
- Using Selenium for browser-based testing
- Writing Bash scripts for automation
- Managing Python environments
- Working with Git workflows

---

## Author

Allen M Chijioke


