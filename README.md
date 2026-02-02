# Pro Grocery (Flask + LocalStorage)

A simple grocery web app built with Flask for page routing and HTML templates, while **seller accounts and grocery items are stored in the browser using `localStorage`**.

> Date: Feb 1, 2026

## Requirements

- Windows
- Python 3.12+ recommended
- Flask

## Setup

### 1) Create / activate virtual environment

If you already have `.venv/`, just activate it.

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**CMD**

```bat
.\.venv\Scripts\activate.bat
```

### 2) Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install flask
```

## Run the app

From the project folder:

```powershell
python app.py
```

Then open:

- http://127.0.0.1:5000/

## Pages / Routes

Main routes are defined in `app.py`:

- `/` → Home
- `/seller-portal` → Seller landing page
- `/seller_register` → New seller registration (stored in localStorage)
- `/sellers` → Registered seller list
- `/seller` → Seller dashboard (add/edit grocery items)
- `/seller-items?id=<sellerId>` → View a specific seller’s items (read-only)
- `/selected-items` → Shows selected/cart items (from localStorage)

## Data storage (Browser LocalStorage)

This project uses browser storage (not a server database).

### Sellers

Stored as an array under:

- `localStorage["sellers"] = [ seller, seller, ... ]`

Each seller looks like:

```json
{
  "id": "...",
  "shopName": "...",
  "ownerName": "...",
  "dob": "YYYY-MM-DD",
  "address": "...",
  "phone": "...",
  "items": [
    {
      "id": "...",
      "name": "...",
      "price": 10,
      "qty": 2,
      "qtyType": "pcs",
      "imageDataUrl": "data:image/jpeg;base64,..." 
    }
  ]
}
```

Active seller selection:

- `sessionStorage["activeSellerId"]` (preferred)
- `localStorage["activeSellerId"]` (fallback)

> Backward compatibility: some pages also read `localStorage["seller"]` (single seller object) if present.

### Selected items / cart

The selected-items page reads:

- `localStorage["cart"]` (preferred)
- `localStorage["selectedItems"]` (fallback)

Example:

```json
[
  { "name": "Rice", "price": 60, "qty": 2, "qtyType": "kg" }
]
```

## Static files

Flask serves static files from the `static/` folder.

- CSS should be located at `static/style.css`
- Templates link CSS like:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

## Notes / Troubleshooting

### CSS not applied

If pages look unstyled, check DevTools → Network for `/static/style.css`.

- Ensure the file exists at `static/style.css`
- Ensure templates use `url_for('static', filename='style.css')`

### LocalStorage limits

Images are stored as base64 strings. Browsers typically limit total localStorage to around ~5MB per origin.

- Use small images
- The seller dashboard resizes images before saving

## Project structure

Key files:

- `app.py` — Flask routes
- `templates/` — Flask templates
- `static/style.css` — CSS

## Next improvements (optional)

- Replace localStorage with a real database (SQLite) and server-side CRUD.
- Add authentication for sellers.
- Add delete-item support and customer-facing browsing/cart flows.
