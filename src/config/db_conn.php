<?php 
$DB_HOST = 'localhost';
$DB_USER = 'Raji';
$DB_PASS = 'library';
$DB_NAME = 'gestion_emprunts';

$conn = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>