<?php
$data = $_POST['msg'];
$message = '{"type": "speak", "data": {"utterance": " ' . $data . ' "} }' ;

echo 'Message sent: ' . $message;

//include_once('lib/Client.php');
require('vendor/autoload.php');
use WebSocket\Client;

$client = new Client("ws://192.168.86.56:8181/core");



$client->send($message);
echo '</br>';

echo $client->receive();

$client->close();

header('Location: index.php');
exit;