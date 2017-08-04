var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;



/* ADD YOUR CODE BELOW */
function checkPassword() {
  // Get user-entered password from input box
  var pw = document.getElementById("pw").value.toLowerCase();

  var isStrongPW = true;
  for (var i = 0; i <wordsList.length; i++) {
    if (wordsList[i] == pw) {
      isStrongPW = false;
      break; }
      /* The code will continue to run until the input is found. */
  }
  if(isStrongPW == true){
    alert("Strong Password");
    /* If not found, "Strong Password" will be said. */
  }else{
    alert("Weak Password");
  }

}
