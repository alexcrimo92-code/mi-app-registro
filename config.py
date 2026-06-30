from supabase import create_client

# ==============================
# SUPABASE
# ==============================

SUPABASE_URL = "https://bggzywzlusinkwwkwzgj.supabase.co"

SUPABASE_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJnZ3p5d3psdXNpbmt3d2t3emdqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0MDMxNjMsImV4cCI6MjA5Nzk3OTE2M30."
    "GtEiVvBZXeAYKap7YOK-CxNmUBHIoxxkJjVV4QyJp4c"
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ==============================
# DATOS DEL TRABAJADOR
# ==============================

TRABAJADOR = "Alex"

EMPRESA = ""

LOGO = "assets/logo.png"

FONDO = "assets/fondo.jpg"

# ==============================
# MATERIALES
# ==============================

MATERIALES = [

    "PEAD 20",

    "PEAD 25",

    "PEAD 32",

    "PEAD 40",

    "PEAD 50",

    "PEAD 63",

    "PEAD 75",

    "PEAD 90",

    "PEAD 110",

    "PVC",

    "Fundición",

    "Acero",

    "Hormigón",

    "Otros"

]

# ==============================
# COLORES
# ==============================

PRIMARY = "#1565C0"

SECONDARY = "#1976D2"

BACKGROUND = "#F3F6FA"

CARD = "#FFFFFF"

TEXT = "#1A1A1A"