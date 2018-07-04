var headContent = '<!DOCTYPE html>\
<html lang="en">\
<head>\
  <title>Bootstrap Example</title>\
  <meta charset="utf-8">\
  <meta name="viewport" content="width=device-width, initial-scale=1">\
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>\
</head>'

function displayCodeAll(fileName) {
	var txtFile = new XMLHttpRequest();
	txtFile.open("GET", fileName, true);
	txtFile.onreadystatechange = function() {
	  if (txtFile.readyState === 4) {  // Makes sure the document is ready to parse.
	    if (txtFile.status === 200) {  // Makes sure it's found the file.
	      allText = txtFile.responseText; 
	  	  allText = headContent + allText
	      //lines = txtFile.responseText.split("\n"); // Will separate each line into an array
	    //  document.getElementById('welcomeText').innerHTML = "";
	      var customTextElement = document.getElementById('description');

	customTextElement.innerHTML = txtFile.responseText;
	    }
	  }
	}
	txtFile.send(null);

}