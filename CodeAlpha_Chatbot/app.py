import streamlit as st
from auth import register, login
from themes import THEMES
from styles import apply_theme
from chatbot import (
    create_chat,
    get_chats,
    save_message,
    load_messages,
    get_response
)

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Nexus AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------
# Session State
# ---------------------------------

if "user" not in st.session_state:
    st.session_state.user = None

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# ---------------------------------
# LOGIN / SIGNUP PAGE
# ---------------------------------

if st.session_state.user is None:
    st.title("🤖 Nexus AI")
    st.markdown("### Intelligent Conversations, Simplified")

    tab1, tab2 = st.tabs(["🔑 Login", "📝 Signup"])

    # LOGIN
    with tab1:

        username = st.text_input(
            "Username",
            key="login_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            if login(username, password):

                st.session_state.user = username
                st.rerun()

            else:

                st.error(
                    "Invalid Username or Password"
                )

    # SIGNUP
    with tab2:

        username = st.text_input(
            "Username",
            key="signup_user"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="signup_pass"
        )

        if st.button("Create Account"):

            if register(username, password):

                st.success(
                    "Account Created Successfully"
                )

            else:

                st.error(
                    "Username already exists"
                )

# ---------------------------------
# CHAT PAGE
# ---------------------------------

else:

    st.sidebar.title("💬 Nexus AI")

    st.sidebar.success(
        f"Welcome, {st.session_state.user}"
    )

    # THEME SELECTOR

    theme_name = st.sidebar.selectbox(
    "🎨 Theme",
    list(THEMES.keys())
)

    theme = THEMES[theme_name]

    st.markdown(
    apply_theme(theme),
    unsafe_allow_html=True
)
    # SEARCH CHATS

    search = st.sidebar.text_input(
        "🔍 Search Chats"
    )

    # NEW CHAT

    if st.sidebar.button("➕ New Chat"):

        count = len(
            get_chats(
                st.session_state.user
            )
        ) + 1

        chat_name = f"Chat {count}"

        create_chat(
            st.session_state.user,
            chat_name
        )

        st.session_state.current_chat = chat_name

        st.rerun()

    # CHAT LIST

    st.sidebar.markdown(
        "### Your Chats"
    )

    chats = get_chats(
        st.session_state.user
    )

    for chat in chats:

        chat_name = chat[0]

        if search:

            if search.lower() not in chat_name.lower():
                continue

        if st.sidebar.button(
            chat_name,
            key=chat_name
        ):

            st.session_state.current_chat = chat_name
            st.rerun()

    # TOOLS

    st.sidebar.markdown("---")

    st.sidebar.subheader("🛠 Tools")

    st.sidebar.button("📎 Upload File")

    st.sidebar.button("🎤 Voice Mode")

    st.sidebar.button("🧠 Memory")

    st.sidebar.button("📥 Export Chat")

    st.sidebar.markdown("---")

    # LOGOUT

    if st.sidebar.button("🚪 Logout"):

        st.session_state.user = None
        st.session_state.current_chat = None

        st.rerun()

    # MAIN AREA

    st.title("🤖 Nexus AI Assistant")

    st.info(
        f"""
👋 Welcome {st.session_state.user}

✨ Powered by Groq

🧠 Chat Memory Enabled

🚀 Nexus AI Platform
"""
    )

    if st.session_state.current_chat:

        messages = load_messages(
            st.session_state.user,
            st.session_state.current_chat
        )

        # DISPLAY HISTORY

        for role, message in messages:

            with st.chat_message(role):
                st.write(message)

        prompt = st.chat_input(
            "Ask me anything..."
        )

        if prompt:

            # SAVE USER MESSAGE

            save_message(
                st.session_state.user,
                st.session_state.current_chat,
                "user",
                prompt
            )

            # LOAD UPDATED CHAT HISTORY

            chat_history = load_messages(
                st.session_state.user,
                st.session_state.current_chat
            )

            # AI RESPONSE

            with st.spinner(
                "🤖 Thinking..."
            ):

                reply = get_response(
                    prompt,
                    chat_history
                )

            # SAVE AI RESPONSE

            save_message(
                st.session_state.user,
                st.session_state.current_chat,
                "assistant",
                reply
            )

            st.rerun()

    else:

        st.info(
            "👈 Create a new chat from the sidebar to begin."
        )