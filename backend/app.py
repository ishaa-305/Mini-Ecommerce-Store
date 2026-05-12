from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [

    {
        "id": 1,
        "name": "T-Shirt",
        "price": 499,
        "image": "/images/T-Shirt.jpg",
        "description": "Comfortable cotton t-shirt for casual wear.",
        "category": "Western",
        "rating": 4.5
    },

    {
        "id": 2,
        "name": "Hoodie",
        "price": 1299,
        "image": "/images/Hoodie.jpg",
        "description": "Warm and trendy hoodie for winter season.",
        "category": "Winter",
        "rating": 3.9
    },

    {
        "id": 3,
        "name": "Jeans",
        "price": 1599,
        "image": "/images/Jeans.jpg",
        "description": "Stylish denim jeans with perfect fitting.",
        "category": "Western",
        "rating": 4.8
    },

    {
        "id": 4,
        "name": "Cotton Kurti",
        "price": 899,
        "image": "/images/Cotton Kurti.jpg",
        "description": "Soft cotton kurti for daily comfort.",
        "category": "Ethnic",
        "rating": 4.5
    },

    {
        "id": 5,
        "name": "Denim Jacket",
        "price": 2199,
        "image": "/images/Denim Jacket.jpg",
        "description": "Classic denim jacket for a fashionable look.",
        "category": "Winter",
        "rating": 4.6
    },

    {
        "id": 6,
        "name": "Short Kurti",
        "price": 799,
        "image": "/images/Short Kurti.jpg",
        "description": "Trendy short kurti with modern design.",
        "category": "Ethnic",
        "rating": 4.2
    },

    {
        "id": 7,
        "name": "Formal Pant",
        "price": 599,
        "image": "/images/Formal Pant.jpg",
        "description": "Elegant formal pants for office and events.",
        "category": "Formal",
        "rating": 4.9
    },

    {
        "id": 8,
        "name": "Formal Shirt",
        "price": 399,
        "image": "/images/Formal Shirt.jpg",
        "description": "Premium formal shirt with stylish finish.",
        "category": "Formal",
        "rating": 4.8
    },

    {
        "id": 9,
        "name": "Printed Saree",
        "price": 1799,
        "image": "/images/Printed Saree.jpg",
        "description": "Beautiful printed saree for festive occasions.",
        "category": "Ethnic",
        "rating": 4.6
    },

    {
        "id": 10,
        "name": "Kurta Set",
        "price": 1499,
        "image": "/images/Kurta Set.jpg",
        "description": "Traditional kurta set with elegant style.",
        "category": "Ethnic",
        "rating": 4.7
    },

    {
        "id": 11,
        "name": "Crop Top",
        "price": 1299,
        "image": "/images/Crop Top.jpg",
        "description": "Stylish crop top for modern casual fashion.",
        "category": "Western",
        "rating": 4.5
    },

    {
        "id": 12,
        "name": "Yellow Lehenga",
        "price": 8999,
        "image": "/images/Yellow Lehenga.jpg",
        "description": "Attractive lehenga perfect for weddings.",
        "category": "Ethnic",
        "rating": 4.9
    },

    {
        "id": 13,
        "name": "Winter Coat",
        "price": 5499,
        "image": "/images/Winter Coat.jpg",
        "description": "Warm winter coat with premium fabric.",
        "category": "Winter",
        "rating": 4.1
    },

    {
        "id": 14,
        "name": "Peplum Top",
        "price": 799,
        "image": "/images/Peplum Top.jpg",
        "description": "Fashionable peplum top with elegant fit.",
        "category": "Western",
        "rating": 4.7
    },

    {
        "id": 15,
        "name": "Ethnic Saree",
        "price": 6799,
        "image": "/images/Ethnic Saree.jpg",
        "description": "Traditional ethnic saree with rich design.",
        "category": "Ethnic",
        "rating": 4.5
    },

    {
        "id": 16,
        "name": "Midi Dress",
        "price": 699,
        "image": "/images/Midi dress.jpg",
        "description": "Comfortable midi dress for casual outings.",
        "category": "Western",
        "rating": 4.8
    },

    {
        "id": 17,
        "name": "Floral Top",
        "price": 899,
        "image": "/images/Floral Top.jpg",
        "description": "Floral printed top with trendy look.",
        "category": "Western",
        "rating": 4.5
    },

    {
        "id": 18,
        "name": "One Piece Dress",
        "price": 1499,
        "image": "/images/One piece dress.jpg",
        "description": "Elegant one-piece dress for party wear.",
        "category": "Western",
        "rating": 4.7
    },

    {
        "id": 19,
        "name": "Trendy Lehenga",
        "price": 6999,
        "image": "/images/Trendy Lehenga.jpg",
        "description": "Designer lehenga with modern ethnic touch.",
        "category": "Ethnic",
        "rating": 4.3
    },

    {
        "id": 20,
        "name": "Top",
        "price": 999,
        "image": "/images/Top.jpg",
        "description": "Stylish top for everyday fashion.",
        "category": "Western",
        "rating": 4.1
    }

]

@app.route("/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)