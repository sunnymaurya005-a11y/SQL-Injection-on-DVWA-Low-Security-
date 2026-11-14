
<?php
// Secure SQL query using PDO prepared statements

$host = "localhost";
$dbname = "dvwa";
$username = "root";
$password = "";

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$dbname;charset=utf8mb4",
        $username,
        $password,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_EMULATE_PREPARES => false
        ]
    );

    $userId = 1;

    $stmt = $pdo->prepare(
        "SELECT first_name, last_name
         FROM users
         WHERE user_id = :id"
    );

    $stmt->execute(['id' => $userId]);

    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    print_r($results);

} catch (PDOException $e) {
    error_log($e->getMessage());
    echo "Database operation failed.";
}
?>
