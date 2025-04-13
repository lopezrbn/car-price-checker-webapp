# car-price-checker-webapp

## 🚗 Project Overview

**car-price-checker-webapp** is the user-facing interface of the full-stack `car-price-checker` system.  
It allows users to input the details of their car and receive an estimated market value via a simple, responsive web interface.

This webapp is built with **[Reflex](https://reflex.dev)** — a Python framework that enables Data Scientists and backend developers to build complete web applications **using only Python**, without the need for JavaScript or frontend frameworks.

The app is live at:  
👉 [https://car-price-checker.lopezrbn.com/](https://car-price-checker.lopezrbn.com/)

---

## 📦 Repository Scope

This repository contains only the **web interface** of the system.

It is tightly coupled with the [car-price-checker-api](https://github.com/lopezrbn/car-price-checker-api) repository, which exposes a REST API used to compute real-time predictions based on a ML model.

---

## 🖥️ Webapp Functionality

- Drop-down selectors for:
  - Manufacturer
  - Model
  - Year
  - Month
  - Fuel type
  - Transmission
- Numeric inputs for:
  - Horsepower (HP)
  - Kilometers driven (Kms)
- A "Search" button that sends the data to the backend API and redirects to a results page.
- The predicted car price is shown clearly, along with a summary of the input.

The webapp is designed to be **minimalist, fast, and functional**, focusing on demonstrating a real-world ML use case.

---

## 📁 Code Structure

- `car-price-checker-webapp.py` – Main Reflex app entrypoint that registers pages.
- `state.py` – Core logic and state management, including API call logic and user interaction flow.
- `index.py` – UI page with the input form.
- `results.py` – UI page with the prediction output.
- `rxconfig.py` – Reflex configuration file (ports, app name, etc.).
- `reflex-bg-car-price-checker.service` – systemd unit file to run the app as a background service on Ubuntu.
- `nginx.conf` – Reverse proxy config to serve the app under a domain.

---

## ⚙️ Reflex Framework

Reflex handles both frontend and backend of the app internally:

- **Frontend** (served on port `3002`) – the visual interface seen by the user.
- **Backend** (served on port `8002`) – handles state, events, and API requests.

Thanks to Reflex, the entire app can be built and maintained using only Python.

---

## 🚀 Deployment

### `rxconfig.py` setup

```python
import reflex as rx

config = rx.Config(
    app_name="car-price-checker-webapp",
    frontend_port=3002,
    backend_port=8002,
)
```

### NGINX configuration

A reverse proxy is required to expose the Reflex app on a public domain. The frontend and backend must both be routed correctly, including WebSocket support:

```nginx
server {
    listen 80;
    server_name car-price-checker.lopezrbn.com;

    # Frontend (port 3002)
    location / {
        proxy_pass http://localhost:3002;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }

    # Backend (port 8002)
    location /_event {
        proxy_pass http://localhost:8002;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $host;
    }
}
```

### systemd service

You can run the Reflex app as a background service using systemd. An example unit file (`reflex-bg-car-price-checker.service`) is included:

```ini
[Unit]
Description=Car Price Checker Webapp (Reflex)
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/webapp
ExecStart=/path/to/.venv/bin/reflex run --env prod
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## ⚙️ Installation & Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/lopezrbn/car-price-checker-webapp.git
cd car-price-checker-webapp
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Reflex

```bash
pip install reflex
```

### 4. Run in development mode

```bash
reflex run
```

### 5. Export for production (optional)

```bash
reflex export --env prod
```

---

## 🛠 Tech Stack

- **Reflex** (Python web framework)
- **Python** for all logic and UI
- **FastAPI** (in backend API consumed by this app)
- **NGINX** as reverse proxy
- **systemd** for background service management

---

## 🔗 Live Demo

The app is deployed and available at:

👉 [https://car-price-checker.lopezrbn.com/](https://car-price-checker.lopezrbn.com/)

---

## 🚧 Future Improvements

- Add client-side input validation.
- Improve responsive design for mobile screens.
- Show loading indicators while waiting for predictions.
- Handle API errors more gracefully with user feedback.
- Expand to include visualizations or comparisons.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute the code with attribution.

---

## 📫 Contact

If you have any questions, suggestions, or feedback, feel free to reach out:

- **Rubén López**  
- Data Scientist  
- 📧 lopezrbn@gmail.com

---
