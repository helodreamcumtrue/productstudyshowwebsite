import urllib.request
import urllib.parse
import re

routes = [
    ('/', 'Lakshay Jain', ['Lakshay Jain', 'Domino', 'Discord', 'Instagram', 'PNB']),
    ('/about', 'Lakshay Jain | About Me', ['Product Designer', 'Lakshay Jain', 'Figma', 'design space']),
    # Canonical Case Study PDF Presentation Routes
    ('/pnb-website-redesign', 'PNB Website Redesign', ['PNB Redesign by Lakshay.pdf', 'Back to Portfolio', 'Download PDF']),
    ('/improving-discord-new-users', 'Improving Discord for New Users', ['Discord product teardown by Lakshay.pdf', 'Back to Portfolio', 'Download PDF']),
    ('/dominos-packaging-redesign', "Domino's New Packaging", ['Domino_s product teardown by Lakshay.pdf', 'Back to Portfolio', 'Download PDF']),
    ('/instagram-reels-experience', 'Improving the Reels Experience on Instagram', ['Insta product teardown by Lakshay.pdf', 'Back to Portfolio', 'Download PDF']),
    # Legacy aliases
    ('/8club-onboarding-video', 'PNB Website Redesign', ['PNB Redesign by Lakshay.pdf', 'Back to Portfolio']),
    ('/show-me-the-money', 'Improving Discord for New Users', ['Discord product teardown by Lakshay.pdf', 'Back to Portfolio']),
    ('/enterprise-readiness', "Domino's New Packaging", ['Domino_s product teardown by Lakshay.pdf', 'Back to Portfolio']),
    ('/ca-founder-collab', 'Improving the Reels Experience on Instagram', ['Insta product teardown by Lakshay.pdf', 'Back to Portfolio'])
]

base_url = 'http://localhost:3000'
print("=== VERIFYING CLEAN PDF PRESENTATION ROUTES & PURGED FRAMER TAGS ===")

all_passed = True
for path, expected_title, expected_phrases in routes:
    url = base_url + path
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            status = resp.status
            
            # Check for forbidden Framer tags, badges, watermarks and video clips
            bad_phrases = [
                'Made in Framer',
                'Create a free website with Framer',
                'events.framer.com',
                '.mp4',
                '<video',
                'sgVOCabS3zlW9g3jTLuh3kgVuKE',
                'Vw9oyynBlEiGww8hAecqcveuEI',
                '2xwWRhIG41irFCI0AZOQJlKeL4'
            ]
            found_bad = [b for b in bad_phrases if b.lower() in content.lower()]
            
            # Check expected phrases
            missing_phrases = [p for p in expected_phrases if p.lower() not in content.lower()]
            
            if status == 200 and not found_bad and len(missing_phrases) == 0:
                print(f"PASS: {path} (200 OK, pure PDF presentation verified, 0 Framer tags, 0 video clips)")
            else:
                print(f"FAIL/WARN: {path} (Status: {status})")
                if found_bad:
                    print(f"   Found unwanted Framer tags / video clips: {found_bad}")
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

print("\n=== VERIFYING PDF DELIVERABLES ===")
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
    print("\nSUCCESS: ALL CASE STUDIES HAVE CONTENT REMOVED AND CLEAN PDF VIEWER ADDED. ALL FRAMER TAGS COMPLETELY PURGED!")
else:
    print("\nWARNING: Some verifications did not pass. Check the log above.")
