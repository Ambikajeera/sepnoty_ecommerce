# Sepnoty E-Commerce Project

## Description
Mini E-Commerce Web App with User & Admin Panel for managing Products & Orders.  
- Users can register, login, browse products, add to cart, checkout, and view orders.  
- Admin can add/edit/delete products, view orders, update order status, and export orders.

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/Ambikajeera/sepnoty_ecommerce.git

2.Navigate to the project folder:

cd sepnoty_project

3.Create a virtual environment:

python -m venv venv

4.Activate the virtual environment:

Windows:
venv\Scripts\activate

5.Install dependencies:

pip install -r requirements.txt

6.Apply migrations:

python manage.py makemigrations
python manage.py migrate

7.Create superuser (for admin login):

python manage.py createsuperuser

8.Run the server:

python manage.py runserver
