<?php

// https://secure.php.net/manual/en/function.srand.php#90215

function generate_random_text ($length) {
    $chars  = "abcdefghijklmnopqrstuvwxyz";
    $chars .= "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    $chars .= "1234567890";
    $text = '';
    for($i = 0; $i < $length; $i++) {
        $text .= $chars[rand () % strlen ($chars)];
    }
    return $text;
}

$time = 1524219801;
srand($time );
echo generate_random_text(255 / 10.0);
echo "\n";

?>
