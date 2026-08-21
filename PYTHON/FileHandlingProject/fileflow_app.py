"""
📁 File Handler Studio
A polished Streamlit UI wrapped around a classic Python file-handling
CRUD project (Create / Read / Update / Delete files on disk).

Run locally with:
    streamlit run file_manager_app.py
"""

import streamlit as st
from pathlib import Path
from datetime import datetime

# ----------------------------------------------------------------------------
# Page config & global styling
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="File Handler Studio",
    page_icon="📁",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sandbox directory so the demo never touches random parts of your disk
WORKDIR = Path("file_studio_sandbox")
WORKDIR.mkdir(exist_ok=True)

CUSTOM_CSS = """
<style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle at 20% 20%, #1b1f3b 0%, #0f1123 55%, #090a17 100%);
    }

    .block-container {
        padding-top: 2.5rem;
        max-width: 780px;
    }

    .hero {
        text-align: center;
        padding: 1.2rem 0 0.4rem 0;
    }
    .hero h1 {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #7dd3fc, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero p {
        color: #9ca3d4;
        font-size: 0.95rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        backdrop-filter: blur(6px);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: rgba(255,255,255,0.03);
        padding: 6px;
        border-radius: 14px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #b6bbe6;
        font-weight: 600;
        padding: 8px 14px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #7dd3fc22, #a78bfa33);
        color: #ffffff !important;
    }

    .stButton>button {
        border-radius: 10px;
        border: none;
        font-weight: 600;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white;
        padding: 0.5rem 1.2rem;
        transition: transform 0.15s ease;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(99, 102, 241, 0.35);
    }

    .stTextInput input, .stTextArea textarea {
        border-radius: 10px !important;
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        color: #e5e7ff !important;
    }

    .file-chip {
        display: inline-block;
        background: rgba(167, 139, 250, 0.15);
        border: 1px solid rgba(167, 139, 250, 0.4);
        color: #c4b5fd;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.78rem;
        margin: 2px 4px 2px 0;
    }

    section[data-testid="stSidebar"] {
        background: #0d0e1f;
        border-right: 1px solid rgba(255,255,255,0.06);
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def list_files():
    return sorted([p for p in WORKDIR.iterdir() if p.is_file()])


def human_size(num_bytes: int) -> str:
    for unit in ["B", "KB", "MB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.0f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} GB"


def toast_ok(msg):
    st.success(msg, icon="✅")


def toast_err(msg):
    st.error(msg, icon="⚠️")


# ----------------------------------------------------------------------------
# Sidebar — live file explorer
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🗂️ Sandbox Explorer")
    st.caption(f"Working directory: `{WORKDIR}/`")

    files = list_files()
    if files:
        for f in files:
            stat = f.stat()
            st.markdown(
                f"**{f.name}**  \n"
                f"<span style='color:#8a8fc0;font-size:0.8rem;'>"
                f"{human_size(stat.st_size)} · "
                f"{datetime.fromtimestamp(stat.st_mtime).strftime('%b %d, %H:%M')}"
                f"</span>",
                unsafe_allow_html=True,
            )
            st.markdown("<hr style='margin:6px 0;opacity:0.08;'>", unsafe_allow_html=True)
    else:
        st.info("No files yet — create one from the main panel!")

    st.markdown("---")
    st.caption("Built with Python `pathlib` + Streamlit")

# ----------------------------------------------------------------------------
# Hero header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>📁 File Handler Studio</h1>
        <p>A clean, interactive UI for Create · Read · Update · Delete file operations</p>
    </div>
    """,
    unsafe_allow_html=True,
)

tab_create, tab_read, tab_update, tab_delete = st.tabs(
    ["✨ Create", "📖 Read", "🛠️ Update", "🗑️ Delete"]
)

