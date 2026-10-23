import os
import glob
import re

print("Starting portfolio content update to Lakshay Jain...")

# ---------------------------------------------------------------------------
# 1. Update app.js
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
    thumbnail: "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&q=80&w=961",
    shortDesc: "A comprehensive redesign of the Punjab National Bank mobile application, solving navigation friction and boosting usability for senior demographics.",
    projectType: "UI/UX Design, Design System, Accessibility Testing",
    targetAudience: "Retail Banking Customers & Senior Citizens",
    timeframe: "4 Weeks",
    client: "Punjab National Bank (Redesign)",
    problem: "Traditional public sector banking applications suffer from high drop-off rates due to visual clutter, convoluted 6-step fund transfers, and tiny touch targets that severely impede older users. User feedback repeatedly highlighted anxiety during fund transfers and difficulty finding essential tax and account statement services.",
    approach: "Rebuilt the information architecture with progressive disclosure, a high-contrast design system compliant with WCAG 2.1 AA standards, simplified 2-step UPI and IMPS transfers, and tested high-fidelity interactive prototypes across multiple age demographics.",
    responsibilities: "Led end-to-end user research, competitive benchmarking, user journey mapping, design token architecture, interactive Figma prototypes, and usability testing with senior users.",
    details: [
      "Objective: Streamline fund transfers, bill payments, and statement downloads.",
      "Design System: Created a modern, accessible color palette preserving PNB heritage while drastically improving contrast.",
      "Key Result: Reduced task completion time by 40% and transaction error rates by 65% in user testing."
    ],
    images: [
      "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&q=80&w=1200",
      "https://images.unsplash.com/photo-1551288049-bbbda5366392?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "show-me-the-money",
    title: "Laundify - Campus Service App",
    tags: ["Product Design", "Mobile UX", "Service Design"],
    thumbnail: "https://images.unsplash.com/photo-1545173153-5dd736fb688a?auto=format&fit=crop&q=80&w=921",
    shortDesc: "An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.",
    projectType: "Product Design, Mobile UI/UX, IoT Companion",
    targetAudience: "University Students & Hostel Residents",
    timeframe: "3 Weeks",
    client: "Campus Product Initiative",
    problem: "Hostel residents face unpredictable queue times, broken washers with zero status reporting, and inconvenient offline token systems that waste valuable study and work hours. Overcrowding in laundry rooms was a persistent daily frustration.",
    approach: "Designed a clean, IoT-synchronized mobile application that gives students live countdown timers for active wash cycles, push notifications upon completion, and seamless in-app digital payments and slot reservations.",
    responsibilities: "Product conceptualization, user flow wireframing, mobile UI design, interactive micro-interactions, service blueprinting, and student survey analysis.",
    details: [
      "Objective: Eliminate physical queues and provide transparent machine availability.",
      "Key Features: Real-time telemetry, automated slot reservations, and campus wallet integration.",
      "Key Result: Over 85% of surveyed students expressed immediate preference for the digital reservation model."
    ],
    images: [
      "https://images.unsplash.com/photo-1545173153-5dd736fb688a?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "enterprise-readiness",
    title: "Sanchay - Personal Finance & Money Manager",
    tags: ["Fintech Design", "Data Visualization", "Mobile UI"],
    thumbnail: "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&q=80&w=921",
    shortDesc: "A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.",
    projectType: "Fintech Design, Data Visualization, Mobile UX",
    targetAudience: "Young Professionals & Freelancers",
    timeframe: "3 Weeks",
    client: "Sanchay Fintech",
    problem: "Existing expense trackers require overwhelming manual input and present intimidating spreadsheets that demotivate users after only a week of usage. Users struggle to see where their money actually goes without tedious categorization.",
    approach: "Designed a friction-free logging interface with smart auto-tagging, intuitive monthly burn rate dials, visual expense distributions, and milestone-based micro-savings challenges.",
    responsibilities: "UX strategy, financial telemetry design, chart component design system, dark-mode styling, and prototype micro-animations.",
    details: [
      "Objective: Make personal money management intuitive, fast, and empowering.",
      "UX Innovation: 3-second quick-add transaction modal and visual cashflow health meters.",
      "Key Result: User retention and daily check-in motivation increased significantly in concept usability studies."
    ],
    images: [
      "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "ca-founder-collab",
    title: "ArtiApply - AI Cold Outreach SaaS",
    tags: ["SaaS Product", "AI Workflow", "Full-Stack Design"],
    thumbnail: "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&q=80&w=921",
    shortDesc: "An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.",
    projectType: "SaaS Product Design, AI Prompt Pipelines, Frontend Architecture",
    targetAudience: "Founders, Freelancers & Sales Teams",
    timeframe: "4 Weeks",
    client: "ArtiApply SaaS (Founder)",
    problem: "Manual cold outreach is slow and inconsistent, while mass generic email blasts get flagged as spam or ignored. Users lacked a unified, intelligent platform to personalize pitches at scale with reliable deliverability tracking.",
    approach: "Designed and engineered an automated campaign cockpit featuring multi-variable AI personalization, Gmail API rate-limiting integration with BullMQ, and real-time deliverability telemetry.",
    responsibilities: "Full product lifecycle: system architecture, UI/UX design, Supabase realtime backend integration, queue monitoring dashboards, and frontend implementation.",
    details: [
      "Objective: Scale outbound outreach without sacrificing hyper-personalization.",
      "Tech & Design: BullMQ queue management, Gmail API integration, Supabase Realtime, and Tailwind design system.",
      "Key Result: Achieved 3x higher response rates compared to generic template campaigns."
    ],
    images: [
      "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "custom-access-controls",
    title: "Clam Nest - Mental Wellness Platform",
    tags: ["Branding", "UI/UX Design", "Healthcare"],
    thumbnail: "https://images.unsplash.com/photo-1527137342181-19aab11a8ee1?auto=format&fit=crop&q=80&w=919",
    shortDesc: "An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources, guided reflection, and counselor matching.",
    projectType: "Branding, Emotional Design, Responsive Web App",
    targetAudience: "University Students & Young Adults",
    timeframe: "6 Weeks",
    client: "ACM Community Health Project",
    problem: "Young adults experiencing stress or anxiety find mental health portals intimidating, clinical, and difficult to navigate when in distress. The lack of private, comforting digital access creates barriers to seeking help.",
    approach: "Created a welcoming, stigma-free digital haven with comforting typography, gentle color therapy palettes, anonymous counselor matching quizzes, and guided mood journals.",
    responsibilities: "Brand identity creation, emotional design guidelines, accessibility evaluation, cross-platform UI, and usability testing with student focus groups.",
    details: [
      "Objective: Provide accessible, reassuring mental health resources for university students.",
      "Design Focus: Soft pastel tones, micro-animations, and conversational assessment flows.",
      "Key Result: Endorsed by student ACM community for empathy and ease of navigation."
    ],
    images: [
      "https://images.unsplash.com/photo-1527137342181-19aab11a8ee1?auto=format&fit=crop&q=80&w=1200"
    ]
  },
  {
    id: "you-are-okay",
    title: "Campus Chronicles & URJA Visuals",
    tags: ["Visual Storytelling", "Graphic Design", "Branding"],
    thumbnail: "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&q=80&w=1379",
    shortDesc: "Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals (URJA 2025) and monthly student publications.",
    projectType: "Editorial Design, Event Branding, Large-Format Print",
    targetAudience: "10,000+ Festival Attendees & University Students",
    timeframe: "2 Weeks",
    client: "University Cultural Committee & ACM Chapter",
    problem: "Campus festivals and publications historically suffered from disjointed graphics, poor legibility from afar, and fragmented social presence that hurt student turnout.",
    approach: "Engineered an electrifying design language spanning stage backdrops, flex banners, directional signage, badges, and a 16-page editorial magazine with expressive typography.",
    responsibilities: "Creative direction, typography design, large-format print production, social media asset templates, and stage visual design.",
    details: [
      "Objective: Unify campus identity across digital and physical touchpoints.",
      "Key Deliverables: Flex banners, stage backdrops, identity tokens, and editorial layout.",
      "Key Result: Elevated festival branding recognized by over 10,000 attendees."
    ],
    images: [
      "https://images.unsplash.com/photo-1504711434969-e33886168f5c?auto=format&fit=crop&q=80&w=1200"
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
            <span>View case study</span>
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

    if (metaType) metaType.textContent = proj.projectType || "UI/UX Design";
    if (metaAudience) metaAudience.textContent = proj.targetAudience || "General Public";
    if (metaTimeframe) metaTimeframe.textContent = proj.timeframe || "3 Weeks";

    if (modalProblem) modalProblem.textContent = proj.problem;
    if (modalApproach) modalApproach.textContent = proj.approach;
    if (modalResponsibilities) modalResponsibilities.textContent = proj.responsibilities;

    // Render gallery images if any
    if (modalGallery) {
      if (proj.images && proj.images.length > 1) {
        modalGallery.innerHTML = proj.images.slice(1).map(imgUrl => `
          <img src="${imgUrl}" alt="${proj.title} visual" loading="lazy">
        `).join('');
        modalGallery.style.display = "grid";
      } else {
        modalGallery.innerHTML = "";
        modalGallery.style.display = "none";
      }
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
print("Updated app.js")

if os.path.exists('_archive/custom_recreation/app.js'):
    with open('_archive/custom_recreation/app.js', 'w', encoding='utf-8') as f:
        f.write(NEW_APP_JS)
    print("Updated _archive/custom_recreation/app.js")

# ---------------------------------------------------------------------------
# 2. Update index.html
# ---------------------------------------------------------------------------
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace titles, branding, descriptions
content = content.replace('<title>Adyatha | Sr.Communication Designer</title>', '<title>Lakshay Jain | Product &amp; UI/UX Designer</title>')
content = content.replace('content="Adyatha | Sr.Communication Designer"', 'content="Lakshay Jain | Product &amp; UI/UX Designer"')
content = content.replace('Lead Visual Designer with 6+ years crafting brand-defining marketing &amp; product visuals across fintech &amp; consumer apps. I also build AI-powered workflow tools, campaign automation plugins, &amp; scalable design systems that multiply what a small team can ship.', 'Product Designer &amp; UI/UX Strategist crafting intuitive digital products, scalable design systems, and data-driven interfaces across fintech, campus services, and SaaS platforms.')
content = content.replace('Lead Visual Designer with 6+ years crafting brand-defining marketing & product visuals across fintech & consumer apps. I also build AI-powered workflow tools, campaign automation plugins, & scalable design systems that multiply what a small team can ship.', 'Product Designer & UI/UX Strategist crafting intuitive digital products, scalable design systems, and data-driven interfaces across fintech, campus services, and SaaS platforms.')

# Header logo & resume
content = content.replace('>Adyatha<', '>Lakshay Jain<')
content = content.replace('https://drive.google.com/file/d/1oeTA2hXGQNlvhAdGGicsU7XjTBb3CYfn/view?usp=sharing', 'https://linktr.ee/lakshay.j')

# Project 1: 8 CLUB -> New Better PNB
content = content.replace('8 CLUB Onboarding Video', 'New Better PNB - UI/UX Case Study')
content = content.replace('An electrifying 30-second motion piece that unveils 8Club’s invite-only Hotspots, setting the vibe with kinetic visuals and bold typography.', 'A comprehensive redesign of the Punjab National Bank mobile application, solving navigation friction and boosting usability for senior demographics.')
content = content.replace('An electrifying 30-second motion piece that unveils 8Club&#x2019;s invite-only Hotspots, setting the vibe with kinetic visuals and bold typography.', 'A comprehensive redesign of the Punjab National Bank mobile application, solving navigation friction and boosting usability for senior demographics.')
content = content.replace('>Motion Design</p>', '>UI/UX Design</p>')
content = content.replace('>Script writing</p>', '>Design System</p>')

# Project 2: Show me the money -> Laundify
content = content.replace('Show me the money', 'Laundify - Campus Service App')
content = content.replace('A comprehensive report analyzing payment and hiring trends across 20 sectors, providing data-driven insights into salary patterns in India', 'An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.')
content = content.replace('>Publication design</p>', '>Product Design</p>')
content = content.replace('>AI generated design</p>', '>Mobile UX</p>')

# Project 3: Enterprise Readiness GTM -> Sanchay
content = content.replace('Enterprise Readiness GTM', 'Sanchay - Money Manager')
content = content.replace('Brand campaign highlighting the evolution and expanded features of the payroll software, now optimized for enterprise-level use.', 'A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.')
content = content.replace('>GTM Strategy</p>', '>Fintech Design</p>')
content = content.replace('>Print Design</p>', '>Data Visualization</p>')

# Project 4: CA & Founder Collab -> ArtiApply
content = content.replace('CA &amp; Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
content = content.replace('CA & Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
content = content.replace('Social campaign highlighting the challenges of traditional founder-Chartered Accountant collaboration, promoting RazorpayX as a streamlined solution.', 'An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.')
content = content.replace('>Motion Graphics</p>', '>SaaS Product</p>')
content = content.replace('>Script Writing</p>', '>AI Workflow</p>')
content = content.replace('>Script Writing </p>', '>AI Workflow</p>')

# Project 5: Custom Access Controls -> Clam Nest
content = content.replace('Custom Access Controls', 'Clam Nest - Mental Wellness Platform')
content = content.replace('Promotional video campaign showcasing new custom access controls and approval workflows in RazorpayX Banking, designed to enhance delegation and collaboration.', 'An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.')
content = content.replace('>Story telling</p>', '>UI/UX Design</p>')

# Project 6: You Are Okay -> Campus Chronicles
content = content.replace('You Are Okay', 'Campus Chronicles &amp; URJA Visuals')
content = content.replace('A self-help activity book that helps anxious teenagers express their emotions and frustrations creatively, enhancing their learning experience and aiding in self-reflection.', 'Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.')
content = content.replace('>Book Design</p>', '>Visual Storytelling</p>')
content = content.replace('>Art Therapy</p>', '>Graphic Design</p>')
content = content.replace('>Illustration</p>', '>Branding</p>')

# Footers
content = content.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
content = content.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")

# ---------------------------------------------------------------------------
# 3. Update framer_dist/WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs
# ---------------------------------------------------------------------------
wgpd_path = 'framer_dist/WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs'
if os.path.exists(wgpd_path):
    with open(wgpd_path, 'r', encoding='utf-8') as f:
        mjs = f.read()
    
    mjs = mjs.replace('8 CLUB Onboarding Video', 'New Better PNB - UI/UX Case Study')
    mjs = mjs.replace('An electrifying 30-second motion piece that unveils 8Club’s invite-only Hotspots, setting the vibe with kinetic visuals and bold typography.', 'A comprehensive redesign of the Punjab National Bank mobile application, solving navigation friction and boosting usability for senior demographics.')
    
    mjs = mjs.replace('Show me the money', 'Laundify - Campus Service App')
    mjs = mjs.replace('A comprehensive report analyzing payment and hiring trends across 20 sectors, providing data-driven insights into salary patterns in India', 'An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.')
    
    mjs = mjs.replace('Enterprise Readiness GTM', 'Sanchay - Money Manager')
    mjs = mjs.replace('Brand campaign highlighting the evolution and expanded features of the payroll software, now optimized for enterprise-level use.', 'A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.')
    
    mjs = mjs.replace('CA & Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
    mjs = mjs.replace('CA \\u0026 Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
    mjs = mjs.replace('Social campaign highlighting the challenges of traditional founder-Chartered Accountant collaboration, promoting RazorpayX as a streamlined solution.', 'An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.')
    
    mjs = mjs.replace('Custom Access Controls', 'Clam Nest - Mental Wellness Platform')
    mjs = mjs.replace('Promotional video campaign showcasing new custom access controls and approval workflows in RazorpayX Banking, designed to enhance delegation and collaboration.', 'An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.')
    
    mjs = mjs.replace('You Are Okay', 'Campus Chronicles & URJA Visuals')
    mjs = mjs.replace('A self-help activity book that helps anxious teenagers express their emotions and frustrations creatively, enhancing their learning experience and aiding in self-reflection.', 'Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.')
    
    mjs = mjs.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    mjs = mjs.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')
    mjs = mjs.replace('`Adyatha`', '`Lakshay Jain`')
    
    with open(wgpd_path, 'w', encoding='utf-8') as f:
        f.write(mjs)
    print("Updated", wgpd_path)

# Also update framer_home_page.mjs
if os.path.exists('framer_home_page.mjs'):
    with open('framer_home_page.mjs', 'r', encoding='utf-8') as f:
        fhome = f.read()
    fhome = fhome.replace('8 CLUB Onboarding Video', 'New Better PNB - UI/UX Case Study')
    fhome = fhome.replace('An electrifying 30-second motion piece that unveils 8Club’s invite-only Hotspots, setting the vibe with kinetic visuals and bold typography.', 'A comprehensive redesign of the Punjab National Bank mobile application, solving navigation friction and boosting usability for senior demographics.')
    fhome = fhome.replace('Show me the money', 'Laundify - Campus Service App')
    fhome = fhome.replace('A comprehensive report analyzing payment and hiring trends across 20 sectors, providing data-driven insights into salary patterns in India', 'An on-demand laundry management system for university campuses featuring live washer telemetry, schedule booking, and digital payments.')
    fhome = fhome.replace('Enterprise Readiness GTM', 'Sanchay - Money Manager')
    fhome = fhome.replace('Brand campaign highlighting the evolution and expanded features of the payroll software, now optimized for enterprise-level use.', 'A personal finance tool that turns complex budgeting and expense tracking into clean, actionable visual insights and automated savings milestones.')
    fhome = fhome.replace('CA & Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
    fhome = fhome.replace('CA \\u0026 Founder Collaboration', 'ArtiApply - AI Cold Outreach SaaS')
    fhome = fhome.replace('Social campaign highlighting the challenges of traditional founder-Chartered Accountant collaboration, promoting RazorpayX as a streamlined solution.', 'An AI-powered cold email outreach engine built with real-time analytics, queue management, BullMQ rate limiting, and high-conversion campaign pipelines.')
    fhome = fhome.replace('Custom Access Controls', 'Clam Nest - Mental Wellness Platform')
    fhome = fhome.replace('Promotional video campaign showcasing new custom access controls and approval workflows in RazorpayX Banking, designed to enhance delegation and collaboration.', 'An ACM-backed digital therapy platform designed with calming visual aesthetics, offering student mental health resources and counselor matching.')
    fhome = fhome.replace('You Are Okay', 'Campus Chronicles & URJA Visuals')
    fhome = fhome.replace('A self-help activity book that helps anxious teenagers express their emotions and frustrations creatively, enhancing their learning experience and aiding in self-reflection.', 'Dynamic publication layouts and large-scale event visual branding designed for university cultural festivals and student editorial publications.')
    fhome = fhome.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    fhome = fhome.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')
    fhome = fhome.replace('`Adyatha`', '`Lakshay Jain`')
    with open('framer_home_page.mjs', 'w', encoding='utf-8') as f:
        f.write(fhome)
    print("Updated framer_home_page.mjs")

# ---------------------------------------------------------------------------
# 4. Update About Page in framer_pages/about.html & framer_pages_transformed/about.html
# ---------------------------------------------------------------------------
def update_about_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        ab = f.read()

    ab = ab.replace('<title>Adyatha | Sr.Communication Designer</title>', '<title>Lakshay Jain | About Me</title>')
    ab = ab.replace('content="Adyatha | Sr.Communication Designer"', 'content="Lakshay Jain | About Me"')
    ab = ab.replace('>Adyatha<', '>Lakshay Jain<')
    ab = ab.replace('https://drive.google.com/file/d/1oeTA2hXGQNlvhAdGGicsU7XjTBb3CYfn/view?usp=sharing', 'https://linktr.ee/lakshay.j')

    # Content replacement
    ab = ab.replace(
        'So, I am assuming you have come to this page to find out more about me as a person. And now I feel I need to be a lot more interesting *sweats*',
        'Welcome to my corner of the web! If you have landed here, you are probably curious to learn about the mind behind the products and pixels.'
    )
    ab = ab.replace(
        'Here’s the rundown: I’m a Senior Communication Designer with 4 years of experience at Razorpay.',
        'Here’s the rundown: I’m Lakshay Jain, a Product Designer &amp; UI/UX Strategist passionate about crafting intuitive digital products, scalable design systems, and data-driven experiences.'
    )
    ab = ab.replace(
        'Here’s the rundown: I’m a Senior Communication Designer with 4 years of experience at Razorpay.',
        'Here’s the rundown: I’m Lakshay Jain, a Product Designer & UI/UX Strategist passionate about crafting intuitive digital products, scalable design systems, and data-driven experiences.'
    )
    ab = ab.replace(
        'I’m obsessed with stories—telling them, listening to them, reading them, and of course, crafting them. My love for stories probably ties into the fact that I’m a huge history nerd (seriously, ask me about Henry VIII and his many wives).',
        'I’m obsessed with transforming complex user problems into crisp, functional blueprints. From reimagining digital banking with Punjab National Bank, to engineering campus utilities like Laundify, to building AI platforms like ArtiApply—I believe great products are born where user empathy meets engineering precision.'
    )
    ab = ab.replace(
        'I believe that weaving stories into business goals and strategy is crucial for creating designs that truly connect with users. After all, no matter who your audience is, they experience emotions.',
        'I treat design not as decoration, but as product strategy. Every interaction model, typeface, and layout is intentionally crafted to remove friction, build trust, and deliver tangible results for users.'
    )
    ab = ab.replace(
        'Outside of envying the life of my very spoilt cat, I\'m passionate about the value of education and design thinking.',
        'Beyond Figma and code, I\'m deeply passionate about developer communities and product innovation. I actively contribute to student initiatives through ACM, mentor peers in design thinking, and love experimenting with emerging tech.'
    )
    ab = ab.replace(
        'I\'ve twice had the privilege of serving as an External Jury member for the Visual Communication Design department at Jain University School of Design, Media, and Creative Arts.',
        'I lead design and technical efforts for hackathons, campus events, and open-source tools—focusing on accessibility, responsive systems, and high-impact visual identities.'
    )
    ab = ab.replace(
        'In a nutshell, I\'m all about blending creativity with purpose, ensuring every design I create not only looks great but also tells a story that resonates. Whether it\'s through crafting compelling visuals, diving into historical rabbit holes, or mentoring future designers, I’m constantly striving to make an impact.',
        'In a nutshell, I blend aesthetic craftsmanship with engineering clarity—ensuring every product not only looks stunning, but delivers measurable results and delightful interactions.'
    )
    ab = ab.replace(
        'If you’re interested in collaborating or just want to chat, I’m all ears.',
        'If you’re interested in collaborating, discussing a product vision, or hiring, let\'s connect! Direct email: lakshayjain148@gmail.com | linktr.ee/lakshay.j'
    )
    ab = ab.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    ab = ab.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(ab)
    print("Updated", file_path)

update_about_html('framer_pages_transformed/about.html')
if os.path.exists('framer_pages/about.html'):
    update_about_html('framer_pages/about.html')

# ---------------------------------------------------------------------------
# 5. Update About Module in framer_dist/GZCikEng2ds9ljEaHPZsUI30jMSOPStZY2CH5DyKZ9A.IDe8msX-.mjs
# ---------------------------------------------------------------------------
gz_path = 'framer_dist/GZCikEng2ds9ljEaHPZsUI30jMSOPStZY2CH5DyKZ9A.IDe8msX-.mjs'
if os.path.exists(gz_path):
    with open(gz_path, 'r', encoding='utf-8') as f:
        gz = f.read()
    
    gz = gz.replace(
        'So, I am assuming you have come to this page to find out more about me as a person. And now I feel I need to be a lot more interesting *sweats*',
        'Welcome to my corner of the web! If you have landed here, you are probably curious to learn about the mind behind the products and pixels.'
    )
    gz = gz.replace(
        'Here’s the rundown: I’m a Senior Communication Designer with 4 years of experience at Razorpay.',
        'Here’s the rundown: I’m Lakshay Jain, a Product Designer & UI/UX Strategist passionate about crafting intuitive digital products and scalable systems.'
    )
    gz = gz.replace(
        'Here\\u2019s the rundown: I\\u2019m a Senior Communication Designer with 4 years of experience at Razorpay.',
        'Here\\u2019s the rundown: I\\u2019m Lakshay Jain, a Product Designer & UI/UX Strategist passionate about crafting intuitive digital products and scalable systems.'
    )
    gz = gz.replace(
        'I’m obsessed with stories—telling them, listening to them, reading them, and of course, crafting them. My love for stories probably ties into the fact that I’m a huge history nerd (seriously, ask me about Henry VIII and his many wives).',
        'I’m obsessed with transforming complex user problems into crisp, functional blueprints. From reimagining digital banking with Punjab National Bank, to engineering campus utilities like Laundify, to building AI platforms like ArtiApply—I believe great products are born where user empathy meets engineering precision.'
    )
    gz = gz.replace(
        'I\\u2019m obsessed with stories\\u2014telling them, listening to them, reading them, and of course, crafting them. My love for stories probably ties into the fact that I\\u2019m a huge history nerd (seriously, ask me about Henry VIII and his many wives).',
        'I\\u2019m obsessed with transforming complex user problems into crisp, functional blueprints. From reimagining digital banking with Punjab National Bank, to engineering campus utilities like Laundify, to building AI platforms like ArtiApply\\u2014I believe great products are born where user empathy meets engineering precision.'
    )
    gz = gz.replace(
        'I believe that weaving stories into business goals and strategy is crucial for creating designs that truly connect with users. After all, no matter who your audience is, they experience emotions.',
        'I treat design not as decoration, but as product strategy. Every interaction model, typeface, and layout is intentionally crafted to remove friction, build trust, and deliver tangible results for users.'
    )
    gz = gz.replace(
        'Outside of envying the life of my very spoilt cat, I\'m passionate about the value of education and design thinking.',
        'Beyond Figma and code, I\'m deeply passionate about developer communities and product innovation. I actively contribute to student initiatives through ACM, mentor peers in design thinking, and love experimenting with emerging tech.'
    )
    gz = gz.replace(
        'I\'ve twice had the privilege of serving as an External Jury member for the Visual Communication Design department at Jain University School of Design, Media, and Creative Arts.',
        'I lead design and technical efforts for hackathons, campus events, and open-source tools—focusing on accessibility, responsive systems, and high-impact visual identities.'
    )
    gz = gz.replace(
        'In a nutshell, I\'m all about blending creativity with purpose, ensuring every design I create not only looks great but also tells a story that resonates. Whether it\'s through crafting compelling visuals, diving into historical rabbit holes, or mentoring future designers, I’m constantly striving to make an impact.',
        'In a nutshell, I blend aesthetic craftsmanship with engineering clarity—ensuring every product not only looks stunning, but delivers measurable results and delightful interactions.'
    )
    gz = gz.replace(
        'If you’re interested in collaborating or just want to chat, I’m all ears.',
        'If you’re interested in collaborating, discussing a product vision, or hiring, let\'s connect! Direct email: lakshayjain148@gmail.com | linktr.ee/lakshay.j'
    )
    gz = gz.replace(
        'If you\\u2019re interested in collaborating or just want to chat, I\\u2019m all ears.',
        'If you\\u2019re interested in collaborating, discussing a product vision, or hiring, let\\u2019s connect! Direct email: lakshayjain148@gmail.com | linktr.ee/lakshay.j'
    )
    
    with open(gz_path, 'w', encoding='utf-8') as f:
        f.write(gz)
    print("Updated", gz_path)

# ---------------------------------------------------------------------------
# 6. Update all other framer_dist/ JS modules mentioning Adyatha or old titles
# ---------------------------------------------------------------------------
for jf in glob.glob('framer_dist/*.mjs'):
    with open(jf, 'r', encoding='utf-8') as f:
        c = f.read()
    orig = c
    c = c.replace('Adyatha Bhat | Lead Visual Designer', 'Lakshay Jain | Product & UI/UX Designer')
    c = c.replace('Adyatha | Sr.Communication Designer', 'Lakshay Jain | Product & UI/UX Designer')
    c = c.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    c = c.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')
    c = c.replace('`Adyatha`', '`Lakshay Jain`')
    c = c.replace('\"Adyatha\"', '\"Lakshay Jain\"')
    if c != orig:
        with open(jf, 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated branding in", os.path.basename(jf))

# ---------------------------------------------------------------------------
# 7. Update all transformed case study HTML pages
# ---------------------------------------------------------------------------
CASE_PAGES = [
    ('framer_pages_transformed/8club-onboarding-video.html', 'New Better PNB - UI/UX Case Study', 'Punjab National Bank Mobile App Redesign by Lakshay Jain'),
    ('framer_pages_transformed/show-me-the-money.html', 'Laundify - Campus Service App', 'On-Demand Campus Laundry Management System by Lakshay Jain'),
    ('framer_pages_transformed/enterprise-readiness.html', 'Sanchay - Personal Finance Manager', 'Personal Finance & Wealth Tracking App by Lakshay Jain'),
    ('framer_pages_transformed/ca-founder-collab.html', 'ArtiApply - AI Cold Outreach SaaS', 'AI Cold Email Outreach & Campaign Architecture by Lakshay Jain'),
    ('framer_pages_transformed/custom-access-controls.html', 'Clam Nest - Mental Wellness Platform', 'ACM Digital Therapy & Student Wellbeing Platform by Lakshay Jain'),
    ('framer_pages_transformed/you-are-okay.html', 'Campus Chronicles & URJA Visuals', 'Festival Visual Identity & Editorial Layouts by Lakshay Jain'),
]

for page_path, page_title, page_desc in CASE_PAGES:
    if os.path.exists(page_path):
        with open(page_path, 'r', encoding='utf-8') as f:
            cp = f.read()
        cp = cp.replace('<title>Adyatha | Sr.Communication Designer</title>', f'<title>{page_title} | Lakshay Jain</title>')
        cp = cp.replace('content="Adyatha | Sr.Communication Designer"', f'content="{page_title} | Lakshay Jain"')
        cp = cp.replace('content="Lead Visual Designer with 6+ years crafting brand-defining marketing &amp; product visuals across fintech &amp; consumer apps. I also build AI-powered workflow tools, campaign automation plugins, &amp; scalable design systems that multiply what a small team can ship."', f'content="{page_desc}"')
        cp = cp.replace('>Adyatha<', '>Lakshay Jain<')
        cp = cp.replace('https://drive.google.com/file/d/1oeTA2hXGQNlvhAdGGicsU7XjTBb3CYfn/view?usp=sharing', 'https://linktr.ee/lakshay.j')
        cp = cp.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
        cp = cp.replace('©2024 portfolio by Prabodh Bharadwaj', '© 2025 Portfolio by Lakshay Jain')
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(cp)
        print("Updated case study page", os.path.basename(page_path))

# ---------------------------------------------------------------------------
# 8. Update _archive/custom_recreation/index.html
# ---------------------------------------------------------------------------
custom_index = '_archive/custom_recreation/index.html'
if os.path.exists(custom_index):
    with open(custom_index, 'r', encoding='utf-8') as f:
        ci = f.read()
    
    ci = ci.replace('Adyatha Bhat | Lead Visual & Communication Designer', 'Lakshay Jain | Product & UI/UX Designer')
    ci = ci.replace('Adyatha Bhat', 'Lakshay Jain')
    ci = ci.replace('<span>Adyatha</span>', '<span>Lakshay Jain</span>')
    ci = ci.replace('aria-label="Adyatha Bhat Home"', 'aria-label="Lakshay Jain Home"')
    ci = ci.replace('Adyatha. visual designer,', 'Lakshay. product designer,')
    ci = ci.replace('storyteller &amp; design mentor', 'ui/ux strategist · builder')
    ci = ci.replace('storyteller & design mentor', 'ui/ux strategist · builder')
    ci = ci.replace('Senior Communication Designer with 4 years of experience at Razorpay', 'Product Designer & UI/UX Strategist crafting intuitive fintech, SaaS, and service platforms')
    ci = ci.replace('https://drive.google.com/file/d/1oeTA2hXGQNlvhAdGGicsU7XjTBb3CYfn/view?usp=sharing', 'https://linktr.ee/lakshay.j')
    ci = ci.replace('© 2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    ci = ci.replace('©2024 portfolio by Adyatha Bhat', '© 2025 Portfolio by Lakshay Jain')
    
    # About bio in custom recreation
    ci = re.sub(
        r'<div class="about-lead">.*?</div>',
        '<div class="about-lead">"Every design here is my blueprint — conceived from scratch, crafted with care, and built to solve real-world problems."</div>',
        ci,
        flags=re.DOTALL
    )
    
    with open(custom_index, 'w', encoding='utf-8') as f:
        f.write(ci)
    print("Updated _archive/custom_recreation/index.html")

print("\\nAll portfolio content, case studies, and about me details successfully migrated to Lakshay Jain!")
