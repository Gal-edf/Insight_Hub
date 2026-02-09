import streamlit as st
import streamlit.components.v1 as components

# All code comments are written in English

# Professional Hub Configuration
st.set_page_config(page_title="Insight Hub", layout="wide", initial_sidebar_state="collapsed")

# --- NAVIGATION LOGIC ---
if 'current_app' not in st.session_state:
    st.session_state.current_app = 'hub'


def navigate_to(app_name):
    st.session_state.current_app = app_name


# --- DATA DEFINITION ---
# Added 'text_offset' to control spacing between icon and text per app
apps = {
    "operative": {
        "title": "Operative Dashboard",
        "description": "Light Up Performance",
        "url": "https://app.powerbi.com/reportEmbed?reportId=1ee02e78-e959-426a-b281-98d9a4fbdf54&autoAuth=true&ctid=38d142cb-643c-4f01-a704-99d5fffe36e4&chromeless=1&navContentPaneEnabled=false",
        "icon": "https://i.imgur.com/HWd95M3.png",
        "icon_size": "65px",
        "text_offset": "12px", # Standard spacing
        "category": ""
    },
    "bess": {
        "title": "BESS Dashboard",
        "description": "Charge Your Insight",
        "url": "https://app.powerbi.com/reportEmbed?reportId=e44bf9f4-492d-4098-80de-2b9658faea83&autoAuth=true&ctid=38d142cb-643c-4f01-a704-99d5fffe36e4&chromeless=1&navContentPaneEnabled=false",
        "icon": "https://i.imgur.com/zr9MwD0.png",
        "icon_size": "65px",
        "text_offset": "12px",
        "category": ""
    },
    "portfolio": {
        "title": "Portfolio Overview",
        "description": "One Grid Total Insights",
        "url": "https://app.powerbi.com/reportEmbed?reportId=0edd3e84-b6ab-4bc1-b670-53f26c133e19&autoAuth=true&ctid=38d142cb-643c-4f01-a704-99d5fffe36e4",
        "icon": "https://i.imgur.com/WX1KijU.png",
        "icon_size": "65px",
        "text_offset": "12px",
        "category": ""
    },
    "maps": {
        "title": "Site Navigator",
        "description": "Know Where Your Sites Are",
        "url": "https://app.powerbi.com/reportEmbed?reportId=1fb1aaae-7974-4171-b2d6-258b54a30a7a&autoAuth=true&ctid=38d142cb-643c-4f01-a704-99d5fffe36e4",
        "icon": "https://i.imgur.com/lVXwJ9d.png",
        "icon_size": "65px",
        "text_offset": "12px",
        "category": ""
    },
    "iec": {
        "title": "IEC Comparison",
        "description": "Our Data Their Records",
        "url": "https://app.powerbi.com/reportEmbed?reportId=e2c7c7ce-1e4d-4ce3-95e5-fe76b81d1662&autoAuth=true&ctid=38d142cb-643c-4f01-a704-99d5fffe36e4",
        "icon": "https://i.imgur.com/MslXbmI.png",
        "icon_size": "65px",
        "text_offset": "12px", # Reduced spacing to pull text up
        "category": ""
    },
    "soilsense": {
        "title": "",
        "description": "Turn Dust Into Energy",
        "url": "https://soilsense.streamlit.app",
        "icon": "https://i.imgur.com/09b9kI7.png",
        "icon_size": "200px",
        "text_offset": "-60px", # Reduced spacing to pull text up
        "category": ""
    }
}

