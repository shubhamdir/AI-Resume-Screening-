from PyPDF2 import PdfReader
import re


# =====================================
# PDF Text Extraction
# =====================================

def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


# =====================================
# Email Extraction
# =====================================

def extract_email(text):

    emails = re.findall(
        r"[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return emails[0] if emails else None


# =====================================
# Phone Extraction
# =====================================

def extract_phone(text):

    match = re.search(
        r"(\+91[- ]?)?[6-9]\d{9}",
        text
    )

    return match.group() if match else None


# =====================================
# Skill Extraction
# =====================================

def extract_skills(text):

    skill_list = [

        # =====================================
        # IT & Computer Science
        # =====================================

        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "TypeScript",
        "PHP",
        "Go",
        "Rust",
        "Kotlin",
        "Swift",
        "HTML",
        "CSS",
        "Bootstrap",
        "Tailwind CSS",
        "React",
        "Angular",
        "Vue.js",
        "Next.js",
        "Node.js",
        "Express.js",
        "FastAPI",
        "Django",
        "Flask",
        "Spring Boot",
        "ASP.NET",
        "REST API",
        "GraphQL",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "MongoDB",
        "Oracle",
        "Redis",
        "Firebase",
        "Git",
        "GitHub",
        "GitLab",
        "Docker",
        "Kubernetes",
        "Jenkins",
        "CI/CD",
        "Linux",
        "Shell Scripting",
        "AWS",
        "Azure",
        "Google Cloud",
        "Power BI",
        "Tableau",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "AI",
        "NLP",
        "Computer Vision",
        "LLM",
        "Data Analysis",
        "Data Visualization",
        "Data Structures",
        "Algorithms",
        "DBMS",
        "OOP",
        "System Design",
        "Cyber Security",
        "Ethical Hacking",
        "Network Security",
        "Penetration Testing",
        "Android",
        "Android Studio",
        "Flutter",
        "React Native",
        "Blockchain",
        "Ethereum",
        "Smart Contracts",

        # =====================================
        # IoT & Embedded Systems
        # =====================================

        "IoT",
        "Internet of Things",
        "Arduino",
        "ESP8266",
        "ESP32",
        "NodeMCU",
        "Raspberry Pi",
        "Embedded Systems",
        "Embedded C",
        "Embedded Linux",
        "RTOS",
        "Firmware Development",
        "Electronics",
        "Digital Electronics",
        "Analog Electronics",
        "Circuit Design",
        "PCB Design",
        "Sensors",
        "Actuators",
        "RFID",
        "GPS",
        "GSM Module",
        "I2C",
        "SPI",
        "UART",
        "MQTT",
        "Bluetooth",
        "BLE",
        "WiFi",
        "Zigbee",
        "LoRaWAN",
        "NFC",
        "AWS IoT",
        "Azure IoT",
        "ThingSpeak",
        "Blynk",
        "Robotics",

        # =====================================
        # Finance
        # =====================================

        "Financial Analysis",
        "Financial Modeling",
        "Valuation",
        "Forecasting",
        "Budgeting",
        "Accounting",
        "Bookkeeping",
        "Investment Banking",
        "Corporate Banking",
        "Credit Analysis",
        "Investment Analysis",
        "Portfolio Management",
        "Equity Research",
        "Stock Market",
        "Mutual Funds",
        "Asset Management",
        "Risk Management",
        "Compliance",
        "Auditing",
        "Taxation",
        "GST",
        "Income Tax",
        "Financial Planning",
        "Financial Reporting",
        "Cash Flow Management",
        "Tally",
        "SAP FICO",
        "QuickBooks",
        "Advanced Excel",
        "FinTech",
        "Digital Payments",
        "CFA",
        "FRM",
        "NISM",

        # =====================================
        # Marketing
        # =====================================

        "Digital Marketing",
        "SEO",
        "SEM",
        "Keyword Research",
        "Social Media Marketing",
        "Instagram Marketing",
        "Facebook Marketing",
        "LinkedIn Marketing",
        "YouTube Marketing",
        "Influencer Marketing",
        "Content Marketing",
        "Content Creation",
        "Content Strategy",
        "Copywriting",
        "Blog Writing",
        "Google Ads",
        "Facebook Ads",
        "PPC",
        "Campaign Management",
        "Google Analytics",
        "Performance Marketing",
        "Lead Generation",
        "Email Marketing",
        "Mailchimp",
        "Customer Acquisition",
        "Growth Marketing",
        "Brand Management",

        # =====================================
        # Human Resources
        # =====================================

        "Human Resources",
        "HR Management",
        "Recruitment",
        "Talent Acquisition",
        "Candidate Screening",
        "Interviewing",
        "Campus Recruitment",
        "Employee Relations",
        "Employee Engagement",
        "Payroll",
        "Compensation Management",
        "Labor Laws",
        "Training",
        "Learning and Development",
        "Onboarding",
        "Workforce Planning",
        "HRMS",
        "Workday",
        "SAP SuccessFactors",
        "HR Analytics",
        "People Analytics",
        "Performance Management",

        # =====================================
        # Operations
        # =====================================

        "Operations Management",
        "Supply Chain Management",
        "Logistics",
        "Warehouse Management",
        "Inventory Management",
        "Procurement",
        "Vendor Management",
        "Contract Management",
        "Production Planning",
        "Production Management",
        "Quality Management",
        "Quality Assurance",
        "Quality Control",
        "Six Sigma",
        "Lean Manufacturing",
        "Kaizen",
        "SAP MM",
        "SAP SCM",
        "MIS Reporting",
        "Process Improvement",

        # =====================================
        # Content & Media
        # =====================================

        "Content Writing",
        "Copywriting",
        "Technical Writing",
        "Creative Writing",
        "Article Writing",
        "Proofreading",
        "Editing",
        "Grammar",
        "Research",
        "Script Writing",
        "Storytelling",
        "Journalism",
        "News Reporting",
        "Media Production",
        "Videography",
        "Photography",
        "Cinematography",
        "Video Editing",
        "Photo Editing",
        "Adobe Premiere Pro",
        "After Effects",

        # =====================================
        # Design
        # =====================================

        "UI Design",
        "UX Design",
        "User Research",
        "Wireframing",
        "Prototyping",
        "Figma",
        "Adobe XD",
        "Sketch",
        "Photoshop",
        "Illustrator",
        "Canva",
        "Design Thinking",
        "Interaction Design",
        "Responsive Design",
        "Visual Design",
        "Typography",

        # =====================================
        # Sales
        # =====================================

        "Sales",
        "Business Development",
        "Lead Generation",
        "CRM",
        "Salesforce",
        "Cold Calling",
        "Inside Sales",
        "B2B Sales",
        "B2C Sales",
        "Client Relationship Management",
        "Negotiation",
        "Prospecting",
        "Customer Acquisition",
        "Revenue Growth",
        "Pipeline Management",
        "Account Management",

        # =====================================
        # Customer Support
        # =====================================

        "Customer Support",
        "Customer Service",
        "Technical Support",
        "Zendesk",
        "Freshdesk",
        "Problem Resolution",
        "Complaint Handling",
        "Email Support",
        "Chat Support",
        "Call Center Operations",

        # =====================================
        # Chemical Engineering
        # =====================================

        "Chemical Engineering",
        "Process Engineering",
        "Process Design",
        "Plant Operations",
        "Process Safety",
        "Industrial Safety",
        "Heat Transfer",
        "Mass Transfer",
        "Thermodynamics",
        "Fluid Mechanics",
        "Aspen HYSYS",
        "Aspen Plus",
        "AutoCAD",
        "MATLAB",
        "Petrochemical",
        "Oil and Gas",
        "Environmental Engineering",
        "Wastewater Treatment",

        # =====================================
        # Common Soft Skills
        # =====================================

        "Communication",
        "Leadership",
        "Problem Solving",
        "Critical Thinking",
        "Teamwork",
        "Project Management",
        "Time Management",
        "Presentation Skills",
        "Decision Making"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skill_list:

        pattern = r"\b" + re.escape(
            skill.lower()
        ) + r"\b"

        if re.search(
            pattern,
            text_lower
        ):
            found_skills.append(skill)

    return list(set(found_skills))