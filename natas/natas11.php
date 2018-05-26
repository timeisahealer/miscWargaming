<html>
<? 
function xor_find_key() {
    $XORcipher = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmh");
    $XORplain = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"), true);
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($XORcipher);$i++) {
    $outText .= $XORcipher[$i] ^ $XORplain[$i % strlen($XORplain)];
    }

    return $outText;
}
//print xor_find_key();

function xor_encrypt($in) {
    $key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$arr = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
print base64_encode(xor_encrypt(json_encode($arr)))

?>
</html>
