document.addEventListener("DOMContentLoaded", function () {
    const events = document.querySelectorAll(".event-card");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("show");
                }
            });
        },
        { threshold: 0.2 }
    );

    events.forEach((event) => observer.observe(event));
});
