<?php

if (!file_exists("data")) mkdir("data");

$data = json_decode(file_get_contents("https://ponies.equestria.horse/api/badger"), true);
file_put_contents("data/list.json", json_encode($data));

foreach ($data as $pony) {
    echo($pony['id'] . "\n");
    exec('convert "' . $pony['avatar'] . '" -background "#ffffff" -flatten -scale 100 -gravity south -extent 128x128 data/' . $pony['id'] . ".jpeg");
}
