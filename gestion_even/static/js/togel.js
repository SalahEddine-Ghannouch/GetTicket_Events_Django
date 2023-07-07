const toggleBlur = (title,desc) => {

  const blurEl = document.getElementById("blur");
  blurEl.classList.toggle("active");

  const popupEl = document.getElementById("popup");
  popupEl.classList.toggle("active");

  const eventTitleEl = document.getElementById("title");
  var eventTitle = title;
  eventTitleEl.textContent = eventTitle;

  const eventDesc = document.getElementById("desc");
  var eventdesc = desc;
  eventDesc.textContent = eventdesc;


  return false;
};
