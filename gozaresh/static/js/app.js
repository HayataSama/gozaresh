// loads latest theme preference
var theme = window.localStorage.getItem("theme");
if (theme == "dark") {
  document.documentElement.setAttribute("data-theme", "dark");
  document.querySelector("#switch").checked = true;
} else {
  document.documentElement.setAttribute("data-theme", "light");
  document.querySelector("#switch").checked = false;
}

// theme toggle button
var checkbox = document.querySelector("input[name=theme]");

checkbox.addEventListener("change", function () {
  if (this.checked) {
    document.documentElement.setAttribute("data-theme", "dark");
    window.localStorage.setItem("theme", "dark");
  } else {
    document.documentElement.setAttribute("data-theme", "light");
    window.localStorage.setItem("theme", "light");
  }
});

// checks for what page we are on
page = document.querySelector("title");
if ((page = "نتیجه")) {
  function copy() {
    var text = document.querySelector("#textarea");
    text.select();
    document.execCommand("copy");
  }
  var copy_btn = document.querySelector(".copybtn");

  copy_btn.addEventListener("click", copy);
} else {
  console.log("we're on the index page!");
}
