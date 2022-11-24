$(document).ready(function () {
  let algorithm = "";

  $body = $("body");

  $(document).on({
    ajaxStart: function () {
      $body.addClass("loading");
    },
    ajaxStop: function () {
      $body.removeClass("loading");
    },
  });

  $("#send-button").on("click", function () {
    $("#summerized-text").val("");
    let url = "";
    let text = "";

    let inputType = $("input[type='radio']:checked").val();
    algorithm = $("#algorithm").val();

    if (inputType === "url") {
      url = $("#input-text").val();
      if(!url.includes("http://") && !url.includes("https://")) {
        alert('Não é url válida');
        return;
      }
      console.log(url);
    }
    if (inputType === "text") {
      text = $("#input-text").val();
      console.log(text);
    }
    console.log(algorithm + " " + inputType);

    let request = {
      algorithm: algorithm,
      url: url,
      text: text,
    };

    $.ajax({
      type: "POST",
      url: "https://dd55-170-231-252-113.sa.ngrok.io/summarize",
      data: JSON.stringify(request),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function (response) {
        console.log(response);
        let noTagResponse = response.summarizedText.replace(
          /(<([^>]+)>)/gi,
          ""
        );
        let finalResponse = noTagResponse.replace(/\s\s+/g, " ").trim();
        $("#summerized-text").val(finalResponse);
      },
      error: function (response) {
        console.log(response.message);
        alert(response.message);
      },
    });
  });
});
