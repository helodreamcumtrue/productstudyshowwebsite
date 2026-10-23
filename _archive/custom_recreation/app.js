// ==========================================================================
// ADYATHA BHAT PORTFOLIO - APPLICATION SCRIPT
// Theme switcher, Client-side navigation, Case study modal reader
// ==========================================================================

const PROJECTS_DATA = [
  {
    id: "8club-onboarding-video",
    title: "8 CLUB Onboarding Video",
    tags: ["Motion Design", "Script writing"],
    thumbnail: "https://framerusercontent.com/images/TTX6I3wwJ52GRBE0gUz9lXbJds.png?width=961&height=961",
    shortDesc: "An electrifying 30-second motion piece that unveils 8Club’s invite-only Hotspots, setting the vibe with kinetic visuals and bold typography.",
    projectType: "Motion Graphics, Visual design, Script Writing",
    targetAudience: "Young Urban Professionals",
    timeframe: "2 Weeks",
    client: "8Club",
    problem: "8Club reached out with an exciting ask: craft an onboarding video that captures the essence of their platform. 8Club is a members-only social platform that curates offline experiences called 'Hotspots' designed for people to meet, connect, and build real communities. This video needed to introduce what 8Club is, what makes it different, and what users can expect next.",
    approach: "The brief was open-ended: no brand style guide, no visual references—just a clear ask for a video that felt fresh, dynamic, and uniquely them. 8Club isn’t just an events platform; it’s a curated experience about music, moments, and memory-making. From the start, I knew the video couldn’t just 'tell' people about 8Club. It had to sound like a beat drop, move like a dance floor, and look like a late-night poster you’d want to steal.",
    responsibilities: "I was brought on as the communication designer to lead the entire process—from scripting and storyboarding to visual design and final animation. I developed the script from scratch, crafting an edgy rhythm, kinetic typography transitions, and vibrant high-contrast visual cues.",
    images: [
      "https://framerusercontent.com/images/TTX6I3wwJ52GRBE0gUz9lXbJds.png?width=961&height=961"
    ]
  },
  {
    id: "show-me-the-money",
    title: "Show me the money",
    tags: ["Publication design", "AI generated design"],
    thumbnail: "https://framerusercontent.com/images/VmS3aMgSsdk4LF6effc4953Cclk.png?width=921&height=921",
    shortDesc: "A comprehensive report analyzing payment and hiring trends across 20 sectors, providing data-driven insights into salary patterns in India.",
    projectType: "Publication design, AI generated design",
    targetAudience: "Businesses of all sizes",
    timeframe: "3 Weeks",
    client: "RazorpayX Payroll",
    problem: "Businesses often face challenges in understanding evolving salary trends and hiring patterns, which can hinder their ability to make informed, data-driven decisions. Existing customers need fresh, insightful data to stay competitive, while new customers seek robust research tools to understand market dynamics. Without comprehensive analysis, companies may struggle to align their strategies with current corporate landscape trends.",
    approach: "Designed a landmark 60+ page salary benchmark report featuring bespoke AI-generated visual motifs representing each sector, custom information design, infographics, and scannable visual executive summaries that made complex compensation metrics intuitive.",
    responsibilities: "Lead publication designer, creative director for AI image synthesis pipelines, data visualization specialist, and layout typography director.",
    images: [
      "https://framerusercontent.com/images/VmS3aMgSsdk4LF6effc4953Cclk.png?width=921&height=921",
      "https://framerusercontent.com/images/g5KVRjBRFsmT99uhTbSd0YG9w.png",
      "https://framerusercontent.com/images/RjddwP5s8UYE5YocYcjbPOzBzYg.png",
      "https://framerusercontent.com/images/qjqcrU49O6gdzjURI715eVapRNY.png",
      "https://framerusercontent.com/images/ytdMP227GFhEbbJptlLQ5geRw.png"
    ]
  },
  {
    id: "enterprise-readiness",
    title: "Enterprise Readiness GTM",
    tags: ["GTM Strategy", "Motion Design", "Print Design"],
    thumbnail: "https://framerusercontent.com/images/8xt1f8uMJqhBTJdZ7iTfaUqp1M8.svg",
    shortDesc: "Brand campaign highlighting the evolution and expanded features of the payroll software, now optimized for enterprise-level use.",
    projectType: "GTM Strategy, Motion design & Print Design",
    targetAudience: "Enterprise businesses",
    timeframe: "3 Weeks",
    client: "RazorpayX Payroll",
    problem: "As companies grow and evolve into large enterprises, their payroll systems often struggle to keep up with increased demands, leading to issues such as payroll errors, compliance challenges, and inefficient processes. Many enterprises in India seek advanced payroll solutions offering institutional accuracy, scalability, and seamless integration with existing HR systems.",
    approach: "Devised a comprehensive multi-channel Go-To-Market visual identity that communicated robustness, security compliance, and effortless scale. Produced high-fidelity motion graphics for launch events, architectural product diagrams, and executive physical collateral.",
    responsibilities: "GTM narrative design, key visual direction, animation storyboarding, interactive asset guidelines, and trade show presentation materials.",
    images: [
      "https://framerusercontent.com/images/8xt1f8uMJqhBTJdZ7iTfaUqp1M8.svg",
      "https://framerusercontent.com/images/XytG8JmwkXGxemOLdVPup3WpGt0.png",
      "https://framerusercontent.com/images/xGC69A1DxUHyR2xVkE1NUOJq8C8.png",
      "https://framerusercontent.com/images/yKFJYHVJL99wosMCKdU1tHIBQo.png"
    ]
  },
  {
    id: "ca-founder-collab",
    title: "CA & Founder Collaboration",
    tags: ["Motion Graphics", "Script Writing"],
    thumbnail: "https://framerusercontent.com/images/6HbTgFxHBUu2DKXduj34oBzJ4S8.png?width=921&height=929",
    shortDesc: "Social campaign highlighting the challenges of traditional founder-Chartered Accountant collaboration, promoting RazorpayX as a streamlined solution.",
    projectType: "Motion Graphics, Script Writing",
    targetAudience: "Startup Founders and Chartered Accountants",
    timeframe: "2 Weeks",
    client: "RazorpayX",
    problem: "Many Founders and Chartered Accountants are unaware of the inefficiencies and challenges in their current collaboration process (or believe there is no better method available). Traditional practices often lead to miscommunication, incomplete data sharing, and administrative bottlenecks.",
    approach: "Created a relatable, humorous, and insight-driven social campaign emphasizing common pain points—such as endless OTP ping-pongs, missing invoices at 11 PM on tax deadlines, and fragmented spreadsheets. Positioned RazorpayX as the ultimate unified workspace for CAs and founders.",
    responsibilities: "Concept ideation, script writing, character and graphic illustration style, storyboard animatics, and final motion design.",
    images: [
      "https://framerusercontent.com/images/6HbTgFxHBUu2DKXduj34oBzJ4S8.png?width=921&height=929",
      "https://framerusercontent.com/images/cvqQSjDSnDnnuUHr7246xSUYfN0.png",
      "https://framerusercontent.com/images/i4MG0UAmoHGUFgqT3tBjzGfKPJM.png",
      "https://framerusercontent.com/images/oXIdNsLxSbC9lRhm7weqiJZOctc.png"
    ]
  },
  {
    id: "custom-access-controls",
    title: "Custom Access Controls",
    tags: ["Motion Graphics", "Story telling"],
    thumbnail: "https://framerusercontent.com/images/Nivxw3CPF9PHkeZAxFyEE6gkq3A.png?width=919&height=920",
    shortDesc: "Promotional video campaign showcasing new custom access controls and approval workflows in RazorpayX Banking, designed to enhance delegation and collaboration.",
    projectType: "Motion Graphics, Script Writing",
    targetAudience: "Founders & Finance Managers",
    timeframe: "1.5 Weeks",
    client: "RazorpayX Banking",
    problem: "Startups often struggle with managing and delegating financial tasks effectively due to concerns about privacy, control, and security. The lack of customisable access and approval workflows can lead to bottlenecks and security vulnerabilities, making it stressful to ensure only the right team members have access to sensitive financial information.",
    approach: "Crafted a slick UI walkthrough animation that demonstrated granular role creation, approval thresholds, and automated maker-checker workflows in under 45 seconds, transforming dry security architecture into an empowering feature.",
    responsibilities: "Motion design, UI asset reconstruction, motion choreography, sound design curation, and script pacing.",
    images: [
      "https://framerusercontent.com/images/Nivxw3CPF9PHkeZAxFyEE6gkq3A.png?width=919&height=920",
      "https://framerusercontent.com/images/yfb4KMewFtLxqnmeNHHFZMong.png",
      "https://framerusercontent.com/images/W1eHgCXCoDG9o1EdQIpymcRw6U.png",
      "https://framerusercontent.com/images/H08TH8bPdrvF2DzFL1RDeVLmAMM.png"
    ]
  },
  {
    id: "you-are-okay",
    title: "You Are Okay",
    tags: ["Book Design", "Illustration", "Art Therapy"],
    thumbnail: "https://framerusercontent.com/images/5LW0UNClgrtUszuu7lyCZ7HOESk.png?width=1379&height=1379",
    shortDesc: "A self-help activity book that helps anxious teenagers express their emotions and frustrations creatively, enhancing their learning experience and aiding in self-reflection.",
    projectType: "Illustration, Book Design, Art Therapy",
    targetAudience: "Teenagers & young adults who experience anxiety, worry & stress",
    timeframe: "6 Months",
    client: "Graduation Project",
    problem: "Anxiety, worry, and stress are prevalent mental health issues among teenagers, impacting their daily lives and overall well-being. Despite the availability of various psychological treatments, many teens struggle to find accessible and effective self-help tools that allow them to manage their anxiety independently without feeling judged.",
    approach: "Conducted field research with adolescent psychologists and teenagers to design an interactive, tactfully illustrated workbook combining cognitive behavioral exercises with expressive art therapy prompts, tactile printing techniques, and soothing visual metaphors.",
    responsibilities: "Research, narrative design, copy, visual styling, hand illustrations, publication layout, and print production.",
    images: [
      "https://framerusercontent.com/images/5LW0UNClgrtUszuu7lyCZ7HOESk.png?width=1379&height=1379",
      "https://framerusercontent.com/images/SHeO9oDajrofd5foo4IFT4ZEEVA.png",
      "https://framerusercontent.com/images/O62O8h2jOzC4ofjrjLL1kQ3MN98.png",
      "https://framerusercontent.com/images/0Cncw0QLK5peyPmchGXk09XtgE.png",
      "https://framerusercontent.com/images/iiYizBml6OFyx7M8SvF80VUKKaQ.png"
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

    modalHeroImg.src = proj.thumbnail;
    modalHeroImg.alt = proj.title;
    modalTags.innerHTML = proj.tags.map(t => `<span class="tag-badge">${t}</span>`).join('');
    modalTitle.textContent = proj.title;

    metaType.textContent = proj.projectType || "Communication Design";
    metaAudience.textContent = proj.targetAudience || "General Public";
    metaTimeframe.textContent = proj.timeframe || "2 Weeks";

    modalProblem.textContent = proj.problem;
    modalApproach.textContent = proj.approach;
    modalResponsibilities.textContent = proj.responsibilities;

    // Render gallery images if any
    if (proj.images && proj.images.length > 1) {
      modalGallery.innerHTML = proj.images.slice(1).map(imgUrl => `
        <img src="${imgUrl}" alt="${proj.title} visual" loading="lazy">
      `).join('');
      modalGallery.style.display = "grid";
    } else {
      modalGallery.innerHTML = "";
      modalGallery.style.display = "none";
    }

    modalOverlay.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    modalOverlay.classList.remove("active");
    document.body.style.overflow = "";
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener("click", closeModal);
  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) closeModal();
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modalOverlay.classList.contains("active")) {
      closeModal();
    }
  });

  // 3. Navigation View Switching (Home vs About)
  function switchView(viewName) {
    if (viewName === "about") {
      homeView.classList.add("hidden");
      aboutView.classList.add("active");
      navHome.parentElement.classList.remove("active");
      navAbout.parentElement.classList.add("active");
      header.classList.add("scrolled-light");
      window.scrollTo({ top: 0, behavior: "smooth" });
    } else {
      aboutView.classList.remove("active");
      homeView.classList.remove("hidden");
      navAbout.parentElement.classList.remove("active");
      navHome.parentElement.classList.add("active");
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
    localStorage.setItem("adyatha_theme", theme);

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

  // Load saved theme or default to 'indigo' (replaces pink)
  const savedTheme = localStorage.getItem("adyatha_theme") || "indigo";
  setTheme(savedTheme);

  // 5. Scroll Header Visual State
  function handleScroll() {
    if (aboutView.classList.contains("active")) {
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
