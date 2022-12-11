<?php

$operation = htmlentities($_GET["o"]);
$number = htmlentities($_GET["nA"]);
$number2 = htmlentities($_GET["nB"]);
if(!$number || !$number2 || !is_numeric($number) || !is_numeric($number2)){
    print_r(["message" => "Invalid number"]);
    exit;
}
switch($operation){
    default:
        print_r(["message" => "Invalid operator"]);
        exit;
    case "add" || "sum":
        $number3 = $number + $number2;
        break;
    case "sub":
        $number3 = $number - $number2;
        break;
    case "mul":
        $number3 = $number * $number2;
        break;
    case "div":
        $number3 = $number / $number2;
        break;
}
print_r(["message" => "Everything good", "result " => $number3]);
