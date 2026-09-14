"""
Lohith Sankar S — AI Engineer Portfolio & Copilot
Pixel-perfect implementation of new_UI/newui.png design mockup
Integrated scenic mountain header background from new_UI/headerimg.png
Fixed Left Profile & Control Panel, 4 Metric Tiles, Interactive Conversation Hub
100% Rule-Based Answers Grounded in Official Resume
"""

import os
import base64
from pathlib import Path
import streamlit as st

from resume_data import PROFILE_DATA, get_rule_based_answer

# Page Configuration - Hide Streamlit default sidebar
st.set_page_config(
    page_title="Lohith Sankar S | AI Engineer Portfolio & Copilot",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# Check for profile image
profile_img_candidates = [
    BASE_DIR / "profile image.png",
    BASE_DIR / "profile.png",
    BASE_DIR / "profile.jpg",
    BASE_DIR / "avatar.png",
]
PROFILE_IMG_PATH = None
for candidate in profile_img_candidates:
    if candidate.exists():
        PROFILE_IMG_PATH = candidate
        break

profile_img_b64 = ""
if PROFILE_IMG_PATH and PROFILE_IMG_PATH.exists():
    with open(PROFILE_IMG_PATH, "rb") as img_f:
        profile_img_b64 = base64.b64encode(img_f.read()).decode("utf-8")

# Check for scenic header background image
header_bg_candidates = [
    BASE_DIR / "assets" / "header_bg.jpg",
    BASE_DIR / "headerimg.png",
    BASE_DIR / "new_UI" / "headerimg.png",
    BASE_DIR / "header_bg.jpg",
]
header_bg_b64 = ""
for h_cand in header_bg_candidates:
    if h_cand.exists():
        with open(h_cand, "rb") as hf:
            header_bg_b64 = base64.b64encode(hf.read()).decode("utf-8")
        break

# Check for GitHub & LinkedIn logos
LOGOS_DIR = BASE_DIR / "Logos"
github_logo_candidates = [
    BASE_DIR / "github.png",
    BASE_DIR / "github_clean.png",
    LOGOS_DIR / "github.png",
    LOGOS_DIR / "github_clean.png",
]
linkedin_logo_candidates = [
    BASE_DIR / "linedin.png",
    BASE_DIR / "linkedin.png",
    LOGOS_DIR / "linedin.png",
    LOGOS_DIR / "linkedin.png",
]

github_img_b64 = ""
for g_cand in github_logo_candidates:
    if g_cand.exists():
        with open(g_cand, "rb") as gf:
            github_img_b64 = base64.b64encode(gf.read()).decode("utf-8")
        break

linkedin_img_b64 = ""
for l_cand in linkedin_logo_candidates:
    if l_cand.exists():
        with open(l_cand, "rb") as lf:
            linkedin_img_b64 = base64.b64encode(lf.read()).decode("utf-8")
        break

# Check for resume PDF across all known file naming variants (local & GitHub Cloud)
resume_candidates = [
    BASE_DIR / "Lohith_CS(AI)_Resume_.pdf",
    BASE_DIR / "Lohith_Sankar_S_Resume.pdf",
    BASE_DIR / "static" / "resume.pdf",
    BASE_DIR / "resume.pdf",
    BASE_DIR / "static" / "Lohith_CS(AI)_Resume_.pdf",
    BASE_DIR / "static" / "Lohith_Sankar_S_Resume.pdf",
]
RESUME_PDF_PATH = None
for r_path in resume_candidates:
    if r_path.exists():
        RESUME_PDF_PATH = r_path
        break

# Dynamic search fallback: find any .pdf in project root or static directory
if not RESUME_PDF_PATH:
    all_pdfs = list(BASE_DIR.glob("*.pdf"))
    if (BASE_DIR / "static").exists():
        all_pdfs += list((BASE_DIR / "static").glob("*.pdf"))
    for pdf_f in all_pdfs:
        if pdf_f.is_file():
            RESUME_PDF_PATH = pdf_f
            break

resume_bytes = b""
if RESUME_PDF_PATH and RESUME_PDF_PATH.exists():
    with open(RESUME_PDF_PATH, "rb") as f:
        resume_bytes = f.read()

# Cloud fallback: if local file read produced empty bytes, fetch directly from GitHub repository
if not resume_bytes:
    try:
        import urllib.request
        raw_url = "https://raw.githubusercontent.com/Loh2004/Portfolio_Chatbot/main/Lohith_CS(AI)_Resume_.pdf"
        with urllib.request.urlopen(raw_url, timeout=5) as resp:
            resume_bytes = resp.read()
    except Exception:
        pass

# -------------------------------------------------------------
# 🎨 HIGH-FIDELITY CSS DESIGN SYSTEM (MATCHING newui.png)
# -------------------------------------------------------------
UI_DESIGN_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Caveat:wght@500;600;700&display=swap');

/* Typography rule */
html, body, p, h1, h2, h3, h4, h5, h6, input, select, textarea, div.stMarkdown {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}}

/* Hide collapsible sidebar completely */
[data-testid="stSidebar"],
[data-testid="stSidebarCollapseButton"],
[data-testid="collapsedControl"] {{
    display: none !important;
}}

/* Deep Midnight Blue Page Background */
.stApp {{
    background-color: #070b14 !important;
    color: #f8fafc !important;
}}

/* Layout Container */
.block-container {{
    padding-top: 1.4rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1460px !important;
}}

/* Sticky Left Panel */
div[data-testid="column"]:first-child {{
    position: sticky !important;
    top: 1.2rem !important;
    align-self: flex-start !important;
}}

/* --------------------------------------------------------- */
/* 🌟 LEFT SIDEBAR CARD (MATCHING newui.png) 🌟             */
/* --------------------------------------------------------- */
.sidebar-panel-card {{
    background-color: #0c1322 !important;
    border: 1.5px solid #17233d !important;
    border-radius: 24px !important;
    padding: 22px 20px !important;
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6) !important;
}}

.sidebar-header-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 18px;
}}

