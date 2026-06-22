"""
DineReserve - Restaurant Management System
Full GUI Application with PostgreSQL Integration
"""
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import customtkinter as ctk
from db import execute_query, execute_many, call_procedure, call_function, test_connection
import threading

# ─── Theme ──────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG       = "#0f1117"
CARD     = "#1a1d27"
CARD2    = "#21253a"
ACCENT   = "#4f8ef7"
ACCENT2  = "#7c3aed"
SUCCESS  = "#22c55e"
WARNING  = "#f59e0b"
DANGER   = "#ef4444"
TEXT     = "#e2e8f0"
MUTED    = "#64748b"
BORDER   = "#2d3348"
SIDEBAR  = "#13151f"

FONT_TITLE  = ("Segoe UI", 22, "bold")
FONT_HEAD   = ("Segoe UI", 14, "bold")
FONT_BODY   = ("Segoe UI", 12)
FONT_SMALL  = ("Segoe UI", 10)
FONT_MONO   = ("Consolas", 11)

# ─── Helpers ────────────────────────────────────────────────────────────────
def label(parent, text, font=FONT_BODY, color=TEXT, **kw):
    return ctk.CTkLabel(parent, text=text, font=font, text_color=color, **kw)

def btn(parent, text, command, color=ACCENT, text_color="white", width=120, **kw):
    return ctk.CTkButton(parent, text=text, command=command,
                         fg_color=color, hover_color=_darken(color),
                         text_color=text_color, width=width,
                         corner_radius=8, font=FONT_BODY, **kw)

def entry(parent, placeholder="", width=220, show="", **kw):
    return ctk.CTkEntry(parent, placeholder_text=placeholder, width=width,
                        fg_color=CARD2, border_color=BORDER,
                        text_color=TEXT, placeholder_text_color=MUTED,
                        show=show, font=FONT_BODY, **kw)

def card(parent, **kw):
    return ctk.CTkFrame(parent, fg_color=CARD, corner_radius=12,
                        border_width=1, border_color=BORDER, **kw)

def _darken(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(max(r-30,0), max(g-30,0), max(b-30,0))

# ─── Scrollable Table Widget ─────────────────────────────────────────────────
class DataTable(ctk.CTkFrame):
    def __init__(self, parent, columns, **kw):
        super().__init__(parent, fg_color="transparent", **kw)
        self.columns = columns
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Dark.Treeview",
            background=CARD2, foreground=TEXT,
            fieldbackground=CARD2, rowheight=30,
            font=FONT_BODY, borderwidth=0)
        style.configure("Dark.Treeview.Heading",
            background=CARD, foreground=ACCENT,
            font=("Segoe UI", 11, "bold"), relief="flat")
        style.map("Dark.Treeview", background=[("selected", ACCENT2)])

        frame = ctk.CTkFrame(self, fg_color=CARD2, corner_radius=10)
        frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(frame, columns=columns, show="headings",
                                  style="Dark.Treeview")
        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=max(120, len(col)*12), anchor="center")

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    def load(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, row in enumerate(rows):
            tag = "even" if i % 2 == 0 else "odd"
            vals = [row[c] if c in row and row[c] is not None else "" for c in self.columns]
            self.tree.insert("", "end", values=vals, tags=(tag,))
        self.tree.tag_configure("even", background=CARD2)
        self.tree.tag_configure("odd", background="#252840")

    def selected_values(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return dict(zip(self.columns, self.tree.item(sel[0])["values"]))


# ═══════════════════════════════════════════════════════════════════════════
#  LOGIN SCREEN
# ═══════════════════════════════════════════════════════════════════════════
class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, on_login):
        super().__init__(parent, fg_color=BG)
        self.on_login = on_login
        self._build()

    def _build(self):
        self.pack(fill="both", expand=True)
        # Left decorative panel
        left = ctk.CTkFrame(self, fg_color=SIDEBAR, width=420, corner_radius=0)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        ctk.CTkLabel(left, text="🍽️", font=("Segoe UI", 64)).pack(pady=(80, 10))
        ctk.CTkLabel(left, text="DineReserve", font=("Segoe UI", 32, "bold"),
                     text_color=ACCENT).pack()
        ctk.CTkLabel(left, text="Restaurant Management System",
                     font=FONT_BODY, text_color=MUTED).pack(pady=(4, 40))

        for item in ["📊 Full CRUD Operations", "🔍 Advanced Queries",
                     "⚙️ Stored Procedures", "📈 Live Analytics"]:
            row = ctk.CTkFrame(left, fg_color="transparent")
            row.pack(anchor="w", padx=50, pady=6)
            ctk.CTkLabel(row, text=item, font=FONT_BODY, text_color=TEXT).pack(side="left")

        # Right login form
        right = ctk.CTkFrame(self, fg_color=BG)
        right.pack(side="right", fill="both", expand=True)

        form = card(right)
        form.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.75)

        label(form, "Welcome Back", font=FONT_TITLE).pack(pady=(30, 4))
        label(form, "Sign in to manage your system", color=MUTED).pack(pady=(0, 24))

        self.tabs = ctk.CTkTabview(form, fg_color=CARD, segmented_button_fg_color=CARD2,
                                    segmented_button_selected_color=ACCENT)
        self.tabs.pack(fill="x", padx=24, pady=4)
        self.tabs.add("Tourist Login")
        self.tabs.add("Admin Login")

        # Tourist tab
        t = self.tabs.tab("Tourist Login")
        label(t, "Email").pack(anchor="w", padx=8, pady=(8,2))
        self.t_email = entry(t, "tourist@email.com", width=340)
        self.t_email.pack(padx=8, pady=(0, 8))
        label(t, "Password").pack(anchor="w", padx=8, pady=(0,2))
        self.t_pwd = entry(t, "••••••••", width=340, show="•")
        self.t_pwd.pack(padx=8, pady=(0, 12))
        btn(t, "Sign In as Tourist", self._tourist_login, width=340).pack(padx=8, pady=(0,16))

        # Admin tab
        a = self.tabs.tab("Admin Login")
        label(a, "Admin Password").pack(anchor="w", padx=8, pady=(8,2))
        self.a_pwd = entry(a, "Enter admin password", width=340, show="•")
        self.a_pwd.pack(padx=8, pady=(0, 12))
        btn(a, "Sign In as Admin", self._admin_login, width=340, color=ACCENT2).pack(padx=8, pady=(0,16))

        self.err = label(form, "", color=DANGER)
        self.err.pack(pady=(4, 16))

        # DB status
        ok, msg = test_connection()
        status_color = SUCCESS if ok else DANGER
        status_text = "● DB Connected" if ok else f"● DB Error: {msg}"
        label(form, status_text, color=status_color, font=FONT_SMALL).pack(pady=(0, 20))

    def _tourist_login(self):
        email = self.t_email.get().strip()
        pwd = self.t_pwd.get().strip()
        if not email or not pwd:
            self.err.configure(text="Please fill in all fields")
            return
        rows = execute_query(
            "SELECT touristid, firstname, lastname, email, country FROM public.tourist WHERE email=%s AND password=%s",
            (email, pwd)
        )
        if rows:
            self.on_login(rows[0], role="tourist")
        else:
            self.err.configure(text="Invalid email or password")

    def _admin_login(self):
        pwd = self.a_pwd.get().strip()
        if pwd == "AYALA10":
            self.on_login({"touristid": 0, "firstname": "Admin", "lastname": "", "email": "admin"}, role="admin")
        else:
            rows = execute_query(
                "SELECT customer_id, customer_name, customer_email FROM public.customer WHERE customer_password=%s AND customer_role='Admin'",
                (pwd,)
            )
            if rows:
                self.on_login(rows[0], role="admin")
            else:
                self.err.configure(text="Incorrect admin password")


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN APP SHELL
# ═══════════════════════════════════════════════════════════════════════════
class MainApp(ctk.CTkFrame):
    def __init__(self, parent, user, role):
        super().__init__(parent, fg_color=BG)
        self.user = user
        self.role = role
        self.pack(fill="both", expand=True)
        self._build()
        self._show("dashboard")

    def _build(self):
        # Sidebar
        self.sidebar = ctk.CTkFrame(self, fg_color=SIDEBAR, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="🍽️ DineReserve",
                     font=("Segoe UI", 16, "bold"), text_color=ACCENT).pack(pady=(24, 4))

        name = self.user.get("firstname", self.user.get("customer_name", "User"))
        ctk.CTkLabel(self.sidebar, text=f"Hello, {name}",
                     font=FONT_SMALL, text_color=MUTED).pack(pady=(0, 20))

        # Nav items
        nav = [
            ("📊 Dashboard",      "dashboard"),
            ("🏢 Providers",      "providers"),
            ("👤 Tourists",       "tourists"),
            ("📅 Reservations",   "reservations"),
            ("🍜 Menu Items",     "menu"),
            ("🎟️ Coupons",       "coupons"),
            ("🏖️ Attractions",   "attractions"),
            ("🔍 Queries",        "queries"),
            ("⚙️ Procedures",    "procedures"),
        ]
        if self.role == "tourist":
            nav = [n for n in nav if n[1] in ("dashboard", "reservations", "attractions", "coupons")]

        self.nav_btns = {}
        for label_text, view in nav:
            b = ctk.CTkButton(self.sidebar, text=label_text,
                              command=lambda v=view: self._show(v),
                              fg_color="transparent", hover_color=CARD2,
                              text_color=TEXT, anchor="w",
                              font=FONT_BODY, corner_radius=8, width=200, height=38)
            b.pack(padx=10, pady=2)
            self.nav_btns[view] = b

        btn(self.sidebar, "🚪 Logout", self._logout, color=DANGER, width=180).pack(side="bottom", pady=20)

        # Content area
        self.content = ctk.CTkFrame(self, fg_color=BG)
        self.content.pack(side="right", fill="both", expand=True)

    def _show(self, view):
        for v, b in self.nav_btns.items():
            b.configure(fg_color=ACCENT if v == view else "transparent")
        for w in self.content.winfo_children():
            w.destroy()

        screens = {
            "dashboard":    DashboardScreen,
            "providers":    ProvidersScreen,
            "tourists":     TouristsScreen,
            "reservations": ReservationsScreen,
            "menu":         MenuScreen,
            "coupons":      CouponsScreen,
            "attractions":  AttractionsScreen,
            "queries":      QueriesScreen,
            "procedures":   ProceduresScreen,
        }
        cls = screens.get(view)
        if cls:
            cls(self.content, self.user, self.role).pack(fill="both", expand=True)

    def _logout(self):
        for w in self.master.winfo_children():
            w.destroy()
        LoginScreen(self.master, lambda u, role: _launch_main(self.master, u, role))


