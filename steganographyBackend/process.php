<?php

$processType = $_POST["function"];
$scrtMessage = $_POST["eMessage"];
$targetDir = "uploads/" . $processType . "/";
$fileType = explode("/", $_FILES["fileUpload"]["type"])[1];
$filePath = $targetDir . basename($_FILES["fileUpload"]["name"]);

// asign the file to a random name that does not exist in the uploads directory
do {
    $filePath = $targetDir . md5(microtime()) . "." . $fileType;
} while (file_exists($filePath));

$acceptableTypes = array("jpeg", "png");

// TODO redirect to homepage if $uploadSuccess changes to zero
$uploadSuccess = true;

// check the submit button has been pressed
if (isset($_POST["submit"])) {

    // check that image is of an acceptable type
    if (!in_array($fileType, $acceptableTypes)) {
        $uploadSuccess = false;
    }

    // check that file is image
    if (!getimagesize($_FILES["fileUpload"]["tmp_name"])) {
        $uploadSuccess = false;
    }

    // check that file is smaller than 3mb
    if ($_FILES["fileUpload"]["size"] > 3000000) {
        $uploadSuccess = false;
    }
}

// if the upload is valid
if ($uploadSuccess) {
    move_uploaded_file($_FILES["fileUpload"]["tmp_name"], $filePath);

    $pyCommand = "python3 imageProcessor.py " . $processType . " " . $filePath;

    // add secret message if the user wants to encrypt
    if ($processType == "encode") {
        $pyCommand .= " '" . $scrtMessage . "'";
    }

    $cmdOutput = trim(shell_exec($pyCommand));
    $baseFileName = explode("/", $filePath)[2];

    if (strlen($cmdOutput) > 2) {

        // TODO pass text back to homepage to display secret message
        if ($processType == "encode") {
            $imgFile = "downloads/" . substr($baseFileName, 0, -4) . "_encoded.png";
            echo $imgFile;
            echo "<img src='" . $imgFile . "' alt=''>";
        } else if ($processType == "decode") {
            $txtFile = "downloads/messages/" . substr($baseFileName, 0, -3) . "txt";
            $msgText = file_get_contents($txtFile);
            echo "<br>Message Text: '" . $msgText . "'<br>";
        }
    }
}


// TODO execute python program to encode / decode


// TODO redirect to page displaying the encoded image if $uploadSuccess
