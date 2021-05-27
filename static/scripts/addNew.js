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
  
  var firstid = newId.split("-")[0] + "first-" +newId.split("-")[1]
  var secondid = newId.split("-")[0] + "second-" +newId.split("-")[1]
  var newEntry = $( `<ul id="${newId}"><input onclick="removeRow(this)" type="button" value="X" id="${newId}" class="removeButton"><br>Od:<input type="time" id="${firstid}" name="${firstid}"><br>Do:<input type="time" id="${secondid}" name="${secondid}"></ul>`);
  newEntry.insertBefore("#".concat(document.getElementById(element.id).parentElement.id))
  }


function removeRow(element)
{
  parentId =  document.getElementById(element.id);
  console.log(parentId.parentElement)
  $("#".concat(parentId.id)).remove();

}