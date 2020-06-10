<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Mycroft tts</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body><h2>Text to mycroft TTS</h2>
<p>Everything you send here will be spoken by MyCroft.</p>
<form action="send-message.php" method="post">
    <p>
        <label for="inputName">Message to TTS:<sup>*</sup></label>
        <input class="form-control" type="text" name="msg" id="msg">
    </p>
   
    <input class="btn btn-primary" type="reset" value="Reset">
    
    <input class="btn btn-primary" type="Submit" value="Send">
</form>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>