# --- PAGE 1: THE DESIGNER HUB ---
if st.session_state.current_app == 'hub':

    # --- UI CONTROL VARIABLES ---
    card_width = "500px"
    card_height = "210px"
    title_font_size = "1.8rem"
    desc_font_size = "1.3rem"
    category_font_size = "12px"

    st.markdown(f"""
        <style>
        .dashboard-card {{
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            text-align: center;
            width: {card_width};
            height: {card_height};
            margin: 0 auto; 
            display: flex;
            flex-direction: column;
            justify-content: center; 
            align-items: center;    
            position: relative;
            border: 1px solid #eef2f6;
            overflow: hidden; /* Prevents large icons from breaking the card */
        }}

        .dashboard-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 120, 212, 0.12);
            border-color: #0078d4;
        }}

        .stButton button {{
            position: relative;
            top: -{card_height}; 
            width: {card_width} !important;
            height: {card_height} !important;
            margin: 0 auto !important; 
            display: block;
            background: transparent !important;
            color: transparent !important;
            border: none !important;
            z-index: 10;
            cursor: pointer;
            margin-bottom: -{card_height} !important; 
        }}

        .stButton button:hover, .stButton button:active, .stButton button:focus {{
            background: transparent !important;
            color: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }}

        [data-testid="stVerticalBlock"] {{
            gap: 1.2rem !important;
        }}
        </style>
        """, unsafe_allow_html=True)

    # --- CENTERED HEADER ---
    header_height = "150px"
    logo_width_px = 320

    h_left, h_center, h_right = st.columns([3, 6, 3])

    with h_left:
        logo_url = "https://i.imgur.com/TUIYtij.png"
        st.markdown(f'''
                    <div style="display: flex; justify-content: flex-start; align-items: center; height: {header_height}; width: 100%;">
                        <img src="{logo_url}" 
                             width="{logo_width_px}" 
                             style="display: block; height: auto; max-width: none !important;">
                    </div>
                ''', unsafe_allow_html=True)

    with h_center:
        st.markdown(f"""
                    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: {header_height}; text-align: center;">
                        <h1 style='color: #1e3d59; font-size: 3.5rem; margin-bottom: 0; line-height: 1;'> Insights Hub </h1>
                        <h1 style='color: #5f6368; font-size: 2rem; margin-top: 5px;'>Watts Of Wisdom</h1>
                    </div>
                """, unsafe_allow_html=True)

    with h_right:
        st.markdown(f"""
                    <div style="display: flex; justify-content: flex-end; align-items: center; height: {header_height};">
                        <p style="color: #5f6368; font-size: 2.2rem; margin: 0; font-weight: 600;">
                            © Performance
                        </p>
                    </div>
                """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    # --- CARD GRID ---
    col1, col2, col3 = st.columns(3)

    for i, (app_id, app_info) in enumerate(apps.items()):
        target_col = [col1, col2, col3][i % 3]

        with target_col:
            current_icon_size = app_info.get('icon_size', '60px')
            current_offset = app_info.get('text_offset', '12px')

            if app_info['icon'].startswith("http"):
                icon_html = f'<img src="{app_info["icon"]}" style="width: {current_icon_size}; max-height: 120px; object-fit: contain;">'
            else:
                icon_html = f'<div style="font-size: {current_icon_size};">{app_info["icon"]}</div>'

            # Render the visual Card (HTML)
            st.markdown(f"""
                    <div class="dashboard-card">
                        <div style="margin-bottom: {current_offset}; display: flex; justify-content: center; align-items: center;">
                            {icon_html}
                        </div>
                        <p style="color: #0078d4; font-weight: bold; font-size: {category_font_size}; text-transform: uppercase; margin:0;">{app_info['category']}</p>
                        <h3 style="color: #1e293b; margin: 8px 0; font-size: {title_font_size}; font-weight: 600; line-height: 1.2;">{app_info['title']}</h3>
                        <p style="color: #5f6368; font-size: {desc_font_size}; margin: 0; line-height: 1.3; max-width: 90%;">{app_info['description']}</p>
                    </div>
                """, unsafe_allow_html=True)

            # --- DYNAMIC NAVIGATION LOGIC ---
            # If the URL is an external Streamlit app, we use a transparent <a> link
            if "streamlit.app" in app_info["url"]:
                st.markdown(f"""
                        <a href="{app_info['url']}" target="_blank" style="
                            position: relative;
                            top: -{card_height};
                            width: {card_width};
                            height: {card_height};
                            display: block;
                            z-index: 100;
                            text-decoration: none;
                            background: transparent;
                            margin-bottom: -{card_height};
                        "></a>
                    """, unsafe_allow_html=True)
            else:
                # For PowerBI or internal pages, keep the original button logic
                if st.button("", key=f"btn_{app_id}", use_container_width=False):
                    navigate_to(app_id)
                    st.rerun()

# --- PAGE 2: THE DASHBOARD VIEW ---
else:
    # (Rest of the code remains unchanged)
    selected_app = apps[st.session_state.current_app]

    st.markdown("""
        <style>
        .block-container {
            padding-top: 3.5rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        .nav-bar {
            padding-left: 2rem;
            padding-right: 2rem;
            margin-bottom: 25px; 
        }
        .stVerticalBlock { gap: 0rem !important; }
        footer { visibility: hidden; }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
    h_col_empty, h_col_btn, h_col_spacer = st.columns([12, 1, 0.18])

    with h_col_btn:
        if st.button("⬅️ Back to Hub", use_container_width=True):
            navigate_to('hub')
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    if "YOUR_" in selected_app["url"]:
        st.warning(f"Configuration Required: Please update the URL for the **{selected_app['title']}** dashboard.")
    elif selected_app["url"] == "":
        st.info(f"Dashboard URL for **{selected_app['title']}** is not provided yet.")
    else:
        components.iframe(selected_app["url"], height=900, scrolling=False)