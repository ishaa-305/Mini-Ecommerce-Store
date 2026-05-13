import { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");

  useEffect(() => {

    fetch("http://127.0.0.1:5000/products")
      .then((response) => response.json())
      .then((data) => setProducts(data));

  }, []);

  // Add to cart
  const addToCart = (product) => {

    setCart([...cart, product]);

  };

  // Remove from cart
  const removeFromCart = (indexToRemove) => {

    const updatedCart = cart.filter(
      (_, index) => index !== indexToRemove
    );

    setCart(updatedCart);

  };

  // Total price
  const total = cart.reduce(
    (sum, item) => sum + item.price,
    0
  );

  // Search + Category Filter
  const filteredProducts = products.filter((product) => {

    const matchesSearch =
      product.name.toLowerCase().includes(search.toLowerCase());

    const matchesCategory =
      category === "All" ||
      product.category === category;

    return matchesSearch && matchesCategory;

  });

  return (

    <div className="container">
        <h1>Mini E-Commerce Store</h1>
      
      {/* Search Box */}

      <input
        type="text"
        placeholder="Search products..."
        className="search-box"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {/* Filter Buttons */}

      <div className="filter-buttons">

        <button
          className={category === "All" ? "active" : ""}
          onClick={() => setCategory("All")}
        >
          All
        </button>

        <button
          className={category === "Western" ? "active" : ""}
          onClick={() => setCategory("Western")}
        >
          Western
        </button>

        <button
          className={category === "Ethnic" ? "active" : ""}
          onClick={() => setCategory("Ethnic")}
        >
          Ethnic
        </button>

        <button
          className={category === "Winter" ? "active" : ""}
          onClick={() => setCategory("Winter")}
        >
          Winter
        </button>

        <button
          className={category === "Formal" ? "active" : ""}
          onClick={() => setCategory("Formal")}
        >
          Formal
        </button>

      </div>

      {/* Products */}

      <div className="products">

        {filteredProducts.map((product) => (

          <div className="card" key={product.id}>

            <img
              src={product.image}
              alt={product.name}
            />

            <div className="card-content">

              <h3>{product.name}</h3>

              <p>{product.description}</p>
              <div className="rating">
                {product.rating} ★
              </div>

              <h4>₹ {product.price}</h4>

              <button onClick={() => addToCart(product)}>
                Add to Cart
              </button>

            </div>

          </div>

        ))}

      </div>

      {/* Cart */}

      <div className="cart">

        <h2>Shopping Cart</h2>

        {cart.length === 0 ? (

          <p>Cart is empty</p>

        ) : (

          cart.map((item, index) => (

            <div className="cart-item" key={index}>

              <p>
                {item.name} - ₹ {item.price}
              </p>

              <button
                className="remove-btn"
                onClick={() => removeFromCart(index)}
              >
                Remove
              </button>

            </div>

          ))

        )}

        <h3>Total: ₹ {total}</h3>

      </div>
        <footer className="footer">
           © 2026 Mini E-Commerce Store
        </footer>
    </div>

  );
}

export default App;