function addRow(element) {
  var beforeId = document.getElementById(element.id).parentElement.previousElementSibling.id;
  var newId;
  if(beforeId)
  {
    newId = beforeId.split("_")[0].concat("_");
    newId = newId.concat((parseInt(beforeId.split("_")[1])+1).toString());
  }
  else
  {
    newId = document.getElementById(element.id).parentElement.parentElement.id.concat("_0");
  }
  var newEntry = $( "<ul id=".concat(newId).concat("><a href=\"#\">Proba</a></ul>"));
  newEntry.insertBefore("#".concat(document.getElementById(element.id).parentElement.id))
  }