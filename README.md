# 🛍️ Sepnoty E-Commerce Project

## 📘 Description
Mini E-Commerce Web App with **User & Admin Panel** for managing **Products & Orders**.  
Users can register, login, browse products, add to cart, checkout, and view orders.  
Admin can manage products, view orders, update status, and export orders.

---

## ⚙️ Setup Instructions (Commands Included)

### 1️⃣ Clone the Repository

git clone https://github.com/Ambikajeera/sepnoty_ecommerce.git
2️⃣ Navigate to the Project Folder
bash

cd sepnoty_project
3️⃣ Create a Virtual Environment


python -m venv venv
4️⃣ Activate the Virtual Environment
For Windows:
venv\Scripts\activate
For Mac/Linux:

source venv/bin/activate
5️⃣ Install Dependencies

pip install -r requirements.txt
6️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate
7️⃣ Create Superuser (Admin Login)

python manage.py createsuperuser
8️⃣ Run the Server

python manage.py runserver
Then open your browser and go to:
👉 http://127.0.0.1:8000/admin

👨‍💻 Admin Credentials (for demo)
pgsql

Email: admin@example.com
Password: Admin@12345
🌟 Features
🧑‍💼 User Panel
Register & Login (JWT)

Browse and View Products

Add Products to Cart

Checkout & View Orders

🛒 Admin Panel
Manage Products (CRUD)

View Orders & Order Items

Update Order Status

Export Orders to CSV

🖼️ Screenshots
1️⃣ Admin Login Page
2️⃣ Admin Dashboard
3️⃣ Product List (Admin)
4️⃣ Add Product Page
5️⃣ Orders List (Admin)
6️⃣ Order Items Page
7️⃣ Add Order Page
8️⃣ Add Order Item Page
9️⃣ Frontend Cart & Products Page


🧾 Notes
All screenshots are stored inside the screenshots folder.

Make sure your virtual environment (venv) is activated before running Django commands.

For demo/testing, use the provided admin credentials.

sepnoty_project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── screenshots/
│   ├── Admin_login.png
│   ├── admin_dashboard.png
│   ├── add_product.png
│   ├── products_list.png
│   ├── orders_list.png
│   ├── ordered_itemlist.png
│   ├── add_order.png
│   ├── add_orderitem.png
│   ├── frontend_cart.png
│
├── shop/
├── users/
└── sepnoty_project/

👩‍💻 Developed by: Jeera Ambika
💼 Role: Python Full Stack Developer
🏢 Project: Sepnoty E-Commerce (Admin & User Panel)
