function $(id) {
  return document.getElementById(id);
}

let uploadedFile;

$("upload").onclick = function () {
  $("file").click();
};

$("file").onchange = function (e) {
  if (!e.target.files?.[0]) return;

  const file = e.target.files[0];
  const fileExt = file.name.split('.').pop().toLowerCase();

  if (fileExt !== 'csv' && fileExt !== 'xlsx') {
    // Display error message if file extension is not .csv or .xlsx
    $("status").innerHTML = "Sorry, we only accept .csv or .xlsx files.";
    $("status").style.color = "red";
    $("status").style.textAlign = "center";
    return;
  } else {
    uploadedFile = file;
    $("status").innerHTML = file.name + " was uploaded successfully.";
    $("status").style.color = "green";
    $("status").style.textAlign = "center";
  }
};

$("submit").onclick = function (e) {
  e.preventDefault();
  if (!uploadedFile) {
    // Display error message if no file has been uploaded
    $("status").innerHTML = "Please upload a CSV or XLSX file first.";
    $("status").style.color = "red";
    $("status").style.textAlign = "center";
    return;
  }

  const formData = new FormData();
  formData.append("file", uploadedFile);

  fetch("http://127.0.0.1:5500/api/submit", {
    method: "POST",
    body: formData,
    headers: {},
  })
    .then((res) => {
      console.log(res, "response submit");
      // Display success message if the file was successfully submitted
      $("status").innerHTML = "File submitted successfully!";
      $("status").style.color = "green";
      $("status").style.textAlign = "center";
    })
    .catch((e) => {
      console.log(e, "Error submitting file");
      // Display error message if an error occurred while submitting the file
      $("status").innerHTML = "Error submitting file. Please try again.";
      $("status").style.color = "red";
      $("status").style.textAlign = "center";
    });
};
