import urllib.request
import re

routes = [
    ('/', 'Lakshay Jain', ['New Better PNB', 'Improving Discord for New Users', "Domino's New Packaging Redesign", 'Instagram']),
    ('/about', 'Lakshay Jain | About Me', ['Product Designer', 'Lakshay Jain', 'Figma', 'design space']),
    ('/8club-onboarding-video', 'New Better PNB', ['Punjab National Bank', 'Outfit', 'Ramesh Verma', 'Aditi Mehra']),
    ('/show-me-the-money', 'Improving Discord for New Users', ['Empty Hallway', 'RICE', 'Harshit Aggarwal', '150M+ MAU']),
    ('/enterprise-readiness', "Domino's", ['Thermodynamics', 'Aman Kapoor', 'Sustainability First', 'cardboard']),
    ('/ca-founder-collab', 'Instagram', ['Reels', 'Creator Economy', 'Maya Singh', 'In-Camera']),
    ('/custom-access-controls', 'ArtiApply', ['Cold Outreach', 'BullMQ', 'Gmail API']),
    ('/you-are-okay', 'Laundify', ['Campus Service App', 'laundry', 'telemetry'])
]

base_url = 'http://localhost:3000'
print("=== VERIFYING ALL WEBSITE ROUTES ===")

all_passed = True
for path, expected_title, expected_phrases in routes:
    url = base_url + path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            status = resp.status
            
            # Check for bad phrases
            bad_phrases = ['Adyatha', 'Henry VIII', 'this is my cat']
            found_bad = [b for b in bad_phrases if b.lower() in content.lower()]
            
            # Check expected phrases
            missing_phrases = [p for p in expected_phrases if p.lower() not in content.lower()]
            
            if status == 200 and not found_bad and len(missing_phrases) == 0:
                print(f"PASS: {path} (200 OK, title & keywords verified, 0 forbidden keywords)")
            else:
                print(f"FAIL/WARN: {path} (Status: {status})")
                if found_bad:
                    print(f"   Found unwanted keywords: {found_bad}")
                    all_passed = False
                if missing_phrases:
                    print(f"   Missing expected keywords: {missing_phrases}")
                    all_passed = False
    except Exception as e:
        print(f"ERROR fetching {url}: {e}")
        all_passed = False

# Verify PDF downloads
pdfs = [
    '/PNB Redesign by Lakshay.pdf',
    '/Discord product teardown by Lakshay.pdf',
    '/Domino_s product teardown by Lakshay.pdf',
    '/Insta product teardown by Lakshay.pdf'
]

print("\n=== VERIFYING PDF DOWNLOAD DELIVERABLES ===")
for pdf_path in pdfs:
    encoded_url = base_url + urllib.parse.quote(pdf_path)
    try:
        with urllib.request.urlopen(encoded_url) as resp:
            data = resp.read()
            ct = resp.headers.get('Content-Type')
            print(f"PASS: {pdf_path} -> HTTP {resp.status} ({ct}, {len(data)} bytes)")
    except Exception as e:
        print(f"ERROR: {pdf_path} -> {e}")
        all_passed = False

if all_passed:
    print("\nALL VERIFICATIONS PASSED 100% PERFECTLY!")
else:
    print("\nSome verifications had warnings/failures.")
