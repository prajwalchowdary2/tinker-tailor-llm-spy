import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
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
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#cc0000"))
            self.drawString(54, 755, "black hat")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#555555"))
            self.drawString(98, 755, " |  Black Hat India – Briefings Submission Proposal")
            
            self.setStrokeColor(colors.HexColor("#dddddd"))
            self.setLineWidth(0.5)
            self.line(54, 747, 558, 747)
            
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#888888"))
            self.drawString(54, 40, "CONFIDENTIAL – FOR REVIEW BOARD ONLY")
            
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 40, page_text)
        else:
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#888888"))
            self.drawString(54, 40, "CONFIDENTIAL – FOR REVIEW BOARD ONLY")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(558, 40, page_text)
            
        self.restoreState()

def build_pdf():
    pdf_path = r"c:\Users\sapna\Downloads\verity-windows-build\ai-forensics-dashboard\blackhat_india_submission_proposal.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=54, rightMargin=54, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor("#111111"), spaceAfter=15)
    section_style = ParagraphStyle('SectionHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor("#cc0000"), spaceBefore=16, spaceAfter=8, keepWithNext=True)
    subsection_style = ParagraphStyle('SubsectionHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=11, leading=14, textColor=colors.HexColor("#222222"), spaceBefore=10, spaceAfter=4, keepWithNext=True)
    body_style = ParagraphStyle('ProposalBody', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, spaceAfter=6, textColor=colors.HexColor("#2b2b2b"))
    bullet_style = ParagraphStyle('ProposalBullet', parent=body_style, leftIndent=15, firstLineIndent=-10, spaceAfter=4)
    code_style = ParagraphStyle('ProposalCode', parent=styles['Normal'], fontName='Courier', fontSize=8.5, leading=11, textColor=colors.HexColor("#111111"), backColor=colors.HexColor("#f8f8f8"), borderPadding=6, spaceBefore=5, spaceAfter=5)
    
    story = []
    logo_data = [[Paragraph("<font color='white' size='24'><b>black hat</b></font>", ParagraphStyle('LogoL', fontName='Helvetica-Bold', fontSize=24, textColor=colors.white)), Paragraph("<font color='#cccccc' size='10'><b>Briefings Submission Proposal</b></font>", ParagraphStyle('LogoR', fontName='Helvetica-Bold', fontSize=10, alignment=2, textColor=colors.HexColor("#cccccc")))]]
    logo_table = Table(logo_data, colWidths=[250, 254])
    logo_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#111111")), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('BOTTOMPADDING', (0,0), (-1,-1), 12), ('TOPPADDING', (0,0), (-1,-1), 12), ('LEFTPADDING', (0,0), (-1,-1), 15), ('RIGHTPADDING', (0,0), (-1,-1), 15)]))
    story.append(logo_table)
    story.append(Spacer(1, 15))
    story.append(Paragraph("Tinker Tailor LLM Spy: Reconstructing 'Deleted' Chats & Hijacking Sessions from Chromium LevelDB Caches with Verity", title_style))
    story.append(Table([[""]], colWidths=[504], rowHeights=[2], style=TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#cc0000")), ('TOPPADDING', (0,0), (-1,-1), 0), ('BOTTOMPADDING', (0,0), (-1,-1), 0)])))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Proposal Info", section_style))
    
    meta_data = [
        [Paragraph("<b>Title:</b>", body_style), Paragraph("Tinker Tailor LLM Spy: Reconstructing 'Deleted' Chats & Hijacking Sessions from Chromium LevelDB Caches with Verity", body_style)],
        [Paragraph("<b>Status:</b>", body_style), Paragraph("Submitted / For Board Review", body_style)],
        [Paragraph("<b>Session Type:</b>", body_style), Paragraph("Briefings", body_style)],
        [Paragraph("<b>Speaker:</b>", body_style), Paragraph("Dr. Sapna Vikram Mewundi (Lead Forensics Researcher, Verity Project)", body_style)],
        [Paragraph("<b>Tracks:</b>", body_style), Paragraph("AI, ML, & Data Science; Threat Hunting & Incident Response", body_style)],
        [Paragraph("<b>Format:</b>", body_style), Paragraph("40-Minute Briefings", body_style)],
    ]
    meta_table = Table(meta_data, colWidths=[90, 414])
    meta_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 4), ('TOPPADDING', (0,0), (-1,-1), 4), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0), ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#eeeeee"))]))
    story.append(meta_table)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Abstract", section_style))
    story.append(Paragraph("It's coming, and you aren't ready—your first forensic investigation involving Large Language Model (LLM) data leakage. GenAI portals (like ChatGPT, Claude, and Gemini) have become standard corporate utilities. To speed up workflows, developers and executives routinely copy and paste sensitive proprietary source code, internal configurations, and credentials into these clients. But when users click 'Delete Chat' or clear histories, does that data actually get erased?", body_style))
    story.append(Paragraph("The truth is far more persistent. Chromium-based browsers (Google Chrome, Microsoft Edge) and native Electron desktop wrappers cache conversation telemetry inside client-side IndexedDB databases, which are backed by Google's LevelDB storage engine. Since LevelDB uses an append-only log-structured merge-tree (LSM tree), deleted records remain intact in write-ahead logs (<code>.log</code>) and uncompacted Sorted String Tables (<code>.sst</code>/<code>.ldb</code>) on local disks for days or weeks.", body_style))
    story.append(Paragraph("In this talk, we reveal the low-level serialization structures of client-side LLM databases and how to carve this 'deleted' telemetry. We reverse engineer the V8 deserialization format (<code>ValueSerializer</code>), specifically dissecting V8 string tags (<code>OneByteString</code> vs <code>TwoByteString</code> UTF-16LE anomalies) and nested object boundary parsing. We introduce <b>Verity</b>, an open-source, zero-dependency python framework that dynamically sweeps all user profiles, bypasses active Windows file locks, and reconstructs deleted histories. Finally, we establish a cryptographically secured chain of custody using in-browser HMAC-SHA256 verification. Attendees will leave with a ready-to-use incident response playbook and the open-source Verity tool to audit and protect their organizations.", body_style))
    
    story.append(Paragraph("Presentation Outline – NOTE THE DETAILED OUTLINE", section_style))
    story.append(Paragraph("<b>1. INTRODUCTION: THE EPHEMERAL AI FALLACY (5 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>The Mirage of Deletion:</b> Contrast cloud-side deletion logic with local disk remnants. Explain the LevelDB LSM-tree append-only structure.", bullet_style))
    story.append(Paragraph("&bull; <b>Threat Modeling:</b> Assess how malicious actors, insider threats, and infostealer malware harvest unencrypted local browser caches to steal corporate intellectual property.", bullet_style))
    story.append(Paragraph("&bull; <b>Target Mapping:</b> Location of IndexedDB LevelDB instances for ChatGPT, Claude, and Gemini on Windows AppData and macOS Library.", bullet_style))
    
    story.append(Paragraph("<b>2. REVERSING CHROMIUM LEVELDB & STORAGE SCHEMA STRUCTURES (5 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>ChatGPT (Web & Desktop):</b> Layout of keys and IndexedDB schemas storing conversation content, model attributes, and temporary states.", bullet_style))
    story.append(Paragraph("&bull; <b>Claude & Gemini:</b> Structural differences in LevelDB records, and mapping active workspace telemetry.", bullet_style))
    story.append(Paragraph("&bull; <b>Session Credentials:</b> Identifying unencrypted session tokens (e.g. JWTs and session IDs) stored in IndexedDB that allow session hijacking.", bullet_style))
    
    story.append(Paragraph("<b>3. ZERO-DEPENDENCY CARVING OF LEVELDB & COMPRESSED SSTABLES (10 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>Production Constrains:</b> Why native C++ leveldb drivers cannot be compiled/installed on endpoint machines during triage.", bullet_style))
    story.append(Paragraph("&bull; <b>Pure-Python Parsers:</b> Building a pure-Python Protocol Buffer varint32 reader and block boundary parser.", bullet_style))
    story.append(Paragraph("&bull; <b>Snappy Decompression:</b> Rebuilding a Snappy decompressor (literals and copy tags) in Python to extract compressed data blocks directly from SSTables.", bullet_style))
    story.append(Paragraph("&bull; <b>Active Lock Bypass:</b> Opening write-ahead logs (<code>.log</code>) in read-only binary mode to clone records without tripping OS locks.", bullet_style))
    
    story.append(Paragraph("<b>4. REBUILDING CONVERSATION TREES & DECODING V8 SERIALIZATION (10 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>V8 Deserialization format:</b> Decoding JavaScript serialized values.", bullet_style))
    story.append(Paragraph("&bull; <b>String Anomalies:</b> Solving the <code>OneByteString</code> (ASCII) vs <code>TwoByteString</code> (UTF-16LE) tag length calculation byte bug.", bullet_style))
    story.append(Paragraph("&bull; <b>Nesting & Boundaries:</b> Handling padding bytes and tracking nesting depth (object/array tags) to prevent premature parsing termination on <code>0x7b</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>Role Math:</b> Mapping user vs assistant roles via Smi-shifted index keys and index parity:", subsection_style))
    story.append(Paragraph("<code>role = 'user' if (index / 2) mod 2 = 1 else 'assistant'</code>", code_style))
    story.append(Paragraph("&bull; <b>Timeline Assembly:</b> Ordering chats using file modification times (mtime) and database byte offsets.", bullet_style))
    
    story.append(Paragraph("<b>5. INCIDENT SCENARIO: THE INSIDER INTELLECTUAL PROPERTY EXFILTRATION (5 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>Scenario setup:</b> Developer pastes proprietary source code and API keys, deletes the chat, and clears browser history.", bullet_style))
    story.append(Paragraph("&bull; <b>Forensic Acquisition:</b> Bypassing locks, cloning raw log files, and executing the Verity carver.", bullet_style))
    story.append(Paragraph("&bull; <b>Reconstruction:</b> Demonstrating how the entire code block and thread context are recovered with zero-data loss.", bullet_style))
    
    story.append(Paragraph("<b>6. INCIDENT SCENARIO: SESSION HIJACKING & FORENSIC INTEGRITY (5 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>The Session Takeover:</b> Extracting unencrypted session tokens from IndexedDB caches and hijacking the user's active session without entering credentials.", bullet_style))
    story.append(Paragraph("&bull; <b>Chain of Custody:</b> Creating a tamper-proof forensic envelope by signing canonical JSON payloads using HMAC-SHA256.", bullet_style))
    story.append(Paragraph("&bull; <b>Integrity Verification:</b> Validating signature seals in the dashboard using the Web Cryptography API.", bullet_style))
    
    story.append(Paragraph("<b>7. CONCLUSION & MITIGATIONS (3 mins)</b>", subsection_style))
    story.append(Paragraph("&bull; <b>Key takeaways:</b> V8 deserialization, Snappy decompression, and browser multi-profile path audits.", bullet_style))
    story.append(Paragraph("&bull; <b>Mitigations:</b> Implementing active cache eviction policies on logout, disk encryption (BitLocker), and EDR monitoring rules.", bullet_style))
    story.append(Paragraph("&bull; <b>Open Source Release:</b> Announcing the public GitHub release of the Verity framework.", bullet_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("Questions & Answers", section_style))
    
    story.append(Paragraph("<b>Is This Content New (Not Previously Presented/Published)?</b>", subsection_style))
    story.append(Paragraph("Yes. While general SQLite/LevelDB structures are documented, the reverse engineering of client-side IndexedDB databases for LLM interfaces and the creation of a zero-dependency, pure-Python Snappy block carver for deleted data reconstruction is brand-new research.", body_style))
    
    story.append(Paragraph("<b>Have You/Do You Plan to Submit This Talk to Another Conference?</b>", subsection_style))
    story.append(Paragraph("No.", body_style))
    
    story.append(Paragraph("<b>What new research, concept, technique, or approach is included in your submission?</b>", subsection_style))
    story.append(Paragraph("1. <b>Low-Level V8 Forensics of GenAI Clients:</b> We document the client-side IndexedDB database schemas of ChatGPT, Claude, and Gemini, proving that cleared conversations remain on disk.", body_style))
    story.append(Paragraph("2. <b>Zero-Dependency Snappy/SSTable Carver:</b> We introduce a technique to parse LevelDB SSTables and decompress Snappy blocks entirely in memory using pure Python, eliminating compiled C++ dependencies.", body_style))
    story.append(Paragraph("3. <b>Dynamic Profile Sweeping & Lock Bypass:</b> Automatically identifies all active Chromium browser profiles and reads write-ahead logs in read-only mode to bypass OS file locks.", body_style))
    
    story.append(Paragraph("<b>Provide 3 Audience Takeaways.</b>", subsection_style))
    story.append(Paragraph("1. <b>AI Local Footprint Map:</b> Deep technical knowledge of where and how local AI client data is stored, and the specific database keys containing session credentials and chat logs.", body_style))
    story.append(Paragraph("2. <b>LevelDB V8 Carving Mechanics:</b> The ability to write compile-free scripts to parse Protocol Buffer varints, Snappy blocks, and V8 serialized strings from raw disk dumps.", body_style))
    story.append(Paragraph("3. <b>Open-Source Tooling:</b> Access to the open-source Verity tool to immediately audit endpoints and secure corporate AI workloads.", body_style))
    
    story.append(Paragraph("<b>If applicable, what problem does your research solve?</b>", subsection_style))
    story.append(Paragraph("Traditional EDR agents and forensic suites do not parse GenAI IndexedDB records. If sensitive intellectual property or active AI account credentials are leaked, incident responders lack playbooks to audit the breach. Verity solves this by providing a single-file, zero-dependency Python script that bypasses locks, extracts browser profiles, and compiles verified reports under a cryptographic chain of custody.", body_style))
    
    story.append(Paragraph("<b>Will You Be Releasing a New Tool? If Yes, Describe the Tool.</b>", subsection_style))
    story.append(Paragraph("Yes. We will be releasing <b>Verity</b>, an open-source, zero-dependency Python framework designed for incident responders. It automates the extraction and parsing of LLM databases (browser IndexedDB and desktop wrappers), handles live SQLite lock bypasses, performs process-to-socket audits, and outputs a clean forensic evidence report to JSON or a centralized web-based lab interface.", body_style))
    
    story.append(Paragraph("<b>Is This a New Vulnerability? If Yes, Describe the Vulnerability.</b>", subsection_style))
    story.append(Paragraph("Yes. While not a direct remote code execution exploit in Chromium, our research exposes two distinct local vulnerabilities that directly impact modern enterprise AI usage:", body_style))
    story.append(Paragraph("1. <b>Unprotected Local Session Credential Leakage in IndexedDB (Chrome/Edge):</b> Chromium-based browsers fail to apply OS-level cryptographic protections (like DPAPI or Keychain) to cookies and authorization tokens stored within IndexedDB LevelDB instances. Standard cookies and passwords are encrypted, but IndexedDB stores active LLM tokens in plaintext, enabling low-privilege processes or infostealers to hijack AI sessions.", bullet_style))
    story.append(Paragraph("2. <b>Forensic Leakage of Deleted Telemetry (LevelDB LSM-Tree Persistence):</b> LevelDB's append-only design means that clicking 'Delete Chat' in an LLM web UI does not purge the data from disk. It merely deletes the database index pointer. The actual chat messages, source code blocks, and sensitive credentials remain on-disk in write-ahead logs (<code>.log</code>) and uncompacted Sorted String Tables (<code>.sst</code>/<code>.ldb</code>) indefinitely. We show how these can be forensically reconstructed using raw byte carving.", bullet_style))
    
    story.append(Paragraph("<b>Will Your Presentation Include a Demo? If Yes, Describe the Demo.</b>", subsection_style))
    story.append(Paragraph("Yes. The presentation will include a pre-recorded demo video showing:", body_style))
    story.append(Paragraph("1. A developer pasting proprietary corporate source code into ChatGPT under Chrome <code>Profile 3</code>, and then deleting the conversation using the web interface.", bullet_style))
    story.append(Paragraph("2. The execution of the Verity script on the target workstation.", bullet_style))
    story.append(Paragraph("3. The dynamic discovery of <code>Profile 3</code> databases and the instant forensic reassembly of the 'deleted' code blocks by carving the LevelDB data files.", bullet_style))
    story.append(Paragraph("4. The extraction of active session tokens to hijack the developer's session, followed by the verification of the evidence integrity using the Web Cryptography API.", bullet_style))
    
    story.append(Paragraph("<b>Provide the Names of the Speakers Presenting and Their Previous Speaking Experience.</b>", subsection_style))
    story.append(Paragraph("<b>Speaker:</b> Dr. Sapna Vikram Mewundi (Lead Forensics Researcher, Verity Project)<br/><b>Speaking Experience:</b> Regular presenter at local security meetups, DEF CON Groups, and contributor to open-source forensic tools. First-time speaker at Black Hat Briefings.", body_style))
    
    story.append(Paragraph("<b>Does Your Company/ Employer Provide a Solution to the Issue Addressed? If Yes, Please Provide Details.</b>", subsection_style))
    story.append(Paragraph("No.", body_style))
    
    story.append(Paragraph("<b>Do You Want to Provide a White Paper for Review by the Board?</b>", subsection_style))
    story.append(Paragraph("Yes. We will provide our comprehensive whitepaper detailing the exact binary layouts, Snappy decompression code, and timeline reassembly algorithms.", body_style))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF build completed successfully.")

if __name__ == '__main__':
    build_pdf()
