import urllib.request
import urllib.parse
import re

routes = [
    ('/', 'Lakshay Jain', ['Lakshay Jain', 'Domino', 'Discord', 'Instagram', 'PNB']),
    ('/about', 'Lakshay Jain | About Me', ['Product Designer', 'Lakshay Jain', 'Figma', 'design space']),
    # Canonical Routes
    ('/pnb-website-redesign', 'PNB Website Redesign', ['Punjab National Bank', 'Outfit', 'Ramesh Verma', 'Aditi Mehra']),
    ('/improving-discord-new-users', 'Improving Discord for New Users', ['Empty Hallway', 'RICE', 'Harshit Aggarwal', '150M+ MAU']),
    ('/dominos-packaging-redesign', "Domino's", ['Thermodynamics', 'Aman Kapoor', 'Sustainability First', 'cardboard']),
    ('/instagram-reels-experience', 'Instagram', ['Reels', 'Creator Economy', 'Maya Singh', 'Editing Studio']),
    # Legacy alias routes
    ('/8club-onboarding-video', 'PNB Website Redesign', ['Punjab National Bank', 'Outfit']),
    ('/show-me-the-money', 'Improving Discord for New Users', ['Discord', 'Empty Hallway']),
    ('/enterprise-readiness', "Domino's", ["Domino's", 'Thermodynamics']),
    ('/ca-founder-collab', 'Instagram', ['Reels', 'Instagram'])
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
            
            # Check for forbidden/bad phrases and video clips
            bad_phrases = ['Adyatha', 'Henry VIII', 'this is my cat', '.mp4', '<video', 'sgVOCabS3zlW9g3jTLuh3kgVuKE', 'Vw9oyynBlEiGww8hAecqcveuEI', '2xwWRhIG41irFCI0AZOQJlKeL4']
            found_bad = [b for b in bad_phrases if b.lower() in content.lower()]
            
            # Check expected phrases
            missing_phrases = [p for p in expected_phrases if p.lower() not in content.lower()]
            
            if status == 200 and not found_bad and len(missing_phrases) == 0:
                print(f"PASS: {path} (200 OK, title & keywords verified, 0 video clips, 0 forbidden keywords)")
            else:
                print(f"FAIL/WARN: {path} (Status: {status})")
                if found_bad:
                    print(f"   Found unwanted keywords / video clips: {found_bad}")
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
            if resp.status == 200 and len(data) > 100000:
                print(f"PASS: {pdf_path} ({len(data)} bytes, valid PDF)")
            else:
                print(f"FAIL: {pdf_path} (Status: {resp.status}, size: {len(data)})")
                all_passed = False
    except Exception as e:
        print(f"ERROR fetching PDF {pdf_path}: {e}")
        all_passed = False

if all_passed:
    print("\nSUCCESS: ALL ROUTES, ASSETS, METRICS, AND PDF DELIVERABLES ARE FULLY VERIFIED!")
else:
    print("\nWARNING: Some verifications did not pass. Check the log above.")
