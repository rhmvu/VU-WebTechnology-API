//fill the product table when the page is loaded
$(document).ready(function(){
  FillTable();
  sortProtocolTable();
})

//function for AJAX GET request to fill the product table
function FillTable(){
  $.ajax({
    type: "GET",
    url: 'http://localhost:8080/retrieve-all',
    dataType: "json",
    cache: false,
    success: function (data) {
      var length = data.length;
      for (var i = 0; i < length; i++) {
        var rowNumber = i+1;
        var name  = data[i].name;
        var category  = data[i].category;
        var amount  = data[i].amount;
        var location  = data[i].location;
        var date  = data[i].date;
        $("#body").append("<tr><td>"+ rowNumber +"</td><td>"+ name +"</td><td>"+ category +"</td><td>"+ amount +"</td><td>"+ location +"</td><td>"+ date +"</td></tr>");
      }
    }
  });
}

//function for submit product
function SubmitForm (){
  var name = $("#name").val();
  var category = $("#category").val();
  var amount = $("#amount").val();
  var location = $("#location").val();
  var date = $("#date").val();
  var formData = {name: name, category: category, amount: amount, location: location, date: date};
  // if statement to check if all field are filled
  if(IsEmpty(name)&& IsEmpty(category)&&IsEmpty(amount)&&IsEmpty(location)&&IsEmpty(date)){
  }else{
    alert("Please fill in all fields");
    event.preventDefault();
    return;
  }
  $.ajax({
    url:'http://localhost:8080/create',
    type:"POST",
    contentType: 'application/json',
    data: JSON.stringify(formData),
    complete: function(){
      document.forms['submitForm'].reset()
      Reload();
    }
  });
  event.preventDefault();
}

//function to check if a variable/field is empty
function IsEmpty(variable){
  if(variable === "")
  {
    return false;
  }
  return true;
}

//function for update product
function UpdateProduct (){
  var row = $("#row").val();
  var name = $("#name").val();
  var category = $("#category").val();
  var amount = $("#amount").val();
  var location = $("#location").val();
  var date = $("#date").val();
//if statement to check if all field are filled
  if(IsEmpty(row) && IsEmpty(name)&& IsEmpty(category)&&IsEmpty(amount)&&IsEmpty(location)&&IsEmpty(date)){
  }else{alert("Please fill in all fields");
  event.preventDefault();
  return;
}
//function to post the update via AJAX
var formData = {name: name, category: category, amount: amount, location: location, date: date};
$.ajax({
  url:'http://localhost:8080/update/' + row,
  type:"PUT",
  contentType: 'application/json',
  data: JSON.stringify(formData),
  complete: function(){
    document.forms['submitForm'].reset()
    Reload();
  }
});
event.preventDefault();
}

//function for reset database
function ResetForm (){
  $.ajax({
    url:'http://localhost:8080/reset-all',
    type:'DELETE',
    complete: function(){
      Reload();
    }
  });
  event.preventDefault();
}

//function for removing a specific product
function RemoveElement (){
  var row = $("#row").val();
  if(IsEmpty(row)){
  }else{
    alert("Please fill the rownumber");
    event.preventDefault();
    return;
  }
  $.ajax({
    url: 'http://localhost:8080/delete/' + row,
    type: 'DELETE',
    dataType: 'json',
    complete: function(){
      Reload();
    }
  });
  event.preventDefault();
}

//function for update only the product table
function Reload(){
  $("#body tr").remove();
  $('#productTable').load(FillTable());
}

//function to make the protocol table sortable
function sortProtocolTable(){
  $("#protocolTable").tablesorter();
}

//google map script
var mapOptions = {
  center: new google.maps.LatLng(52.2873863,4.2102205),
  zoom: 8,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};

var map = new google.maps.Map(document.getElementById('map'), mapOptions);

var markerOptions1 = {
  position: new google.maps.LatLng(52.3702157,4.895167899999933),
  map: map
};
var markerOptions2 = {
  position: new google.maps.LatLng(52.2291696,5.166897400000039),
  map: map
};
var markerOptions3 = {
  position: new google.maps.LatLng(51.9244201,4.477732500000002),
  map: map
};

var marker1 = new google.maps.Marker(markerOptions1);
marker1.setMap(map);
var marker2 = new google.maps.Marker(markerOptions2);
marker2.setMap(map);
var marker3 = new google.maps.Marker(markerOptions3);
marker3.setMap(map);

var infoWindowOptions1 = {
  content: "Amsterdam"
};
var infoWindowOptions2 = {
  content: "Hilversum"
};
var infoWindowOptions3 = {
  content: "Rotterdam"
};

var infoWindow1 = new google.maps.InfoWindow(infoWindowOptions1);
google.maps.event.addListener(marker1,'mouseover',function(){
  infoWindow1.open(map, marker1);
});
var infoWindow2 = new google.maps.InfoWindow(infoWindowOptions2);
google.maps.event.addListener(marker2,'mouseover',function(){
  infoWindow2.open(map, marker2);
});
var infoWindow3 = new google.maps.InfoWindow(infoWindowOptions3);
google.maps.event.addListener(marker3,'mouseover',function(){
  infoWindow3.open(map, marker3);
});

//script to override default event response when clicking links
function preventEvent(event) {
  event.preventDefault();
  alert("Link is prevented");
}
