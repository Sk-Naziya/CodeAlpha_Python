def apply_theme(theme):

    return f"""
<style>

.stApp {{
    background:
    linear-gradient(
    135deg,
    {theme['secondary']},
    #000000);

    color:white;
}}

.main-title {{
    font-size:60px;
    font-weight:900;
    text-align:center;

    background:
    linear-gradient(
    90deg,
    {theme['primary']},
    {theme['accent']}
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}}

.glass {{
    background:
    rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

    border-radius:20px;

    padding:20px;

    border:
    1px solid rgba(255,255,255,0.15);
}}

.stButton button {{
    width:100%;
    border-radius:15px;
    background:{theme['primary']};
    color:white;
}}

</style>
"""