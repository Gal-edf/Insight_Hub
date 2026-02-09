# ⚡ Insight Hub | Watts of Wisdom

A professional, high-performance navigation portal built with **Streamlit**. This application serves as a centralized "Control Tower" for accessing various PowerBI reports and specialized energy analytics tools.

## 🚀 Overview

The **Insight Hub** is designed to provide a seamless user experience for data-driven teams. Instead of managing multiple browser bookmarks, users can navigate through a sleek, card-based interface to access real-time operational data, portfolio insights, and battery storage performance.

## ✨ Key Features

* **Unified Dashboard:** A central entry point for all organizational reports.
* **PowerBI Integration:** Securely embeds PowerBI reports using high-performance iframes.
* **Custom UI/UX:** Built with custom CSS to provide a modern "SaaS" feel, including hover animations and responsive card layouts.
* **Dual-Navigation Logic:** Support for both internal embedded views and external application links.
* **Dynamic Scaling:** Automatically adjusts layout for different screen sizes.

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** [Streamlit](https://streamlit.io/)
* **Frontend:** Custom CSS / HTML Components
* **BI Integration:** Microsoft PowerBI Embedded

## 📂 Project Structure

| Module | Purpose |
| :--- | :--- |
| **Operative Dashboard** | Real-time performance monitoring. |
| **BESS Dashboard** | Battery Energy Storage System insights. |
| **Portfolio Overview** | Holistic grid and asset view. |
| **Site Navigator** | Geographic mapping of assets. |
| **IEC Comparison** | Data validation against official records. |
| **SoilSense** | Specialized solar cleaning/dust analytics. |

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/insight-hub.git](https://github.com/your-username/insight-hub.git)
   cd insight-hub
   
**Install requirements:**
   ```bash
   pip install streamlit
   ```
   3. **Run the application:**
   ```bash
    streamlit run your_filename.py 
    ```
   4. **Configuration:**
      To add or modify dashboards, update the apps dictionary in the source code:
       ```python 
   apps = {
       "app_id": {
           "title": "Display Name",
           "description": "Short Tagline",
           "url": "Your_PowerBI_Embed_URL",
           "icon": "Icon_URL",
           "category": "Department"
       }
   }
```   
5. **License:**
   Copyright © 2026 Performance. All rights reserved.  