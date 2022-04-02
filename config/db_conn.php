<?php 
$DB_HOST = 'localhost';
$DB_USER = 'Raji';
$DB_PASS = 'library';
$DB_NAME = 'biblio';

$conn = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>