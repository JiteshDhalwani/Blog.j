const scrollToTop = () => {
    window.scroll({
        top: 0,
        behavior: "smooth",
    });
};

document.querySelector("#page_up_button").onclick = scrollToTop;