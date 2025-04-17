<?php

if (!file_exists("icons")) mkdir("icons");

$name = $argv[1];
$file = $argv[2] ?? $argv[1];
exec('convert "' . $name . '" -background "#ffffff" -scale 24x24 -flatten icons/' . $file . ".jpeg");
