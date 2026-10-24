// ==========================================================================
// LAKSHAY JAIN PORTFOLIO - APPLICATION SCRIPT
// Theme switcher, Client-side navigation, Case study modal reader
// ==========================================================================

const PROJECTS_DATA = [
  {
    id: "dominos-packaging-redesign",
    legacyId: "enterprise-readiness",
    title: "Domino's New Packaging: A Strategic Redesign",
    tags: ["Product Teardown", "Sustainability", "Systems Design"],
    thumbnail: "/assets/case_dominos_thumb.png",
    pdfUrl: "/Domino_s product teardown by Lakshay.pdf",
    shortDesc: "A strategic redesign deconstructing thermal thermodynamics, eco-accountability, and supply-chain stackability across 1,500+ franchise locations.",
    projectType: "Product Teardown, Systems UX & Packaging Strategy",
    targetAudience: "Eco-Conscious Cravers & Last-Mile Delivery Fleets",
    timeframe: "3 Weeks",
    client: "Product Strategy Teardown",
    problem: "Why the legacy box failed: 1) Thermodynamics - 40% heat loss within 15 minutes due to standard uninsulated corrugated cardboard; 2) Sustainability - 30% of legacy boxes rendered unrecyclable due to oil and grease saturation; 3) Structural Integrity - weak sidewalls caused crushing beyond 3 stacked boxes during rush delivery periods.",
    approach: "Strategic pivot across 4 core business pillars: 1) Sustainability First (-30% plastic, shifting to 100% recycled materials); 2) Heat Retention (+15% longer thermal holding with corrugated air pockets); 3) Stackability (doubled courier bag density); 4) Brand Modernization (bi-color minimalist aesthetic inspired by tech-first unboxing). Designed phased rollout across 1,500+ franchise locations.",
    responsibilities: "Thermodynamic heat loss deconstruction, material recyclability analysis, user persona modeling (Aman Kapoor, Junior Developer), operational ROI analysis, sustainability metrics, and unboxing UX.",
    details: [
      "Operational Results: 22% waste reduction in cardboard usage and 15% material cost savings.",
      "Customer Sentiment: 4.8★ delivery rating (75% 5-star share, +14% vs old packaging).",
      "Thermal Performance: +15 minutes longer optimal eating temperature after 20m delivery.",
      "Sustainability Target: On track for 100% plastic-free packaging by 2025."
    ],
    images: [
      "/assets/case_dominos_thumb.png",
      "/assets/case_dominos_preview.png",
      "/assets/slides/dominos/page_1.png",
      "/assets/slides/dominos/page_2.png",
      "/assets/slides/dominos/page_3.png",
      "/assets/slides/dominos/page_4.png",
      "/assets/slides/dominos/page_5.png",
      "/assets/slides/dominos/page_6.png",
      "/assets/slides/dominos/page_7.png",
      "/assets/slides/dominos/page_8.png",
      "/assets/slides/dominos/page_9.png"
    ]
  },
  {
    id: "instagram-reels-experience",
    legacyId: "ca-founder-collab",
    title: "Improving the Reels Experience on Instagram",
    tags: ["Product Teardown", "Growth Strategy", "Mobile UX", "Creator Economy"],
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
      "Key Equation: Engagement = Watch Time x Creator Follows x No. of Sessions.",
      "Solution 1: In-Camera Editing Studio with multi-track audio, precise timeline trimming, and effect overlays.",
      "Solution 2: Collaborative Reels with dual profile posting and shared attribution.",
      "Scale: Serves 2B+ MAU, 200B+ daily plays across 140+ countries."
    ],
    images: [
      "/assets/case_insta_thumb.png",
      "/assets/case_insta_preview.png",
      "/assets/slides/insta/page_1.png",
      "/assets/slides/insta/page_2.png",
      "/assets/slides/insta/page_3.png",
      "/assets/slides/insta/page_4.png",
      "/assets/slides/insta/page_5.png",
      "/assets/slides/insta/page_6.png",
      "/assets/slides/insta/page_7.png",
      "/assets/slides/insta/page_8.png",
      "/assets/slides/insta/page_9.png",
      "/assets/slides/insta/page_10.png",
      "/assets/slides/insta/page_11.png"
    ]
  },
  {
    id: "pnb-website-redesign",
    legacyId: "8club-onboarding-video",
    title: "UI/UX Case Study: PNB Website Redesign",
    tags: ["UI/UX Design", "Design System", "Accessibility", "Fintech"],
    thumbnail: "/assets/case_pnb_thumb.png",
    pdfUrl: "/PNB Redesign by Lakshay.pdf",
    shortDesc: "A complete usability redesign of Punjab National Bank’s digital experience, resolving navigation clutter and reducing transaction friction by 40%.",
    projectType: "UI/UX Case Study, Banking Redesign (2025)",
    targetAudience: "50M+ Retail Banking Customers, Senior Citizens & Youth",
    timeframe: "4 Weeks",
    client: "Punjab National Bank (Redesign by Himani & Lakshay)",
    problem: "PNB's banking website is difficult to navigate, with complex menus and a cluttered homepage that frustrate users trying to complete tasks like fund transfers, bill payments, and account management. The lack of personalization and outdated design further complicates the user experience, especially for mobile users. These issues lead to inefficiency, user frustration, and a negative impact on customer retention.",
    approach: "Followed a 3-step design process: 1) DISCOVERY: Conducted primary & secondary research via user surveys and interviews uncovering acute friction for elders and mobile youth; 2) IDEATION: Formulated How-Might-We (HMW) frameworks, simplified 2-step UPI transfers, and designed a softer, accessible high-contrast palette; 3) IMPLEMENTATION: Built an Outfit-based design system and interactive high-fidelity prototypes.",
    responsibilities: "User research, persona development, information architecture, wireframing, high-contrast design tokens, interactive prototyping, and usability benchmarking.",
    details: [
      "Key Result: Task completion time reduced by 40% in user testing.",
      "Error Reduction: 65% drop in transaction drop-offs and input errors.",
      "Typography & Colors: Outfit modern geometric typeface with bank-heritage tones (#AF2A30, #FFF1D3, #C00000).",
      "User Journey: Optimized Homepage -> Login -> Using Services -> Completing a Task."
    ],
    images: [
      "/assets/case_pnb_thumb.png",
      "/assets/case_pnb.png",
      "/assets/slides/pnb/page_1.png"
    ]
  },
  {
    id: "improving-discord-new-users",
    legacyId: "show-me-the-money",
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
      "Scale: 150M+ Monthly Active Users, 19M+ Active Servers, 4B min/day conversation volume."
    ],
    images: [
      "/assets/case_discord_thumb.png",
      "/assets/case_discord_preview.png",
      "/assets/slides/discord/page_1.png",
      "/assets/slides/discord/page_2.png",
      "/assets/slides/discord/page_3.png",
      "/assets/slides/discord/page_4.png",
      "/assets/slides/discord/page_5.png",
      "/assets/slides/discord/page_6.png",
      "/assets/slides/discord/page_7.png",
      "/assets/slides/discord/page_8.png",
      "/assets/slides/discord/page_9.png",
      "/assets/slides/discord/page_10.png",
      "/assets/slides/discord/page_11.png"
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
            <a href="/${proj.legacyId || proj.id}" style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 13px 22px; border-radius: 999px; text-decoration: none; font-weight: 600; font-size: 14px;">
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
