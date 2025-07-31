// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "Peer-reviewed articles published in journals and conference proceedings",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-curriculum-vitae",
          title: "Curriculum Vitae",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-promoted-to-associate-professor-with-tenure",
          title: 'Promoted to Associate Professor with tenure',
          description: "",
          section: "News",},{id: "news-recognized-as-a-distinguished-member-of-asis-amp-t",
          title: 'Recognized as a Distinguished Member of ASIS&amp;amp;T',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2024-10-28/";
            },},{id: "news-our-research-article-college-students-credibility-assessments-of-genai-generated-information-for-academic-tasks-an-interview-study-has-been-accepted-for-publication-in-jasist",
          title: 'Our research article, “College Students’ Credibility Assessments of GenAI-generated Information for Academic Tasks:...',
          description: "",
          section: "News",},{id: "news-our-arist-chapter-investigating-the-interactions-between-individuals-with-disabilities-and-information-retrieval-systems-a-review-of-help-seeking-situations-search-tactics-and-design-recommendations-has-been-accepted-for-publication-in-jasist",
          title: 'Our ARIST chapter, “Investigating the Interactions between Individuals with Disabilities and Information Retrieval...',
          description: "",
          section: "News",},{id: "news-our-short-paper-ranked-among-the-top-10-of-most-viewed-papers-in-2023-proceedings-of-asis-amp-t",
          title: 'Our short paper ranked among the top 10% of most-viewed papers in 2023...',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-04-16/";
            },},{id: "news-accepted-for-a-penal-at-the-2025-asis-amp-amp-t-virtual-setellite-meeting-december-2025",
          title: 'Accepted for a penal at the 2025 ASIS&amp;amp;amp;T Virtual Setellite Meeting (December 2025)...',
          description: "",
          section: "News",},{id: "news-two-posters-accepted-for-the-2025-asis-amp-amp-t-annual-meeing-which-will-be-held-in-washington-d-c-november-2025",
          title: 'Two posters accepted for the 2025 ASIS&amp;amp;amp;T Annual Meeing, which will be held...',
          description: "",
          section: "News",},{id: "projects-rethinking-digital-literacy-in-the-age-of-generative-ai-college-students-use-of-chatgpt-for-educational-purposes",
          title: 'Rethinking Digital Literacy in the Age of Generative AI - College Students’ Use...',
          description: "Funded by UWM CCEP to explore college students&#39; use of generative artificial intelligence tools for academic tasks. 2023–2024 ($6,000)",
          section: "Projects",handler: () => {
              window.location.href = "/projects/genai-literacy/";
            },},{id: "projects-developing-a-scale-for-credibility-assessment-on-interactive-web-platforms",
          title: 'Developing a Scale for Credibility Assessment on Interactive Web Platforms',
          description: "Funded by UWM to develop a psychometric scale to measure pereceived credibility of online information created by anonymous users and GenAI bots on the web. 2023 ($2,451)",
          section: "Projects",handler: () => {
              window.location.href = "/projects/ic-scale-dev/";
            },},{id: "projects-web-credibility-assessments-in-the-context-of-social-q-amp-a-sites",
          title: 'Web Credibility Assessments in the Context of Social Q&amp;amp;A Sites',
          description: "Funded by UWM to explore cues and heuristics employed users in their credibility assessments of information on social Q&amp;A sites. 2021 ($4,887)",
          section: "Projects",handler: () => {
              window.location.href = "/projects/ic-socialqa/";
            },},{id: "projects-mobile-digital-library-accessibility-and-usability-guidelines-mdlaug",
          title: 'Mobile Digital Library Accessibility and Usability Guidelines (mDLAUG)',
          description: "Funded by IMLS to develop guidelines for building digitial libraries for blind and visually impaired users. 2022–2024 (extended to 2025) ($695,631)",
          section: "Projects",handler: () => {
              window.location.href = "/projects/mdlaug/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
