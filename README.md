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

Admin Credentials (for evaluation)

Email: admin@example.com

Password: Admin@12345

Features
User Panel

User Registration & Login (JWT)

Browse & view products

Add products to cart

Checkout & view orders

Admin Panel

Manage Products (CRUD)

View Orders & Order Items

Update Order Status

Export Orders to CSV

Screenshots
1. Admin Login Page

2. Admin Dashboard

3. Product List (Admin)

4. Add Product Page

5. Orders List (Admin)

6. Order Items Page

7. Add Order Page

8. Add Order Item Page

9. Frontend Cart & Products Page

Notes

All screenshots are included in the screenshots folder.

Make sure the virtual environment is activated before running commands.

For demo/testing, you can use the provided admin credentials.
sepnoty_project/
├─ shop/
├─ users/
├─ sepnoty_project/
├─ screenshots/ <- all images here
└─ README.md

👩‍💻 Developed by: Jeera Ambika
💼 Role: Python Full Stack Developer
🏢 Project: Sepnoty E-Commerce (Admin & User Panel)
