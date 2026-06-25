import os
from reportlab.lib.pagesizes import letter, A3, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# ======================================================================
# NUMBERED CANVAS FOR LATEX WHITEPAPER & SLIDES
# ======================================================================
class AcademicCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(AcademicCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Footer
        self.setFont("Times-Roman", 9)
        self.setFillColor(colors.HexColor("#333333"))
        page_text = f"{self._pageNumber}"
        self.drawCentredString(306, 36, page_text) # centered bottom
        
        # Header (only on page 2 and later)
        if self._pageNumber > 1:
            self.setFont("Times-Italic", 9)
            self.drawString(54, 750, "Mewundi: Tinker Tailor LLM Spy — Forensic Reconstructions")
            self.setStrokeColor(colors.HexColor("#dddddd"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
        self.restoreState()

class SlidesCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(SlidesCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_slide_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_slide_decorations(self, page_count):
        self.saveState()
        # Header bar background (Black Hat theme)
        self.setFillColor(colors.HexColor("#111111"))
        self.rect(0, 540, 792, 72, fill=True, stroke=False)
        
        # Header Text
        self.setFont("Helvetica-Bold", 10)
        self.setFillColor(colors.HexColor("#cc0000"))
        self.drawString(36, 575, "black hat")
        self.setFont("Helvetica", 10)
        self.setFillColor(colors.white)
        self.drawString(88, 575, " |  Tinker Tailor LLM Spy: Reconstructing Chats with Verity")
        
        # Red separator line
        self.setStrokeColor(colors.HexColor("#cc0000"))
        self.setLineWidth(2)
        self.line(0, 540, 792, 540)
        
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#666666"))
        self.drawString(36, 20, "Black Hat India Briefings Proposal  |  Dr. Sapna Vikram Mewundi")
        
        # Slide number
        slide_text = f"Slide {self._pageNumber} of {page_count}"
        self.drawRightString(756, 20, slide_text)
        self.restoreState()


# ======================================================================
# GENERATE LATEX-STYLE WHITEPAPER
# ======================================================================
def build_whitepaper():
    pdf_path = r"c:\Users\sapna\Downloads\verity-windows-build\ai-forensics-dashboard\whitepaper.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    # LaTeX-like styles (Times Roman, justified, indentations)
    title_style = ParagraphStyle('AcademicTitle', parent=styles['Normal'], fontName='Times-Bold', fontSize=18, leading=22, alignment=1, spaceAfter=8)
    author_style = ParagraphStyle('AcademicAuthor', parent=styles['Normal'], fontName='Times-Roman', fontSize=10, leading=13, alignment=1, spaceAfter=15)
    abstract_heading = ParagraphStyle('AbstractHeading', parent=styles['Normal'], fontName='Times-Bold', fontSize=9, leading=12, spaceBefore=10, spaceAfter=4, alignment=1)
    abstract_body = ParagraphStyle('AbstractBody', parent=styles['Normal'], fontName='Times-Roman', fontSize=8.5, leading=11, alignment=4, leftIndent=25, rightIndent=25, spaceAfter=15)
    
    section_style = ParagraphStyle('AcademicSection', parent=styles['Normal'], fontName='Times-Bold', fontSize=10.5, leading=14, spaceBefore=16, spaceAfter=8, alignment=1, keepWithNext=True)
    subsection_style = ParagraphStyle('AcademicSubsection', parent=styles['Normal'], fontName='Times-BoldItalic', fontSize=10, leading=13, spaceBefore=12, spaceAfter=6, keepWithNext=True)
    
    body_style = ParagraphStyle('AcademicBody', parent=styles['Normal'], fontName='Times-Roman', fontSize=10, leading=13, spaceAfter=6, alignment=4, firstLineIndent=18)
    body_no_indent = ParagraphStyle('AcademicBodyNoIndent', parent=styles['Normal'], fontName='Times-Roman', fontSize=10, leading=13, spaceAfter=6, alignment=4)
    
    bullet_style = ParagraphStyle('AcademicBullet', parent=body_no_indent, leftIndent=30, firstLineIndent=-12, spaceAfter=4)
    code_style = ParagraphStyle('AcademicCode', parent=styles['Normal'], fontName='Courier', fontSize=8, leading=10, textColor=colors.HexColor("#111111"), backColor=colors.HexColor("#f8f8f8"), borderPadding=6, spaceBefore=4, spaceAfter=4, leftIndent=15)
    
    story = []
    
    # Title & Authors
    story.append(Spacer(1, 10))
    story.append(Paragraph("Unveiling the Hidden Echoes: Zero-Dependency Forensic Reconstruction of 'Deleted' LLM Chats from Browser & Desktop LevelDB Instances", title_style))
    story.append(Paragraph("<b>Dr. Sapna Vikram Mewundi</b><br/>Lead Forensics Researcher, Verity Project<br/><i>sapna@local.dev</i>", author_style))
    
    # Abstract
    story.append(Paragraph("ABSTRACT", abstract_heading))
    story.append(Paragraph("As Large Language Model (LLM) portals become standard corporate utilities, proprietary source code, credentials, and sensitive configurations are routinely processed by users. When a user clicks 'Delete Chat' inside ChatGPT, Claude, or Gemini interfaces, they expect their local trace data to be permanently erased. However, because Chromium-based browsers (Chrome, Edge) and Electron desktop clients store this telemetry inside IndexedDB databases backed by Google's LevelDB engine, these deleted records persist on disk in write-ahead logs (.log) and uncompacted Sorted String Tables (.sst/.ldb). This paper details the reverse engineering of client-side LLM storage schemas and the V8 deserialization format. We present the mechanics of rebuilding conversation trees directly from raw binary fragments. Finally, we introduce a zero-dependency, pure-Python carving methodology to bypass active database locks and dynamically reconstruct deleted chat histories across all user profiles, providing incident responders with a secure, cryptographically validated chain of custody.", abstract_body))
    
    # Sections
    story.append(Paragraph("I. INTRODUCTION", section_style))
    story.append(Paragraph("The security industry has focused heavily on Generative AI security at the boundary layer: prompt injections, data guardrails, and cloud storage compliance. Virtually unmapped, however, is the client-side forensic footprint left behind by web interfaces and native wrapper applications on employee workstations.", body_style))
    story.append(Paragraph("When a user deletes a chat thread, the cloud-side storage is updated. Locally on the endpoint, however, the deletion is simply written as a LevelDB tombstone or index update. Because LevelDB is an append-only log-structured merge-tree (LSM tree), the actual serialized data blocks containing the prompts and responses remain intact in write-ahead log records or orphaned data blocks until compaction occurs. This creates a critical forensic window: an attacker or examiner with local access can recover sensitive, supposedly 'deleted' data.", body_style))
    
    story.append(Paragraph("II. LOW-LEVEL DATABASE ARCHITECTURE: INDEXEDDB & LEVELDB", section_style))
    story.append(Paragraph("Chromium browsers implement IndexedDB using LevelDB as the underlying storage engine. On Windows, these files reside in user AppData folders:", body_style))
    story.append(Paragraph("<code>%LOCALAPPDATA%\\Google\\Chrome\\User Data\\&lt;ProfileName&gt;\\IndexedDB\\https_chatgpt.com_0.indexeddb.leveldb\\</code>", code_style))
    story.append(Paragraph("Traditional forensics tools rely on loading LevelDB using compiled C++ drivers (like plyvel). During a live incident response triage, installing compiler tools on production machines is prohibited. Incident responders require a zero-dependency byte carver that directly dissects raw files.", body_style))
    
    story.append(Paragraph("III. REVERSING V8 SERIALIZATION: THE BINARY STRUCTURE", section_style))
    story.append(Paragraph("Chrome and Edge store IndexedDB records serialized in V8's internal binary serialization format (ValueSerializer).", body_style))
    
    story.append(Paragraph("A. Varint Decoding", subsection_style))
    story.append(Paragraph("V8 uses Google Protocol Buffer style varints (variable-length integers) to encode lengths and indexes. Every byte's highest-order bit (bit 7) is a flag: 1 means another byte follows, and 0 indicates the end of the varint. The lower 7 bits of each byte are concatenated to form the integer value.", body_style))
    
    story.append(Paragraph("B. V8 String Tags and UTF-16LE Encoding", subsection_style))
    story.append(Paragraph("Strings in the serialized format are prefixed with data type tags: OneByteString (0x22) indicates ASCII string, and TwoByteString (0x63) indicates UTF-16LE string. Crucially, the varint length of TwoByteString represents the number of bytes, not characters. The string is decoded by reading exactly length bytes and translating them using UTF-16LE.", body_style))
    
    story.append(Paragraph("IV. MESSAGE REASSEMBLY & ROLE RECONSTRUCTION", section_style))
    story.append(Paragraph("To map raw strings into chronological conversations, we reverse-engineered the serialization structure of the messages array.", body_style))
    
    story.append(Paragraph("A. Smi-Shifted Index Keys", subsection_style))
    story.append(Paragraph("V8 serializes array element properties using small integers (Smi) as keys. V8 encodes Smis by shifting the integer left by 1 bit (encoded = actual &lt;&lt; 1). The actual message index indicates the role: Odd actual indices represent User Prompts, and Even actual indices represent Assistant Responses. The role mapping is mathematically defined as:", body_style))
    story.append(Paragraph("<code>role = 'user' if (index / 2) mod 2 = 1 else 'assistant'</code>", code_style))
    
    story.append(Paragraph("B. Nesting Depth Tracking", subsection_style))
    story.append(Paragraph("V8 serialized message objects contain nested objects. Because object ends are marked by 0x7b, a simple parser would break out of the message parsing loop prematurely. A forensic-grade parser must track nesting depth, incrementing on object (0x6f) or array (0x61) tags, and decrementing on object end (0x7b).", body_style))
    
    story.append(Paragraph("V. THE VERITY FORENSIC FRAMEWORK", section_style))
    story.append(Paragraph("To operationalize these findings, we developed Verity, a zero-dependency, pure-Python carving tool. It bypasses Windows exclusive write locks by accessing write-ahead logs in read-only binary mode, cloning files dynamically, and reassembling conversation threads across all user profiles. To ensure evidence integrity, Verity seals the output using HMAC-SHA256 signatures, validated in-browser via the Web Cryptography API.", body_style))
    
    story.append(Paragraph("VI. CONCLUSION", section_style))
    story.append(Paragraph("This paper demonstrates that client-side ephemeral AI sessions are a myth. By parsing raw V8 serialized objects from LevelDB logs, investigators can fully recover deleted records. The Verity framework provides incident responders with a secure, lightweight tool to audit endpoints and protect corporate data assets.", body_style))
    
    doc.build(story, canvasmaker=AcademicCanvas)
    print("Academic Whitepaper built successfully.")


# ======================================================================
# GENERATE PRESENTATION SLIDES
# ======================================================================
def build_slides():
    pdf_path = r"c:\Users\sapna\Downloads\verity-windows-build\ai-forensics-dashboard\presentation_slides.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        leftMargin=36,
        rightMargin=36,
        topMargin=90,
        bottomMargin=54
    )
    styles = getSampleStyleSheet()
    
    slide_title_style = ParagraphStyle(
        'SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#cc0000"),
        spaceAfter=15
    )
    
    slide_body_style = ParagraphStyle(
        'SlideBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#222222"),
        spaceAfter=8
    )
    
    slide_bullet_style = ParagraphStyle(
        'SlideBullet',
        parent=slide_body_style,
        leftIndent=25,
        firstLineIndent=-15,
        spaceAfter=8
    )
    
    story = []
    
    # Slide 1: Title
    story.append(Spacer(1, 20))
    story.append(Paragraph("Tinker Tailor LLM Spy", ParagraphStyle('CoverT', fontName='Helvetica-Bold', fontSize=26, leading=32, alignment=1)))
    story.append(Paragraph("Reconstructing 'Deleted' Chats & Hijacking Sessions from Chromium Caches", ParagraphStyle('CoverSubT', fontName='Helvetica', fontSize=15, leading=20, alignment=1, spaceAfter=30)))
    story.append(Paragraph("<b>Dr. Sapna Vikram Mewundi</b><br/>Lead Forensics Researcher, Verity Project", ParagraphStyle('CoverAuth', fontName='Helvetica', fontSize=12, leading=16, alignment=1, spaceAfter=20)))
    story.append(Paragraph("Black Hat India 2026 Submission Proposal", ParagraphStyle('CoverVenue', fontName='Helvetica-Bold', fontSize=10, leading=14, alignment=1, textColor=colors.HexColor("#cc0000"))))
    story.append(PageBreak())
    
    # Slide 2: The Problem
    story.append(Paragraph("The Ephemeral AI Fallacy", slide_title_style))
    story.append(Paragraph("&bull; <b>The Illusion:</b> Users paste code/credentials into LLM portals (ChatGPT/Claude/Gemini) and delete the chats to avoid tracking.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Reality:</b> Chromium IndexedDB (backed by LevelDB LSM-tree) writes append-only. Deleted rows persist in raw logs (.log) and SSTables (.sst/.ldb).", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Risk:</b> Malware, compromise, or malicious insiders can carve these unencrypted caches to steal high-value corporate IP.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 3: LevelDB & IndexedDB Storage
    story.append(Paragraph("Chromium LevelDB Forensics", slide_title_style))
    story.append(Paragraph("&bull; <b>Target Paths:</b> Located in Local AppData folders under browser profiles (Default, Profile 1, Profile 3, etc.).", slide_bullet_style))
    story.append(Paragraph("&bull; <b>LSM-Tree Blocks:</b> Multi-level Sorted String Tables (SSTables) compressed with Snappy.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Exclusive Locks:</b> Browsers place exclusive file locks (LOCK) on active databases.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Triage Constraint:</b> Traditional tools require C++ leveldb compiling (plyvel), which is prohibited on production endpoint environments.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 4: Reversing V8 Serialization
    story.append(Paragraph("Reversing V8 ValueSerializer", slide_title_style))
    story.append(Paragraph("&bull; <b>IndexedDB Schema:</b> Records are serialized using V8's internal binary format.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Varint32 Reader:</b> Numbers are serialized using Protocol Buffer-style base-128 varints.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>OneByteString (0x22):</b> Standard ASCII string containing length prefix and bytes.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>TwoByteString (0x63):</b> UTF-16LE string. Length represents byte count, not character count. Reading too far causes parser alignment drift.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 5: Reassembling Chats & Role Math
    story.append(Paragraph("Decoding Conversation Trees", slide_title_style))
    story.append(Paragraph("&bull; <b>Smi-Shifted Keys:</b> Indexes in V8 arrays are shifted left by 1 bit (actual = encoded >> 1).", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Role Parity Math:</b> Distinguish user vs assistant using actual index parity:<br/><code>role = 'user' if (index / 2) mod 2 = 1 else 'assistant'</code>", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Nesting Depth Tracking:</b> Incrementing depth on object/array start (0x6f, 0x61), decrementing on end (0x7b). Prevents early termination on sub-properties.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Chronology:</b> Ordering using file modification times (mtime) and database byte offsets.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 6: Incident 1 - IP Leakage
    story.append(Paragraph("Scenario 1: Insider Data Exfiltration", slide_title_style))
    story.append(Paragraph("&bull; <b>The Incident:</b> A developer uploads sensitive source code and API keys, then deletes the conversation to cover tracks.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Obstacle:</b> Active browser maintains exclusive database locks.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Solution:</b> Open logs in read-only binary mode to bypass locks, clone active records in memory, and parse logs.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Evidence:</b> Carver successfully reconstructs the complete thread and leaked code block.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 7: Incident 2 - Session Hijacking
    story.append(Paragraph("Scenario 2: AI Account Hijacking", slide_title_style))
    story.append(Paragraph("&bull; <b>The Incident:</b> Infostealer malware harvests browser IndexedDB directories from target endpoints.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Vulnerability:</b> Active OAuth session tokens and JWTs for AI portals are stored in plaintext inside IndexedDB (bypassing DPAPI/Keychain).", slide_bullet_style))
    story.append(Paragraph("&bull; <b>The Takeover:</b> Attacker extracts the cookie string and takes over the user's active session without requiring credentials or triggering MFA.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 8: The Verity Forensic Tool
    story.append(Paragraph("Verity: Pure-Python Forensic Tool", slide_title_style))
    story.append(Paragraph("&bull; <b>Zero Dependencies:</b> Single-file python script running without compiled binary modules.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Dynamic sweeps:</b> Automatically walks and detects all default and custom Chrome/Edge browser user profiles.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Forensic Integrity:</b> Seals outputs with HMAC-SHA256 signatures, verified in-browser using Web Cryptography API to guarantee chain of custody.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Timeline Explorer:</b> A clean web-based dashboard interface to review evidence.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 9: Mitigations & Defense
    story.append(Paragraph("Enterprise Mitigations", slide_title_style))
    story.append(Paragraph("&bull; <b>Purge Policies:</b> Configure enterprise browsers to evict and wipe IndexedDB directories on user session logout.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Disk Protection:</b> Enforce full-disk encryption (BitLocker, FileVault) to prevent offline physical disk carving.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>EDR Monitoring:</b> Create threat rules to flag unusual read/copy requests on browser AppData folders.", slide_bullet_style))
    story.append(PageBreak())
    
    # Slide 10: Conclusion & Q&A
    story.append(Paragraph("Conclusion", slide_title_style))
    story.append(Paragraph("&bull; <b>Summary:</b> Ephemeral GenAI sessions leave deep, recoverable traces locally.", slide_bullet_style))
    story.append(Paragraph("&bull; <b>GitHub Release:</b> Open-source code available at: <i>github.com/prajwalchowdary2/verity-forensics</i>", slide_bullet_style))
    story.append(Paragraph("&bull; <b>Whitepaper:</b> Comprehensive academic whitepaper submitted to Review Board.", slide_bullet_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Q&A — Thank You!</b>", ParagraphStyle('SlideQA', fontName='Helvetica-Bold', fontSize=15, leading=20, alignment=1)))
    
    doc.build(story, canvasmaker=SlidesCanvas)
    print("Presentation slides built successfully.")


# ======================================================================
# GENERATE LARGE ACADEMIC POSTER (A3 Landscape)
# ======================================================================
def build_poster():
    pdf_path = r"c:\Users\sapna\Downloads\verity-windows-build\ai-forensics-dashboard\research_poster.pdf"
    
    # A3 Landscape size: 1190.55 width, 841.89 height
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A3),
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = getSampleStyleSheet()
    
    poster_title = ParagraphStyle('PosterTitle', fontName='Helvetica-Bold', fontSize=26, leading=30, alignment=1, textColor=colors.white)
    poster_authors = ParagraphStyle('PosterAuth', fontName='Helvetica', fontSize=12, leading=15, alignment=1, textColor=colors.HexColor("#dddddd"))
    
    card_title = ParagraphStyle('CardTitle', fontName='Helvetica-Bold', fontSize=13, leading=15, textColor=colors.HexColor("#cc0000"), spaceBefore=4, spaceAfter=6, keepWithNext=True)
    card_body = ParagraphStyle('CardBody', fontName='Helvetica', fontSize=9, leading=12.5, textColor=colors.HexColor("#222222"), spaceAfter=4)
    card_bullet = ParagraphStyle('CardBullet', parent=card_body, leftIndent=15, firstLineIndent=-8, spaceAfter=3)
    card_code = ParagraphStyle('CardCode', fontName='Courier', fontSize=7.5, leading=9, backColor=colors.HexColor("#f5f5f5"), borderPadding=4, leftIndent=10)
    
    # Title Block Table
    title_data = [
        [Paragraph("Tinker Tailor LLM Spy: Reconstructing Deleted Chats from Chromium LevelDB Caches", poster_title)],
        [Paragraph("<b>Dr. Sapna Vikram Mewundi</b> &bull; Lead Forensics Researcher, Verity Project", poster_authors)]
    ]
    title_table = Table(title_data, colWidths=[1118])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#111111")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('LINEBELOW', (0,0), (-1,-1), 3, colors.HexColor("#cc0000")),
    ]))
    
    # Columns setup
    col_w = 356
    
    # Column 1 elements
    col1_story = [
        Paragraph("Abstract & Background", card_title),
        Paragraph("GenAI portals like ChatGPT, Claude, and Gemini have become standard corporate utilities. Developers routinely copy and paste sensitive source code, internal configurations, and credentials into these clients. When users click 'Delete Chat' or clear histories, they believe it is erased. In reality, it stays on disk. Chromium-based browsers cache conversation telemetry inside client-side IndexedDB databases, backed by Google's LevelDB engine. Since LevelDB uses an append-only LSM-tree, deleted records remain intact in write-ahead logs (.log) and Sorted String Tables (.sst/.ldb) for days or weeks.", card_body),
        Spacer(1, 10),
        Paragraph("The Forensic Challenge", card_title),
        Paragraph("&bull; <b>File Locks:</b> Browsers place exclusive OS write locks on LevelDB databases during operation.", card_bullet),
        Paragraph("&bull; <b>Triage Barriers:</b> Traditional LevelDB parsers rely on compiled C++ libraries (plyvel), which cannot be compiled/installed on endpoint machines during live incident response.", card_bullet),
        Paragraph("&bull; <b>Data Formats:</b> Telemetry is packed inside V8 binary serialization arrays and Snappy-compressed blocks.", card_bullet),
        Spacer(1, 10),
        Paragraph("Chromium LevelDB Architecture", card_title),
        Paragraph("LevelDB stores data in active write-ahead logs (.log) and level-structured tables (.ldb/.sst). We bypass exclusive write locks on running browsers by reading the logs in read-only binary mode ('rb'), allowing us to clone logs in real-time without tripping filesystem blocks.", card_body),
    ]
    
    # Column 2 elements
    col2_story = [
        Paragraph("Reversing V8 ValueSerializer", card_title),
        Paragraph("IndexedDB values are serialized using V8's internal binary <code>ValueSerializer</code>. We implement a zero-dependency varint32 reader and block parser to decode these structures.", card_body),
        Paragraph("&bull; <b>Varint Decoding:</b> Rebuilding Google Protocol Buffer varint decoders in Python.", card_bullet),
        Paragraph("&bull; <b>String tag 0x22 (OneByte):</b> Standard ASCII string representation.", card_bullet),
        Paragraph("&bull; <b>String tag 0x63 (TwoByte):</b> UTF-16LE string. The length prefix represents the number of bytes, not characters. Correctly reading exactly length bytes prevents parser offset drift.", card_bullet),
        Paragraph("&bull; <b>Object boundaries:</b> Nesting depth tracking increments on object/array start (0x6f, 0x61) and decrements on end (0x7b) to prevent early parser breakages.", card_bullet),
        Spacer(1, 10),
        Paragraph("Reassembling Chats & Role Math", card_title),
        Paragraph("V8 encodes array property indices as Smi values (shifted left by 1 bit: actual = Smi >> 1). The role of the speaker (user prompt vs assistant response) is mapped mathematically using index parity:", card_body),
        Paragraph("<code>role = 'user' if (index / 2) mod 2 = 1 else 'assistant'</code>", card_code),
        Paragraph("Using this, we chronological sort carved records using file modification times (mtime) and database byte offsets.", card_body),
    ]
    
    # Column 3 elements
    col3_story = [
        Paragraph("Incident Scenario 1: Insider Leak", card_title),
        Paragraph("An employee uploads proprietary source code into ChatGPT, then deletes the conversation to bypass logging. Verity bypasses locks, clones logs, decompresses Snappy blocks, decodes V8 serialization, and fully reconstructs the deleted code block in under 5 seconds.", card_body),
        Spacer(1, 10),
        Paragraph("Incident Scenario 2: Token Hijack", card_title),
        Paragraph("Infostealer malware sweeps the browser's IndexedDB path and exfiltrates active session tokens. Because browsers fail to encrypt IndexedDB data (unlike standard cookies/passwords encrypted by DPAPI), the attacker extracts the token from local LevelDB caches, instantly taking over the user's active session without credentials or MFA.", card_body),
        Spacer(1, 10),
        Paragraph("Verity Tool & Mitigations", card_title),
        Paragraph("&bull; <b>Verity:</b> Open-source, zero-dependency Python script to audit endpoints and reassemble conversation logs.", card_bullet),
        Paragraph("&bull; <b>Integrity:</b> Seals evidence using HMAC-SHA256 signatures, validated in-browser.", card_bullet),
        Paragraph("&bull; <b>Mitigations:</b> Configure browsers to wipe IndexedDB on exit, enforce BitLocker/FileVault, and flag profile folder accesses via EDR.", card_bullet),
    ]
    
    # Format columns as tables
    column_table = Table([[col1_story, col2_story, col3_story]], colWidths=[360, 360, 360])
    column_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 15),
        ('BOTTOMPADDING', (0,0), (-1,-1), 15),
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#fafafa")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#ffffff")),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor("#fafafa")),
        ('LINEAFTER', (0,0), (1,0), 0.5, colors.HexColor("#dddddd")),
    ]))
    
    story = [
        title_table,
        Spacer(1, 15),
        column_table
    ]
    
    doc.build(story)
    print("Research Poster built successfully.")


if __name__ == '__main__':
    build_whitepaper()
    build_slides()
    build_poster()
