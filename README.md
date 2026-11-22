# Django Product Catalog

A simple Django web application that models products, categories, and tags, allowing users to search products by description and filter by category and tags.

## Setup & Run Instructions

1. **Clone the repository**
   ```
   git clone https://github.com/NJ911/django-product-catalog.git
   cd django-product-catalog
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```
   python manage.py migrate
   ```

5. **Load sample data**
   ```
   python manage.py loaddata sample_data.json
   ```

6. **Start the server**
   ```
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser to view the application, or `http://127.0.0.1:8000/admin/` to access the admin panel.

## Assumptions & Notes

- **Pre-populated Items:** It is assumed that any item being searched for is already part of the product list populated via the Django Admin interface (5 categories, 10 tags, and 20 products).
- **Fallback Display:** If an item is not found in the list, the page displays all available products across all categories.
- **Combined Filtering:** Users can search by description and filter by category and tags individually or all at the same time.
- **Tag Logic:** Selecting multiple tags displays products matching any of the selected tags.
- **Sample Data:** sample_data.json is located in catalog/fixtures folder
