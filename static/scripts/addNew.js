function addRow(element) {
  var beforeId = document.getElementById(element.id).parentElement.previousElementSibling.id;
  var newId;
  var newIdfirst;
  var newIdsecond;
  if(beforeId)
  {
    newId = beforeId.split("_")[0].concat("_");
    newId = newId.concat((parseInt(beforeId.split("_")[1])+1).toString());
    newIdfirst = "timeEntryfirst-".concat(beforeId.split("-")[1].split("_")[0]).concat("_")
    newIdfirst = newIdfirst.concat((parseInt(beforeId.split("_")[1])+1).toString());
    newIdsecond = "timeEntrysecond-".concat(beforeId.split("-")[1].split("_")[0]).concat("_")
    newIdsecond = newIdfirst.concat((parseInt(beforeId.split("_")[1])+1).toString());
  }
  else
  {
    newId = "timeEntry-".concat(document.getElementById(element.id).parentElement.parentElement.id.split("-")[1].concat("_0"));
    newIdfirst = "timeEntryfirst-".concat(document.getElementById(element.id).parentElement.parentElement.id.split("-")[1].concat("_0"));
    newIdsecond = "timeEntrysecond-".concat(document.getElementById(element.id).parentElement.parentElement.id.split("-")[1].concat("_0"));
  }
  var newEntry = `<ul id="${newId}">Od:<input type="time" id="${newIdfirst}" name="${newIdfirst}$"><br> Do:<input type="time" id="${newIdsecond}" name="${newIdsecond}"></ul>`;
  console.log(newEntry)
  var acNewEntry = $(newEntry);
  acNewEntry.insertBefore("#".concat(document.getElementById(element.id).parentElement.id))
  }


  var slideIndex = 1;
  showFirst(slideIndex);
  
  // Next/previous controls
  function plusSlides(n) {
    showSlides(slideIndex += n);
  }
  
  // Thumbnail image controls
  function currentSlide(n) {
    showSlides(slideIndex = n);
  }
  function showFirst(n)
  {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    try {
      slides[0].style.display = "block";
    }
    catch(err) {
      console.log(err)
    }
    
  }
  function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    try {
      slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    }
    catch(err) {
      console.log(err)
    }
    
  }