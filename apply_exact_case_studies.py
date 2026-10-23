import os
import glob
import re

print("Applying complete case study content from Lakshay's PDFs & projects...")

# ---------------------------------------------------------------------------
# 1. Update app.js with the exact Case Studies from Lakshay's PDFs
# ---------------------------------------------------------------------------
NEW_APP_JS = '''// ==========================================================================
// LAKSHAY JAIN PORTFOLIO - APPLICATION SCRIPT
// Theme switcher, Client-side navigation, Case study modal reader
// ==========================================================================

const PROJECTS_DATA = [
  {
    id: "8club-onboarding-video",
    title: "New Better PNB - UI/UX Case Study",
    tags: ["UI/UX Design", "Design System", "Accessibility"],
    thumbnail: "/assets/case_pnb_thumb.png",
    pdfUrl: "/PNB Redesign by Lakshay.pdf",
    shortDesc: "A complete usability redesign of Punjab National Bank’s digital experience, resolving navigation clutter and reducing transaction friction by 40%.",
    projectType: "UI/UX Case Study, Banking Redesign",
    targetAudience: "Retail Banking Customers & Senior Citizens",
    timeframe: "4 Weeks",
    client: "Punjab National Bank (Redesign)",
    problem: "PNB's banking website is difficult to navigate, with complex menus and a cluttered homepage that frustrate users trying to complete tasks like fund transfers, bill payments, and account management. The lack of personalization and outdated design further complicates the user experience, especially for mobile users. These issues lead to inefficiency, user frustration, and a negative impact on customer retention.",
    approach: "Discovery: Primary & secondary user interviews uncovering key friction points for elder demographics (Ramesh Verma, 56) and mobile-first students (Aditi Mehra, 20). Ideation: Formulated How-Might-We (HMW) frameworks, simplified 2-step UPI transfers, and designed a softer, accessible high-contrast palette (HEX #AF2A30, #FFF1D3, #C00000). Implementation: Built a complete design system with Outfit variable typography and interactive prototypes.",
    responsibilities: "User research, persona development, information architecture, wireframing, high-contrast design tokens, interactive prototyping, and usability benchmarking.",
    details: [
      "Key Result: Task completion time reduced by 40% in user testing.",
      "Typography & Colors: Outfit modern geometric typeface with accessible bank-heritage tones.",
      "Personas Addressed: Ramesh Verma (simplified non-glitchy transfers) & Aditi Mehra (2-3 tap quick UPI)."
    ],
    images: [
      "/assets/case_pnb_thumb.png"
    ]
  },
  {
    id: "show-me-the-money",
    title: "Improving Discord for New Users",
    tags: ["Product Strategy", "UX Research", "FTUX & Retention"],
    thumbnail: "/assets/case_discord_thumb.png",
    pdfUrl: "/Discord product teardown by Lakshay.pdf",
    shortDesc: "A strategic deep dive into Discord’s first-time user experience, tackling the 'Empty Hallway' problem with role-based guided tours to boost Day-1 retention by 20%.",
    projectType: "Product Teardown, Growth & Retention Strategy",
    targetAudience: "Novice Discord Users, Students & Casual Gamers",
    timeframe: "3 Weeks",
    client: "Product Teardown (Self-Directed)",
    problem: "Discord has 150M+ MAU and 4B min/day conversations, but experiences ~60% Day 1 drop-off among non-gamers. 'The Empty Hallway' effect causes 4 out of 5 new users to leave a server within 10 minutes without posting a single message due to choice paralysis, cognitive load from bot notifications, and generic welcome screens.",
    approach: "Evaluated user journeys and prioritized interventions using the RICE framework (Contextual Tooltips: RICE 900; Interactive Onboarding: RICE 600). Designed structured, role-based setup wizards ('I\\'m a Designer', 'I\\'m a Developer', 'Just Browsing') that highlight key channels and suppress notification noise until onboarding is complete. Created a Guided Discovery flow for interest curation in 3 clicks.",
    responsibilities: "Product teardown research, friction mapping, RICE prioritization matrix, user journey maps, high-fidelity UI solutions, and projected retention modeling.",
    details: [
      "Projected Impact: +20% Day-1 Retention and +35% increase in first-week engagement.",
      "Solution 1: Interactive Guided Tours replacing empty states with role-based setup (+15% retention, 2.5x speed).",
      "Solution 2: Guided Discovery 'Curating the Chaos' helping users find top communities in under 3 clicks."
    ],
    images: [
      "/assets/case_discord_thumb.png",
      "/assets/case_discord_preview.png"
    ]
  },
  {
    id: "enterprise-readiness",
    title: "Domino's New Packaging Redesign",
    tags: ["Product Teardown", "Sustainability", "Systems Design"],
    thumbnail: "/assets/case_dominos_thumb.png",
    pdfUrl: "/Domino_s product teardown by Lakshay.pdf",
    shortDesc: "A strategic redesign deconstructing thermal thermodynamics, eco-accountability, and supply-chain stackability across 1,500+ franchise locations.",
    projectType: "Product & Packaging Strategy, Operations UX",
    targetAudience: "Eco-Conscious Cravers & Last-Mile Delivery Fleets",
    timeframe: "3 Weeks",
    client: "Product Strategy Teardown",
    problem: "Why the old pizza box failed: 1) Thermodynamics - 40% heat loss within 15 minutes due to standard uninsulated corrugated cardboard; 2) Sustainability - 30% of legacy boxes rendered unrecyclable due to oil grease saturation; 3) Structural Integrity - weak sidewalls caused crushing beyond 3 stacked boxes during rush deliveries.",
    approach: "Strategic pivot across 4 core business pillars: 1) Sustainability First (-30% plastic, -12.5% carbon footprint); 2) Heat Retention (+15% longer thermal holding with corrugated air pockets); 3) Stackability (doubled courier bag density); 4) Brand Modernization (bi-color minimalist aesthetic inspired by tech-first unboxing). Designed phased rollout across 1,500+ franchise locations.",
    responsibilities: "Strategic rationale decomposition, user persona modeling (Aman Kapoor, Junior Developer), operational ROI analysis, sustainability metrics, and unboxing UX.",
    details: [
      "Operational Results: 22% waste reduction in cardboard usage and 15% material cost savings.",
      "Customer Sentiment: +8 Pts NPS post-launch customer satisfaction rating.",
      "Rollout Plan: Phased transition from Tier-1 pilots (98% positive) to nationwide supply chain deployment."
    ],
    images: [
      "/assets/case_dominos_thumb.png",
      "/assets/case_dominos_preview.png"
    ]
  },
  {
    id: "ca-founder-collab",
    title: "Improving the Reels Experience on Instagram",
    tags: ["Growth Strategy", "Mobile UX", "Creator Economy"],
    thumbnail: "/assets/case_insta_thumb.png",
    pdfUrl: "/Insta product teardown by Lakshay.pdf",
    shortDesc: "Analyzing creator fatigue and algorithmic discovery on Instagram Reels, proposing collaborative co-creation flows and in-camera editing suites.",
    projectType: "Product Teardown, Feature Design & Creator Strategy",
    targetAudience: "Content Creators, Viewers & Emerging Influencers",
    timeframe: "3 Weeks",
    client: "Product Teardown (Instagram)",
    problem: "Instagram Reels drives 200B+ daily plays, yet creators face high friction: 1) Content discovery fatigue from repetitive algorithm suggestions; 2) Intense pressure to perform with unpredictable reach; 3) Clunky built-in editing tools compared to dedicated tools, forcing creators to edit off-platform.",
    approach: "Mapped the full Reels user journey from consumption to creation. Used RICE scoring to prioritize solutions: 1) Enhanced In-Camera Editing Suite with timeline trimming, multi-track audio mixing, and AI effect overlays; 2) Collaborative Reels enabling multiple co-creators to stitch clips into a single shared post with dual-attribution.",
    responsibilities: "Product analytics teardown, user journey mapping, persona synthesis (Maya Singh, 22), RICE feature scoring, and high-fidelity mobile prototype design.",
    details: [
      "Strategic Solutions: Integrated In-Camera Studio & Collaborative Co-Creation posting.",
      "Success Metrics: Tracked creation attempts, session duration, daily active users, and share frequency.",
      "Outcome: Solved creator friction while elevating niche creator discovery beyond viral trends."
    ],
    images: [
      "/assets/case_insta_thumb.png",
      "/assets/case_insta_preview.png"
    ]
  },
  {
    id: "custom-access-controls",
    title: "ArtiApply - AI Cold Outreach SaaS",
    tags: ["SaaS Product", "AI Workflow", "Full-Stack Design"],
    thumbnail: "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&q=80&w=921",
    shortDesc: "An automated outreach engine featuring BullMQ queue rate-limiting, Gmail API integration, and real-time deliverability analytics.",
    projectType: "SaaS Product Design, AI Prompt Pipelines, Frontend Architecture",
    targetAudience: "Founders, Freelancers & Sales Development Reps",
    timeframe: "4 Weeks",
    client: "ArtiApply SaaS (Founder)",
    problem: "Manual cold outreach is slow, generic email templates generate dismal open rates, and conventional tools lack transparent deliverability monitoring, resulting in burned domain reputations and lost business opportunities.",
    approach: "Designed and engineered an automated campaign cockpit featuring multi-step AI personalization pipelines, Gmail API rate-limiting via BullMQ worker queues, and live Supabase Realtime deliverability dashboards.",
    responsibilities: "Product vision, system architecture, UX flow design, analytics dashboards, and frontend UI design.",
    details: [
      "Key Architecture: BullMQ queue management, Gmail API integration, Supabase Realtime, and Tailwind design system.",
      "Key Result: Achieved 3x higher response rates compared to generic template campaigns."
    ],
    images: [
      "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "you-are-okay",
    title: "Laundify - Campus Service App",
    tags: ["Product Design", "Mobile App", "IoT Companion"],
    thumbnail: "https://images.unsplash.com/photo-1545173153-5dd736fb688a?auto=format&fit=crop&q=80&w=921",
    shortDesc: "An on-demand laundry reservation system for student residences featuring live machine telemetry, push notifications, and frictionless digital payments.",
    projectType: "Product Design, Mobile UI/UX, IoT Companion",
    targetAudience: "University Students & Hostel Residents",
    timeframe: "3 Weeks",
    client: "Campus Product Initiative",
    problem: "Hostel students experience extreme scheduling friction with zero visibility into washer availability, resulting in long queues, wasted study time, and lost garments.",
    approach: "Designed an IoT-synced mobile companion that provides live machine status countdowns, automated push alerts when cycles complete, and unified in-app QR payments.",
    responsibilities: "Product conceptualization, mobile UI workflows, service blueprinting, prototype animation, and user testing with 100+ campus students.",
    details: [
      "Objective: Eliminate physical queues and provide transparent machine availability.",
      "Key Features: Real-time telemetry, automated slot reservations, and campus wallet integration."
    ],
    images: [
      "https://images.unsplash.com/photo-1545173153-5dd736fb688a?auto=format&fit=crop&q=80&w=1200"
    ]
  }
];

document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const header = document.getElementById("site-header");
  const homeView = document.getElementById("home-view");
  const aboutView = document.getElementById("about-view");
  const navHome = document.getElementById("nav-home");
  const navAbout = document.getElementById("nav-about");
  const projectsGrid = document.getElementById("projects-grid");
  const modalOverlay = document.getElementById("modal-overlay");
  const modalCloseBtn = document.getElementById("modal-close-btn");
  const modalHeroImg = document.getElementById("modal-hero-img");
  const modalTags = document.getElementById("modal-tags");
  const modalTitle = document.getElementById("modal-title");
  const metaType = document.getElementById("meta-type");
  const metaAudience = document.getElementById("meta-audience");
  const metaTimeframe = document.getElementById("meta-timeframe");
  const modalProblem = document.getElementById("modal-problem");
  const modalApproach = document.getElementById("modal-approach");
  const modalResponsibilities = document.getElementById("modal-responsibilities");
  const modalGallery = document.getElementById("modal-gallery");
  const paletteDots = document.querySelectorAll(".palette-dot");

  // 1. Render Projects Grid
  function renderProjects() {
    if (!projectsGrid) return;
    projectsGrid.innerHTML = PROJECTS_DATA.map((proj, idx) => `
      <article class="project-card" data-id="${proj.id}" id="card-${proj.id}" tabindex="0" role="button" aria-label="Open case study for ${proj.title}">
        <div class="card-media">
          <img src="${proj.thumbnail}" alt="${proj.title}" loading="${idx < 2 ? 'eager' : 'lazy'}" width="600" height="400">
        </div>
        <div class="card-body">
          <div class="tag-list">
            ${proj.tags.map(tag => `<span class="tag-badge">${tag}</span>`).join('')}
          </div>
          <h3 class="card-title">${proj.title}</h3>
          <p class="card-desc">${proj.shortDesc}</p>
          <div class="card-cta">
            <span>View Case Study</span>
            <svg width="17" height="17" viewBox="0 0 17 17" fill="none">
              <path d="M3.68 8.1H13.01" stroke="currentColor" stroke-width="1.33" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M8.34 3.43L13.01 8.1L8.34 12.77" stroke="currentColor" stroke-width="1.33" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
        </div>
      </article>
    `).join('');

    // Attach card click handlers
    document.querySelectorAll(".project-card").forEach(card => {
      card.addEventListener("click", () => {
        const id = card.getAttribute("data-id");
        openCaseStudy(id);
      });
      card.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          const id = card.getAttribute("data-id");
          openCaseStudy(id);
        }
      });
    });
  }

  // 2. Open Case Study Modal
  function openCaseStudy(id) {
    const proj = PROJECTS_DATA.find(p => p.id === id);
    if (!proj) return;

    if (modalHeroImg) {
      modalHeroImg.src = proj.thumbnail;
      modalHeroImg.alt = proj.title;
    }
    if (modalTags) {
      modalTags.innerHTML = proj.tags.map(t => `<span class="tag-badge">${t}</span>`).join('');
    }
    if (modalTitle) modalTitle.textContent = proj.title;

    if (metaType) metaType.textContent = proj.projectType || "UI/UX Case Study";
    if (metaAudience) metaAudience.textContent = proj.targetAudience || "General Public";
    if (metaTimeframe) metaTimeframe.textContent = proj.timeframe || "3 Weeks";

    if (modalProblem) modalProblem.textContent = proj.problem;
    if (modalApproach) modalApproach.textContent = proj.approach;
    if (modalResponsibilities) modalResponsibilities.textContent = proj.responsibilities;

    // Render gallery images or PDF action
    if (modalGallery) {
      let galleryHtml = "";
      if (proj.pdfUrl) {
        galleryHtml += `
          <div style="grid-column: 1 / -1; margin-bottom: 1rem; display: flex; gap: 12px; align-items: center;">
            <a href="${proj.pdfUrl}" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 8px; background: #2563eb; color: #fff; padding: 12px 24px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 14px; box-shadow: 0 4px 14px rgba(37,99,235,0.4);">
              <span>Download / Open Full PDF Presentation</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            </a>
          </div>
        `;
      }
      if (proj.images && proj.images.length > 1) {
        galleryHtml += proj.images.slice(1).map(imgUrl => `
          <img src="${imgUrl}" alt="${proj.title} visual" loading="lazy">
        `).join('');
      }
      modalGallery.innerHTML = galleryHtml;
      modalGallery.style.display = "grid";
    }

    if (modalOverlay) {
      modalOverlay.classList.add("active");
      document.body.style.overflow = "hidden";
    }
  }

  function closeModal() {
    if (modalOverlay) modalOverlay.classList.remove("active");
    document.body.style.overflow = "";
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener("click", closeModal);
  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) closeModal();
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modalOverlay && modalOverlay.classList.contains("active")) {
      closeModal();
    }
  });

  // 3. Navigation View Switching (Home vs About)
  function switchView(viewName) {
    if (viewName === "about") {
      if (homeView) homeView.classList.add("hidden");
      if (aboutView) aboutView.classList.add("active");
      if (navHome) navHome.parentElement.classList.remove("active");
      if (navAbout) navAbout.parentElement.classList.add("active");
      if (header) header.classList.add("scrolled-light");
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      if (aboutView) aboutView.classList.remove("active");
      if (homeView) homeView.classList.remove("hidden");
      if (navAbout) navAbout.parentElement.classList.remove("active");
      if (navHome) navHome.parentElement.classList.add("active");
      handleScroll();
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  }

  if (navHome) {
    navHome.addEventListener("click", (e) => {
      e.preventDefault();
      switchView("home");
    });
  }

  if (navAbout) {
    navAbout.addEventListener("click", (e) => {
      e.preventDefault();
      switchView("about");
    });
  }

  // 4. Color Palette Switcher
  function setTheme(theme) {
    if (!theme) return;
    document.body.setAttribute("data-theme", theme);
    try { localStorage.setItem("lakshay_theme", theme); } catch(e){}

    paletteDots.forEach(dot => {
      if (dot.getAttribute("data-theme") === theme) {
        dot.classList.add("active");
      } else {
        dot.classList.remove("active");
      }
    });
  }

  paletteDots.forEach(dot => {
    dot.addEventListener("click", () => {
      const theme = dot.getAttribute("data-theme");
      setTheme(theme);
    });
  });

  // Load saved theme or default to 'indigo'
  let savedTheme = "indigo";
  try { savedTheme = localStorage.getItem("lakshay_theme") || "indigo"; } catch(e){}
  setTheme(savedTheme);

  // 5. Scroll Header Visual State
  function handleScroll() {
    if (!header) return;
    if (aboutView && aboutView.classList.contains("active")) {
      header.classList.add("scrolled-light");
      return;
    }
    const heroHeight = document.querySelector(".hero-section")?.offsetHeight || 500;
    if (window.scrollY > heroHeight - 100) {
      header.classList.add("scrolled-light");
    } else {
      header.classList.remove("scrolled-light");
    }
  }

  window.addEventListener("scroll", handleScroll, { passive: true });

  // Initial render
  renderProjects();
  handleScroll();
});
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(NEW_APP_JS)
print("Updated app.js with PDF case study metadata")

if os.path.exists('_archive/custom_recreation/app.js'):
    with open('_archive/custom_recreation/app.js', 'w', encoding='utf-8') as f:
        f.write(NEW_APP_JS)
    print("Updated _archive/custom_recreation/app.js")

# ---------------------------------------------------------------------------
# 2. Update index.html Cards with Exact Teardown Titles & Descriptions
# ---------------------------------------------------------------------------
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Card 2: Laundify -> Discord Teardown
html = html.replace('Laundify - Campus Service App', 'Improving Discord for New Users')
html = html.replace('An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.', 'A strategic deep dive into Discord’s first-time user experience, tackling the \'Empty Hallway\' problem with role-based guided tours to boost Day-1 retention by 20%.')
html = html.replace('>Product Design</p>', '>Product Strategy</p>')
html = html.replace('>Mobile UX</p>', '>UX Research</p>')

# Replace Card 3: Sanchay -> Domino's Packaging Redesign
html = html.replace('Sanchay - Money Manager', 'Domino\'s New Packaging Redesign')
html = html.replace('A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.', 'A strategic redesign deconstructing thermal thermodynamics, eco-accountability, and supply-chain stackability across 1,500+ franchise locations.')
html = html.replace('>Fintech Design</p>', '>Sustainability</p>')
html = html.replace('>Data Visualization</p>', '>Product Strategy</p>')

# Replace Card 4: ArtiApply -> Instagram Reels Experience
html = html.replace('ArtiApply - AI Cold Outreach SaaS', 'Improving the Reels Experience on Instagram')
html = html.replace('An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.', 'Analyzing creator fatigue and algorithmic discovery on Instagram Reels, proposing collaborative co-creation flows and in-camera editing suites.')
html = html.replace('>SaaS Product</p>', '>Growth Strategy</p>')
html = html.replace('>AI Workflow</p>', '>Mobile UX</p>')

# Replace Card 5: Clam Nest -> ArtiApply
html = html.replace('Clam Nest - Mental Wellness Platform', 'ArtiApply - AI Cold Outreach Engine')
html = html.replace('An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.', 'An automated outreach engine featuring BullMQ queue rate-limiting, Gmail API integration, and real-time deliverability analytics.')
html = html.replace('>Branding</p>', '>SaaS Product</p>')
html = html.replace('>UI/UX Design</p>', '>AI Workflow</p>')

# Replace Card 6: Campus Chronicles -> Laundify
html = html.replace('Campus Chronicles &amp; URJA Visuals', 'Laundify - Campus Service App')
html = html.replace('Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.', 'An on-demand laundry reservation system for student residences featuring live machine telemetry, push notifications, and frictionless digital payments.')
html = html.replace('>Visual Storytelling</p>', '>Product Design</p>')
html = html.replace('>Graphic Design</p>', '>IoT Companion</p>')

# Update Card Images to use local rendered screenshots where available
html = html.replace('https://framerusercontent.com/images/TTX6I3wwJ52GRBE0gUz9lXbJds.png', '/assets/case_pnb_thumb.png')
html = html.replace('https://framerusercontent.com/images/VmS3aMgSsdk4LF6effc4953Cclk.png', '/assets/case_discord_thumb.png')
html = html.replace('https://framerusercontent.com/images/8xt1f8uMJqhBTJdZ7iTfaUqp1M8.svg', '/assets/case_dominos_thumb.png')
html = html.replace('https://framerusercontent.com/images/6HbTgFxHBUu2DKXduj34oBzJ4S8.png', '/assets/case_insta_thumb.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html with Lakshay's exact teardown case studies")

# ---------------------------------------------------------------------------
# 3. Update framer_dist/WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs
# ---------------------------------------------------------------------------
wgpd_path = 'framer_dist/WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs'
if os.path.exists(wgpd_path):
    with open(wgpd_path, 'r', encoding='utf-8') as f:
        mjs = f.read()

    mjs = mjs.replace('Laundify - Campus Service App', 'Improving Discord for New Users')
    mjs = mjs.replace('An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.', 'A strategic deep dive into Discord’s first-time user experience, tackling the \'Empty Hallway\' problem with role-based guided tours to boost Day-1 retention by 20%.')

    mjs = mjs.replace('Sanchay - Money Manager', 'Domino\'s New Packaging Redesign')
    mjs = mjs.replace('A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.', 'A strategic redesign deconstructing thermal thermodynamics, eco-accountability, and supply-chain stackability across 1,500+ franchise locations.')

    mjs = mjs.replace('ArtiApply - AI Cold Outreach SaaS', 'Improving the Reels Experience on Instagram')
    mjs = mjs.replace('An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.', 'Analyzing creator fatigue and algorithmic discovery on Instagram Reels, proposing collaborative co-creation flows and in-camera editing suites.')

    mjs = mjs.replace('Clam Nest - Mental Wellness Platform', 'ArtiApply - AI Cold Outreach Engine')
    mjs = mjs.replace('An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.', 'An automated outreach engine featuring BullMQ queue rate-limiting, Gmail API integration, and real-time deliverability analytics.')

    mjs = mjs.replace('Campus Chronicles & URJA Visuals', 'Laundify - Campus Service App')
    mjs = mjs.replace('Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.', 'An on-demand laundry reservation system for student residences featuring live machine telemetry, push notifications, and frictionless digital payments.')

    mjs = mjs.replace('https://framerusercontent.com/images/TTX6I3wwJ52GRBE0gUz9lXbJds.png', '/assets/case_pnb_thumb.png')
    mjs = mjs.replace('https://framerusercontent.com/images/VmS3aMgSsdk4LF6effc4953Cclk.png', '/assets/case_discord_thumb.png')
    mjs = mjs.replace('https://framerusercontent.com/images/8xt1f8uMJqhBTJdZ7iTfaUqp1M8.svg', '/assets/case_dominos_thumb.png')
    mjs = mjs.replace('https://framerusercontent.com/images/6HbTgFxHBUu2DKXduj34oBzJ4S8.png', '/assets/case_insta_thumb.png')

    with open(wgpd_path, 'w', encoding='utf-8') as f:
        f.write(mjs)
    print("Updated", wgpd_path)

# ---------------------------------------------------------------------------
# 4. Update framer_home_page.mjs
# ---------------------------------------------------------------------------
if os.path.exists('framer_home_page.mjs'):
    with open('framer_home_page.mjs', 'r', encoding='utf-8') as f:
        fhome = f.read()

    fhome = fhome.replace('Laundify - Campus Service App', 'Improving Discord for New Users')
    fhome = fhome.replace('An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.', 'A strategic deep dive into Discord’s first-time user experience, tackling the \'Empty Hallway\' problem with role-based guided tours to boost Day-1 retention by 20%.')
    fhome = fhome.replace('Sanchay - Money Manager', 'Domino\'s New Packaging Redesign')
    fhome = fhome.replace('A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.', 'A strategic redesign deconstructing thermal thermodynamics, eco-accountability, and supply-chain stackability across 1,500+ franchise locations.')
    fhome = fhome.replace('ArtiApply - AI Cold Outreach SaaS', 'Improving the Reels Experience on Instagram')
    fhome = fhome.replace('An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.', 'Analyzing creator fatigue and algorithmic discovery on Instagram Reels, proposing collaborative co-creation flows and in-camera editing suites.')
    fhome = fhome.replace('Clam Nest - Mental Wellness Platform', 'ArtiApply - AI Cold Outreach Engine')
    fhome = fhome.replace('An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.', 'An automated outreach engine featuring BullMQ queue rate-limiting, Gmail API integration, and real-time deliverability analytics.')
    fhome = fhome.replace('Campus Chronicles & URJA Visuals', 'Laundify - Campus Service App')
    fhome = fhome.replace('Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.', 'An on-demand laundry reservation system for student residences featuring live machine telemetry, push notifications, and frictionless digital payments.')

    fhome = fhome.replace('https://framerusercontent.com/images/TTX6I3wwJ52GRBE0gUz9lXbJds.png', '/assets/case_pnb_thumb.png')
    fhome = fhome.replace('https://framerusercontent.com/images/VmS3aMgSsdk4LF6effc4953Cclk.png', '/assets/case_discord_thumb.png')
    fhome = fhome.replace('https://framerusercontent.com/images/8xt1f8uMJqhBTJdZ7iTfaUqp1M8.svg', '/assets/case_dominos_thumb.png')
    fhome = fhome.replace('https://framerusercontent.com/images/6HbTgFxHBUu2DKXduj34oBzJ4S8.png', '/assets/case_insta_thumb.png')

    with open('framer_home_page.mjs', 'w', encoding='utf-8') as f:
        f.write(fhome)
    print("Updated framer_home_page.mjs")

# ---------------------------------------------------------------------------
# 5. Enhance each transformed case study page with PDF download and Teardown content
# ---------------------------------------------------------------------------
PAGES_META = [
    {
        'file': 'framer_pages_transformed/8club-onboarding-video.html',
        'title': 'New Better PNB - UI/UX Case Study | Lakshay Jain',
        'heading': 'New Better PNB',
        'subheading': 'UI/UX Banking Redesign',
        'pdf': '/PNB Redesign by Lakshay.pdf'
    },
    {
        'file': 'framer_pages_transformed/show-me-the-money.html',
        'title': 'Improving Discord for New Users | Lakshay Jain',
        'heading': 'Improving Discord for New Users',
        'subheading': 'Product Teardown & Onboarding FTUX',
        'pdf': '/Discord product teardown by Lakshay.pdf'
    },
    {
        'file': 'framer_pages_transformed/enterprise-readiness.html',
        'title': 'Domino\'s New Packaging Redesign | Lakshay Jain',
        'heading': 'Domino\'s Packaging Redesign',
        'subheading': 'Strategic Product Teardown & Sustainability',
        'pdf': '/Domino_s product teardown by Lakshay.pdf'
    },
    {
        'file': 'framer_pages_transformed/ca-founder-collab.html',
        'title': 'Improving the Reels Experience on Instagram | Lakshay Jain',
        'heading': 'Instagram Reels Teardown',
        'subheading': 'Creator Experience & Algorithmic Discovery',
        'pdf': '/Insta product teardown by Lakshay.pdf'
    },
]

for p in PAGES_META:
    if os.path.exists(p['file']):
        with open(p['file'], 'r', encoding='utf-8') as f:
            c = f.read()
        
        # Inject floating "View Full PDF Presentation" badge
        badge_html = f'''
        <div style="position: fixed; bottom: 24px; left: 24px; z-index: 999999; display: flex; align-items: center; gap: 8px;">
          <a href="{p['pdf']}" target="_blank" rel="noopener noreferrer" style="display: flex; align-items: center; gap: 8px; background: rgba(18, 18, 18, 0.9); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.2); color: #fff; padding: 10px 18px; border-radius: 999px; font-family: sans-serif; font-size: 13px; font-weight: 600; text-decoration: none; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
            <span>Read Original PDF Presentation ↗</span>
          </a>
        </div>
        '''
        if '</body>' in c and 'Read Original PDF Presentation' not in c:
            c = c.replace('</body>', badge_html + '\n</body>')
        
        with open(p['file'], 'w', encoding='utf-8') as f:
            f.write(c)
        print("Injected PDF badge into", p['file'])

print("\\nSuccessfully updated all files with exact case study data from PDFs!")
