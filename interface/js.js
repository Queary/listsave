window.onload = function() {
  eel.openpy()
};
var i = 0;
function create() {
  i+=1;
  // alert("create")
  var ndiv = document.createElement("div")
  // alert("create div")
  // div.className = "alert";
  // div.innerHTML = "<strong>Всем привет!</strong> Вы прочитали важное сообщение.";
  ndiv.className = 'list'
  // alert("create class")
  ndiv.id = 'list'+i
  // alert("create id")
  ndiv.innerHTML = '<text id="text'+i+'"></text><input id="text'+i+'in" type="text" name="" value=""><button id="button'+i+'" type="button" name="button" onclick="save(\'text'+i+'\',\'text'+i+'in\',\'button'+i+'\',\'button_'+i+'\')">save</button><button onclick="del(\'text'+i+'\',\'list'+i+'\')" id=\'button_'+i+'\'style="display:none;"type="button" name="button">delete</button>'
  document.getElementById("toplist").appendChild(ndiv)
  // alert("create append")
}
eel.expose(createjs)
function createjs(id,value) {
  // alert("create")
  i=id+1
  var ndiv = document.createElement("div")
  // alert("create div")
  // div.className = "alert";
  // div.innerHTML = "<strong>Всем привет!</strong> Вы прочитали важное сообщение.";
  ndiv.className = 'list'
  // alert("create class")
  ndiv.id = 'list'+i
  // alert("create id")
  ndiv.innerHTML = '<text style="display:inline-block;" id="text'+i+'">'+ value +'</text><button onclick="del(\'text'+i+'\',\'list'+i+'\')" id=\'button_'+i+'\'style="display:block;"type="button" name="button">delete</button>'
  // alert("create innerHTML")
  document.getElementById("toplist").appendChild(ndiv)
  // alert("create append")
}
// .removeChild
function save(arg,arg2,but,but_) {
  // alert(arg)
  // alert(document.getElementById(arg2).value)
  document.getElementById(arg).style.display = "inline-block"
  document.getElementById(arg).innerHTML = document.getElementById(arg2).value
  document.getElementById(arg2).style.display = "none"
  document.getElementById(but).style.display = "none"
  document.getElementById(but_).style.display = "inline"
  eel.savepy(arg,document.getElementById(arg2).value)
}
function del(arg,argdouble) {
  // alert(arg)
  document.getElementById(argdouble).remove(argdouble)
  eel.delpy(arg)
}
