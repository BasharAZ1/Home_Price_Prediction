# House Rent or Buy Predictor

This Flask application assists users in determining whether to rent or buy a house in Islamabad, Karachi, Rawalpindi, and Faisalabad. It provides tailored recommendations based on user input and predicts prices for either renting or buying properties.

## Application Overview

The application takes the following inputs from the user to provide a recommendation:

- **City**: The city where the user is interested in renting or buying a property. Choices include Islamabad, Karachi, Rawalpindi, and Faisalabad.
- **Number of Bathrooms**: The desired number of bathrooms in the property.
- **Area**: The total area of the property in square feet.
- **Bedrooms**: The number of bedrooms desired in the property.

Based on these inputs, the application uses a predictive model to estimate the price of renting or buying the specified property in the selected city. This helps users make informed decisions about whether renting or buying is a more feasible option based on their financial situation and market conditions.

## Getting Started

Follow these instructions to get the application running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.8 or later installed on your system. If not, download it from [python.org](https://www.python.org/downloads/).

### Installation

Clone the repository and navigate into it:
```bash
git clone https://github.com/BasharAZ1/Home_Price_Prediction.git
cd Home_Price_Prediction
```

Set up and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
.\venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

Install the necessary packages using the provided requirements file:
```bash
pip install -r requirements.txt
```

### Running the Application

With the setup complete, you can start the Flask application:
```bash
flask run
```
The server will start running on `http://127.0.0.1:5000/` where you can access the application through your web browser.

## Usage

Visit `http://127.0.0.1:5000/` on your browser, input the required details about the property and your financial status, and the application will suggest whether renting or buying is the better option for you.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your enhancements. Make sure your code adheres to the existing style to maintain the project's consistency.

## License

This project is released under the MIT License. See the LICENSE file for further details.
