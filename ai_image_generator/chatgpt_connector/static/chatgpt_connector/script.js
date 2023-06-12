document.getElementById("loginButton").addEventListener("click", function() {
  document.getElementById("loginPopup").classList.remove("d-none");
});

document.getElementById("closeButton").addEventListener("click", function() {
  document.getElementById("loginPopup").classList.add("d-none");
});

document.addEventListener("click", function(event) {
  if (event.target === document.getElementById("loginPopup")) {
    document.getElementById("loginPopup").classList.add("d-none");
  }
});