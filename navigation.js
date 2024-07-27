var currentPage = 0;
var totalPages = 0;

function showPage(page) {
  document.querySelectorAll(".page").forEach(function (div, index) {
    div.classList.remove("active");
    if (index === page) {
      div.classList.add("active");
    }
  });
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    showPage(currentPage);
  }
}

function nextPage() {
  if (currentPage < totalPages - 1) {
    currentPage++;
    showPage(currentPage);
  }
}

document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    prevPage();
  } else if (event.key === "ArrowRight") {
    nextPage();
  }
});

function initialize(total) {
  totalPages = total;
  showPage(currentPage);
}