.sidebar-brand-icon {{
    width: 32px;
    height: 32px;
    flex-shrink: 0;
}}

.sidebar-brand-title {{
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin: 0 !important;
    line-height: 1.2 !important;
}}

.sidebar-brand-sub {{
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    color: #94a3b8 !important;
    margin: 2px 0 0 0 !important;
    line-height: 1.2 !important;
}}

.sidebar-moon-btn {{
    margin-left: auto;
    font-size: 1.15rem;
    color: #cbd5e1;
    cursor: pointer;
}}

/* Avatar with Glowing Cyan Neon Halo */
.avatar-center-box {{
    display: flex;
    justify-content: center;
    margin: 10px 0 14px 0;
}}

.avatar-neon-img {{
    width: 122px;
    height: 122px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 0 0 3px #0284c7, 0 0 28px rgba(56, 189, 248, 0.55), 0 8px 24px rgba(0, 0, 0, 0.6);
}}

/* Status Pill */
.status-pill-box {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #091724;
    border: 1.5px solid #059669;
    border-radius: 20px;
    padding: 7px 16px;
    margin: 12px 0 20px 0;
    text-decoration: none;
}}

.status-dot-text {{
    display: flex;
    align-items: center;
    gap: 8px;
    color: #34d399 !important;
    font-size: 0.82rem;
    font-weight: 700;
}}

.status-green-dot {{
    width: 8px;
    height: 8px;
    background-color: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10b981;
}}

.status-chevron {{
    color: #059669;
    font-weight: 800;
    font-size: 0.85rem;
}}

/* Portfolio Menu */
.menu-section-title {{
    font-size: 0.74rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.12em !important;
    color: #64748b !important;
    text-transform: uppercase !important;
    margin: 0 0 10px 0 !important;
}}

.menu-item-btn {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 12px;
    margin-bottom: 9px;
    text-decoration: none !important;
    transition: all 0.22s ease;
    cursor: pointer;
    background: #0d1527;
    border: 1.5px solid #1c2a47;
}}

.menu-item-btn.active {{
    background: linear-gradient(90deg, #13274f 0%, #1a3666 100%) !important;
    border: 1.5px solid #38bdf8 !important;
    box-shadow: 0 0 20px rgba(56, 189, 248, 0.25) !important;
}}

.menu-item-btn:hover {{
    border-color: #38bdf8;
    background: #142240;
    transform: translateY(-1px);
}}

.menu-item-icon {{
    width: 22px;
    height: 22px;
    object-fit: contain;
    flex-shrink: 0;
}}

.menu-item-label {{
    font-size: 0.94rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
}}

.menu-item-chevron {{
    margin-left: auto;
    color: #38bdf8;
    font-size: 0.95rem;
    font-weight: 800;
}}

/* Contact Block */
.contact-info-list {{
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin: 18px 0;
}}

.contact-info-item {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.contact-icon-box {{
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: #101a2d;
    border: 1.5px solid #1c2b4a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.05rem;
    color: #94a3b8;
    flex-shrink: 0;
}}

.contact-text-meta {{
    display: flex;
    flex-direction: column;
}}

.contact-label {{
    font-size: 0.72rem !important;
    color: #94a3b8 !important;
    font-weight: 600 !important;
    text-transform: capitalize;
    line-height: 1.2;
}}

.contact-val {{
    font-size: 0.86rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    line-height: 1.2;
    text-decoration: none !important;
}}

.contact-val.cyan {{
    color: #38bdf8 !important;
}}

/* Resume CTA Header & Pulse Badge */
.resume-cta-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 18px;
    margin-bottom: 8px;
    padding: 0 4px;
}}

.resume-cta-title {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    color: #38bdf8;
    text-transform: uppercase;
}}

.resume-badge-pulse {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #38bdf8;
    box-shadow: 0 0 10px #38bdf8;
    animation: resumePulse 2s infinite ease-in-out;
}}

