# E2E UI Test for Saucedemo

This repository contains an end-to-end (E2E) UI test for the [Saucedemo](https://www.saucedemo.com) website, implemented using either Selenium or Playwright. The test script automates the process of logging in, selecting a product, and completing a purchase.

## Prerequisites

Before running the test, ensure you have the following installed:

- Python 3.6 or later
- [Chrome Browser](https://www.google.com/chrome/) (if using Selenium)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/varckin/E2E-UI.git
   cd E2E-UI
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

### Selenium
1. **Run the Selenium test:**

   ```bash
   python test_selenium.py
   ```

### Playwright
1. **Run the Playwright test:**

   ```bash
   python test_playwright.py
   ```

## Test Scenarios
The test script performs the following actions:

1. **Authorization:**
   - Logs in using the following credentials:
     - Username: `standard_user`
     - Password: `secret_sauce`

2. **Product Selection:**
   - Selects the product "Sauce Labs Backpack" and adds it to the cart.

3. **Checkout:**
   - Navigates to the cart, proceeds to checkout, and fills in the required fields.
   - Completes the purchase.

4. **Verification:**
   - Confirms that the purchase was successful by checking for the "THANK YOU FOR YOUR ORDER" message.

## Configuration

For Selenium, the script uses the default Chrome browser settings. Ensure you have Chrome installed.

For Playwright, the script uses Chromium. The necessary browser binaries will be downloaded during installation.

## Troubleshooting

- Ensure that your internet connection is stable.
- Make sure Chrome is up-to-date if using Selenium.
- Verify that all dependencies are correctly installed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