# ═══════════════════════════════════════════════════════════════════════════
#  BASE SCREEN with CRUD toolbar
# ═══════════════════════════════════════════════════════════════════════════
class BaseScreen(ctk.CTkFrame):
    title = "Screen"
    icon  = "📄"

    def __init__(self, parent, user, role):
        super().__init__(parent, fg_color=BG)
        self.user = user
        self.role = role
        self._build_header()
        self.body = ctk.CTkFrame(self, fg_color=BG)
        self.body.pack(fill="both", expand=True, padx=20, pady=(0, 16))
        self.build()

    def _build_header(self):
        hdr = ctk.CTkFrame(self, fg_color=BG, height=60)
        hdr.pack(fill="x", padx=20, pady=(16, 8))
        ctk.CTkLabel(hdr, text=f"{self.icon} {self.title}",
                     font=FONT_TITLE, text_color=TEXT).pack(side="left")

    def build(self):
        pass

    def notify(self, msg, is_error=False):
        color = DANGER if is_error else SUCCESS
        messagebox.showinfo("Error" if is_error else "Success", msg)


# ═══════════════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════
class DashboardScreen(BaseScreen):
    title = "Dashboard"
    icon  = "📊"

    def build(self):
        try:
            stats = {
                "Tourists":     execute_query("SELECT COUNT(*) AS c FROM public.tourist")[0]["c"],
                "Reservations": execute_query("SELECT COUNT(*) AS c FROM public.reservation")[0]["c"],
                "Providers":    execute_query("SELECT COUNT(*) AS c FROM public.serviceprovider")[0]["c"],
                "Attractions":  execute_query("SELECT COUNT(*) AS c FROM public.attraction")[0]["c"],
                "Menu Items":   execute_query("SELECT COUNT(*) AS c FROM public.menuitem")[0]["c"],
                "Coupons":      execute_query("SELECT COUNT(*) AS c FROM public.coupon")[0]["c"],
            }
        except Exception as e:
            label(self.body, f"DB Error: {e}", color=DANGER).pack()
            return

        # Stat cards
        grid = ctk.CTkFrame(self.body, fg_color="transparent")
        grid.pack(fill="x", pady=(0, 16))
        icons = ["👤","📅","🏢","🏖️","🍜","🎟️"]
        colors = [ACCENT, SUCCESS, ACCENT2, WARNING, "#06b6d4", DANGER]
        for i, (k, v) in enumerate(stats.items()):
            c = card(grid)
            c.grid(row=i//3, column=i%3, padx=8, pady=8, sticky="nsew")
            grid.grid_columnconfigure(i%3, weight=1)
            ctk.CTkLabel(c, text=icons[i], font=("Segoe UI", 28)).pack(pady=(16,4))
            ctk.CTkLabel(c, text=str(v), font=("Segoe UI", 28, "bold"),
                         text_color=colors[i]).pack()
            ctk.CTkLabel(c, text=k, font=FONT_SMALL, text_color=MUTED).pack(pady=(0,16))

        # Recent reservations
        bottom = ctk.CTkFrame(self.body, fg_color="transparent")
        bottom.pack(fill="both", expand=True)
        label(bottom, "Recent Reservations", font=FONT_HEAD).pack(anchor="w", pady=(0,8))
        try:
            rows = execute_query("""
                SELECT r.reservationid AS "ID",
                       t.firstname || ' ' || t.lastname AS "Tourist",
                       sp.providername AS "Provider",
                       r.reservationdate AS "Date",
                       r.numberofpeople AS "People",
                       r.status AS "Status"
                FROM public.reservation r
                JOIN public.tourist t ON r.touristid = t.touristid
                JOIN public.serviceprovider sp ON r.providerid = sp.providerid
                ORDER BY r.reservationdate DESC LIMIT 8
            """)
            cols = ["ID","Tourist","Provider","Date","People","Status"]
            tbl = DataTable(bottom, cols)
            tbl.pack(fill="both", expand=True)
            tbl.load(rows)
        except Exception as e:
            label(bottom, f"Error: {e}", color=DANGER).pack()


# ═══════════════════════════════════════════════════════════════════════════
#  PROVIDERS
# ═══════════════════════════════════════════════════════════════════════════
class ProvidersScreen(BaseScreen):
    title = "Service Providers"
    icon  = "🏢"

    def build(self):
        # Toolbar
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add", self._add, color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit", self._edit, color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh", self._load).pack(side="left", padx=4)

        self.search_var = ctk.StringVar()
        se = entry(tb, "Search by name or city...", width=250)
        se.pack(side="right", padx=4)
        se.bind("<KeyRelease>", lambda e: self._search(se.get()))

        self.tbl = DataTable(self.body,
            ["ID","Name","Type","Phone","Address","City"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self, search=""):
        sql = """SELECT providerid AS "ID", providername AS "Name",
                        servicetype AS "Type", phone AS "Phone",
                        address AS "Address", city AS "City"
                 FROM public.serviceprovider"""
        if search:
            sql += " WHERE providername ILIKE %s OR city ILIKE %s"
            rows = execute_query(sql, (f"%{search}%", f"%{search}%"))
        else:
            rows = execute_query(sql)
        self.tbl.load(rows)

    def _search(self, val):
        self._load(val)

    def _add(self):
        dlg = FormDialog(self, "Add Provider", [
            ("Provider Name", "text"),
            ("Service Type",  "combo", ["Restaurant","Cafe","Hotel","Bar"]),
            ("Phone",         "text"),
            ("Address",       "text"),
            ("City",          "text"),
        ])
        self.wait_window(dlg)
        if dlg.result:
            n, t, ph, a, c = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.serviceprovider (providername,servicetype,phone,address,city)
                    VALUES (%s,%s,%s,%s,%s)
                """, (n, t, ph, a, c), fetch=False)
                self._load()
                self.notify("Provider added!")
            except Exception as e:
                self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row:
            self.notify("Select a row first", True); return
        pid = row["ID"]
        dlg = FormDialog(self, "Edit Provider", [
            ("Provider Name", "text", row["Name"]),
            ("Service Type",  "combo", ["Restaurant","Cafe","Hotel","Bar"], row["Type"]),
            ("Phone",         "text", str(row["Phone"])),
            ("Address",       "text", row["Address"]),
            ("City",          "text", row["City"]),
        ])
        self.wait_window(dlg)
        if dlg.result:
            n, t, ph, a, c = dlg.result
            try:
                execute_query("""
                    UPDATE public.serviceprovider
                    SET providername=%s,servicetype=%s,phone=%s,address=%s,city=%s
                    WHERE providerid=%s
                """, (n, t, ph, a, c, pid), fetch=False)
                self._load()
                self.notify("Provider updated!")
            except Exception as e:
                self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row:
            self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete provider '{row['Name']}'?"):
            try:
                execute_query("DELETE FROM public.serviceprovider WHERE providerid=%s",
                              (row["ID"],), fetch=False)
                self._load()
                self.notify("Provider deleted!")
            except Exception as e:
                self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  TOURISTS
# ═══════════════════════════════════════════════════════════════════════════
class TouristsScreen(BaseScreen):
    title = "Tourists"
    icon  = "👤"

    def build(self):
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add",    self._add,    color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit",   self._edit,   color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh",self._load).pack(side="left", padx=4)

        se = entry(tb, "Search by name/country...", width=250)
        se.pack(side="right", padx=4)
        se.bind("<KeyRelease>", lambda e: self._search(se.get()))

        self.tbl = DataTable(self.body,
            ["ID","First Name","Last Name","Email","Phone","Country"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self, search=""):
        sql = """SELECT touristid AS "ID", firstname AS "First Name",
                        lastname AS "Last Name", email AS "Email",
                        phone AS "Phone", country AS "Country"
                 FROM public.tourist"""
        if search:
            sql += " WHERE firstname ILIKE %s OR lastname ILIKE %s OR country ILIKE %s"
            rows = execute_query(sql, (f"%{search}%",)*3)
        else:
            rows = execute_query(sql + " ORDER BY touristid")
        self.tbl.load(rows)

    def _search(self, val): self._load(val)

    def _add(self):
        dlg = FormDialog(self, "Add Tourist", [
            ("First Name", "text"),
            ("Last Name",  "text"),
            ("Email",      "text"),
            ("Phone",      "text"),
            ("Country",    "text"),
            ("Password",   "password"),
        ])
        self.wait_window(dlg)
        if dlg.result:
            fn, ln, em, ph, co, pw = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.tourist(firstname,lastname,email,phone,country,password)
                    VALUES(%s,%s,%s,%s,%s,%s)
                """, (fn, ln, em, ph, co, pw), fetch=False)
                self._load(); self.notify("Tourist added!")
            except Exception as e: self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        tid = row["ID"]
        dlg = FormDialog(self, "Edit Tourist", [
            ("First Name", "text", row["First Name"]),
            ("Last Name",  "text", row["Last Name"]),
            ("Email",      "text", row["Email"]),
            ("Phone",      "text", str(row["Phone"] or "")),
            ("Country",    "text", row["Country"]),
        ])
        self.wait_window(dlg)
        if dlg.result:
            fn, ln, em, ph, co = dlg.result
            try:
                execute_query("""
                    UPDATE public.tourist
                    SET firstname=%s,lastname=%s,email=%s,phone=%s,country=%s
                    WHERE touristid=%s
                """, (fn, ln, em, ph, co, tid), fetch=False)
                self._load(); self.notify("Tourist updated!")
            except Exception as e: self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete tourist '{row['First Name']} {row['Last Name']}'?"):
            try:
                execute_query("DELETE FROM public.tourist WHERE touristid=%s",
                              (row["ID"],), fetch=False)
                self._load(); self.notify("Tourist deleted!")
            except Exception as e: self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  RESERVATIONS
# ═══════════════════════════════════════════════════════════════════════════
class ReservationsScreen(BaseScreen):
    title = "Reservations"
    icon  = "📅"

    def build(self):
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add",    self._add,    color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit",   self._edit,   color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh",self._load).pack(side="left", padx=4)

        se = entry(tb, "Search by tourist name...", width=250)
        se.pack(side="right", padx=4)
        se.bind("<KeyRelease>", lambda e: self._search(se.get()))

        self.tbl = DataTable(self.body,
            ["ID","Tourist","Provider","Date","People","Status"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self, search=""):
        sql = """SELECT r.reservationid AS "ID",
                        t.firstname || ' ' || t.lastname AS "Tourist",
                        sp.providername AS "Provider",
                        r.reservationdate AS "Date",
                        r.numberofpeople AS "People",
                        r.status AS "Status"
                 FROM public.reservation r
                 JOIN public.tourist t ON r.touristid = t.touristid
                 JOIN public.serviceprovider sp ON r.providerid = sp.providerid"""
        if search:
            sql += " WHERE t.firstname ILIKE %s OR t.lastname ILIKE %s"
            rows = execute_query(sql + " ORDER BY r.reservationdate DESC", (f"%{search}%",)*2)
        else:
            rows = execute_query(sql + " ORDER BY r.reservationdate DESC LIMIT 200")
        self.tbl.load(rows)

    def _search(self, val): self._load(val)

    def _get_tourists(self):
        rows = execute_query("SELECT touristid, firstname||' '||lastname AS name FROM public.tourist ORDER BY firstname")
        return {r["name"]: r["touristid"] for r in rows}

    def _get_providers(self):
        rows = execute_query("SELECT providerid, providername FROM public.serviceprovider ORDER BY providername")
        return {r["providername"]: r["providerid"] for r in rows}

    def _add(self):
        tourists  = self._get_tourists()
        providers = self._get_providers()
        dlg = FormDialog(self, "Add Reservation", [
            ("Tourist",     "combo", list(tourists.keys())),
            ("Provider",    "combo", list(providers.keys())),
            ("Date (YYYY-MM-DD)", "text"),
            ("# of People", "text"),
            ("Status",      "combo", ["Pending","Confirmed","Cancelled","Completed"]),
        ])
        self.wait_window(dlg)
        if dlg.result:
            tn, pn, dt, np, st = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.reservation(touristid,providerid,reservationdate,numberofpeople,status)
                    VALUES(%s,%s,%s,%s,%s)
                """, (tourists[tn], providers[pn], dt, int(np), st), fetch=False)
                self._load(); self.notify("Reservation added!")
            except Exception as e: self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        rid = row["ID"]
        dlg = FormDialog(self, "Edit Reservation", [
            ("Date (YYYY-MM-DD)", "text", str(row["Date"])),
            ("# of People",       "text", str(row["People"])),
            ("Status",            "combo", ["Pending","Confirmed","Cancelled","Completed"], row["Status"]),
        ])
        self.wait_window(dlg)
        if dlg.result:
            dt, np, st = dlg.result
            try:
                execute_query("""
                    UPDATE public.reservation
                    SET reservationdate=%s, numberofpeople=%s, status=%s
                    WHERE reservationid=%s
                """, (dt, int(np), st, rid), fetch=False)
                self._load(); self.notify("Reservation updated!")
            except Exception as e: self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete reservation #{row['ID']}?"):
            try:
                execute_query("DELETE FROM public.orderline WHERE reservationid=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.reservedattraction WHERE reservation_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.restaurant_table WHERE reservationid=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.reservation WHERE reservationid=%s", (row["ID"],), fetch=False)
                self._load(); self.notify("Reservation deleted!")
            except Exception as e: self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  MENU ITEMS
# ═══════════════════════════════════════════════════════════════════════════
class MenuScreen(BaseScreen):
    title = "Menu Items"
    icon  = "🍜"

    def build(self):
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add",    self._add,    color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit",   self._edit,   color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh",self._load).pack(side="left", padx=4)

        self.tbl = DataTable(self.body, ["Item ID","Item Name","Price","Category","Provider"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self):
        rows = execute_query("""
            SELECT m.itemid AS "Item ID", m.itemname AS "Item Name",
                   m.price AS "Price", m.category AS "Category",
                   sp.providername AS "Provider"
            FROM public.menuitem m
            JOIN public.serviceprovider sp ON m.providerid = sp.providerid
            ORDER BY sp.providername, m.itemname
        """)
        self.tbl.load(rows)

    def _get_providers(self):
        rows = execute_query("SELECT providerid, providername FROM public.serviceprovider ORDER BY providername")
        return {r["providername"]: r["providerid"] for r in rows}

    def _add(self):
        providers = self._get_providers()
        dlg = FormDialog(self, "Add Menu Item", [
            ("Item Name", "text"),
            ("Price",     "text"),
            ("Category",  "combo", ["Main","Starter","Drink","Dessert","Salad","Soup"]),
            ("Provider",  "combo", list(providers.keys())),
        ])
        self.wait_window(dlg)
        if dlg.result:
            nm, pr, ca, pn = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.menuitem(itemname,price,category,providerid)
                    VALUES(%s,%s,%s,%s)
                """, (nm, int(pr), ca, providers[pn]), fetch=False)
                self._load(); self.notify("Menu item added!")
            except Exception as e: self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        providers = self._get_providers()
        dlg = FormDialog(self, "Edit Menu Item", [
            ("Item Name", "text", row["Item Name"]),
            ("Price",     "text", str(row["Price"])),
            ("Category",  "combo", ["Main","Starter","Drink","Dessert","Salad","Soup"], row["Category"]),
            ("Provider",  "combo", list(providers.keys()), row["Provider"]),
        ])
        self.wait_window(dlg)
        if dlg.result:
            nm, pr, ca, pn = dlg.result
            try:
                execute_query("""
                    UPDATE public.menuitem SET itemname=%s,price=%s,category=%s,providerid=%s
                    WHERE itemid=%s
                """, (nm, int(pr), ca, providers[pn], row["Item ID"]), fetch=False)
                self._load(); self.notify("Menu item updated!")
            except Exception as e: self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete menu item '{row['Item Name']}'?"):
            try:
                execute_query("DELETE FROM public.orderline WHERE itemid=%s AND providerid=(SELECT providerid FROM public.menuitem WHERE itemid=%s LIMIT 1)",
                              (row["Item ID"], row["Item ID"]), fetch=False)
                execute_query("DELETE FROM public.menuitem WHERE itemid=%s", (row["Item ID"],), fetch=False)
                self._load(); self.notify("Menu item deleted!")
            except Exception as e: self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  COUPONS
# ═══════════════════════════════════════════════════════════════════════════
class CouponsScreen(BaseScreen):
    title = "Coupons"
    icon  = "🎟️"

    def build(self):
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add",    self._add,    color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit",   self._edit,   color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh",self._load).pack(side="left", padx=4)

        self.tbl = DataTable(self.body,
            ["ID","Code","Discount%","Start","End","Status","Provider"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self):
        rows = execute_query("""
            SELECT c.couponid AS "ID", c.couponcode AS "Code",
                   c.discountpercent AS "Discount%", c.startdate AS "Start",
                   c.enddate AS "End", c.status AS "Status",
                   sp.providername AS "Provider"
            FROM public.coupon c
            JOIN public.serviceprovider sp ON c.providerid = sp.providerid
            ORDER BY c.enddate DESC
        """)
        self.tbl.load(rows)

    def _get_providers(self):
        rows = execute_query("SELECT providerid, providername FROM public.serviceprovider ORDER BY providername")
        return {r["providername"]: r["providerid"] for r in rows}

    def _add(self):
        providers = self._get_providers()
        dlg = FormDialog(self, "Add Coupon", [
            ("Coupon Code",    "text"),
            ("Discount %",     "text"),
            ("Start (YYYY-MM-DD)", "text"),
            ("End (YYYY-MM-DD)",   "text"),
            ("Status",         "combo", ["A","U","E"]),
            ("Provider",       "combo", list(providers.keys())),
        ])
        self.wait_window(dlg)
        if dlg.result:
            co, di, st, en, ss, pn = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.coupon(couponcode,discountpercent,startdate,enddate,status,providerid)
                    VALUES(%s,%s,%s,%s,%s,%s)
                """, (co, int(di), st, en, ss, providers[pn]), fetch=False)
                self._load(); self.notify("Coupon added!")
            except Exception as e: self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        dlg = FormDialog(self, "Edit Coupon", [
            ("Coupon Code",    "text", row["Code"]),
            ("Discount %",     "text", str(row["Discount%"])),
            ("End (YYYY-MM-DD)", "text", str(row["End"])),
            ("Status",         "combo", ["A","U","E"], str(row["Status"]).strip()),
        ])
        self.wait_window(dlg)
        if dlg.result:
            co, di, en, ss = dlg.result
            try:
                execute_query("""
                    UPDATE public.coupon
                    SET couponcode=%s,discountpercent=%s,enddate=%s,status=%s
                    WHERE couponid=%s
                """, (co, int(di), en, ss, row["ID"]), fetch=False)
                self._load(); self.notify("Coupon updated!")
            except Exception as e: self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete coupon '{row['Code']}'?"):
            try:
                execute_query("DELETE FROM public.include WHERE couponid=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.attractioncoupon WHERE coupon_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.customercoupon WHERE coupon_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.coupon WHERE couponid=%s", (row["ID"],), fetch=False)
                self._load(); self.notify("Coupon deleted!")
            except Exception as e: self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  ATTRACTIONS
# ═══════════════════════════════════════════════════════════════════════════
class AttractionsScreen(BaseScreen):
    title = "Attractions"
    icon  = "🏖️"

    def build(self):
        tb = ctk.CTkFrame(self.body, fg_color="transparent")
        tb.pack(fill="x", pady=(0,10))
        btn(tb, "➕ Add",    self._add,    color=SUCCESS).pack(side="left", padx=4)
        btn(tb, "✏️ Edit",   self._edit,   color=WARNING).pack(side="left", padx=4)
        btn(tb, "🗑️ Delete", self._delete, color=DANGER).pack(side="left", padx=4)
        btn(tb, "🔄 Refresh",self._load).pack(side="left", padx=4)

        self.tbl = DataTable(self.body,
            ["ID","Name","Location","Price","Category","Description"])
        self.tbl.pack(fill="both", expand=True)
        self._load()

    def _load(self):
        rows = execute_query("""
            SELECT a.attraction_id AS "ID", a.attraction_name AS "Name",
                   a.attraction_location AS "Location",
                   a.attraction_price AS "Price",
                   c.category_name AS "Category",
                   a.attraction_description AS "Description"
            FROM public.attraction a
            JOIN public.category c ON a.category_id = c.category_id
            ORDER BY a.attraction_name
        """)
        self.tbl.load(rows)

    def _get_categories(self):
        rows = execute_query("SELECT category_id, category_name FROM public.category ORDER BY category_name")
        return {r["category_name"]: r["category_id"] for r in rows}

    def _add(self):
        cats = self._get_categories()
        dlg = FormDialog(self, "Add Attraction", [
            ("Name",          "text"),
            ("Location",      "text"),
            ("Price",         "text"),
            ("Category",      "combo", list(cats.keys())),
            ("Description",   "text"),
        ])
        self.wait_window(dlg)
        if dlg.result:
            nm, lo, pr, ca, de = dlg.result
            try:
                execute_query("""
                    INSERT INTO public.attraction(attraction_name,attraction_location,attraction_price,category_id,attraction_description)
                    VALUES(%s,%s,%s,%s,%s)
                """, (nm, lo, float(pr), cats[ca], de), fetch=False)
                self._load(); self.notify("Attraction added!")
            except Exception as e: self.notify(str(e), True)

    def _edit(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        cats = self._get_categories()
        dlg = FormDialog(self, "Edit Attraction", [
            ("Name",        "text", row["Name"]),
            ("Location",    "text", row["Location"]),
            ("Price",       "text", str(row["Price"])),
            ("Category",    "combo", list(cats.keys()), row["Category"]),
            ("Description", "text", str(row["Description"] or "")),
        ])
        self.wait_window(dlg)
        if dlg.result:
            nm, lo, pr, ca, de = dlg.result
            try:
                execute_query("""
                    UPDATE public.attraction
                    SET attraction_name=%s,attraction_location=%s,attraction_price=%s,
                        category_id=%s,attraction_description=%s
                    WHERE attraction_id=%s
                """, (nm, lo, float(pr), cats[ca], de, row["ID"]), fetch=False)
                self._load(); self.notify("Attraction updated!")
            except Exception as e: self.notify(str(e), True)

    def _delete(self):
        row = self.tbl.selected_values()
        if not row: self.notify("Select a row first", True); return
        if messagebox.askyesno("Confirm", f"Delete attraction '{row['Name']}'?"):
            try:
                execute_query("DELETE FROM public.reservedattraction WHERE attraction_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.attractioncoupon WHERE attraction_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.review WHERE attraction_id=%s", (row["ID"],), fetch=False)
                execute_query("DELETE FROM public.attraction WHERE attraction_id=%s", (row["ID"],), fetch=False)
                self._load(); self.notify("Attraction deleted!")
            except Exception as e: self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  QUERIES SCREEN
# ═══════════════════════════════════════════════════════════════════════════
class QueriesScreen(BaseScreen):
    title = "SQL Queries"
    icon  = "🔍"

    QUERIES = {
        "1. Tourists who reserved in Jan 2026": {
            "sql": """SELECT t.firstname AS "First Name", t.lastname AS "Last Name", t.country AS "Country"
                      FROM public.tourist t
                      JOIN public.reservation r ON t.touristid = r.touristid
                      WHERE EXTRACT(YEAR FROM r.reservationdate)=2026
                        AND EXTRACT(MONTH FROM r.reservationdate)=1""",
            "params": [],
            "desc": "Tourists who made a reservation in January 2026"
        },
        "2. Reservations for tourist 'First80'": {
            "sql": """SELECT t.firstname AS "Tourist", sp.providername AS "Provider",
                             sp.address AS "Address", sp.city AS "City"
                      FROM public.tourist t
                      JOIN public.reservation r ON t.touristid=r.touristid
                      JOIN public.serviceprovider sp ON r.providerid=sp.providerid
                      WHERE t.firstname=%s""",
            "params": [("Tourist first name", "text", "First80")],
            "desc": "Reservations made by a specific tourist"
        },
        "3. Menu items in Cafe providers": {
            "sql": """SELECT m.itemname AS "Item Name", m.price AS "Price", sp.providername AS "Provider"
                      FROM public.menuitem m
                      JOIN public.serviceprovider sp ON m.providerid=sp.providerid
                      WHERE sp.servicetype='Cafe'
                      ORDER BY m.itemname""",
            "params": [],
            "desc": "All menu items from Cafe-type providers, ordered by name"
        },
        "4. Most ordered item per provider": {
            "sql": """SELECT sp.providername AS "Provider", m.itemname AS "Item",
                             COUNT(ol.reservationid) AS "Total Orders",
                             SUM(m.price) AS "Total Revenue"
                      FROM public.serviceprovider sp
                      JOIN public.menuitem m ON sp.providerid=m.providerid
                      JOIN public.orderline ol ON m.itemid=ol.itemid AND m.providerid=ol.providerid
                      WHERE sp.providername=%s
                      GROUP BY sp.providername,m.itemname
                      ORDER BY "Total Orders" DESC LIMIT 5""",
            "params": [("Provider Name", "text", "Provider1")],
            "desc": "Top ordered items for a specific provider"
        },
        "5. Multi-language tourists with reservations": {
            "sql": """SELECT t.firstname AS "First Name", t.country AS "Country",
                             COUNT(tl.language) AS "Languages"
                      FROM public.tourist t
                      JOIN public.tourist_language tl ON t.touristid=tl.touristid
                      WHERE t.touristid IN (SELECT r.touristid FROM public.reservation r)
                      GROUP BY t.touristid,t.firstname,t.country
                      HAVING COUNT(tl.language)>=2
                      ORDER BY "Languages" DESC""",
            "params": [],
            "desc": "Tourists who speak at least 2 languages and have reservations"
        },
        "6. Coupons for Provider2 tourists from France": {
            "sql": """SELECT c.couponcode AS "Code", c.discountpercent AS "Discount%",
                             c.enddate AS "End Date", sp.providername AS "Provider", td.country AS "Country"
                      FROM public.coupon c
                      JOIN public.serviceprovider sp ON c.providerid=sp.providerid
                      JOIN public.include i ON c.couponid=i.couponid
                      JOIN public.touristdiscount td ON i.discountid=td.discountid
                      WHERE sp.providername='Provider2' AND td.country='France'""",
            "params": [],
            "desc": "Coupons for Provider2 that include France discount"
        },
        "7. Q4 2025 reservations for Provider1": {
            "sql": """SELECT r.reservationid AS "ID", r.reservationdate AS "Date",
                             t.firstname AS "Tourist", sp.providername AS "Provider"
                      FROM public.reservation r
                      JOIN public.tourist t ON r.touristid=t.touristid
                      JOIN public.serviceprovider sp ON r.providerid=sp.providerid
                      WHERE sp.providername='Provider1'
                        AND EXTRACT(YEAR FROM r.reservationdate)=2025
                        AND EXTRACT(MONTH FROM r.reservationdate) IN (10,11,12)""",
            "params": [],
            "desc": "Reservations at Provider1 in Q4 of 2025"
        },
        "8. Menu items never ordered": {
            "sql": """SELECT sp.providername AS "Provider", m.itemname AS "Item", m.price AS "Price"
                      FROM public.serviceprovider sp
                      JOIN public.menuitem m ON sp.providerid=m.providerid
                      WHERE NOT EXISTS (
                          SELECT 1 FROM public.orderline ol
                          WHERE ol.itemid=m.itemid AND ol.providerid=m.providerid)
                      ORDER BY sp.providername""",
            "params": [],
            "desc": "Menu items that have never appeared in any order"
        },
    }

    def build(self):
        top = ctk.CTkFrame(self.body, fg_color="transparent")
        top.pack(fill="x", pady=(0,10))

        label(top, "Select Query:").pack(side="left", padx=(0,10))
        self.qvar = ctk.StringVar(value=list(self.QUERIES.keys())[0])
        qmenu = ctk.CTkOptionMenu(top, variable=self.qvar,
                                   values=list(self.QUERIES.keys()),
                                   width=380, fg_color=CARD2,
                                   button_color=ACCENT,
                                   command=self._on_select)
        qmenu.pack(side="left", padx=4)
        btn(top, "▶ Run", self._run, color=SUCCESS, width=90).pack(side="left", padx=8)

        self.desc_lbl = label(self.body, "", color=MUTED, font=FONT_SMALL)
        self.desc_lbl.pack(anchor="w", pady=(0,6))

        # Param frame
        self.param_frame = ctk.CTkFrame(self.body, fg_color="transparent")
        self.param_frame.pack(fill="x", pady=(0,6))
        self.param_entries = []

        self.tbl = DataTable(self.body, ["Result"])
        self.tbl.pack(fill="both", expand=True)
        self._on_select(self.qvar.get())

    def _on_select(self, name):
        q = self.QUERIES[name]
        self.desc_lbl.configure(text=f"ℹ️  {q['desc']}")
        for w in self.param_frame.winfo_children(): w.destroy()
        self.param_entries = []
        for p in q["params"]:
            label(self.param_frame, p[0]+":").pack(side="left", padx=(0,4))
            e = entry(self.param_frame, width=180)
            if len(p) > 2: e.insert(0, p[2])
            e.pack(side="left", padx=(0,12))
            self.param_entries.append(e)

    def _run(self):
        name = self.qvar.get()
        q = self.QUERIES[name]
        params = [e.get() for e in self.param_entries]
        try:
            rows = execute_query(q["sql"], params if params else None)
            if not rows:
                messagebox.showinfo("Result", "Query returned 0 rows.")
                return
            cols = list(rows[0].keys())
            for w in self.body.winfo_children():
                if isinstance(w, DataTable): w.destroy()
            self.tbl = DataTable(self.body, cols)
            self.tbl.pack(fill="both", expand=True)
            self.tbl.load(rows)
        except Exception as e:
            self.notify(str(e), True)


# ═══════════════════════════════════════════════════════════════════════════
#  PROCEDURES SCREEN
# ═══════════════════════════════════════════════════════════════════════════
class ProceduresScreen(BaseScreen):
    title = "Procedures & Functions"
    icon  = "⚙️"

    def build(self):
        # Two columns
        left = card(self.body)
        left.place(relx=0, rely=0, relwidth=0.48, relheight=1)
        right = card(self.body)
        right.place(relx=0.52, rely=0, relwidth=0.48, relheight=1)

        self._build_left(left)
        self._build_right(right)

    def _build_left(self, parent):
        label(parent, "Functions", font=FONT_HEAD).pack(pady=(16,8), padx=16, anchor="w")

        # fn_get_tourist_spending
        f1 = card(parent)
        f1.pack(fill="x", padx=12, pady=8)
        label(f1, "fn_get_tourist_spending", font=("Segoe UI", 12, "bold"), color=ACCENT).pack(anchor="w", padx=12, pady=(12,4))
        label(f1, "Get total attraction spending for a tourist", color=MUTED, font=FONT_SMALL).pack(anchor="w", padx=12)
        row1 = ctk.CTkFrame(f1, fg_color="transparent")
        row1.pack(fill="x", padx=12, pady=8)
        label(row1, "Tourist ID:").pack(side="left")
        self.fn1_id = entry(row1, "e.g. 1", width=120)
        self.fn1_id.pack(side="left", padx=8)
        btn(row1, "Run", self._run_fn_spending, width=70).pack(side="left")
        self.fn1_result = label(f1, "", color=SUCCESS)
        self.fn1_result.pack(padx=12, pady=(0,12))

        # fn_get_provider_coupon_count
        f2 = card(parent)
        f2.pack(fill="x", padx=12, pady=8)
        label(f2, "fn_get_provider_coupon_count", font=("Segoe UI", 12, "bold"), color=ACCENT).pack(anchor="w", padx=12, pady=(12,4))
        label(f2, "Count coupons for a provider", color=MUTED, font=FONT_SMALL).pack(anchor="w", padx=12)
        row2 = ctk.CTkFrame(f2, fg_color="transparent")
        row2.pack(fill="x", padx=12, pady=8)
        label(row2, "Provider ID:").pack(side="left")
        self.fn2_id = entry(row2, "e.g. 403", width=120)
        self.fn2_id.pack(side="left", padx=8)
        btn(row2, "Run", self._run_fn_coupons, width=70).pack(side="left")
        self.fn2_result = label(f2, "", color=SUCCESS)
        self.fn2_result.pack(padx=12, pady=(0,12))

    def _build_right(self, parent):
        label(parent, "Procedures", font=FONT_HEAD).pack(pady=(16,8), padx=16, anchor="w")

        # pr_optimize_reservation_people
        p1 = card(parent)
        p1.pack(fill="x", padx=12, pady=8)
        label(p1, "pr_optimize_reservation_people", font=("Segoe UI", 12, "bold"), color=ACCENT2).pack(anchor="w", padx=12, pady=(12,4))
        label(p1, "Sets all single-person reservations to 2 people", color=MUTED, font=FONT_SMALL).pack(anchor="w", padx=12)
        btn(p1, "▶ Execute", self._run_pr_optimize, color=ACCENT2, width=140).pack(padx=12, pady=10)
        self.pr1_result = label(p1, "", color=SUCCESS)
        self.pr1_result.pack(padx=12, pady=(0,12))

        # pr_update_provider_coupon_status
        p2 = card(parent)
        p2.pack(fill="x", padx=12, pady=8)
        label(p2, "pr_update_provider_coupon_status", font=("Segoe UI", 12, "bold"), color=ACCENT2).pack(anchor="w", padx=12, pady=(12,4))
        label(p2, "Update all coupons of a provider to a new status", color=MUTED, font=FONT_SMALL).pack(anchor="w", padx=12)
        row_p = ctk.CTkFrame(p2, fg_color="transparent")
        row_p.pack(fill="x", padx=12, pady=8)
        label(row_p, "Provider ID:").pack(side="left")
        self.pr2_id = entry(row_p, "e.g. 403", width=100)
        self.pr2_id.pack(side="left", padx=6)
        label(row_p, "Status:").pack(side="left")
        self.pr2_status = ctk.CTkOptionMenu(row_p, values=["A","U","E"],
                                             width=80, fg_color=CARD2, button_color=ACCENT2)
        self.pr2_status.pack(side="left", padx=6)
        btn(row_p, "Run", self._run_pr_coupon_status, color=ACCENT2, width=70).pack(side="left")
        self.pr2_result = label(p2, "", color=SUCCESS)
        self.pr2_result.pack(padx=12, pady=(0,12))

        # Output console
        label(parent, "Output Console", font=FONT_HEAD).pack(pady=(16,4), padx=16, anchor="w")
        self.console = ctk.CTkTextbox(parent, fg_color=CARD2, text_color=SUCCESS,
                                       font=FONT_MONO, height=140)
        self.console.pack(fill="both", expand=True, padx=12, pady=(0,16))

    def _log(self, messages, ok=True):
        self.console.configure(state="normal")
        self.console.delete("1.0", "end")
        color = "✅" if ok else "❌"
        for m in messages:
            self.console.insert("end", f"{color} {m}\n")
        self.console.configure(state="disabled")

    def _run_fn_spending(self):
        tid = self.fn1_id.get().strip()
        if not tid: return
        ok, result, notices = call_function(
            "SELECT public.fn_get_tourist_spending(%s)", (int(tid),))
        if ok:
            self.fn1_result.configure(text=f"Total spending: {result} ₪", text_color=SUCCESS)
            self._log([f"Tourist {tid} total spending: {result}"] + notices)
        else:
            self.fn1_result.configure(text="Error - see console", text_color=DANGER)
            self._log(notices, ok=False)

    def _run_fn_coupons(self):
        pid = self.fn2_id.get().strip()
        if not pid: return
        ok, result, notices = call_function(
            "SELECT public.fn_get_provider_coupon_count(%s)", (int(pid),))
        if ok:
            self.fn2_result.configure(text=f"Coupon count: {result}", text_color=SUCCESS)
            self._log([f"Provider {pid} has {result} coupons"] + notices)
        else:
            self.fn2_result.configure(text="Error - see console", text_color=DANGER)
            self._log(notices, ok=False)

    def _run_pr_optimize(self):
        if not messagebox.askyesno("Confirm", "This will update all single-person reservations to 2 people. Continue?"):
            return
        ok, notices = call_procedure("CALL public.pr_optimize_reservation_people()")
        self.pr1_result.configure(
            text="Completed!" if ok else "Failed",
            text_color=SUCCESS if ok else DANGER)
        self._log(notices, ok)

    def _run_pr_coupon_status(self):
        pid = self.pr2_id.get().strip()
        status = self.pr2_status.get()
        if not pid: return
        if not messagebox.askyesno("Confirm", f"Update all coupons of provider {pid} to status '{status}'?"):
            return
        ok, notices = call_procedure(
            "CALL public.pr_update_provider_coupon_status(%s,%s)", (int(pid), status))
        self.pr2_result.configure(
            text="Updated!" if ok else "Failed",
            text_color=SUCCESS if ok else DANGER)
        self._log(notices, ok)


# ═══════════════════════════════════════════════════════════════════════════
#  FORM DIALOG
# ═══════════════════════════════════════════════════════════════════════════
class FormDialog(ctk.CTkToplevel):
    def __init__(self, parent, title, fields):
        super().__init__(parent)
        self.title(title)
        self.resizable(False, False)
        self.configure(fg_color=CARD)
        self.grab_set()
        self.result = None
        self.entries = []

        ctk.CTkLabel(self, text=title, font=FONT_HEAD, text_color=ACCENT).pack(pady=(20,16))

        for field in fields:
            name = field[0]
            ftype = field[1]
            default = field[3] if len(field) > 3 else (field[2] if ftype not in ("combo","text","password") else "")

            row = ctk.CTkFrame(self, fg_color="transparent")
            row.pack(fill="x", padx=24, pady=4)
            ctk.CTkLabel(row, text=name+":", width=160, anchor="w", font=FONT_BODY, text_color=TEXT).pack(side="left")

            if ftype == "combo":
                vals = field[2]
                var = ctk.StringVar(value=default if default else vals[0])
                w = ctk.CTkOptionMenu(row, variable=var, values=vals,
                                       width=220, fg_color=CARD2, button_color=ACCENT)
                w.pack(side="left")
                self.entries.append(var)
            elif ftype == "password":
                w = ctk.CTkEntry(row, show="•", width=220, fg_color=CARD2,
                                  border_color=BORDER, text_color=TEXT)
                if default: w.insert(0, default)
                w.pack(side="left")
                self.entries.append(w)
            else:
                w = ctk.CTkEntry(row, width=220, fg_color=CARD2,
                                  border_color=BORDER, text_color=TEXT)
                if default: w.insert(0, str(default))
                w.pack(side="left")
                self.entries.append(w)

        brow = ctk.CTkFrame(self, fg_color="transparent")
        brow.pack(pady=20)
        btn(brow, "✔ Save", self._save, color=SUCCESS, width=100).pack(side="left", padx=8)
        btn(brow, "✖ Cancel", self.destroy, color=DANGER, width=100).pack(side="left", padx=8)

    def _save(self):
        vals = []
        for e in self.entries:
            if isinstance(e, ctk.StringVar):
                vals.append(e.get())
            else:
                vals.append(e.get().strip())
        if any(v == "" for v in vals):
            messagebox.showwarning("Warning", "Please fill in all fields", parent=self)
            return
        self.result = vals
        self.destroy()


# ═══════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════
def _launch_main(root, user, role):
    for w in root.winfo_children():
        w.destroy()
    MainApp(root, user, role).pack(fill="both", expand=True)

def main():
    root = ctk.CTk()
    root.title("DineReserve – Restaurant Management System")
    root.geometry("1280x780")
    root.minsize(1000, 650)
    #fake_user = {"touristid": 1, "firstname": "First1", "lastname": "Last1", "email": "user1@mail.com", "country": "Israel"}
    #_launch_main(root, fake_user, role="tourist")
    LoginScreen(root, lambda u, role: _launch_main(root, u, role))
    root.mainloop()

if __name__ == "__main__":
    main()