@keyframes resumePulse {{
    0%, 100% {{ transform: scale(1); opacity: 0.85; box-shadow: 0 0 8px #38bdf8; }}
    50% {{ transform: scale(1.35); opacity: 1; box-shadow: 0 0 16px #38bdf8; }}
}}

.resume-tag {{
    font-size: 0.76rem;
    font-weight: 800;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.4);
    border-radius: 6px;
    padding: 2px 8px;
    letter-spacing: 0.04em;
}}

/* 🌟 HIGHLIGHTED DOWNLOAD RESUME BOX & LABEL (DESKTOP & MOBILE) 🌟 */
div[data-testid="stDownloadButton"] {{
    width: 100% !important;
    margin-bottom: 12px !important;
}}

div[data-testid="stDownloadButton"] > button,
.resume-download-btn {{
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 50%, #4f46e5 100%) !important;
    color: #ffffff !important;
    border: 2px solid #38bdf8 !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.02em !important;
    padding: 14px 20px !important;
    min-height: 54px !important;
    box-shadow: 0 6px 24px rgba(56, 189, 248, 0.45), 0 0 14px rgba(2, 132, 199, 0.35) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 10px !important;
    width: 100% !important;
    cursor: pointer !important;
    text-decoration: none !important;
}}

div[data-testid="stDownloadButton"] > button p,
div[data-testid="stDownloadButton"] > button span,
.resume-download-btn span {{
    color: #ffffff !important;
    font-weight: 900 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.02em !important;
    margin: 0 !important;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.5) !important;
}}

div[data-testid="stDownloadButton"] > button:hover,
.resume-download-btn:hover {{
    background: linear-gradient(135deg, #0ea5e9 0%, #3b82f6 50%, #6366f1 100%) !important;
    border-color: #a5f3fc !important;
    box-shadow: 0 8px 32px rgba(56, 189, 248, 0.65), 0 0 22px rgba(56, 189, 248, 0.6) !important;
    transform: translateY(-2px) !important;
    color: #ffffff !important;
}}

div[data-testid="stDownloadButton"] > button:active,
.resume-download-btn:active {{
    transform: translateY(1px) !important;
    box-shadow: 0 2px 10px rgba(56, 189, 248, 0.4) !important;
}}

/* Hero Banner Direct Download Pill Button */
.hero-download-badge-row {{
    margin-top: 14px;
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
}}

.hero-resume-download-link {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%) !important;
    border: 2px solid #38bdf8 !important;
    color: #ffffff !important;
    border-radius: 30px !important;
    padding: 9px 20px !important;
    font-size: 0.92rem !important;
    font-weight: 800 !important;
    text-decoration: none !important;
    box-shadow: 0 4px 20px rgba(56, 189, 248, 0.45), 0 0 10px rgba(2, 132, 199, 0.35) !important;
    transition: all 0.22s ease !important;
}}

.hero-resume-download-link:hover {{
    transform: translateY(-2px) !important;
    border-color: #a5f3fc !important;
    box-shadow: 0 6px 28px rgba(56, 189, 248, 0.65) !important;
    color: #ffffff !important;
}}

/* Clear Chat Button */
.clear-chat-gradient-btn {{
    background: linear-gradient(90deg, #818cf8 0%, #38bdf8 100%) !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 800 !important;
    box-shadow: 0 4px 20px rgba(56, 189, 248, 0.35) !important;
}}

.clear-chat-gradient-btn:hover {{
    box-shadow: 0 6px 26px rgba(56, 189, 248, 0.55) !important;
    transform: translateY(-2px) !important;
}}

/* Footer Handwritten Script */
.sidebar-footer-script {{
    font-family: 'Caveat', cursive !important;
    font-size: 1.5rem !important;
    color: #94a3b8 !important;
    text-align: center;
    margin: 14px 0 4px 0;
    position: relative;
}}

.script-underline {{
    width: 65px;
    height: 2px;
    background: #64748b;
    margin: 2px auto 0 auto;
    border-radius: 2px;
}}

/* --------------------------------------------------------- */
/* 🌟 RIGHT COLUMN: HERO BANNER (MATCHING newui.png) 🌟     */
/* --------------------------------------------------------- */
.hero-banner-box {{
    background: linear-gradient(90deg, #070c17 0%, #070c17 40%, rgba(7, 12, 23, 0.78) 64%, rgba(7, 12, 23, 0.25) 100%),
                url('data:image/jpeg;base64,{header_bg_b64}') right center / cover no-repeat !important;
    border: 1.5px solid #1a2946 !important;
    border-radius: 24px !important;
    padding: 34px 38px !important;
    margin-bottom: 20px !important;
    min-height: 250px !important;
    position: relative !important;
    box-shadow: 0 14px 45px rgba(0, 0, 0, 0.55) !important;
}}

.hero-tagline {{
    font-size: 0.8rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.14em !important;
    color: #94a3b8 !important;
    text-transform: uppercase !important;
    margin-bottom: 8px !important;
}}

.hero-title-main {{
    font-size: 2.85rem !important;
    font-weight: 900 !important;
    color: #38bdf8 !important;
    margin: 0 0 6px 0 !important;
    line-height: 1.15 !important;
    letter-spacing: -0.02em !important;
}}

.hero-sub-academic {{
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin: 0 0 4px 0 !important;
}}

.hero-sub-college {{
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    color: #cbd5e1 !important;
    margin: 0 0 12px 0 !important;
}}

.hero-location-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.88rem;
    font-weight: 700;
    color: #f8fafc;
}}

.hero-impact-script {{
    position: absolute;
    right: 38px;
    bottom: 24px;
    font-family: 'Caveat', cursive !important;
    font-size: 2.1rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    text-shadow: 0 2px 14px rgba(0, 0, 0, 0.85);
    line-height: 1.1;
    transform: rotate(-3deg);
}}

/* --------------------------------------------------------- */
/* 🌟 4 METRIC CARDS (MATCHING newui.png) 🌟                */
/* --------------------------------------------------------- */
.metric-card-box {{
    background-color: #0d1527 !important;
    border: 1.5px solid #1c2a47 !important;
    border-radius: 20px !important;
    padding: 18px 20px !important;
    transition: all 0.22s ease !important;
}}

.metric-card-box:hover {{
    border-color: #38bdf8 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(56, 189, 248, 0.2) !important;
}}

.metric-top-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.metric-icon-circle {{
    width: 44px;
    height: 44px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
}}

.metric-icon-blue {{
    background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
}}

.metric-icon-green {{
    background: linear-gradient(135deg, #059669 0%, #10b981 100%);
}}

.metric-icon-amber {{
    background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%);
}}

.metric-icon-pink {{
    background: linear-gradient(135deg, #be185d 0%, #ec4899 100%);
}}

.metric-big-num {{
    font-size: 1.95rem !important;
    font-weight: 900 !important;
    line-height: 1 !important;
}}

.num-blue {{ color: #60a5fa !important; }}
.num-green {{ color: #34d399 !important; }}
.num-amber {{ color: #fbbf24 !important; }}
.num-pink {{ color: #f472b6 !important; }}

.metric-title-text {{
    font-size: 0.84rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.06em !important;
    color: #f8fafc !important;
    text-transform: uppercase !important;
    margin: 14px 0 3px 0 !important;
}}

.metric-bottom-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.8rem !important;
    color: #94a3b8 !important;
}}

.metric-chevron {{
    font-weight: 800;
    font-size: 0.85rem;
}}

/* --------------------------------------------------------- */
/* 🌟 INTERACTIVE CONVERSATION HUB (MATCHING newui.png) 🌟   */
/* --------------------------------------------------------- */
.chat-outer-card {{
    background-color: #0c1424 !important;
    border: 1.5px solid #1a2744 !important;
    border-radius: 24px !important;
    padding: 26px 28px !important;
    margin-top: 22px !important;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.5) !important;
}}

.chat-header-row {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.chat-bubble-badge {{
    width: 38px;
    height: 38px;
    border-radius: 12px;
    background: #142647;
    border: 1.5px solid #233c6a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
}}

.chat-header-title {{
    font-size: 1.28rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin: 0 !important;
}}

.chat-soundwave {{
    color: #10b981;
    font-size: 1.15rem;
    font-weight: 800;
    margin-left: 4px;
}}

.chat-header-sub {{
    color: #94a3b8 !important;
    font-size: 0.92rem !important;
    margin: 6px 0 16px 0 !important;
    line-height: 1.5 !important;
}}

/* Quick Dropdown Card */
.inquiry-dropdown-box {{
    background: #111b30;
    border: 1.5px solid #203156;
    border-radius: 16px;
    padding: 14px 18px;
    margin: 16px 0 20px 0;
}}

.inquiry-box-title {{
    display: flex;
    align-items: center;
    gap: 8px;
    color: #38bdf8;
    font-size: 0.9rem;
    font-weight: 800;
    margin-bottom: 8px;
}}

/* Custom Streamlit Selectbox */
div[data-baseweb="select"] > div {{
    background-color: #0b1322 !important;
    border: 1.5px solid #233659 !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    min-height: 44px !important;
}}

div[data-baseweb="select"] span {{
    color: #ffffff !important;
    font-size: 0.96rem !important;
    font-weight: 600 !important;
}}

ul[role="listbox"] {{
    background-color: #0d1527 !important;
    border: 1.5px solid #233659 !important;
    border-radius: 10px !important;
}}

li[role="option"] {{
    color: #ffffff !important;
    font-size: 0.95rem !important;
    padding: 10px 16px !important;
}}

li[role="option"]:hover, li[aria-selected="true"] {{
    background-color: #1a2d52 !important;
    color: #38bdf8 !important;
}}

/* Digital Twin Message Card */
.digital-twin-bubble {{
    background-color: #101b33;
    border: 1.5px solid #1e2f54;
    border-radius: 18px;
    padding: 20px 24px;
    margin: 16px 0;
}}

.dt-header-row {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 12px;
}}

.dt-avatar-img {{
    width: 38px;
    height: 38px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #38bdf8;
}}

.dt-title-text {{
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    margin: 0 !important;
}}

.dt-body-text {{
    color: #e2e8f0 !important;
    font-size: 0.98rem !important;
    line-height: 1.68 !important;
    margin: 0 !important;
}}

/* Streamlit Chat Messages */
[data-testid="stChatMessage"] {{
    background-color: #101b33 !important;
    border: 1.5px solid #1e2f54 !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    margin-bottom: 12px !important;
}}

[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li {{
    color: #ffffff !important;
    font-size: 0.98rem !important;
    line-height: 1.68 !important;
}}

[data-testid="stChatMessage"] strong {{
    color: #38bdf8 !important;
}}

/* Chat Input Bar */
[data-testid="stChatInput"] textarea {{
    background-color: #10192d !important;
    color: #ffffff !important;
    border: 1.5px solid #233454 !important;
    border-radius: 24px !important;
    font-size: 0.98rem !important;
    padding: 12px 18px !important;
}}

[data-testid="stChatInput"] textarea:focus {{
    border-color: #38bdf8 !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.4) !important;
}}

/* Content Card for Other Sections */
.content-card {{
    background-color: #0c1424 !important;
    border: 1.5px solid #1a2744 !important;
    border-radius: 20px !important;
    padding: 24px !important;
    margin-bottom: 18px !important;
}}

.tech-pill {{
    display: inline-block;
    background-color: #10192d !important;
    color: #f1f5f9 !important;
    border: 1px solid #233659 !important;
    border-radius: 8px !important;
    padding: 5px 12px !important;
    font-size: 0.86rem !important;
    font-family: 'JetBrains Mono', monospace !important;
    margin: 4px 3px !important;
    font-weight: 600 !important;
}}

.badge-cyan {{
    display: inline-block;
    background-color: rgba(2, 132, 199, 0.3) !important;
    color: #38bdf8 !important;
    border: 1.5px solid #0284c7 !important;
    border-radius: 20px !important;
    padding: 4px 14px !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
}}

.pub-pill {{
    display: inline-block;
    background-color: rgba(124, 58, 237, 0.3) !important;
    color: #d8b4fe !important;
    border: 1.5px solid #7c3aed !important;
    border-radius: 20px !important;
    padding: 5px 16px !important;
    font-size: 0.86rem !important;
    font-weight: 700 !important;
}}

/* Custom primary buttons */
div.stButton > button {{
    background: linear-gradient(90deg, #818cf8 0%, #38bdf8 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-weight: 800 !important;
    padding: 10px 22px !important;
    font-size: 0.95rem !important;
    box-shadow: 0 4px 18px rgba(56, 189, 248, 0.3) !important;
}}

div.stButton > button:hover {{
    box-shadow: 0 6px 24px rgba(56, 189, 248, 0.5) !important;
    transform: translateY(-1px) !important;
}}

/* 📱 Responsive Mobile Enhancements */
@media (max-width: 768px) {{
    div[data-testid="stDownloadButton"] > button,
    .resume-download-btn {{
        min-height: 58px !important;
        font-size: 1.08rem !important;
        padding: 16px 20px !important;
        border-width: 2.5px !important;
        box-shadow: 0 8px 30px rgba(56, 189, 248, 0.55), 0 0 20px rgba(2, 132, 199, 0.5) !important;
    }}

    div[data-testid="stDownloadButton"] > button p,
    .resume-download-btn span {{
        font-size: 1.08rem !important;
        font-weight: 900 !important;
    }}

    .hero-banner-box {{
        padding: 24px 20px !important;
        min-height: auto !important;
    }}

    .hero-title-main {{
        font-size: 2.2rem !important;
    }}

    .hero-impact-script {{
        position: static !important;
        margin-top: 14px !important;
        text-align: right !important;
        font-size: 1.7rem !important;
    }}
}}
</style>
"""
st.markdown(UI_DESIGN_CSS, unsafe_allow_html=True)

# -------------------------------------------------------------
# 🌟 UNIFIED 2-COLUMN MAIN PAGE LAYOUT (NO SIDEBAR GLITCHES) 🌟
# -------------------------------------------------------------
left_col, right_col = st.columns([1, 2.6], gap="large")

# =============================================================
# LEFT COLUMN: FIXED PROFILE & CONTROL PANEL (MATCHING newui.png)
# =============================================================
with left_col:
    # Top Mini Header (Glowing Logo + Name + Moon Icon)
    neon_star_svg = """<svg class="sidebar-brand-icon" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="neonGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#a855f7" />
                <stop offset="50%" stop-color="#6366f1" />
                <stop offset="100%" stop-color="#38bdf8" />
            </linearGradient>
        </defs>
        <path d="M50 0 C50 32 68 50 100 50 C68 50 50 68 50 100 C50 68 32 50 0 50 C32 50 50 32 50 0 Z" fill="url(#neonGrad)" />
    </svg>"""

    # Sidebar Header HTML
    sidebar_top_html = (
        f'<div class="sidebar-panel-card">'
        f'<div class="sidebar-header-row">'
        f'{neon_star_svg}'
        f'<div>'
        f'<div class="sidebar-brand-title">Lohith Sankar S</div>'
        f'<div class="sidebar-brand-sub">B.Tech CSE (Artificial Intelligence)</div>'
        f'</div>'
        f'<div class="sidebar-moon-btn">🌙</div>'
        f'</div>'
    )

    # Avatar with Glowing Halo
    if profile_img_b64:
        sidebar_top_html += (
            f'<div class="avatar-center-box">'
            f'<img src="data:image/png;base64,{profile_img_b64}" class="avatar-neon-img" alt="Lohith Sankar S" />'
            f'</div>'
        )
    else:
        sidebar_top_html += (
            f'<div class="avatar-center-box">'
            f'<div style="width: 122px; height: 122px; border-radius: 50%; background: linear-gradient(135deg, #0284c7, #6366f1); display: flex; align-items: center; justify-content: center; font-size: 42px; font-weight: 800; color: #ffffff; box-shadow: 0 0 28px rgba(56, 189, 248, 0.55);">'
            f'LS'
            f'</div>'
            f'</div>'
        )

    # Status Pill (Open for AI / SWE Roles >)
    sidebar_top_html += (
        f'<div class="status-pill-box">'
        f'<div class="status-dot-text">'
        f'<span class="status-green-dot"></span>'
        f'<span>Open for AI / SWE Roles</span>'
        f'</div>'
        f'<span class="status-chevron">&#10095;</span>'
        f'</div>'
    )

    # Section: PORTFOLIO MENU
    sidebar_top_html += f'<div class="menu-section-title">PORTFOLIO MENU</div>'

    # 1. Chat with Lohith AI (Active Menu Pill)
    sidebar_top_html += (
        f'<div class="menu-item-btn active">'
        f'<span style="font-size: 1.15rem;">💬</span>'
        f'<span class="menu-item-label">Chat with Lohith AI</span>'
        f'<span class="menu-item-chevron">&#10095;</span>'
        f'</div>'
    )

    # 2. Connect to LinkedIn (Official LinkedIn Logo)
    if linkedin_img_b64:
        linkedin_icon_html = f'<img src="data:image/png;base64,{linkedin_img_b64}" class="menu-item-icon" alt="LinkedIn Logo" />'
    else:
        linkedin_icon_html = '<svg class="menu-item-icon" viewBox="0 0 24 24" width="20" height="20" fill="#0a66c2" style="flex-shrink: 0;"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.25V10.9H6.46M7.86 6.81a1.45 1.45 0 0 0-1.45 1.45 1.45 1.45 0 0 0 1.45 1.45 1.45 1.45 0 0 0 1.45-1.45 1.45 1.45 0 0 0-1.45-1.45Z"/></svg>'

    sidebar_top_html += (
        f'<a href="{PROFILE_DATA["personal"]["linkedin"]}" target="_blank" rel="noopener noreferrer" class="menu-item-btn">'
        f'{linkedin_icon_html}'
        f'<span class="menu-item-label">Connect to LinkedIn</span>'
        f'<span class="menu-item-chevron" style="color: #64748b;">&#10095;</span>'
        f'</a>'
    )

    # 3. Connect to GitHub (Official White Octocat Logo)
    if github_img_b64:
        github_icon_html = f'<img src="data:image/png;base64,{github_img_b64}" class="menu-item-icon" alt="GitHub Logo" />'
    else:
        github_icon_html = '<svg class="menu-item-icon" viewBox="0 0 24 24" width="20" height="20" fill="#ffffff" style="flex-shrink: 0;"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>'

    sidebar_top_html += (
        f'<a href="{PROFILE_DATA["personal"]["github"]}" target="_blank" rel="noopener noreferrer" class="menu-item-btn">'
        f'{github_icon_html}'
        f'<span class="menu-item-label">Connect to GitHub</span>'
        f'<span class="menu-item-chevron" style="color: #64748b;">&#10095;</span>'
        f'</a>'
    )

    # Contact Info Block (Email, Phone, Location with Rounded Icon Badges)
    sidebar_top_html += (
        f'<div class="contact-info-list">'
        f'<div class="contact-info-item">'
        f'<div class="contact-icon-box">✉</div>'
        f'<div class="contact-text-meta">'
        f'<div class="contact-label">Email</div>'
        f'<a href="mailto:{PROFILE_DATA["personal"]["email"]}" class="contact-val cyan">{PROFILE_DATA["personal"]["email"]}</a>'
        f'</div>'
        f'</div>'
        f'<div class="contact-info-item">'
        f'<div class="contact-icon-box">📞</div>'
        f'<div class="contact-text-meta">'
        f'<div class="contact-label">Phone</div>'
        f'<div class="contact-val">{PROFILE_DATA["personal"]["phone"]}</div>'
        f'</div>'
        f'</div>'
        f'<div class="contact-info-item">'
        f'<div class="contact-icon-box">📍</div>'
        f'<div class="contact-text-meta">'
        f'<div class="contact-label">Location</div>'
        f'<div class="contact-val">{PROFILE_DATA["personal"]["location"]}</div>'
        f'</div>'
        f'</div>'
        f'</div>'
    )

    sidebar_top_html += f'</div>'
    st.html(sidebar_top_html)

    # Section Navigation Dropdown (Seamless switching to other portfolio views)
    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)
    active_section = st.selectbox(
        "Navigate Portfolio Views:",
        [
            "💬 Chat with Lohith AI",
            "🚀 Featured Projects",
            "💻 Skills & Tech Stack",
            "🎓 Education & Publications",
            "🏢 Work Experience",
        ],
        index=0,
        label_visibility="collapsed"
    )

    # 🌟 Highlighted Resume Download Box (Prominent on Desktop & Mobile) 🌟
    st.markdown(
        """<div class="resume-cta-header">
            <div class="resume-cta-title">
                <span class="resume-badge-pulse"></span>
                <span>OFFICIAL RESUME</span>
            </div>
            <span class="resume-tag">PDF &bull; UPDATED</span>
        </div>""",
        unsafe_allow_html=True
    )

    if resume_bytes:
        st.download_button(
            label="📄 DOWNLOAD OFFICIAL RESUME (PDF)",
            data=resume_bytes,
            file_name="Lohith_CS(AI)_Resume_.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.markdown(
            '<a href="https://raw.githubusercontent.com/Loh2004/Portfolio_Chatbot/main/Lohith_CS(AI)_Resume_.pdf" download="Lohith_CS(AI)_Resume_.pdf" target="_blank" class="sidebar-action-btn resume-download-btn">'
            '<span>📄</span> <span>DOWNLOAD OFFICIAL RESUME (PDF)</span>'
            '</a>',
            unsafe_allow_html=True
        )

    # Clear Chat History Button (matching newui.png gradient button)
    if st.button("✨ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.pending_query = None
        st.rerun()

    # Footer Handwritten Script ("Build • Learn • Grow")
    st.html(
        '<div class="sidebar-footer-script">'
        'Build &bull; Learn &bull; Grow'
        '<div class="script-underline"></div>'
        '</div>'
    )

# =============================================================
# RIGHT COLUMN: HERO BANNER, METRIC TILES & INTERACTIVE CONTENT
# =============================================================
with right_col:
    # 🌟 HERO HEADER BANNER (EXACT MATCH WITH newui.png & headerimg.png) 🌟
    hero_html = (
        f'<div class="hero-banner-box">'
        f'<div class="hero-tagline">ARTIFICIAL INTELLIGENCE &bull; EMBEDDED IOT &bull; FULL-STACK SOFTWARE</div>'
        f'<h1 class="hero-title-main">Lohith Sankar <span style="color: #c084fc;">S</span></h1>'
        f'<div class="hero-sub-academic">B.Tech <span style="color: #38bdf8; font-weight: 800;">in Computer Science & Engineering (Artificial Intelligence)</span></div>'
        f'<div class="hero-sub-college" style="display: flex; align-items: center; gap: 8px; font-size: 0.98rem; font-weight: 600; color: #cbd5e1; margin-top: 6px;">'
        f'<span>📍</span><span>Mar Baselios College of Engineering and Technology (Autonomous), Thiruvananthapuram</span>'
        f'</div>'
        f'<div class="hero-download-badge-row">'
        f'<a href="https://raw.githubusercontent.com/Loh2004/Portfolio_Chatbot/main/Lohith_CS(AI)_Resume_.pdf" download="Lohith_CS(AI)_Resume_.pdf" target="_blank" class="hero-resume-download-link">'
        f'<span>📄</span><span>Download Official Resume (PDF)</span><span style="font-weight: 900; font-size: 1.05rem; margin-left: 2px;">&#10095;</span>'
        f'</a>'
        f'</div>'
        f'<div class="hero-impact-script">Ideas<br><span style="font-size: 1.4rem;">into</span><br>Impact<div style="width: 70px; height: 2px; background: #ffffff; margin: 2px auto 0 auto;"></div></div>'
        f'</div>'
    )
    st.html(hero_html)

    # 🌟 4 METRIC STATS TILES (MATCHING newui.png) 🌟
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.html(
            '<div class="metric-card-box">'
            '<div class="metric-top-row">'
            '<div class="metric-icon-circle metric-icon-blue">🎓</div>'
            '<div class="metric-big-num num-blue">4+</div>'
            '</div>'
            '<div class="metric-title-text">AI & ML PROJECTS</div>'
            '<div class="metric-bottom-row">'
            '<span>Built real-world solutions</span>'
            '<span class="metric-chevron" style="color: #60a5fa;">&#10095;</span>'
            '</div>'
            '</div>'
        )

    with m2:
        st.html(
            '<div class="metric-card-box">'
            '<div class="metric-top-row">'
            '<div class="metric-icon-circle metric-icon-green">📄</div>'
            '<div class="metric-big-num num-green">1</div>'
            '</div>'
            '<div class="metric-title-text">ICSAIC-2026 PAPER</div>'
            '<div class="metric-bottom-row">'
            '<span>Research & Innovation</span>'
            '<span class="metric-chevron" style="color: #34d399;">&#10095;</span>'
            '</div>'
            '</div>'
        )

    with m3:
        st.html(
            '<div class="metric-card-box">'
            '<div class="metric-top-row">'
            '<div class="metric-icon-circle metric-icon-amber">📅</div>'
            '<div class="metric-big-num num-amber">2026</div>'
            '</div>'
            '<div class="metric-title-text">B.TECH AI GRADUATE</div>'
            '<div class="metric-bottom-row">'
            '<span>Next chapter awaits</span>'
            '<span class="metric-chevron" style="color: #fbbf24;">&#10095;</span>'
            '</div>'
            '</div>'
        )

    with m4:
        st.html(
            '<div class="metric-card-box">'
            '<div class="metric-top-row">'
            '<div class="metric-icon-circle metric-icon-pink">💡</div>'
            '<div class="metric-big-num num-pink" style="font-size: 1.55rem;">IoT + AI</div>'
            '</div>'
            '<div class="metric-title-text">HARDWARE & VISION</div>'
            '<div class="metric-bottom-row">'
            '<span>Building smart systems</span>'
            '<span class="metric-chevron" style="color: #f472b6;">&#10095;</span>'
            '</div>'
            '</div>'
        )

    # -------------------------------------------------------------
    # SECTION 1: CHAT WITH LOHITH AI (MATCHING newui.png)
    # -------------------------------------------------------------
    if active_section == "💬 Chat with Lohith AI":
        # Conversation Container Header matching newui.png
        chat_header_html = (
            f'<div class="chat-outer-card">'
            f'<div class="chat-header-row">'
            f'<div class="chat-bubble-badge">💬</div>'
            f'<div class="chat-header-title">Interactive Portfolio Conversation <span class="chat-soundwave">&bull;||&bull;</span></div>'
            f'</div>'
            f'<div class="chat-header-sub">Ask me anything about my AI/Engineering projects, technical skills, research, or education! Answers are grounded directly in my verified resume.</div>'
            f'</div>'
        )
        st.html(chat_header_html)

        # State initialization
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        faq_options = [
            "--- Choose a question here, to ask immediately, or type below ---",
            "👋 Who is Lohith? (Introduction & Background)",
            "🛡️ Tell me about ZenGuard (Published Research & IoT)",
            "⚡ How does Genei AI Voice Assistant work?",
            "⚽ Tell me about FootLink (Football ML Platform)",
            "🚙 Tell me about EcoRanger (Autonomous Wildlife Rover)",
            "💻 What is your complete technical skill set?",
            "🎓 Where did you study? (Education & College)",
            "📫 How can I contact Lohith?",
            "📄 How can I download your official resume?",
        ]

        def on_faq_selected():
            selected = st.session_state.get("faq_dropdown_val")
            if selected and not selected.startswith("---"):
                query_map = {
                    "👋 Who is Lohith? (Introduction & Background)": "Tell me about yourself and your background",
                    "🛡️ Tell me about ZenGuard (Published Research & IoT)": "Tell me about your published project ZenGuard",
                    "⚡ How does Genei AI Voice Assistant work?": "How does Genei AI assistant work?",
                    "⚽ Tell me about FootLink (Football ML Platform)": "Tell me about FootLink football transfer market system",
                    "🚙 Tell me about EcoRanger (Autonomous Wildlife Rover)": "Tell me about EcoRanger autonomous wildlife guide vehicle",
                    "💻 What is your complete technical skill set?": "What is your complete technical skill set and tech stack?",
                    "🎓 Where did you study? (Education & College)": "Where did you study and what is your education?",
                    "📫 How can I contact Lohith?": "How can I contact Lohith?",
                    "📄 How can I download your official resume?": "How can I download your official resume?"
                }
                user_q = query_map.get(selected, selected)
                # Deduplicate safeguard: only append if not immediately identical to the last message
                if not st.session_state.chat_history or st.session_state.chat_history[-1].get("content") != user_q:
                    st.session_state.chat_history.append({"role": "user", "content": user_q})
                    bot_ans = get_rule_based_answer(user_q)
                    st.session_state.chat_history.append({"role": "assistant", "content": bot_ans})
                # Reset selectbox to index 0 so it never loops or triggers again
                st.session_state.faq_dropdown_val = faq_options[0]

        # Inquire via Quick Dropdown Card (matching newui.png)
        st.markdown(
            '<div class="inquiry-dropdown-box">'
            '<div class="inquiry-box-title">⚡ Inquire via Quick Dropdown:</div>',
            unsafe_allow_html=True
        )

        st.selectbox(
            "Inquire via Quick Dropdown:",
            faq_options,
            key="faq_dropdown_val",
            on_change=on_faq_selected,
            label_visibility="collapsed"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Digital Twin Initial Welcome Bubble (matching newui.png)
        dt_avatar_tag = f'<img src="data:image/png;base64,{profile_img_b64}" class="dt-avatar-img" alt="Lohith Sankar S" />' if profile_img_b64 else '<span style="font-size: 1.8rem;">👨‍💻</span>'
        welcome_bubble_html = (
            f'<div class="digital-twin-bubble">'
            f'<div class="dt-header-row">'
            f'{dt_avatar_tag}'
            f'<div class="dt-title-text">Hello! 👋 <span style="color: #38bdf8;">I\'m Lohith\'s AI Portfolio Digital Twin..</span></div>'
            f'</div>'
            f'<div class="dt-body-text">'
            f'Aspiring Computer Science Engineer with a strong focus on Artificial Intelligence and practical software development. '
            f'Skilled in modern web technologies, object-oriented programming, and IoT hardware interfacing. '
            f'Passionate about engineering real-world solutions that combine machine learning models with intuitive user experiences.<br><br>'
            f'Feel free to choose an inquiry from the dropdown below or type your question directly in the chat box!'
            f'</div>'
            f'</div>'
        )
        st.html(welcome_bubble_html)

        # Render Active Conversation Messages
        for msg in st.session_state.chat_history:
            avatar_val = "👤"
            if msg["role"] == "assistant":
                avatar_val = str(PROFILE_IMG_PATH) if (PROFILE_IMG_PATH and PROFILE_IMG_PATH.exists()) else "🤖"

            with st.chat_message(msg["role"], avatar=avatar_val):
                st.markdown(msg["content"])

        # Chat Input Box (generate exactly once)
        user_input = st.chat_input("Ask a question about Lohith's projects, skills, or background...")
        if user_input and user_input.strip():
            prompt = user_input.strip()
            # Append User Message and answer exactly once
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            rule_answer = get_rule_based_answer(prompt)
            st.session_state.chat_history.append({"role": "assistant", "content": rule_answer})
            st.rerun()

    # -------------------------------------------------------------
    # SECTION 2: FEATURED PROJECTS
    # -------------------------------------------------------------
    elif active_section == "🚀 Featured Projects":
        st.markdown("### 🚀 Flagship Engineering Projects")
        st.markdown("Detailed breakdown of system architecture, machine learning models, and real-world implementations.")

        for project in PROFILE_DATA["projects"]:
            st.markdown(f"""
            <div class="content-card">
                <span class="badge-cyan">{project['category']}</span>
                <h3 style="margin: 10px 0 4px 0; font-size: 1.5rem; color: #ffffff;">{project['name']}</h3>
                <p style="color: #c084fc; font-weight: 700; font-size: 1rem; margin: 2px 0 14px 0;">
                    {project['tagline']}
                </p>
                <p style="color: #f1f5f9; font-size: 1.05rem; line-height: 1.7; margin-bottom: 16px;">
                    {project['description']}
                </p>
                <div style="margin-bottom: 16px;">
                    {' '.join([f'<span class="tech-pill">{tech}</span>' for tech in project['stack']])}
                </div>
                <h4 style="color: #38bdf8; margin: 16px 0 8px 0; font-size: 1.05rem;">✨ Key System Innovations & Architecture:</h4>
                <ul style="color: #e2e8f0; line-height: 1.8; margin-bottom: 8px;">
                    {''.join([f'<li>{feat}</li>' for feat in project['key_features']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # SECTION 3: TECHNICAL SKILLS MATRIX
    # -------------------------------------------------------------
    elif active_section == "💻 Skills & Tech Stack":
        st.markdown("### 💻 Technical Skills Matrix")
        st.markdown("Frameworks, languages, and tools utilized across my engineering projects.")

        sk = PROFILE_DATA["skills"]

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="content-card">
                <h4 style="color: #38bdf8; margin-top: 0; font-size: 1.2rem;">🧠 AI, ML & Core Fundamentals</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["fundamentals"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="content-card">
                <h4 style="color: #38bdf8; margin-top: 0; font-size: 1.2rem;">⚡ Programming Languages</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["languages"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="content-card">
                <h4 style="color: #38bdf8; margin-top: 0; font-size: 1.2rem;">🌐 Web & Mobile Frameworks</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["web_and_apps"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="content-card">
                <h4 style="color: #c084fc; margin-top: 0; font-size: 1.2rem;">🔌 Hardware & IoT Interfacing</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["iot_and_hardware"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="content-card">
                <h4 style="color: #c084fc; margin-top: 0; font-size: 1.2rem;">🗄️ Databases & Storage</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["databases"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("""
            <div class="content-card">
                <h4 style="color: #c084fc; margin-top: 0; font-size: 1.2rem;">🤝 Engineering & Soft Skills</h4>
            """, unsafe_allow_html=True)
            st.markdown(" ".join([f"<span class='tech-pill'>{s}</span>" for s in sk["other_technical"] + sk["soft_skills"]]), unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<hr style='border-color: #334155; margin: 16px 0;'>", unsafe_allow_html=True)
        c_lang, c_hob = st.columns(2)
        with c_lang:
            st.markdown(f"**🗣️ Spoken Languages:** {', '.join(PROFILE_DATA['additional']['languages_spoken'])}")
        with c_hob:
            st.markdown(f"**🎨 Personal Interests:** {', '.join(PROFILE_DATA['additional']['interests_and_hobbies'])}")

    # -------------------------------------------------------------
    # SECTION 4: EDUCATION & RESEARCH
    # -------------------------------------------------------------
    elif active_section == "🎓 Education & Publications":
        st.markdown("### 🎓 Academic Degrees & Research Recognition")

        # Research Paper Feature Card
        st.markdown("""
        <div class="content-card" style="border-color: #7c3aed; background-color: #171c38 !important;">
            <span class="pub-pill">Peer-Reviewed Conference Publication</span>
            <h3 style="color: #ffffff; margin: 10px 0 6px 0; font-size: 1.45rem;">
                ICSAIC-2026 (NICHE) • Research Paper Publication
            </h3>
            <p style="color: #f1f5f9; font-size: 1.05rem; line-height: 1.7; margin: 0 0 10px 0;">
                Authored research on <strong>ZenGuard: Real-time AI Stress Detection & Management System</strong>.
                Selected for official showcase at the prestigious <strong>MBCET 2026 Tech Exhibition</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Degrees List
        for edu in PROFILE_DATA["education"]:
            st.markdown(f"""
            <div class="content-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <h3 style="margin: 0; color: #ffffff; font-size: 1.35rem;">{edu['degree']}</h3>
                        <h4 style="margin: 4px 0 8px 0; color: #38bdf8; font-weight: 600;">{edu['institution']}</h4>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-cyan">{edu['score']}</span>
                        <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">🗓️ {edu['period']}</p>
                    </div>
                </div>
                <p style="color: #e2e8f0; font-size: 1.02rem; line-height: 1.65; margin: 8px 0 0 0;">
                    {edu['highlights']}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # SECTION 5: WORK EXPERIENCE (KEPT SEPARATE, NOT ON MAIN DASHBOARD)
    # -------------------------------------------------------------
    elif active_section == "🏢 Work Experience":
        st.markdown("### 🏢 Professional Experience")

        for exp in PROFILE_DATA["experience"]:
            st.markdown(f"""
            <div class="content-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <h3 style="margin: 0; color: #ffffff; font-size: 1.4rem;">{exp['role']}</h3>
                        <h4 style="margin: 4px 0 10px 0; color: #38bdf8; font-weight: 600;">{exp['company']}</h4>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge-cyan">{exp['period']}</span>
                        <p style="color: #94a3b8; font-size: 0.9rem; margin: 4px 0 0 0;">📍 {exp['location']}</p>
                    </div>
                </div>
                <p style="color: #f1f5f9; font-size: 1.05rem; line-height: 1.65; margin: 12px 0;">
                {exp['overview']}
                </p>
                <div style="margin-bottom: 16px;">
                    {' '.join([f'<span class="tech-pill">{tech}</span>' for tech in exp['tech_stack']])}
                </div>
                <h4 style="color: #c084fc; margin-bottom: 8px; font-size: 1.05rem;">Key Achievements & Responsibilities:</h4>
                <ul style="color: #e2e8f0; line-height: 1.8;">
                    {''.join([f'<li>{c}</li>' for c in exp['contributions']])}
                </ul>
            </div>
            """, unsafe_allow_html=True)


