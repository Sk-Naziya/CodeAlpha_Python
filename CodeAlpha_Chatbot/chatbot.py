from database import conn, c
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =====================================
# CHAT MANAGEMENT FUNCTIONS
# =====================================

def create_chat(username, chat_name):
    c.execute(
        """
        INSERT INTO chats(username, chat_name)
        VALUES (?, ?)
        """,
        (username, chat_name)
    )
    conn.commit()


def get_chats(username):
    c.execute(
        """
        SELECT chat_name
        FROM chats
        WHERE username = ?
        ORDER BY id DESC
        """,
        (username,)
    )
    return c.fetchall()


def save_message(username, chat_name, role, message):
    c.execute(
        """
        INSERT INTO messages
        (username, chat_name, role, message)
        VALUES (?, ?, ?, ?)
        """,
        (username, chat_name, role, message)
    )
    conn.commit()


def load_messages(username, chat_name):
    c.execute(
        """
        SELECT role, message
        FROM messages
        WHERE username = ?
        AND chat_name = ?
        ORDER BY id
        """,
        (username, chat_name)
    )
    return c.fetchall()


# =====================================
# OPTIONAL EXTRA FUNCTIONS
# =====================================

def delete_chat(username, chat_name):

    c.execute(
        """
        DELETE FROM chats
        WHERE username = ?
        AND chat_name = ?
        """,
        (username, chat_name)
    )

    c.execute(
        """
        DELETE FROM messages
        WHERE username = ?
        AND chat_name = ?
        """,
        (username, chat_name)
    )

    conn.commit()


def rename_chat(username, old_name, new_name):

    c.execute(
        """
        UPDATE chats
        SET chat_name = ?
        WHERE username = ?
        AND chat_name = ?
        """,
        (new_name, username, old_name)
    )

    c.execute(
        """
        UPDATE messages
        SET chat_name = ?
        WHERE username = ?
        AND chat_name = ?
        """,
        (new_name, username, old_name)
    )

    conn.commit()


# =====================================
# AI RESPONSE FUNCTION
# =====================================

def get_response(prompt, chat_history=None):

    try:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Nexus AI, a premium AI assistant. "
                    "Be helpful, professional, intelligent, friendly, "
                    "and provide detailed answers whenever needed."
                )
            }
        ]

        # Add previous chat history
        if chat_history:

            for role, message in chat_history:

                messages.append(
                    {
                        "role": role,
                        "content": message
                    }
                )

        # Add latest user prompt
        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"