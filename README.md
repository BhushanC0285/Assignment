# Excel Web Application

This web application allows users to upload an Excel file, store it on the server, parse the data, and store it in a backend database. It also provides a download option to export the data from the database table into an Excel file.

## Features

- User-friendly front-end for Excel file upload
- Backend functionality to store uploaded Excel files
- Backend database with a table for storing order details
- Parsing and insertion of Excel file data into the database
- Download option to export data from the database table into an Excel file

## Technologies Used

- Python
- Django web framework
- SQL or NoSQL database (based on your choice)
- HTML, CSS, and JavaScript for front-end interface

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/excel_app.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the backend database with the required table:
   - For SQL database: Create a table named `orders` with the following fields:
     - `order_id` (integer or string)
     - `product_name` (string)
     - `product_price` (float or decimal)
     - `shipped` (Yes/No or boolean)

   - For NoSQL database: Configure the database according to your chosen NoSQL solution and set up a collection/table to store the order details.

4. Configure the database connection in the Django settings file (`settings.py`).

5. Run database migrations to create necessary tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the web application in your browser at `http://localhost:8000`.

## Usage

1. Upload Excel File:
   - Open the web application in your browser.
   - Click on the "Upload Excel File" button.
   - Choose an Excel file from your local machine and click "Upload".
   - The file will be stored on the server, and its data will be inserted into the database table.

2. Download Excel File:
   - Click on the "Download Excel File" button.
   - An Excel file will be generated with all the details from the database table.
   - The file will be downloaded to your local machine.

## Repository Access

The complete code for this project is hosted in a private GitHub repository.

1. Visit the repository URL: https://github.com/BhushanC0285/Assignment

