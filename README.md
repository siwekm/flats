# 🏠 Python scrapper for sreality.cz

Scraps real estate listing from sreality.cz, stores the result in a PostgreSQL database, creates a simple HTTP server to load the data from the database, and display the listing name and the featured picture of the scraped listings.

### 🚀 Getting Started
Simply use `docker-compose up` to run

Once the services are up, you can access the listings at:<br>
`http://localhost:8080/`

### 🛠️ Features
- Scrapes real estate listings from sreality.cz using <b>Scrapy</b>
- Stores data in a PostgreSQL database using <b>psycopg2</b>
- Serves listings through a lightweight Python HTTP server
