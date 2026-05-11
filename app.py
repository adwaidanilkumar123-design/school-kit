import markupsafe
import markupsafe
import markupsafe
from flask import Flask, render_template

app = Flask(__name__)

# Hardcoded data so we don't need a DB/admin
PRODUCTS = [
    {
        "id": 1,
        "name": "Cute bunny and carrot backpack",
        "category": "School Bags",
        "description": "Spacious bunny-themed backpack with vibrant carrot prints and multiple zip compartments.Comfortable padded straps make it ideal for school, travel, and outings.",
        "price": 999.00,
        "discount_price": 650.00,
        "image": "static/products/Cute bunny and carrot backpack.png",
        "trending": True,
        "most_loved": True,
        "rating": 4.9,
        "review_count": 128
    },
    {
        "id": 2,
        "name": "Pastel Unicorn-Themed Children's Backpack",
        "category": "School Bags",
        "description": "Cute unicorn-themed backpack with vibrant pastel colors and playful cartoon graphics. Comfortable, lightweight, and perfect for kids heading to school or outings..",
        "price": 1899.00,
        "discount_price": 1399.00,
        "image": "static/products/Pastel unicorn-themed children's backpack.png",
        "trending": True,
        "most_loved": True,
        "rating": 4.8,
        "review_count": 210
    },

    {
        "id": 3,
        "name": "Stainless Steel Lunch Carrier",
        "category": "Lunch Boxes",
        "description": "Modern stainless steel lunch box set with airtight pink locking lids for secure storage. Reusable and easy-to-clean design keeps food fresh and spill-free.",
        "price": 650.00,
        "discount_price": 430.00,
        "image": "static/products/lunchbox.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
        # ... previous products ...
    {
        "id": 4, # Make sure this is a unique number
        "name": "Cute Animal Umbrella",
        "category": "Stationery Sets", # Make sure this matches a category in CATEGORIES
        "description": "Fun animal-themed umbrella designed with adorable cartoon facial features and ears. Lightweight and kid-friendly, offering protection from rain with playful charm.",
        "price": 550.00,
        "discount_price": 350.00, # You can set this to None if there's no discount
        "image": "static/products/umberlla.png", # The path to your new image
        "trending": True, # Set to True to show it on the Home Page
        "most_loved": False,
        "rating": 4.5,
        "review_count": 42
    },
    {
        "id": 5,
        "name": "Stainless Steel Water Bottle Set",
        "category": "Lunch Boxes",
        "description": "Premium stainless steel bottles with a sleek finish, ideal for hot and cold beverages. Leak-proof and reusable design makes it perfect for school, office, and outdoor use.",
        "price": 650.00,
        "discount_price": 499.00,
        "image": "static/products/bottle.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 6,
        "name": "Kids Unicorn Lunch Box Set",
        "category": "Lunch Boxes",
        "description": "Cute unicorn-themed lunch box with secure locking clips and matching spoon-fork set. Made for convenient and mess-free meal storage for kids at school or picnics.",
        "price": 499.00,
        "discount_price": 250.00,
        "image": "static/products/box.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id":7,
        "name": "Stainless steel lunchbox",
        "category": "Lunch Boxes",
        "description": "Durable multi-layer stainless steel lunch carrier for keeping meals fresh and organized. Compact stackable design is ideal for office, school, and travel use.",
        "price": 599.00,
        "discount_price": 280.00,
        "image": "static/products/lunch.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 8,
        "name": "Cute penguin charm clogs",
        "category": "Stationery Sets",
        "description": "Adorable penguin-themed clogs with soft cushioning and breathable comfort. Perfect for casual wear, beach trips, and playful everyday activities.",
        "price": 499.00,
        "discount_price": 289.00,
        "image": "static/products/crocs.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 9,
        "name": "Kids Outdoor Clogs Sandals ",
        "category": "Stationery Sets",
        "description": "Comfortable anti-slip clogs with breathable holes and adjustable back straps. Durable lightweight design makes them ideal for indoor and outdoor daily wear.",
        "price": 599.00,
        "discount_price": 399.00,
        "image": "static/products/clog.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 10,
        "name": "Pink Cartoon Pencil Box",
        "category": "Stationery Sets",
        "description": "Cute pink pencil case featuring charming cartoon artwork and multiple storage sections. Keeps pens, pencils, and accessories neatly organized in a fun stylish way.",
        "price": 599.00,
        "discount_price": 299.00,
        "image": "static/products/pencilbox.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 11,
        "name": "Pastel panda pencil case",
        "category": "Stationery Sets",
        "description": "Adorable panda-themed pencil case with spacious compartments for organized storage. Stylish and practical design makes it perfect for school essentials and stationery.",
        "price": 499.00,
        "discount_price": 280.00,
        "image": "static/products/penbox.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 12,
        "name": "Mini Capsule Folding Umbrella",
        "category": "Stationery Sets",
        "description": "Compact folding umbrella with a sleek capsule case for easy portability and storage.Lightweight and travel-friendly design offers protection from sudden rain and sun.",
        "price": 799.00,
        "discount_price": 550.00,
        "image": "static/products/blueumbrella.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 13,
        "name": "Floral Folding Umbrella",
        "category": "Stationery Sets",
        "description": "Elegant purple floral umbrella with a compact foldable design for easy carrying. Provides stylish rain protection with durable fabric and sturdy construction.",
        "price": 499.00,
        "discount_price": 299.00,
        "image": "static/products/floral.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 14,
        "name": "Cartoon-themed slide sandals",
        "category": "Stationery Sets",
        "description": "Comfortable cartoon-themed sliders with soft cushioned soles for everyday wear. Available in playful pastel colors, perfect for kids and casual indoor use.",
        "price": 799.00,
        "discount_price": 480.00,
        "image": "static/products/sliders.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 15,
        "name": "Whimsical unicorn black backpack",
        "category": "School Bags",
        "description": "Elegant black backpack featuring colorful unicorn artwork and floral accents. Spacious and durable design with a magical aesthetic for school or travel.",
        "price": 1399.00,
        "discount_price": 690.00,
        "image": "static/products/Whimsical unicorn print black backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 16,
        "name": "Pastel pink structured backpack",
        "category": "School Bags",
        "description": "Minimal pastel pink backpack designed with a clean and modern aesthetic. Features roomy storage and durable material for everyday school or travel use.",
        "price": 1499.00,
        "discount_price": 1250.00,
        "image": "static/products/Pastel pink structured backpack on white.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 17,
        "name": "Space Explorer Backpack",
        "category": "School Bags",
        "description": "Stylish pastel-colored backpack with multiple compartments and durable straps for comfortable daily use.",
        "price": 1199.00,
        "discount_price": 750.00,
        "image": "static/products/bag.png",
        "trending": False,
        "most_loved": True,
        "rating": 4.7,
        "review_count": 85
    },

    {
        "id": 18,
        "name": "Space-themed pencil case",
        "category": "Stationery Sets",
        "description": "Stylish astronaut-themed pencil case with a sleek hard-shell protective design. Ideal for safely storing pens, pencils, and stationery with a fun space vibe.",
        "price": 399.00,
        "discount_price": 200.00,
        "image": "static/products/Space-themed pencil case with astronaut design.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 19,
        "name": "Unicorn-themed children's backpack",
        "category": "School Bags",
        "description": "Bright unicorn backpack featuring colorful rainbow accents and cute magical details. Designed for comfort and spacious storage, ideal for young school kids.",
        "price": 1499.00,
        "discount_price": 999.00,
        "image": "static/products/Unicorn-themed children's backpack on white.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 20,
        "name": "Heart-patterned backpack",
        "category": "School Bags",
        "description": "Trendy heart-pattern backpack with matching side pouch for extra storage convenience. Spacious lightweight design is perfect for students and everyday use.",
        "price": 1499.00,
        "discount_price": 699.00,
        "image": "static/products/Heart-patterned backpack with accessories.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 21,
        "name": "yellow chick backpack",
        "category": "School Bags",
        "description": "Bright yellow chick-themed backpack with adorable cartoon-inspired detailing. Compact, lightweight, and perfect for toddlers and preschool children.",
        "price": 1399.00,
        "discount_price": 750.00,
        "image": "static/products/yellow chick backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 22,
        "name": "Gradient Water Bottles",
        "category": "Lunch Boxes",
        "description": "Beautiful gradient water bottles with modern matte finishes and ergonomic designs. Leak-proof and stylish, perfect for gym, school, office, or travel hydration.",
        "price": 899.00,
        "discount_price": 500.00,
        "image": "static/products/water bottles.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 23,
        "name": "Vibrant DOMS art kit",
        "category": "Stationery Sets",
        "description": "Complete DOMS art set packed with drawing books, crayons, pencils, and color tools. Perfect creative companion for students, artists, and hobby enthusiasts.",
        "price": 499.00,
        "discount_price": 250.00,
        "image": "static/products/Vibrant DOMS art kit.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 24,
        "name": "Stylish backpack",
        "category": "School Bags",
        "description": "Modern peach-toned backpack with eye-catching graphic patterns and spacious storage. Perfect combination of comfort, durability, and trendy everyday style.",
        "price": 1199.00,
        "discount_price": 650.00,
        "image": "static/products/Stylish backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 25,
        "name": "Stainless steel water bottle",
        "category": "Lunch Boxes",
        "description": "Premium stainless steel bottle designed to keep beverages hot or cold for hours. Sleek, reusable, and eco-friendly for daily hydration anywhere you go.",
        "price": 599.00,
        "discount_price": 350.00,
        "image": "static/products/Stainless steel water bottle.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 26,
        "name": "Sporty backpack",
        "category": "School Bags",
        "description": "Bold sporty backpack featuring dynamic typography prints and multiple zip compartments. Durable and spacious design makes it perfect for school, travel, and outdoor activities.",
        "price": 1199.00,
        "discount_price": 650.00,
        "image": "static/products/Sporty backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 27,
        "name": "Pastel marble-patterned backpack",
        "category": "School Bags",
        "description": "Trendy marble-print backpack with spacious compartments and comfortable padded straps. Perfect for students who want both fashion and functionality in one stylish bag.",
        "price": 1499.00,
        "discount_price": 750.00,
        "image": "static/products/Pastel marble-patterned backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 28,
        "name": "3 Pastel bottles",
        "category": "Lunch Boxes",
        "description": "Elegant pastel-colored bottles with a sleek modern design, perfect for daily hydration in style. Lightweight and durable, ideal for school, office, travel, or gym use.",
        "price": 499.00,
        "discount_price": 299.00,
        "image": "static/products/Pastel bottles.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 29,
        "name": "Lavender Printed Backpack",
        "category": "School Bags",
        "description": "Trendy lavender backpack with cute character prints and spacious storage compartments. Soft padded straps and durable material ensure comfort for daily school use.",
        "price": 1399.00,
        "discount_price": 745.00,
        "image": "static/products/Pastel backpack.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 30,
        "name": "Motivational Gradient Water Bottle",
        "category": "Lunch Boxes",
        "description": "Stylish gradient water bottle with time markers to help track daily hydration goals. Leak-proof reusable design is perfect for gym, travel, office, and school.",
        "price": 299.00,
        "discount_price": 199.00,
        "image": "static/products/Motivational water bottle with time markers.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 31,
        "name": "Rainbow Kids Umbrella",
        "category": "Stationery Sets",
        "description": "Bright multicolor umbrella designed with a curved handle for easy grip and comfort. Strong lightweight frame provides reliable protection during rainy days.",
        "price": 499.00,
        "discount_price": 280.00,
        "image": "static/products/Colourful umbrella.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 32,
        "name": "Children's space-themed art kit",
        "category": "Stationery Sets",
        "description": "Creative astronaut-themed stationery box with built-in compartments and accessories. Comes with essential school supplies in a compact and fun design for kids.",
        "price": 599.00,
        "discount_price": 280.00,
        "image": "static/products/Children's space-themed art kit.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    },
    {
        "id": 33,
        "name": "Children's Learning Activity Books Set",
        "category": "Stationery Sets",
        "description": "Colorful educational books designed to improve creativity, coloring, and early learning skills. Fun and interactive pages help children learn alphabets, numbers, shapes, and more.",
        "price": 229.00,
        "discount_price": 190.00,
        "image": "static/products/Children's colourful activity books.png",
        "trending": True,
        "most_loved": False,
        "rating": 4.8,
        "review_count": 210
    }



]

CATEGORIES = [
    {"name": "School Bags", "icon": "fa-backpack"},
    {"name": "Lunch Boxes", "icon": "fa-box-open"},
    {"name": "Stationery Sets", "icon": "fa-pencil"}
]

@app.route('/')
def home():
    trending_products = [p for p in PRODUCTS if p.get('trending', False)]
    return render_template('store/home.html', products=trending_products, categories=CATEGORIES, whatsapp_number='8891121497')

@app.route('/products')
def product_list():
    return render_template('store/product_list.html', products=PRODUCTS, whatsapp_number='8891121497')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if product is None:
        return "Product not found", 404
    return render_template('store/product_detail.html', product=product, whatsapp_number='8891121497')

if __name__ == '__main__':
    app.run(debug=True)
