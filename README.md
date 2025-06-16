# Selenium Pytest BDD Framework

A professional test automation framework using Selenium WebDriver, Pytest, and BDD.

## Test Site Information

The framework is designed to test the Demo Shop application, which is a sample e-commerce website with the following features:

- User Registration
- User Login
- Product Browsing
- Shopping Cart
- Checkout Process

### Test Site URL
- Main URL: https://shop.demoqa.com/
- Registration Page: https://shop.demoqa.com/my-account/
- Login Page: https://shop.demoqa.com/my-account/

### Test Site Features
1. **User Management**
   - Registration with email and password
   - Login functionality
   - User profile management

2. **Product Features**
   - Product listing
   - Product categories
   - Product search
   - Product details view

3. **Shopping Features**
   - Add to cart
   - Update cart
   - Remove items
   - Checkout process

4. **Account Features**
   - Order history
   - Address management
   - Account settings

## Project Structure
```
selenium_pytest_bdd/
├── config/                     # Configuration files
│   ├── __init__.py
│   └── config.yaml            # Environment configurations
├── features/                   # BDD feature files
│   ├── __init__.py
│   └── login.feature
├── pages/                      # Page Object Models
│   ├── __init__.py
│   └── login_page.py
├── tests/                      # Test implementations
│   ├── __init__.py
│   ├── conftest.py            # Pytest configurations
│   └── steps/                 # Step definitions
│       ├── __init__.py
│       └── test_login.py
├── utils/                      # Utility functions
│   ├── __init__.py
│   ├── driver_factory.py      # WebDriver setup
│   └── clear_cache.py         # Cache cleanup
├── reports/                    # Test reports
├── logs/                       # Log files
├── requirements.txt            # Project dependencies
├── pytest.ini                 # Pytest configurations
└── README.md                  # Project documentation
```

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

1. Run all tests:
```bash
pytest
```

2. Run specific feature:
```bash
pytest features/login.feature
```

3. Run with detailed output:
```bash
pytest -v
```

4. Generate HTML report:
```bash
pytest --html=reports/report.html
```

## Project Features

- Page Object Model design pattern
- BDD with Gherkin syntax
- Configurable test environments
- Detailed test reporting
- Logging system
- Cross-browser testing support
- Utility functions for common tasks

## Best Practices

1. Keep page objects separate from test logic
2. Use meaningful names for features and scenarios
3. Implement proper logging
4. Handle test data separately
5. Use configuration files for different environments
6. Generate and maintain test reports
7. Follow PEP 8 style guide
