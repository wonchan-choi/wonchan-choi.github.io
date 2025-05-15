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
        },{id: "nav-cv",
          title: "CV",
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
            },},{id: "news-recognized-as-a-distinguished-member-of-asis-amp-t",
          title: 'Recognized as a Distinguished Member of ASIS&amp;amp;T',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2024-10-28/";
            },},{id: "news-ranked-among-the-top-10-of-most-viewed-papers-in-2023",
          title: 'Ranked among the top 10% of most-viewed papers in 2023',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/2025-04-16/";
            },},{id: "projects-mdlaug",
          title: 'mDLAUG',
          description: "Mobile Digital Library Accessibility and Usability Guidelines",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2022-mDLAUG/";
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