# ----------------------------------------------------------------------------
# CREATE
# ----------------------------------------------------------------------------
with tab_create:
    with st.container(border=True):
        st.subheader("Create a new file")
        name = st.text_input("File name", placeholder="e.g. notes.txt", key="create_name")
        content = st.text_area("File content", placeholder="Write something...", height=150, key="create_content")

        if st.button("Create File", key="create_btn", use_container_width=True):
            if not name.strip():
                toast_err("Please enter a file name.")
            else:
                path = WORKDIR / name.strip()
                if path.exists():
                    toast_err("A file with that name already exists. Try another name.")
                else:
                    try:
                        path.write_text(content)
                        toast_ok(f"File **{name}** created successfully!")
                        st.rerun()
                    except Exception as e:
                        toast_err(f"An error occurred: {e}")

# ----------------------------------------------------------------------------
# READ
# ----------------------------------------------------------------------------
with tab_read:
    with st.container(border=True):
        st.subheader("Read a file")
        files = list_files()
        if not files:
            st.info("No files in the sandbox yet. Create one first!")
        else:
            choice = st.selectbox("Choose a file", [f.name for f in files], key="read_select")
            if st.button("Read File", key="read_btn", use_container_width=True):
                path = WORKDIR / choice
                try:
                    text = path.read_text()
                    st.code(text if text.strip() else "(file is empty)", language=None)
                except Exception as e:
                    toast_err(f"An error occurred: {e}")

# ----------------------------------------------------------------------------
# UPDATE
# ----------------------------------------------------------------------------
with tab_update:
    with st.container(border=True):
        st.subheader("Update a file")
        files = list_files()
        if not files:
            st.info("No files in the sandbox yet. Create one first!")
        else:
            choice = st.selectbox("Choose a file", [f.name for f in files], key="update_select")
            operation = st.radio(
                "Operation",
                ["Rename", "Append content", "Overwrite content"],
                horizontal=True,
                key="update_op",
            )

            path = WORKDIR / choice

            if operation == "Rename":
                new_name = st.text_input("New file name", key="rename_input")
                if st.button("Rename File", key="rename_btn", use_container_width=True):
                    new_path = WORKDIR / new_name.strip()
                    if not new_name.strip():
                        toast_err("Please enter a new name.")
                    elif new_path.exists():
                        toast_err("A file with that name already exists.")
                    else:
                        try:
                            path.rename(new_path)
                            toast_ok(f"Renamed to **{new_name}** successfully!")
                            st.rerun()
                        except Exception as e:
                            toast_err(f"An error occurred: {e}")

            elif operation == "Append content":
                extra = st.text_area("Content to append", key="append_input")
                if st.button("Append", key="append_btn", use_container_width=True):
                    try:
                        with open(path, "a") as fs:
                            fs.write("\n" + extra)
                        toast_ok("Content appended successfully!")
                    except Exception as e:
                        toast_err(f"An error occurred: {e}")

            else:  # Overwrite
                new_content = st.text_area("New content (replaces everything)", key="overwrite_input")
                if st.button("Overwrite", key="overwrite_btn", use_container_width=True):
                    try:
                        path.write_text(new_content)
                        toast_ok("File overwritten successfully!")
                    except Exception as e:
                        toast_err(f"An error occurred: {e}")

# ----------------------------------------------------------------------------
# DELETE
# ----------------------------------------------------------------------------
with tab_delete:
    with st.container(border=True):
        st.subheader("Delete a file")
        files = list_files()
        if not files:
            st.info("No files in the sandbox yet. Create one first!")
        else:
            choice = st.selectbox("Choose a file", [f.name for f in files], key="delete_select")
            st.warning(f"This will permanently delete **{choice}**.", icon="⚠️")
            confirm = st.checkbox("I understand this cannot be undone.")
            if st.button("Delete File", key="delete_btn", use_container_width=True, disabled=not confirm):
                try:
                    (WORKDIR / choice).unlink()
                    toast_ok(f"File **{choice}** deleted successfully!")
                    st.rerun()
                except Exception as e:
                    toast_err(f"An error occurred: {e}")

st.markdown(
    "<p style='text-align:center;color:#5c5f8a;font-size:0.8rem;margin-top:2rem;'>"
    "File Handler Studio · Python + Streamlit</p>",
    unsafe_allow_html=True,
)