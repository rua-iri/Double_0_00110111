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
            <div>
                <input type="radio" name="function" id="eRadio" value="encode" checked>
                <label for="eRadio">
                    Encode
                </label>
            </div>

            <div>
                <input type="radio" name="function" id="dRadio" value="decode">
                <label for="dRadio">
                    Decode
                </label>
            </div>
        </div>

        <br>
        
        <!-- TODO use js to hide this if user has selected decode -->
        <div>
            <input type="text" name="eMessage" placeholder="Enter Message Here">
        </div>

        <br>

        <div>
            <input type="submit" value="Submit" name="submit">
        </div>


    </form>

</body>

</html>