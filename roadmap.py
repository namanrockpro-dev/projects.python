"""
STUDENTS 40-DAY ROADMAP TRACKER
A personal dashboard for your journey from Python basics 
to college-ready developer .
"""

import customtkinter as ctk
import json
import os
from datetime import datetime, date
from tkinter import messagebox

# ═══════════════════════════════════════════════════════════
# APP CONFIGURATION
# ═══════════════════════════════════════════════════════════

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

DATA_FILE = "roadmap_data.json"

# ═══════════════════════════════════════════════════════════
# YOUR 40-DAY ROADMAP DATA
# ═══════════════════════════════════════════════════════════

ROADMAP = {
    1: {
        "title": "Setup Day + Python Restart",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: Computer basics, number systems, install GCC",
            "💻 Morning: Write Hello World in C",
            "🐍 Afternoon: Revise Python variables, data types, operators",
            "🐍 Afternoon: Solve 5 basic Python problems",
            "🌐 Evening: Learn what Web Dev / HTML / CSS / JS is",
            "📝 Evening: Create what-is-what.md notes file",
            "🏆 Night: LeetCode #1 Two Sum",
            "🏆 Night: HackerRank Python (2 problems)",
            "💚 Git commit & push (Day 1 streak!)"
        ]
    },
    2: {
        "title": "Conditionals Deep Dive",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C data types, sizeof, printf/scanf",
            "💻 Morning: Write 5 C programs (calc, percentage, etc.)",
            "🐍 Afternoon: Python if/elif/else, ternary, match-case",
            "🐍 Afternoon: Solve 7 conditional problems",
            "🌐 Evening: HTML basics, build About Me page",
            "🏆 Night: LeetCode #9 Palindrome Number",
            "💚 Git commit (Day 2 ✅)"
        ]
    },
    3: {
        "title": "Loops Mastery",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C if/else/switch-case",
            "💻 Morning: Write 5 C conditional programs",
            "🐍 Afternoon: Python for, while, break, continue",
            "🐍 Afternoon: Solve 10 loop problems",
            "⭐ Afternoon: Pattern programs (5 patterns)",
            "🎨 Evening: CSS basics, style your About Me page",
            "🏆 Night: LeetCode #13 Roman to Integer",
            "💚 Git commit (Day 3 ✅)"
        ]
    },
    4: {
        "title": "Loops in C + Python Strings",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C for/while/do-while loops",
            "💻 Morning: Write 7 C loop programs",
            "🐍 Afternoon: Python strings, slicing, methods",
            "🐍 Afternoon: 8 string problems",
            "🔵 Evening: What is C++? Hello World in C++",
            "🏆 Night: LeetCode #14 Longest Common Prefix",
            "💚 Git commit (Day 4 ✅)"
        ]
    },
    5: {
        "title": "Arrays (C) + Lists (Python)",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C arrays, traversal, sum/avg/max",
            "💻 Morning: Write 6 C array programs",
            "🐍 Afternoon: Python lists, comprehensions, methods",
            "🐍 Afternoon: 8 list problems",
            "☕ Evening: What is Java? Hello World in Java",
            "🏆 Night: LeetCode #26 Remove Duplicates",
            "💚 Git commit (Day 5 ✅)"
        ]
    },
    6: {
        "title": "Functions",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C functions, recursion basics",
            "💻 Morning: Write 6 C function programs",
            "🐍 Afternoon: Python functions, lambda, map/filter",
            "🐍 Afternoon: Tuples and sets",
            "📜 Evening: JavaScript basics in browser console",
            "🏆 Night: LeetCode #20 Valid Parentheses",
            "💚 Git commit (Day 6 ✅)"
        ]
    },
    7: {
        "title": "Dictionaries + File Handling + Review",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C 2D arrays, matrix operations",
            "💻 Morning: 5 C programs (matrix, strings)",
            "🐍 Afternoon: Python dictionaries, file handling",
            "🐍 Afternoon: 7 dict/file problems",
            "📚 Evening: What is DSA? Big O notation concept",
            "📊 Evening: WEEKLY REVIEW - clean up GitHub",
            "🏆 Night: LeetCode #21 Merge Two Sorted Lists",
            "💚 Git commit (Day 7 ✅) - WEEK 1 COMPLETE! 🎉"
        ]
    },
    8: {
        "title": "OOP in Python",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C pointers basics (&, *)",
            "💻 Morning: 5 C pointer programs",
            "🐍 Afternoon: Python OOP - classes, __init__, self",
            "🐍 Afternoon: Build Student, BankAccount, Rectangle classes",
            "🗄️ Evening: What is SQL? Basic queries",
            "🏆 Night: LeetCode #35 Search Insert Position",
            "💚 Git commit (Day 8 ✅)"
        ]
    },
    9: {
        "title": "OOP Advanced + Structures in C",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C structures, typedef",
            "💻 Morning: 4 C struct programs",
            "🐍 Afternoon: Python inheritance, polymorphism, dunder methods",
            "🤖 Evening: What is AI/ML/DL? Concepts",
            "🏆 Night: LeetCode #53 Maximum Subarray",
            "💚 Git commit (Day 9 ✅)"
        ]
    },
    10: {
        "title": "Modules + Error Handling + Mini Project",
        "phase": "Foundation Reset",
        "tasks": [
            "🌅 Morning: C file handling, malloc",
            "💻 Morning: 4 C programs (file I/O)",
            "🐍 Afternoon: Python exceptions, modules",
            "🚀 Afternoon: BUILD MINI PROJECT (Contact Book/Quiz/etc.)",
            "🔢 Evening: What is NumPy? 10 one-liners",
            "🏆 Night: LeetCode #66 + #67",
            "💚 Git commit (Day 10 ✅) - PHASE 1 COMPLETE! 🏆"
        ]
    },
    11: {
        "title": "DSA: Arrays & Searching",
        "phase": "Building Up",
        "tasks": [
            "🌅 Morning: C sorting (bubble, selection) + searching",
            "🧠 Afternoon: Time complexity, Big O, two pointer",
            "🏆 Afternoon: Solve 5 array problems",
            "🌐 Evening: BUILD portfolio website + deploy on GitHub Pages",
            "🏆 Night: LeetCode #121 + #217",
            "💚 Git commit (Day 11 ✅)"
        ]
    },
    12: {
        "title": "DSA: Strings",
        "phase": "Building Up",
        "tasks": [
            "🌅 Morning: C recursion deep dive",
            "💻 Morning: 5 recursive C programs",
            "🏆 Afternoon: 5 LeetCode string problems",
            "📊 Evening: What is Pandas? Load a Kaggle dataset",
            "🏆 Night: LeetCode #125 Valid Palindrome",
            "💚 Git commit (Day 12 ✅)"
        ]
    },
    13: {
        "title": "DSA: Stack & Queue",
        "phase": "Building Up",
        "tasks": [
            "🌅 Morning: C stack & queue implementation",
            "🐍 Afternoon: Python stack/queue, 5 LeetCode problems",
            "📈 Evening: What is Matplotlib? Create 4 charts",
            "🏆 Night: LeetCode #155 Min Stack",
            "💚 Git commit (Day 13 ✅)"
        ]
    },
    14: {
        "title": "DSA: Linked List + Physics Start",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Engineering Physics syllabus start",
            "🐍 Afternoon: Implement Linked List in Python",
            "🏆 Afternoon: Solve 3 LinkedList problems",
            "🔧 Evening: Git deep dive, create GitHub profile README",
            "🏆 Night: LeetCode #206 Reverse Linked List",
            "💚 Git commit (Day 14 ✅) - 2 WEEKS DONE! 🔥"
        ]
    },
    15: {
        "title": "Math + Hashing",
        "phase": "Building Up",
        "tasks": [
            "📐 Morning: Mathematics I - matrices, determinants",
            "🐍 Afternoon: Python hashing, dictionaries as hashmap",
            "🏆 Afternoon: 5 hashing problems",
            "🎮 Evening: What is Pygame? Bouncing ball animation",
            "🏆 Night: LeetCode #49 Group Anagrams",
            "💚 Git commit (Day 15 ✅)"
        ]
    },
    16: {
        "title": "Sorting Algorithms + Physics",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Physics + Math practice problems",
            "🧠 Afternoon: Bubble, Selection, Insertion, Merge, Quick Sort",
            "🏆 Afternoon: 3 sorting LeetCode problems",
            "🌐 Evening: What is Flask? Build first web app",
            "🏆 Night: LeetCode #75 Sort Colors",
            "💚 Git commit (Day 16 ✅)"
        ]
    },
    17: {
        "title": "Binary Search + C Revision",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: C programming revision",
            "🧠 Afternoon: Binary search variants",
            "🏆 Afternoon: 6 binary search problems",
            "🔌 Evening: What is API? Use Python requests",
            "🏆 Night: LeetCode #33 Search Rotated Array",
            "💚 Git commit (Day 17 ✅)"
        ]
    },
    18: {
        "title": "Trees (Binary Tree, BST)",
        "phase": "Building Up",
        "tasks": [
            "📐 Morning: Math - differential calculus",
            "🌳 Afternoon: Binary Tree, BST, traversals",
            "🏆 Afternoon: 4 tree problems",
            "🤖 Evening: What is TensorFlow/PyTorch?",
            "🏆 Night: LeetCode #104 Max Depth",
            "💚 Git commit (Day 18 ✅)"
        ]
    },
    19: {
        "title": "Graphs (Basics) + Mini Project",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: C enum, union, bitwise",
            "📊 Afternoon: Graphs, BFS, DFS",
            "🚀 Evening: MINI PROJECT (Snake/Flask Todo/Weather App)",
            "🏆 Night: LeetCode #733 Flood Fill",
            "💚 Git commit (Day 19 ✅)"
        ]
    },
    20: {
        "title": "DP Intro + SQL",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Math integration, physics, disaster mgmt",
            "🧠 Afternoon: Dynamic Programming intro",
            "🏆 Afternoon: 5 DP problems",
            "🗄️ Evening: SQL JOINs, GROUP BY, practice 5",
            "🏆 Night: LeetCode #70 Climbing Stairs",
            "💚 Git commit (Day 20 ✅) - HALFWAY! 🔥🔥🔥"
        ]
    },
    21: {
        "title": "Recursion & Backtracking",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Indian Knowledge System overview",
            "🔁 Afternoon: Backtracking - subsets, permutations",
            "🏆 Afternoon: 4 backtracking problems",
            "🖼️ Evening: What is Tkinter? Build simple GUI",
            "🏆 Night: LeetCode #78 Subsets",
            "💚 Git commit (Day 21 ✅)"
        ]
    },
    22: {
        "title": "Heap & Priority Queue + C++ Taste",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: COMPREHENSIVE C revision (10 GFG problems)",
            "🌲 Afternoon: Heap, heapq in Python",
            "🏆 Afternoon: 3 heap problems",
            "🔵 Evening: C++ classes, STL (vector, map, set)",
            "🏆 Night: LeetCode #215 Kth Largest",
            "💚 Git commit (Day 22 ✅)"
        ]
    },
    23: {
        "title": "ML Hands-On Day",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Math differential equations + physics",
            "📖 Morning: Communication Skills basics",
            "🤖 Afternoon: BUILD FIRST ML MODEL (sklearn Iris)",
            "📚 Evening: What is Docker/Cloud/DevOps/Blockchain?",
            "🏆 Night: LeetCode #136 + #169",
            "💚 Git commit (Day 23 ✅)"
        ]
    },
    24: {
        "title": "Project Day 1 (Major Project Start)",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: C revision + math practice",
            "🚀 Afternoon: START MAJOR PROJECT (AI Chatbot/Dashboard/etc.)",
            "🚀 Evening: Continue building",
            "🏆 Night: LeetCode #238 Product Except Self",
            "💚 Git commit (Day 24 ✅)"
        ]
    },
    25: {
        "title": "Project Day 2 (Complete + Deploy)",
        "phase": "Building Up",
        "tasks": [
            "📖 Morning: Mechatronics basics",
            "🚀 Afternoon: FINISH project + write README",
            "🚀 Evening: DEPLOY project (Render/Streamlit)",
            "🏆 Night: LeetCode #11 + #15",
            "💚 Git commit (Day 25 ✅) - PHASE 2 COMPLETE! 🏆"
        ]
    },
    26: {
        "title": "Advanced Python + Robotics Taste",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: Physics + Math + C practice",
            "🐍 Afternoon: Decorators, generators, type hints",
            "🤖 Evening: Robotics - Arduino, ROS, OpenCV try",
            "🏆 Night: LeetCode #102 + #98",
            "💚 Git commit (Day 26 ✅)"
        ]
    },
    27: {
        "title": "Bit Manipulation + Communication Skills",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: Professional email writing, LinkedIn bio",
            "💻 Afternoon: Bit manipulation tricks",
            "🏆 Afternoon: 5 bit manipulation problems",
            "🤖 Evening: What is Vibe Coding? Try Cursor IDE",
            "🏆 Night: LeetCode #268 + #338",
            "💚 Git commit (Day 27 ✅)"
        ]
    },
    28: {
        "title": "Full DSA Revision Day",
        "phase": "Consolidation",
        "tasks": [
            "📚 Morning+Afternoon: REVISE ALL DSA TOPICS",
            "📚 Re-solve 5 weakest problems",
            "📊 Evening: Update portfolio website with all projects",
            "🏆 Night: 3 random Easy problems",
            "💚 Git commit (Day 28 ✅) - 4 WEEKS! 🔥🔥🔥🔥"
        ]
    },
    29: {
        "title": "Intense College Prep - Day 1",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: C Programming FULL revision (20 GFG)",
            "📐 Afternoon: Math - matrices, determinants (15 problems)",
            "⚛️ Evening: Physics first 2 units complete",
            "🏆 Night: 1 LeetCode + Git commit"
        ]
    },
    30: {
        "title": "Intense College Prep - Day 2",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: C pointers, arrays, strings (deep dive)",
            "📐 Afternoon: Calculus (15 problems)",
            "⚛️ Evening: Physics numericals + Mechatronics",
            "🏆 Night: 1 LeetCode + Git commit"
        ]
    },
    31: {
        "title": "Intense College Prep - Day 3",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: C functions, recursion, file handling",
            "📐 Afternoon: Differential equations",
            "💻 Evening: Write 10 classic C lab programs",
            "🏆 Night: 1 LeetCode + Git commit"
        ]
    },
    32: {
        "title": "Intense College Prep - Day 4",
        "phase": "Consolidation",
        "tasks": [
            "⚛️ Morning: Physics lab experiments research",
            "📖 Afternoon: Disaster Management + IKS notes",
            "🗣️ Evening: Communication Skills - self intro practice",
            "🏆 Night: 1 LeetCode + Git commit"
        ]
    },
    33: {
        "title": "Build AI/ML Project",
        "phase": "Consolidation",
        "tasks": [
            "🤖 START AI/ML PROJECT:",
            "  → Image Classifier OR",
            "  → Sentiment Analyzer OR",
            "  → Face Detection App",
            "🚀 Use TensorFlow/Keras + Streamlit",
            "💚 Git commit (Day 33 ✅)"
        ]
    },
    34: {
        "title": "Complete & Deploy AI Project",
        "phase": "Consolidation",
        "tasks": [
            "🚀 FINISH the AI project",
            "🌐 DEPLOY on Streamlit Cloud / HuggingFace",
            "📝 Write AMAZING README with demo GIF",
            "💚 Git commit (Day 34 ✅)"
        ]
    },
    35: {
        "title": "Profile Polish Day",
        "phase": "Consolidation",
        "tasks": [
            "🐙 Morning: GitHub Profile README - badges, stats",
            "💼 Afternoon: LinkedIn profile complete update",
            "🏆 Evening: LeetCode + HackerRank profiles polish",
            "🏅 Evening: Get HackerRank certifications (Python, SQL)",
            "💚 Git commit (Day 35 ✅)"
        ]
    },
    36: {
        "title": "Resume + Competitive Coding",
        "phase": "Consolidation",
        "tasks": [
            "📄 Morning: Create one-page resume (Overleaf/Canva)",
            "🏆 Afternoon+Evening: LeetCode marathon (5 problems)",
            "🏅 Try HackerRank Python Basic + Problem Solving cert",
            "💚 Git commit (Day 36 ✅)"
        ]
    },
    37: {
        "title": "Comprehensive Revision Day",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: C Programming FINAL revision + cheat sheet",
            "🐍 Afternoon: Python FINAL revision + cheat sheet",
            "🧠 Evening: DSA revision + cheat sheet",
            "🏆 Night: 2 LeetCode problems",
            "💚 Git commit (Day 37 ✅)"
        ]
    },
    38: {
        "title": "Advanced Exploration Day",
        "phase": "Consolidation",
        "tasks": [
            "🤖 EXPLORE: TensorFlow/Keras deeper",
            "💬 EXPLORE: NLP basics with NLTK",
            "👁️ EXPLORE: Computer Vision with OpenCV",
            "🎮 EXPLORE: Reinforcement Learning concept",
            "📝 Final update to what-is-what.md",
            "🏆 Night: 2 LeetCode problems",
            "💚 Git commit (Day 38 ✅)"
        ]
    },
    39: {
        "title": "Mock Test Day",
        "phase": "Consolidation",
        "tasks": [
            "📝 Morning: C Programming MOCK TEST (2 hrs, 15 Q)",
            "📐 Afternoon: Math MOCK TEST (2 hrs)",
            "⚛️ Evening: Physics MOCK (1.5 hrs)",
            "🏆 Night: 2 LeetCode problems",
            "📊 Identify weak areas",
            "💚 Git commit (Day 39 ✅)"
        ]
    },
    40: {
        "title": "GRAND FINALE 🎉",
        "phase": "Consolidation",
        "tasks": [
            "📖 Morning: Final revision of weak areas",
            "🚀 Afternoon: Polish all GitHub repos + portfolio",
            "📊 Afternoon: Create '40-Day Journey' LinkedIn post",
            "📊 Evening: Final stats review - all checkboxes",
            "🏆 Night: Solve 3 LeetCode problems to end strong",
            "💚 FINAL Git commit (Day 40 ✅✅✅)",
            "🎉 CELEBRATE! YOU DID IT! 🏆🔥"
        ]
    }
}

