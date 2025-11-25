# 🕷️ Link Reaper: The Ultimate Web Crawler

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-red?style=for-the-badge&logo=flask)
![Render](https://img.shields.io/badge/Deployed_on-Render-black?style=for-the-badge&logo=render)
![Status](https://img.shields.io/badge/Status-Live_&_Hunting-success?style=for-the-badge)

> **A lightweight, high-speed web crawler built for reconnaissance and data gathering.** > Scrapes target URLs, extracts all internal/external links, and returns structured JSON data or a visual report.

---

## 🚀 **Live Demo**
### [👉 CLICK HERE TO LAUNCH LINK REAPER](https://web-crawler-2mk7.onrender.com/)
*(Hosted on Render Free Tier - Give it 50s to wake up if it's sleeping!)*

---

## 📸 Interface
![App Screenshot](Screenshot.png)


---

## ⚡ Features
* **🕵️‍♂️ Stealth Mode:** Uses custom User-Agent headers to mimic a real browser and bypass basic anti-bot protections.
* **🌑 Dark Mode UI:** A clean, hacker-style interface for manual scraping.
* **🔗 API-First Design:** Can be used programmatically via cURL or Postman.
* **⚡ Fast Parsing:** Powered by `BeautifulSoup4` for rapid HTML extraction.
* **🛡️ Error Handling:** Gracefully handles 404s, timeouts, and invalid schemes.

---

## 🛠️ API Documentation
Want to use this in your own scripts? You don't need the UI. Just hit the endpoint.

### **Endpoint:** `GET /scrape`

**Parameters:**
- `url` (Required): The target website to crawl.

**Example Request:**
```bash
curl "
