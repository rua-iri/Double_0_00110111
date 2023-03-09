<?php





?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <h1>
        Upload File
    </h1>

    <form action="process.php" method="POST" enctype="multipart/form-data">

        <div>
            <input type="file" name="fileUpload" id="file-upload">
        </div>

        <br>

        <div>
            <input type="submit" value="Submit" name="submit">
        </div>


    </form>

</body>

</html>