import streamlit as st
from pathlib import Path
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="File Manager",
    page_icon="🗂️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ---------- global ---------- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* gradient header bar */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    color: white;
    text-align: center;
}
.hero h1 { font-size: 2rem; font-weight: 700; margin: 0; letter-spacing: -0.5px; }
.hero p  { font-size: 0.95rem; opacity: .85; margin: .4rem 0 0; }

/* action cards */
.card-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.action-card {
    border: 2px solid transparent;
    border-radius: 14px;
    padding: 1.4rem 1rem;
    text-align: center;
    cursor: pointer;
    transition: all .2s ease;
    background: var(--card-bg, #f8f9ff);
}
.action-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(102,126,234,.2); }
.action-card .icon  { font-size: 2rem; }
.action-card .label { font-weight: 600; font-size: .9rem; margin-top: .4rem; color: #374151; }

/* colored accents per card */
.card-create { background: #f0f4ff; border-color: #c7d2fe; }
.card-read   { background: #f0fdf4; border-color: #bbf7d0; }
.card-update { background: #fffbeb; border-color: #fde68a; }
.card-delete { background: #fff1f2; border-color: #fecdd3; }

/* panel */
.panel {
    background: white;
    border-radius: 14px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(0,0,0,.07);
    border: 1px solid #e5e7eb;
}

/* success / error badges */
.badge-success {
    background: #d1fae5; color: #065f46; border-radius: 8px;
    padding: .5rem 1rem; font-weight: 600; font-size: .85rem;
}
.badge-error {
    background: #fee2e2; color: #991b1b; border-radius: 8px;
    padding: .5rem 1rem; font-weight: 600; font-size: .85rem;
}

/* file content box */
.file-content {
    background: #1e1e2e;
    color: #cdd6f4;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    font-family: 'Courier New', monospace;
    font-size: .88rem;
    line-height: 1.6;
    white-space: pre-wrap;
    max-height: 320px;
    overflow-y: auto;
}

/* sidebar label */
.sidebar-title {
    font-weight: 700;
    font-size: 1rem;
    color: #6366f1;
    margin-bottom: .5rem;
}

/* Streamlit overrides */
div[data-testid="stButton"] > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    transition: all .15s !important;
}
div[data-testid="stTextInput"] > div > input {
    border-radius: 10px !important;
}
div[data-testid="stTextArea"] > div > textarea {
    border-radius: 10px !important;
    font-family: 'Courier New', monospace !important;
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────
WORKSPACE = Path("fm_workspace")
WORKSPACE.mkdir(exist_ok=True)

def safe_path(name: str) -> Path:
    """Resolve a filename inside the workspace (prevents path traversal)."""
    return WORKSPACE / Path(name).name


def list_files():
    return sorted([f.name for f in WORKSPACE.iterdir() if f.is_file()])


# ── Session state defaults ────────────────────────────────────────────────────
if "action" not in st.session_state:
    st.session_state.action = None
if "msg" not in st.session_state:
    st.session_state.msg = ("", "")   # (text, type)  type ∈ {success, error, info}


# ── Hero header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🗂️ File Manager</h1>
    <p>Create · Read · Update · Delete your files with ease</p>
</div>
""", unsafe_allow_html=True)


# ── Action selector (card grid) ───────────────────────────────────────────────
cols = st.columns(4)
actions = [
    ("➕", "Create",  "create", "card-create"),
    ("📖", "Read",    "read",   "card-read"),
    ("✏️",  "Update",  "update", "card-update"),
    ("🗑️", "Delete",  "delete", "card-delete"),
]
for col, (icon, label, key, cls) in zip(cols, actions):
    with col:
        if st.button(f"{icon}\n{label}", key=f"btn_{key}", use_container_width=True):
            st.session_state.action = key
            st.session_state.msg = ("", "")


# ── Sidebar: file browser ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="sidebar-title">📁 Workspace Files</p>', unsafe_allow_html=True)
    files = list_files()
    if files:
        for f in files:
            p = safe_path(f)
            size = p.stat().st_size
            st.markdown(f"**{f}** &nbsp; <small style='color:#9ca3af'>{size} B</small>", unsafe_allow_html=True)
    else:
        st.info("No files yet. Create one!", icon="💡")

    st.divider()
    st.caption("Files are stored in `fm_workspace/`")


# ── Message banner ────────────────────────────────────────────────────────────
msg_text, msg_type = st.session_state.msg
if msg_text:
    if msg_type == "success":
        st.success(msg_text, icon="✅")
    elif msg_type == "error":
        st.error(msg_text, icon="🚫")
    else:
        st.info(msg_text, icon="ℹ️")


# ── Action panels ─────────────────────────────────────────────────────────────
action = st.session_state.action

# ── CREATE ────────────────────────────────────────────────────────────────────
if action == "create":
    st.subheader("➕ Create a New File")
    with st.container(border=True):
        filename = st.text_input("File name", placeholder="e.g. notes.txt")
        content  = st.text_area("File content", height=180,
                                placeholder="Type your content here…")
        if st.button("Create File", type="primary", use_container_width=True):
            if not filename.strip():
                st.session_state.msg = ("Filename cannot be empty.", "error")
            else:
                path = safe_path(filename)
                if path.exists():
                    st.session_state.msg = (f"'{filename}' already exists.", "error")
                else:
                    path.write_text(content, encoding="utf-8")
                    st.session_state.msg = (f"'{filename}' created successfully!", "success")
            st.rerun()

# ── READ ──────────────────────────────────────────────────────────────────────
elif action == "read":
    st.subheader("📖 Read a File")
    files = list_files()
    if not files:
        st.warning("No files found in workspace.", icon="📭")
    else:
        with st.container(border=True):
            filename = st.selectbox("Choose a file", files)
            if st.button("Read File", type="primary", use_container_width=True):
                path = safe_path(filename)
                content = path.read_text(encoding="utf-8")
                st.markdown(f"**Contents of `{filename}`:**")
                st.markdown(f'<div class="file-content">{content if content else "(empty file)"}</div>',
                            unsafe_allow_html=True)
                st.caption(f"Size: {path.stat().st_size} bytes")

# ── UPDATE ────────────────────────────────────────────────────────────────────
elif action == "update":
    st.subheader("✏️ Update a File")
    files = list_files()
    if not files:
        st.warning("No files found in workspace.", icon="📭")
    else:
        with st.container(border=True):
            filename = st.selectbox("Choose a file", files)
            operation = st.radio(
                "Operation",
                ["Rename", "Append content", "Overwrite content"],
                horizontal=True,
            )

            if operation == "Rename":
                new_name = st.text_input("New file name", placeholder="new_name.txt")
                if st.button("Rename", type="primary", use_container_width=True):
                    if not new_name.strip():
                        st.session_state.msg = ("New filename cannot be empty.", "error")
                    else:
                        new_path = safe_path(new_name)
                        if new_path.exists():
                            st.session_state.msg = (f"'{new_name}' already exists.", "error")
                        else:
                            safe_path(filename).rename(new_path)
                            st.session_state.msg = (f"Renamed to '{new_name}' successfully!", "success")
                    st.rerun()

            elif operation == "Append content":
                append_text = st.text_area("Content to append", height=140)
                if st.button("Append", type="primary", use_container_width=True):
                    path = safe_path(filename)
                    with open(path, "a", encoding="utf-8") as f:
                        f.write("\n" + append_text)
                    st.session_state.msg = (f"Content appended to '{filename}'!", "success")
                    st.rerun()

            else:  # Overwrite
                path = safe_path(filename)
                existing = path.read_text(encoding="utf-8")
                new_content = st.text_area("New content (replaces existing)", value=existing, height=180)
                if st.button("Overwrite", type="primary", use_container_width=True):
                    path.write_text(new_content, encoding="utf-8")
                    st.session_state.msg = (f"'{filename}' overwritten successfully!", "success")
                    st.rerun()

# ── DELETE ────────────────────────────────────────────────────────────────────
elif action == "delete":
    st.subheader("🗑️ Delete a File")
    files = list_files()
    if not files:
        st.warning("No files found in workspace.", icon="📭")
    else:
        with st.container(border=True):
            filename = st.selectbox("Choose a file to delete", files)
            st.error(f"⚠️ You are about to permanently delete **{filename}**. This cannot be undone.")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Yes, Delete", type="primary", use_container_width=True):
                    safe_path(filename).unlink()
                    st.session_state.msg = (f"'{filename}' deleted successfully.", "success")
                    st.session_state.action = None
                    st.rerun()
            with col2:
                if st.button("❌ Cancel", use_container_width=True):
                    st.session_state.action = None
                    st.session_state.msg = ("Delete cancelled.", "info")
                    st.rerun()

# ── Idle state ────────────────────────────────────────────────────────────────
elif action is None:
    st.markdown("""
    <div style="text-align:center; padding: 2.5rem 1rem; color: #9ca3af;">
        <div style="font-size: 3.5rem;">👆</div>
        <p style="font-size: 1.05rem; font-weight: 500;">Pick an action above to get started</p>
    </div>
    """, unsafe_allow_html=True)