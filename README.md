# Car Price Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technical Details](#technical-details)
   - [Data Collection](#data-collection)
   - [Data Processing](#data-processing)
   - [Machine Learning Model](#machine-learning-model)
4. [Installation and Usage](#installation-and-usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Project Overview

Car Price Checker is a web application designed to estimate the market value of used cars in Spain. By scraping data from [coches.com](https://www.coches.com/), the application trains a machine learning regression model to predict the price of any specified vehicle. This project serves as a demonstration of data science and machine learning capabilities, and is part of my open portfolio on GitHub.

Access the live application here: [https://car-price-checker.lopezrbn.com/](https://car-price-checker.lopezrbn.com/)

## Features

- **User-Friendly Interface**: Input vehicle details to receive an estimated market price.
- **Comprehensive Data Collection**: Aggregates data from a leading Spanish used car marketplace.
- **Machine Learning Integration**: Utilizes a regression model trained on real-world data for price predictions.

## Technical Details

### Data Collection

The application scrapes listings from [coches.com](https://www.coches.com/), extracting relevant details such as:

- Selling price
- Car model
- Fuel type
- Location
- Year of manufacture
- Mileage
- Transmission type
- Power (HP)
- Number of doors

The scraping process involves:

1. **Gathering Listing URLs**: Constructing search URLs for each car model and iterating through available pages to collect individual listing links.
2. **Extracting Data**: Visiting each listing to extract detailed information, especially attributes not available on summary pages.

For implementation details, refer to the `cars_scraper.py` script in the repository.

### Data Processing

Collected data undergoes cleaning and preprocessing to ensure quality and consistency:

- **Handling Missing Values**: Imputing or removing incomplete records.
- **Data Transformation**: Converting categorical variables into numerical formats suitable for modeling.
- **Feature Engineering**: Creating new features or modifying existing ones to enhance model performance.

### Machine Learning Model

A multivariate linear regression model is employed to predict car prices. Key steps include:

1. **Model Training**: Fitting the regression model using the processed dataset.
2. **Evaluation**: Assessing model performance using metrics such as Mean Absolute Error (MAE) and R-squared.
3. **Prediction**: Deploying the trained model to estimate prices based on user input.

The model accounts for various factors influencing car prices, including age, mileage, brand, model, and additional features.

## Installation and Usage

To run the application locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lopezrbn/car-price-checker.git
   cd car-price-checker

2. **Install Dependencies**: Ensure you have Python 3.7 or higher installed. Then, install required packages:
    ```bash
    pip install -r requirements.txt

3. **Run the Application**: Start the web application using Reflex:
    ```bash
    reflex run

The application will be accessible at [http://localhost:3000](http://localhost:3000)

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request. Ensure that your contributions align with the project's objectives and maintain code quality.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/lopezrbn/car-price-checker/blob/main/LICENSE) file for details.

## Contact

For inquiries or feedback, please contact me at <lopezrbn@gmail.com>.