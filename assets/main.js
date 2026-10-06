/* ============================================================
   Yikun He — personal site behaviour
   Small progressive enhancement only: the mobile hamburger menu.
   The page is fully usable with JavaScript disabled.
   ============================================================ */
(function () {
  "use strict";

  var toggle = document.querySelector(".menu-toggle");
  var menu = document.querySelector(".nav-links");
  if (!toggle || !menu) return;

  function setOpen(open) {
    menu.classList.toggle("active", open);
    toggle.classList.toggle("active", open);
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("menu-open", open);
  }

  toggle.addEventListener("click", function () {
    setOpen(!menu.classList.contains("active"));
  });

  /* Close the menu after choosing a destination */
  menu.addEventListener("click", function (event) {
    if (event.target.closest && event.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") setOpen(false);
  });

  /* Never leave the overlay open when resizing back to desktop */
  window.addEventListener("resize", function () {
    if (window.innerWidth > 768) setOpen(false);
  });

  /* Footer year */
  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
