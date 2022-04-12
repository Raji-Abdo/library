<?php $script = 'SELECT * FROM adherent';
$result = mysqli_query($conn, $script);
$output = mysqli_fetch_all($result, MYSQLI_ASSOC);
echo $output[0]['telephone'];

if (isset($_POST['submit'])) {
  $script = "INSERT INTO adherent(nom, telephone) VALUES('$_POST[nom]', '$_POST[telephone]')";
}
$input = mysqli_query($conn, $script);
echo '<br>' . $script;
?>

<form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="POST">
  <label for="nom">Nom :</label>
  <input type="text" name="nom"><br>
  <label for="telephone">Tel :</label>
  <input type="text" name="telephone">
  <input type="submit" value="Submit" name="submit">

</form>