# Motivational quotes from films you love
QUOTES = [
    '"Mhari chhoriyan chhoron se kam hai ke?" - Dangal',
    '"Buongiorno principessa!" - Life is Beautiful',
    '"I\'m tired, boss." - The Green Mile',
    '"In case I don\'t see ya, good afternoon, good evening, and good night." - Truman Show',
    '"Stupid is as stupid does." - Forrest Gump',
    '"Wake up, Samurai. We have a city to burn." - Cyberpunk 2077',
    '"O Captain! My Captain!" - Dead Poets Society',
    '"Get busy living, or get busy dying." - Shawshank Redemption',
    '"Daulat ke saath laalach bhi aata hai..." - Tumbbad',
    '"Why do we fall? So we can learn to pick ourselves up." - Batman Begins'
]

# ═══════════════════════════════════════════════════════════
# DATA MANAGEMENT
# ═══════════════════════════════════════════════════════════

def load_data():
    """Load saved progress from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        "completed_tasks": {},  # {day: [task_indices]}
        "start_date": str(date.today()),
        "leetcode_count": 0,
        "github_commits": 0,
        "notes": "",
        "last_active_day": 1,
        "completed_days": []
    }

def save_data(data):
    """Save progress to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# ═══════════════════════════════════════════════════════════
# MAIN APP CLASS
# ═══════════════════════════════════════════════════════════

class RoadmapApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("🚀 your's 40-Day Roadmap Tracker")
        self.geometry("1200x750")
        self.minsize(1000, 650)
        
        self.data = load_data()
        self.current_day = self.data.get("last_active_day", 1)
        self.task_vars = []
        
        self.setup_ui()
        self.show_day(self.current_day)
    
    def setup_ui(self):
        """Build the main UI layout"""
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # ═══ SIDEBAR (Left) ═══
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color="#1a1a2e")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(20, weight=1)
        
        # Logo/Title
        title = ctk.CTkLabel(
            self.sidebar, 
            text="🚀 ROADMAP\nTRACKER",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#00ffff"
        )
        title.grid(row=0, column=0, padx=20, pady=(25, 15))
        
        # Subtitle
        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="your\n40 Days to Greatness",
            font=ctk.CTkFont(size=12),
            text_color="#888"
        )
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20))
        
        # Stats Section
        self.stats_frame = ctk.CTkFrame(self.sidebar, fg_color="#16213e", corner_radius=10)
        self.stats_frame.grid(row=2, column=0, padx=15, pady=10, sticky="ew")
        
        stats_title = ctk.CTkLabel(
            self.stats_frame,
            text="📊 YOUR STATS",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ff00ff"
        )
        stats_title.pack(pady=(10, 5))
        
        self.streak_label = ctk.CTkLabel(
            self.stats_frame,
            text="🔥 Streak: 0 days",
            font=ctk.CTkFont(size=13)
        )
        self.streak_label.pack(pady=2)
        
        self.completed_label = ctk.CTkLabel(
            self.stats_frame,
            text="✅ Completed: 0/40",
            font=ctk.CTkFont(size=13)
        )
        self.completed_label.pack(pady=2)
        
        self.leetcode_label = ctk.CTkLabel(
            self.stats_frame,
            text="🏆 LeetCode: 0",
            font=ctk.CTkFont(size=13)
        )
        self.leetcode_label.pack(pady=2)
        
        self.github_label = ctk.CTkLabel(
            self.stats_frame,
            text="💚 GitHub: 0",
            font=ctk.CTkFont(size=13)
        )
        self.github_label.pack(pady=(2, 10))
        
        # Counter Buttons
        counter_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        counter_frame.grid(row=3, column=0, padx=15, pady=5, sticky="ew")
        
        leet_btn = ctk.CTkButton(
            counter_frame,
            text="+ LeetCode",
            command=self.increment_leetcode,
            fg_color="#ffa500",
            hover_color="#ff8c00",
            height=30
        )
        leet_btn.pack(fill="x", pady=3)
        
        git_btn = ctk.CTkButton(
            counter_frame,
            text="+ Git Commit",
            command=self.increment_github,
            fg_color="#00b894",
            hover_color="#00a884",
            height=30
        )
        git_btn.pack(fill="x", pady=3)
        
        # Day Navigation
        nav_label = ctk.CTkLabel(
            self.sidebar,
            text="📅 JUMP TO DAY",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#ff00ff"
        )
        nav_label.grid(row=4, column=0, padx=20, pady=(15, 5))
        
        self.day_option = ctk.CTkOptionMenu(
            self.sidebar,
            values=[f"Day {i}" for i in range(1, 41)],
            command=self.jump_to_day,
            fg_color="#16213e",
            button_color="#0f3460",
            button_hover_color="#00ffff"
        )
        self.day_option.grid(row=5, column=0, padx=15, pady=5, sticky="ew")
        self.day_option.set(f"Day {self.current_day}")
        
        # Quote Box
        quote_frame = ctk.CTkFrame(self.sidebar, fg_color="#0f3460", corner_radius=10)
        quote_frame.grid(row=6, column=0, padx=15, pady=20, sticky="ew")
        
        quote_label = ctk.CTkLabel(
            quote_frame,
            text="💭 DAILY MOTIVATION",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#00ffff"
        )
        quote_label.pack(pady=(8, 5))
        
        import random
        self.quote_text = ctk.CTkLabel(
            quote_frame,
            text=random.choice(QUOTES),
            font=ctk.CTkFont(size=10, slant="italic"),
            wraplength=210,
            text_color="#ddd"
        )
        self.quote_text.pack(padx=10, pady=(0, 10))
        
        # ═══ MAIN CONTENT AREA ═══
        self.main_frame = ctk.CTkFrame(self, fg_color="#0f0f1e")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        
        # Header
        self.header_frame = ctk.CTkFrame(self.main_frame, fg_color="#16213e", corner_radius=10)
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 5))
        
        self.day_title = ctk.CTkLabel(
            self.header_frame,
            text="",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ffff"
        )
        self.day_title.pack(pady=(15, 5))
        
        self.phase_label = ctk.CTkLabel(
            self.header_frame,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#ff00ff"
        )
        self.phase_label.pack(pady=(0, 10))
        
        # Progress bar
        self.progress_label = ctk.CTkLabel(
            self.header_frame,
            text="Progress: 0/0 tasks",
            font=ctk.CTkFont(size=12)
        )
        self.progress_label.pack(pady=(0, 5))
        
        self.progress_bar = ctk.CTkProgressBar(self.header_frame, height=15, progress_color="#00ffff")
        self.progress_bar.pack(fill="x", padx=20, pady=(0, 15))
        self.progress_bar.set(0)
        
        # Navigation buttons
        nav_btn_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        nav_btn_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        nav_btn_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        self.prev_btn = ctk.CTkButton(
            nav_btn_frame,
            text="⬅ Previous Day",
            command=self.prev_day,
            fg_color="#0f3460",
            hover_color="#16213e",
            height=35
        )
        self.prev_btn.grid(row=0, column=0, padx=5, sticky="ew")
        
        self.today_btn = ctk.CTkButton(
            nav_btn_frame,
            text="📍 Mark Day Complete",
            command=self.mark_day_complete,
            fg_color="#00b894",
            hover_color="#00a884",
            height=35
        )
        self.today_btn.grid(row=0, column=1, padx=5, sticky="ew")
        
        self.next_btn = ctk.CTkButton(
            nav_btn_frame,
            text="Next Day ➡",
            command=self.next_day,
            fg_color="#0f3460",
            hover_color="#16213e",
            height=35
        )
        self.next_btn.grid(row=0, column=2, padx=5, sticky="ew")
        
        # Tasks scrollable area
        self.tasks_frame = ctk.CTkScrollableFrame(
            self.main_frame, 
            fg_color="#1a1a2e",
            corner_radius=10,
            label_text="📋 TODAY'S TASKS",
            label_font=ctk.CTkFont(size=16, weight="bold")
        )
        self.tasks_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        
        # Notes section
        notes_frame = ctk.CTkFrame(self.main_frame, fg_color="#16213e", corner_radius=10)
        notes_frame.grid(row=3, column=0, sticky="ew", padx=10, pady=(5, 10))
        
        notes_label = ctk.CTkLabel(
            notes_frame,
            text="📝 QUICK NOTES",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#ff00ff"
        )
        notes_label.pack(pady=(10, 5))
        
        self.notes_text = ctk.CTkTextbox(
            notes_frame,
            height=80,
            fg_color="#0f0f1e",
            text_color="#ddd"
        )
        self.notes_text.pack(fill="x", padx=15, pady=(0, 10))
        self.notes_text.insert("1.0", self.data.get("notes", ""))
        
        save_notes_btn = ctk.CTkButton(
            notes_frame,
            text="💾 Save Notes",
            command=self.save_notes,
            fg_color="#ff00ff",
            hover_color="#cc00cc",
            height=30
        )
        save_notes_btn.pack(pady=(0, 10))
        
        self.update_stats()
    
    def show_day(self, day_num):
        """Display tasks for a specific day"""
        self.current_day = day_num
        day_data = ROADMAP[day_num]
        
        # Update header
        self.day_title.configure(text=f"📅 Day {day_num}: {day_data['title']}")
        self.phase_label.configure(text=f"🎯 Phase: {day_data['phase']}")
        
        # Clear previous tasks
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        
        # Get completed tasks for this day
        completed = self.data["completed_tasks"].get(str(day_num), [])
        
        # Create task checkboxes
        self.task_vars = []
        for idx, task in enumerate(day_data["tasks"]):
            var = ctk.BooleanVar(value=(idx in completed))
            self.task_vars.append(var)
            
            task_frame = ctk.CTkFrame(self.tasks_frame, fg_color="#0f3460", corner_radius=8)
            task_frame.pack(fill="x", padx=5, pady=3)
            
            cb = ctk.CTkCheckBox(
                task_frame,
                text=task,
                variable=var,
                command=lambda i=idx: self.toggle_task(i),
                font=ctk.CTkFont(size=13),
                fg_color="#00ffff",
                hover_color="#00cccc",
                text_color="#fff",
        )
            cb.pack(anchor="w", padx=15, pady=10)
        
        self.update_progress()
        self.data["last_active_day"] = day_num
        save_data(self.data)
    
    def toggle_task(self, task_idx):
        """Toggle a task's completion status"""
        day_str = str(self.current_day)
        if day_str not in self.data["completed_tasks"]:
            self.data["completed_tasks"][day_str] = []
        
        if self.task_vars[task_idx].get():
            if task_idx not in self.data["completed_tasks"][day_str]:
                self.data["completed_tasks"][day_str].append(task_idx)
        else:
            if task_idx in self.data["completed_tasks"][day_str]:
                self.data["completed_tasks"][day_str].remove(task_idx)
        
        save_data(self.data)
        self.update_progress()
        self.update_stats()
    
    def update_progress(self):
        """Update progress bar for current day"""
        total = len(ROADMAP[self.current_day]["tasks"])
        completed = sum(1 for var in self.task_vars if var.get())
        
        self.progress_label.configure(text=f"Progress: {completed}/{total} tasks")
        self.progress_bar.set(completed / total if total > 0 else 0)
    
    def update_stats(self):
        """Update sidebar stats"""
        # Calculate completed days
        completed_days = 0
        for day_num in range(1, 41):
            day_str = str(day_num)
            completed_tasks = self.data["completed_tasks"].get(day_str, [])
            total_tasks = len(ROADMAP[day_num]["tasks"])
            if len(completed_tasks) == total_tasks and total_tasks > 0:
                completed_days += 1
        
        # Calculate streak
        streak = len(self.data.get("completed_days", []))
        
        self.streak_label.configure(text=f"🔥 Streak: {streak} days")
        self.completed_label.configure(text=f"✅ Completed: {completed_days}/40")
        self.leetcode_label.configure(text=f"🏆 LeetCode: {self.data['leetcode_count']}")
        self.github_label.configure(text=f"💚 GitHub: {self.data['github_commits']}")
    
    def mark_day_complete(self):
        """Mark current day as fully complete"""
        # Auto-check all tasks
        for var in self.task_vars:
            var.set(True)
        
        day_str = str(self.current_day)
        self.data["completed_tasks"][day_str] = list(range(len(ROADMAP[self.current_day]["tasks"])))
        
        if self.current_day not in self.data["completed_days"]:
            self.data["completed_days"].append(self.current_day)
        
        save_data(self.data)
        self.show_day(self.current_day)
        self.update_stats()
        
        messagebox.showinfo(
            "Day Complete! 🎉", 
            f"Day {self.current_day} marked as complete!\n\n"
            f"Streak: {len(self.data['completed_days'])} days 🔥\n\n"
            "Keep going! You're building greatness."
        )
    
    def prev_day(self):
        """Go to previous day"""
        if self.current_day > 1:
            self.day_option.set(f"Day {self.current_day - 1}")
            self.show_day(self.current_day - 1)
    
    def next_day(self):
        """Go to next day"""
        if self.current_day < 40:
            self.day_option.set(f"Day {self.current_day + 1}")
            self.show_day(self.current_day + 1)
    
    def jump_to_day(self, choice):
        """Jump to specific day from dropdown"""
        day_num = int(choice.split()[1])
        self.show_day(day_num)
    
    def increment_leetcode(self):
        """Increment LeetCode counter"""
        self.data["leetcode_count"] += 1
        save_data(self.data)
        self.update_stats()
    
    def increment_github(self):
        """Increment GitHub commits counter"""
        self.data["github_commits"] += 1
        save_data(self.data)
        self.update_stats()
    
    def save_notes(self):
        """Save notes to data file"""
        self.data["notes"] = self.notes_text.get("1.0", "end-1c")
        save_data(self.data)
        messagebox.showinfo("Saved! 💾", "Your notes have been saved.")

# ═══════════════════════════════════════════════════════════
# RUN THE APP
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    app = RoadmapApp()
    app.mainloop() 


    # just cheack
