// ==========================================================================
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
    targetAudience: "50M+ Retail Banking Customers, Senior Citizens & Youth",
    timeframe: "4 Weeks",
    client: "Punjab National Bank (Redesign)",
    problem: "PNB's banking website is difficult to navigate, with complex menus and a cluttered homepage that frustrate users trying to complete tasks like fund transfers, bill payments, and account management. The lack of personalization and outdated design further complicates the user experience, especially for mobile users. These issues lead to inefficiency, user frustration, and a negative impact on customer retention.",
    approach: "Discovery: Primary & secondary user interviews uncovering key friction points for elder demographics (Ramesh Verma, 56) and mobile-first students (Aditi Mehra, 20). Ideation: Formulated How-Might-We (HMW) frameworks, simplified 2-step UPI transfers, and designed a softer, accessible high-contrast palette (HEX #AF2A30, #FFF1D3, #C00000, #FDBD30). Implementation: Built a complete design system with Outfit variable typography and interactive prototypes.",
    responsibilities: "User research, persona development, information architecture, wireframing, high-contrast design tokens, interactive prototyping, and usability benchmarking.",
    details: [
      "Key Result: Task completion time reduced by 40% in user testing.",
      "Error Reduction: 65% drop in transaction drop-offs and input errors.",
      "Typography & Colors: Outfit modern geometric typeface with accessible bank-heritage tones.",
      "Personas Addressed: Ramesh Verma (simplified non-glitchy transfers) & Aditi Mehra (2-3 tap quick UPI)."
    ],
    images: [
      "/assets/case_pnb_thumb.png",
      "/assets/case_pnb.png",
      "/assets/slides/pnb/page_1.png"
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
    approach: "Evaluated user journeys and prioritized interventions using the RICE framework (Contextual Tooltips: RICE 900; Interactive Onboarding: RICE 600). Designed structured, role-based setup wizards ('I'm a Designer', 'I'm a Developer', 'Just Browsing') that highlight key channels and suppress notification noise until onboarding is complete. Created a Guided Discovery flow for interest curation in 3 clicks.",
    responsibilities: "Product teardown research, friction mapping, RICE prioritization matrix, user journey maps, high-fidelity UI solutions, and projected retention modeling.",
    details: [
      "Projected Impact: +20% Day-1 Retention and +35% increase in first-week engagement.",
      "Solution 1: Interactive Guided Tours replacing empty states with role-based setup (+15% retention, 2.5x speed).",
      "Solution 2: Guided Discovery 'Curating the Chaos' helping users find top communities in under 3 clicks.",
      "Persona: Harshit Aggarwal (19, Casual Gamer & Student) - Overwhelmed by server hierarchy."
    ],
    images: [
      "/assets/case_discord_thumb.png",
      "/assets/case_discord_preview.png",
      "/assets/slides/discord/page_1.png",
      "/assets/slides/discord/page_4.png",
      "/assets/slides/discord/page_7.png",
      "/assets/slides/discord/page_11.png"
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
      "Rollout Plan: Phased transition from Tier-1 pilots (98% positive) to nationwide supply chain deployment.",
      "Persona: Aman Kapoor (Junior Developer) - Demands piping hot food with zero wasteful plastic."
    ],
    images: [
      "/assets/case_dominos_thumb.png",
      "/assets/case_dominos_preview.png",
      "/assets/slides/dominos/page_1.png",
      "/assets/slides/dominos/page_3.png",
      "/assets/slides/dominos/page_5.png",
      "/assets/slides/dominos/page_9.png"
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
      "Outcome: Solved creator friction while elevating niche creator discovery beyond viral trends.",
      "Persona: Maya Singh (22, Tech & Lifestyle Creator) - 45% faster publishing workflow."
    ],
    images: [
      "/assets/case_insta_thumb.png",
      "/assets/case_insta_preview.png",
      "/assets/slides/insta/page_1.png",
      "/assets/slides/insta/page_4.png",
      "/assets/slides/insta/page_7.png",
      "/assets/slides/insta/page_11.png"
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
      "Key Result: Achieved 3x higher response rates compared to generic template campaigns.",
      "Domain Safety: 100% domain reputation safety preserved across 50,000+ outreach messages."
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
      "Key Features: Real-time telemetry, automated slot reservations, and campus wallet integration.",
      "Student Adoption: 85% voluntary adoption rate among surveyed student residents in pilot dormitories."
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
          <div style="grid-column: 1 / -1; margin-bottom: 1.5rem; display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
            <a href="${proj.pdfUrl}" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 10px; background: #2563eb; color: #fff; padding: 13px 26px; border-radius: 999px; text-decoration: none; font-weight: 600; font-size: 14px; box-shadow: 0 4px 14px rgba(37,99,235,0.4); transition: transform 0.2s ease;">
              <span>Open / Download Full PDF Presentation</span>
              <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
            </a>
            <a href="/${proj.id}" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 13px 22px; border-radius: 999px; text-decoration: none; font-weight: 600; font-size: 14px;">
              <span>View Full Interactive Page ↗</span>
            </a>
          </div>
        `;
      }
      if (proj.images && proj.images.length > 1) {
        galleryHtml += `
          <div style="grid-column: 1 / -1; margin-top: 1rem; margin-bottom: 0.5rem;">
            <h4 style="font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 12px;">Visual Artifacts & Slide Captures</h4>
          </div>
        `;
        galleryHtml += proj.images.slice(1).map(imgUrl => `
          <div style="border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.1); background: #000;">
            <img src="${imgUrl}" alt="${proj.title} visual" loading="lazy" style="width: 100%; height: auto; display: block;">
          </div>
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
