# Ex.07 Restaurant Website
# Date:30/04/2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
res.html
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Krishna’s Kitchen</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

    }

    body {
      background-color: #fff;
    }

    header {
      background-image: url('bac.avif');
      background-size: cover;
      background-position: center;
      height: 100vh;
      color: rgb(252, 252, 252);
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      text-align: center;
      text-shadow: 2px 2px 10px black;
    }


    header h1 {
      font-size: 4rem;
      margin-bottom: 10px;
    }

    header p {
      font-size: 1.5rem;
      margin-bottom: 20px;
    }

    header button {
      padding: 15px 30px;
      font-size: 1rem;
      background-color: #d4af37;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: 0.3s;
    }

    header button:hover {
      background-color: #b88b22;
    }

    section {
      padding: 50px 20px;
      max-width: 1200px;
      margin: auto;
    }

    h2 {
      text-align: center;
      margin-bottom: 30px;
      color: #333;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 30px;
    }

    .card {
      background-color: #f9f9f9;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      text-align: center;
    }

    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
    }

    .card h3 {
      margin: 15px 0 10px;
    }

    .card p {
      padding: 0 10px 20px;
      color: #555;
    }

    .contact {
      background-color: #222;
      color: white;
      text-align: center;
      padding: 40px 20px;
    }

    .contact h2 {
      color: #fff;
    }

    footer {
      background-color: #111;
      color: #aaa;
      text-align: center;
      padding: 20px;
      font-size: 14px;
    }

    @media (max-width: 768px) {
      header h1 {
        font-size: 2.5rem;
      }
      header p {
        font-size: 1.2rem;
      }
    }
  </style>
</head>
<body>

  <!-- Hero Section -->
  <header>
    <h1>Welcome to Krishna’s Kitchen</h1>
    <p>Pure Veg | Taste The Treditional | Book Your Table Now 💙</p>
    <button onclick="alert('Online Booking will be available soon 💙')">Book a Table</button>
  </header>

  <!-- Special Dishes -->
  <section>
    <h2>🍛 Our Special Dishes</h2>
    <div class="cards">
      <div class="card">
        <img src="pannir.jpg" alt="Dish 1">
        <h3>Paneer Tikka</h3>
        <p>Spicy, smoky, and perfectly grilled cottage cheese with masala.</p>
      </div>
      <div class="card">
        <img src="dosa.jpg" alt="Dish 2">
        <h3>Masala Dosa</h3>
        <p>Traditional crispy dosa served with flavorful potato filling.</p>
      </div>
      <div class="card">
        <img src="gulab.jpg" alt="Dish 3">
        <h3>Gulab Jamun</h3>
        <p>Soft, warm, and juicy sweet balls in sugar syrup.</p>
      </div>
    </div>
  </section>

  <!-- Best Chef -->
  <section>
    <h2>👨‍🍳 Our Master Chef</h2>
    <div class="cards">
      <div class="card">
        <img src="chef2.jpg" height="auto" alt="Our Best Chef" />
        <h3>Chef Ram Krishna</h3>
        <p>With 20+ years of experience, Chef Ram Krishna brings devotion and taste together in every meal.</p>
      </div>
    </div>
  </section>

  <!-- Restaurant Views -->
  <section>
    <h2>🌆 Best Views from Our Restaurant</h2>
    <div class="cards">
      <div class="card">
        <img src="night.jpg" alt="View 1">
        <h3>Cozy Night Vibes</h3>
        <p>Enjoy your dinner with a peaceful and romantic ambiance.</p>
      </div>
      <div class="card">
        <img src="open.jpg" alt="View 2">
        <h3>Open-Air Dining</h3>
        <p>Experience divine food under the stars with greenery around you.</p>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section class="contact">
    <h2>📞 Contact Us</h2>
    <p>Location: Krishna Street, Divine Town, India</p>
    <p>Phone: +91 98765 43210</p>
    <p>Email: contact@krishnaskitchen.com</p>
  </section>

  <!-- Footer -->
  <footer>
    &copy; 2025 Krishna’s Kitchen | Designed with 💙 by your bro
  </footer>

</body>
</html>
```

# OUTPUT:
![alt text](<Screenshot (20).png>)

![alt text](<Screenshot (21).png>)

![alt text](<Screenshot (22).png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
